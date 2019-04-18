# -*- coding:utf-8 -*-

import data
import random
from utils import utils

class PassiveEffect(object):

	def __init__(self, battle, user, passive_args, extra_info=None):
		super(PassiveEffect, self).__init__()
		self.battle = battle
		self.user = user
		self.passive_args = passive_args
		self.extra_info = extra_info or {}

		self.target = self.user

		self.execute_time = self.passive_args.get('execute_time')
		self.execute_task = self.passive_args.get('execute_task')
		self.battle.register_event(self.execute_time, self.on_event)

	def destroy(self):
		self.battle.unregister_event(self.execute_time, self.on_event)
		self.battle = None
		self.user = None
		self.skill_data = None

	def on_event(self, *args, **kwds):
		trigger_func = getattr(self, '%s_trigger_check'%self.execute_time)
		is_check_pass = trigger_func(*args, **kwds)
		if not is_check_pass:
			return

		execute_task = self.passive_args.get('execute_task')
		func = getattr(self.battle, 'execute_task_%s'%execute_task)
		func(self.user, self.target, self.passive_args, self.extra_info)

	def battle_prepare_trigger_check(self, *args, **kwds):
		return True

	def round_start_trigger_check(self, *args, **kwds):
		return True

	def before_action_trigger_check(self, avatar, *args, **kwds):
		return avatar == self.user

class BuffPassiveEffect(PassiveEffect):

	def __init__(self, battle, user, passive_args, buff_obj, value):
		super(BuffPassiveEffect, self).__init__(battle, user, passive_args)
		self.buff_obj = buff_obj
		self.value = value

		self.user = self.battle.get_entity(buff_obj.eid)
		self.target = user

		self.extra_info.update({'buff_obj':buff_obj,'value':value})

	def before_action_trigger_check(self, avatar, *args, **kwds):
		return avatar == self.target