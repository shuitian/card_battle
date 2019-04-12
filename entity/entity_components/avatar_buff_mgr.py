# -*- coding:utf-8 -*-

import data

class buff_obj(object):
	"""单个buff对象"""

	def __init__(self, buff_id, turn, extra_info = None):
		super(buff_obj, self).__init__()
		self.buff_id = buff_id # 状态ID
		self.turn = turn # 状态回合数
		self.eid = None # 施法者eid
		self.extra_info = extra_info or {}
		self.user_property = 0 # 施法者参数
		self.buff_data = data.buff[self.buff_id]
		self.deal_extra_info()

	def deal_extra_info(self):
		if not self.extra_info:
			return

		for key, value in self.extra_info.iteritems():
			setattr(self, key, value)

	def merge_buff(self, new_buff_obj):
		assert self.buff_id == new_buff_obj.buff_id
		self.user_property = max(self.user_property, new_buff_obj.user_property)
		
		self.extra_info.update(new_buff_obj.extra_info)
		if 'user_property' in self.extra_info:
			self.extra_info['user_property'] = self.user_property

	def show(self):
		print 'buff:%s  turn:%s  eid:%s' % (self.buff_id, self.turn, self.eid)
		print "user_property",self.user_property
		print 'extra_info',self.extra_info

class AvatarBuffMgr(object):
	"""战斗角色状态管理"""
	
	def init(self):
		self.buffs =  {} # buff_id : buff_obj
		self.states = {} # control_name : [buff_obj,]

	def iter_buff_obj(self):
		for buff_obj in self.buffs.itervalues():
			yield buff_obj

	def find_buff_obj(self, buff_id):
		return self.buffs.get(buff_id, None)

	def can_refresh(self, buff_obj, extra_info):
		user_property = extra_info.get('user_property', 0)
		return buff_obj.buff_data.buff_refresh and buff_obj.user_property < user_property

	def add_buff(self, buff_id, turn, extra_info):
		add_buff_obj = buff_obj(buff_id, turn, extra_info)
		_buff_obj = self.find_buff_obj(buff_id)
		if _buff_obj:
			_buff_obj.merge_buff(add_buff_obj)
		else:
			self.buffs[buff_id] = add_buff_obj
			_buff_obj = add_buff_obj

		self.update_special_effect(_buff_obj)
		return _buff_obj

	def update_special_effect(self, buff_obj):
		special_effect = buff_obj.buff_data.special_effect
		func = getattr(self, 'special_effect_%s'%special_effect)
		func(buff_obj)

	def get_buff_value(self, buff_obj):
		special_effect_args = buff_obj.buff_data.special_effect_args
		attr = special_effect_args.get('attr', None)
		if not attr:
			return None, None


		base_value = special_effect_args.get('base_value', None)
		if not base_value:
			base_value = buff_obj.user_property

		max_value = special_effect_args.get('max_value',None)
		if max_value:
			base_value = max(base_value, max_value)	
		min_value = special_effect_args.get('min_value',None)
		if min_value:
			base_value = min(base_value, min_value)
		return attr, base_value

	def special_effect_add_attr(self, buff_obj):
		attr, value = self.get_buff_value(buff_obj)
		if not attr:
			return

		self.remove_attr_modifier(attr, buff_obj)
		if value:
			self.set_attr_modifier(attr, buff_obj, value)

	def special_effect_sub_attr(self, buff_obj):
		attr, value = self.get_buff_value(buff_obj)
		if not attr:
			return
			
		self.remove_attr_modifier(attr, buff_obj)
		if value:
			self.set_attr_modifier(attr, buff_obj, -value)

	def special_effect_add_control(self, buff_obj):
		special_effect_args = buff_obj.buff_data.special_effect_args
		effect_name = special_effect_args.get('effect', None)
		self.states.setdefault(effect_name, []).append(buff_obj)

	def get_buff_exist_desc(self, buff_obj):
		return self._get_buff_desc(buff_obj, buff_obj.buff_data.exist_desc)

	def get_buff_add_desc(self, buff_obj):
		return self._get_buff_desc(buff_obj, buff_obj.buff_data.add_desc)

	def get_buff_desc(self, buff_obj):
		return self._get_buff_desc(buff_obj, buff_obj.buff_data.desc)

	def _get_buff_desc(self, buff_obj, desc):
		if not desc:
			return desc

		desc = desc.replace('$value$', str(self.get_buff_value(buff_obj)[1]))
		attr_dict = {
			u'$攻击':'atk',
			u'$防御':'defence',
			u'$速度':'speed',
		}
		for text, attr in attr_dict.iteritems():
			desc = desc.replace(text, str(self.get_attr(attr)))
		return desc

	def on_action(self, current_round):
		self.battle.reduce_buff_turn(self, 1)
		# 减少回合数

	def del_buff(self, buff_id):
		buff_obj = self.buffs.pop(buff_id)

		special_effect_args = buff_obj.buff_data.special_effect_args
		attr = special_effect_args.get('attr', None)
		if attr:
			self.remove_attr_modifier(attr, buff_obj)

		effect_name = special_effect_args.get('effect', None)
		if effect_name and effect_name in self.states:
			self.states[effect_name].remove(buff_obj)

	def have_state(self, state_name):
		return self.states.get(state_name, None)