# -*- coding:utf-8 -*-

import data
import const

def create_role(role_id, level):
	attrs = {}

	attrs['role_id'] = role_id
	attrs['level'] = level


	role_data = data.role_info[role_id]
	attrs['hp'] = int(role_data.base_hp + role_data.level_hp_rate * (level - 1))
	attrs['atk'] = role_data.base_atk + role_data.level_atk_rate * (level - 1)
	attrs['defence'] = role_data.base_defence + role_data.level_defence_rate * (level - 1)
	attrs['speed'] = role_data.base_speed + role_data.level_speed_rate * (level - 1)

	attrs['max_hp'] =attrs['hp']
	return attrs

def get_buff_exist_desc(user, buff_obj):
	return _get_buff_desc(user, buff_obj, buff_obj.buff_data.exist_desc)

def get_buff_add_desc(user, buff_obj):
	return _get_buff_desc(user, buff_obj, buff_obj.buff_data.add_desc)

def get_buff_desc(user, buff_obj):
	return _get_buff_desc(user, buff_obj, buff_obj.buff_data.desc)

def _get_buff_desc(user, buff_obj, desc):
	if not desc:
		return desc

	_, value = get_buff_change_attr_value(buff_obj)
	desc = desc.replace('$value$', str(value))

	value *= 100
	if float(int(value)) == value:
		value = int(value)
	desc = desc.replace('%value', str(value))

	attr_dict = {
		u'$攻击':'atk',
		u'$防御':'defence',
		u'$速度':'speed',
	}
	for text, attr in attr_dict.iteritems():
		desc = desc.replace(text, str(user.get_attr(attr)))
	return desc

def get_buff_change_attr_value(buff_obj):
	special_effect_args = buff_obj.buff_data.special_effect_args
	attr = special_effect_args.get('attr', None)

	base_value = special_effect_args.get('base_value', None)
	if not base_value:
		base_value = buff_obj.user_property
	base_value = float(base_value)

	max_value = special_effect_args.get('max_value',None)
	if max_value:
		base_value = min(base_value, float(max_value))
	min_value = special_effect_args.get('min_value',None)
	if min_value:
		base_value = max(base_value, float(min_value))

	if float(int(base_value)) == base_value:
		base_value = int(base_value)

	return attr, base_value

def get_attr_add_rate_value(old_value, user, attr):
	if not attr:
		return

	attr_base = const.ATTR_BASE
	if attr not in attr_base:
		return old_value

	rate = float(user.get_attr(attr)) / attr_base[attr]

	return old_value * rate
	
def _get_value_by_execute_args(execute_args, user, target, default_affect_rate = None):
	if  'fixed_value' in execute_args:
		return float(execute_args['fixed_value'])

	if 'base_value' in execute_args:
		base_value = float(execute_args['base_value'])
	else:
		effect_base = execute_args.get('effect_base', 'atk')
		base_value = user.get_attr(effect_base)
	
	# 系数加成
	rate = float(execute_args.get('rate', 1.0))
	base_value = base_value * rate

	default_affect_rate = default_affect_rate or {}
	# 生命属性加成
	rate = float(execute_args.get('hp_affect_rate', default_affect_rate.get('hp_affect_rate', 0)))
	if rate:
		base_value = get_attr_add_rate_value(base_value, user, 'hp')
		base_value *= rate

	# 攻击属性加成
	rate = float(execute_args.get('atk_affect_rate', default_affect_rate.get('atk_affect_rate', 0)))
	if rate:
		base_value = get_attr_add_rate_value(base_value, user, 'atk')
		base_value *= rate

	# 防御属性加成
	rate = float(execute_args.get('defence_affect_rate', default_affect_rate.get('defence_affect_rate', 0)))
	if rate:
		base_value = get_attr_add_rate_value(base_value, user, 'defence')
		base_value *= rate

	# 速度属性加成
	rate = float(execute_args.get('speed_affect_rate', default_affect_rate.get('speed_affect_rate', 0)))
	if rate:
		base_value = get_attr_add_rate_value(base_value, user, 'speed')
		base_value *= rate

	return base_value

def get_damage_value(execute_args, user, target):
	return _get_value_by_execute_args(execute_args, user, target, default_affect_rate = {'hp_affect_rate':1})

def get_cure_value(execute_args, user, target):
	return get_damage_value(execute_args, user, target)

def get_buff_value(execute_args, user, target):
	return _get_value_by_execute_args(execute_args, user, target)