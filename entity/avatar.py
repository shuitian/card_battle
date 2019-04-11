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
		self.init()

	def init(self):
		pass

	def get_attr(self, name):
		return self.attrs.get(name, None)

	def sub_attr(self, name, value):
		self.set_attr(name, max(self.get_attr(name) - value,0))

	def set_attr(self, name, value):
		self.attrs[name] = value

	def action(self, current_round):
		self.action_round = current_round
		self.do_action(current_round)
		self.battle.on_action(self, current_round)

	def do_action(self, current_round):
		pass

	def destroy(self):
		self.battle = None
		self.attrs = None