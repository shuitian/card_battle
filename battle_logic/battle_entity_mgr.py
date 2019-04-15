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

		self.execute_tasks = {} # execute_time : [task_info, task_info]

	def add_execute_task(self, user, target, execute_args, extra_info):
		execute_time = execute_args.get('execute_time')
		task_info = user, target, execute_args, extra_info
		self.execute_tasks.setdefault(execute_time, []).append(task_info)

	def remove_execute_task(self, execute_time, task_info):
		if execute_time not in self.execute_tasks:
			return

		task_info_list = self.execute_tasks[execute_time]
		if task_info in task_info_list:
			task_info_list.remove(task_info)

	def get_entity_by_pos(self, pos):
		return self.pos_infos[pos]

	def get_entity(self, eid):
		return self.entity_infos.get(eid, None)

	def create_entity_infos(self):
		entity_infos = self.battle_info.get('entity_infos',{})
		for eid, entity_info in entity_infos.iteritems():
			self.create_entity_info(eid, entity_info)

		self.left_infos = self.pos_infos[:3]
		self.right_infos = self.pos_infos[3:]

	def create_entity_info(self, eid, entity_info):
		_avatar = avatar.AvatarInfo(self, eid, entity_info)
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

	def on_event(self, event_name):
		func = getattr(self, 'on_event_%s'%event_name, None)
		func and func()
		task_list = self.execute_tasks.get(event_name, [])
		for task_info in task_list:
			user, target, execute_args, extra_info = task_info
			execute_task = execute_args.get('execute_task')
			func = getattr(self, 'execute_task_%s'%execute_task)
			func(user, target, execute_args, extra_info)

	def on_start_action(self, avatar):
		pass

	def on_action(self, avatar):
		self.reduce_buff_turn(avatar, 1)

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

		if self.right_infos[0].dead:
			self.winner = const.WINNER_LEFT
			return True