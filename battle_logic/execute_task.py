# -*- coding:utf-8 -*-
import battle_common

class ExecuteTask(object):
	"""被动技能和状态的执行效果"""

	def execute_task_absorb_hp(self, user, target, execute_args, extra_info):
		if target.dead or user.dead:
			return
		self.absorb_hp(user, target, extra_info.get('value', None), extra_info = extra_info)

	def execute_task_execute_skill(self, user, target, execute_args, extra_info):
		if user.dead:
			return
		skill_id = int(execute_args.get('execute_id'))
		skill_struct = battle_common.SkillStruct(user, skill_id)

		self.real_use_skill(skill_struct)