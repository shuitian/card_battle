# -*- coding:utf-8 -*-

from entity import avatar

class BattleEntityMgr(object):
	"""战斗角色信息管理"""
	def init(self):
		self.entity_infos = {}

	def create_entity_infos(self):
		entity_infos = self.battle_info.get('entity_infos',{})
		for eid, entity_info in entity_infos.iteritems():
			self.create_entity_info(eid, entity_info)

	def create_entity_info(self, eid, entity_info):
		_avatar = avatar.AvatarInfo(self, eid, entity_info)
		self.entity_infos[_avatar.eid] = _avatar

	def on_next_round(self, current_round):
		_entity = self.get_next_action_entity(current_round)
		while _entity:
			_entity.action(current_round)
			_entity = self.get_next_action_entity(current_round)

	def get_next_action_entity(self, current_round):
		infos = []
		for _entity in self.entity_infos.itervalues():
			if _entity.action_round == current_round:
				continue
			infos.append((_entity.get_attr('speed'), _entity.eid, _entity))
		
		infos.sort(reverse=True)
		return infos[0][-1] if infos else None

	def on_action(self, avatar_info, current_round):
		pass

	def on_end_battle(self):
		for _entity in self.entity_infos.itervalues():
			_entity.destroy()
		self.entity_infos = {}