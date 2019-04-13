# -*- coding:utf-8 -*-

import data
import base_entity
import entity_components
from utils.class_utils import components

@components(*entity_components.import_all())
class AvatarInfo(base_entity.BaseEntity):
	"""战斗角色"""
	def __init__(self, battle, eid, attrs):
		super(AvatarInfo, self).__init__()
		self.battle = battle
		self.eid = eid
		self.attrs = attrs
		self.action_round = 0

		self.role_id = self.attrs.get('role_id')
		self.role_info = data.role_info[self.role_id]
		self.level = self.attrs.get('level', 1)
		self.dead = False

		self.attr_modifiers = {} # {'atk':{m_type:v1}}
		self.init()

	def init(self):
		pass

	def set_attr_modifier(self, name, m_type, value):
		_data = self.attr_modifiers.setdefault(name, {})
		_data[m_type] = value

	def remove_attr_modifier(self, name, m_type):
		if name not in self.attr_modifiers:
			return

		_data = self.attr_modifiers[name]
		if m_type in _data:
			del _data[m_type]

		if not self.attr_modifiers[name]:
			del self.attr_modifiers[name]

	def get_attr(self, name):
		base_value = self.attrs[name]
		_data = self.attr_modifiers.get(name, {})
		for change_value in _data.itervalues():
			base_value += change_value
		return max(base_value, 0)

	def sub_attr(self, name, value):
		self.set_attr(name, max(self.get_attr(name) - value,0))

	def add_attr(self, name, value):
		self.set_attr(name, self.get_attr(name) + value)

	def set_attr(self, name, value):
		self.attrs[name] = value

	def action(self, current_round):
		self.action_round = current_round
		self.do_action(current_round)

	def do_action(self, current_round):
		pass

	def destroy(self):
		self.battle = None
		self.attrs = None