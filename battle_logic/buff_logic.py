# -*- coding:utf-8 -*-

class BuffLogic(object):
	"""状态相关代码"""

	def add_buff_to_target(self, user, target, buff_id, turn, user_property=None):
		'''
			给单个目标增加一个状态
			Args:
				user:是由哪个角色添加的,为None表示target自身添加
				target:目标
				buff_id:状态ID
				turn:状态的回合数
				user_property:施法者参数
		'''
		if not target:
			return
		if not buff_id:
			return
		if not turn:
			return

		turn = int(turn)
		if turn < 1:
			return
		if not user:
			user = target

		extra_info = {}
		if user_property:
			extra_info.update({'user_property':user_property})

		self._raw_add_buff_to_target(target, buff_id, turn, user.eid, extra_info)

	def _raw_add_buff_to_target(self, target, buff_id, turn, eid, extra_info):
		'''真正地给一个角色加状态，不触发额外的逻辑'''
		buff_obj = target.find_buff_obj(buff_id)
		if buff_obj:
			can_refresh = target.can_refresh(buff_obj, extra_info)
			if not can_refresh:
				self.on_add_buff_failed(target, buff_obj)
				return
		else:
			can_refresh = False

		buff_obj = target.add_buff(buff_id, turn, eid, extra_info)
		if can_refresh:
			self.on_refresh_buff(target, buff_obj)
		else:
			self.on_add_buff(target, buff_obj)

	def reduce_buff_turn(self, target, turn):
		remove_buff_ids = []
		for buff_obj in target.iter_buff_obj():
			if buff_obj.turn <= turn:
				remove_buff_ids.append(buff_obj.buff_id)
			else:
				buff_obj.turn -= turn
		
		for buff_id in remove_buff_ids:
			self.remove_buff_from_target(target, buff_id)

	def remove_buff_from_target(self, target, buff_id):
		'''
			给单个目标删除一个状态
			Args:
				target:目标
				buff_id:状态ID
		'''
		buff_obj = target.find_buff_obj(buff_id)
		if not buff_obj:
			return

		target.del_buff(buff_id)

		self.on_remove_buff(target, buff_obj)

	def on_add_buff_failed(self, target, buff_obj):
		pass

	def on_add_buff(self, target, buff_obj):
		pass

	def on_refresh_buff(self, target, buff_obj):
		pass

	def on_remove_buff(self, target, buff_obj):
		pass
