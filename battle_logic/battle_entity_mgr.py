# -*- coding:utf-8 -*-

import const
from entity import avatar

class BattleEntityMgr(object):
	"""战斗角色信息管理"""
	def init(self):
		self.entity_infos = {}
		self.pos_infos = [None]*6
		self.left_infos = [None]*3
		self.right_infos = [None]*3

	def get_entity_by_pos(self, pos):
		return self.pos_infos[pos]

	def get_entity(self, eid):
		return self.entity_infos.get(eid, None)

	def create_entity_infos(self):
		entity_infos = self.battle_info.get('entity_infos',{})
		for eid, attrs in entity_infos.iteritems():
			self.create_entity_info(eid, attrs)

		self.left_infos = self.pos_infos[:3]
		self.right_infos = self.pos_infos[3:]

	def create_entity_info(self, eid, attrs):
		_avatar = avatar.AvatarInfo(self, eid, attrs)
		self.entity_infos[_avatar.eid] = _avatar
		self.pos_infos[_avatar.get_attr('pos')] = _avatar

	def on_next_round(self, current_round):
		self.on_event('round_start')
		_entity = self.get_next_action_entity(current_round)
		while _entity and not self.is_finish:
			self.on_start_action(_entity)
			_entity.action(current_round)
			self.on_action(_entity)
			_entity = self.get_next_action_entity(current_round)

	def on_start_action(self, avatar):
		self.on_event('before_action', avatar)

	def on_action(self, avatar):
		self.reduce_buff_turn(avatar, avatar, 1, const.REASON_TIME)

	def get_next_action_entity(self, current_round):
		infos = []
		for _entity in self.iter_undead_entity_infos():
			if _entity.action_round == current_round:
				continue
			infos.append((_entity.get_attr('speed'), _entity.eid, _entity))
		
		infos.sort(reverse=True)
		return infos[0][-1] if infos else None

	def iter_undead_entity_infos(self):
		for _entity in self.entity_infos.itervalues():
			if _entity.dead:
				continue
			yield _entity

	def destroy(self):
		for _entity in self.entity_infos.itervalues():
			_entity.destroy()
		self.entity_infos = {}

	def on_entity_die(self, killer, dead):
		is_end = self.check_battle_end()
		if is_end:
			self.end_battle()

	def check_battle_end(self):
		if self.left_infos[0].dead:
			self.winner = const.WINNER_RIGHT
			return True

		if self.right_infos[-1].dead:
			self.winner = const.WINNER_LEFT
			return True
	
	def setup_skills(self):
		infos = []
		for _entity in self.iter_undead_entity_infos():
			infos.append((_entity.get_attr('speed'), _entity.eid, _entity))
		
		infos.sort(reverse=True)
		for _, _, info in infos:
			info.setup_skills()