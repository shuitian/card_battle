# -*- coding:utf-8 -*-

import data
import const
import gworld

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
	if float(int(value)) == float(value):
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
	
def get_value_by_execute_args(execute_args, user, target):
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

	return base_value

def create_card(card_id, level=1):
	from entity.player_components import card
	uuid = gworld.gen_object_id()
	_card = card.Card(uuid, card_id, level)
	random_card_ability(_card)
	return _card

def random_card_ability(card):
	import random
	card.set_hp_level(random.randint(1,10))
	card.set_atk_level(random.randint(1,10))
	card.set_defence_level(random.randint(1,10))
	card.set_speed_level(random.randint(1,10))

	card.set_hp_level(10)
	card.set_atk_level(10)
	card.set_defence_level(10)
	card.set_speed_level(10)

	# card.set_hp_level(1)
	# card.set_atk_level(1)
	# card.set_defence_level(1)
	# card.set_speed_level(1)