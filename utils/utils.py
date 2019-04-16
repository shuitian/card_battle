# -*- coding:utf-8 -*-

import data

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