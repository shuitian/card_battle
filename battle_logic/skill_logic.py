# -*- coding:utf-8 -*-

import data
import const
import random

class SkillLogic(object):
	"""技能相关代码"""

	def use_skill(self, user, skill):
		r = random.random()
		if r >= skill.trigger_prob:
			return

		self.real_use_skill(user, skill)
	
	def real_use_skill(self, user, skill):
		effect_list = skill.skill_effect_list
		if not effect_list:
			return
		for effect_id in effect_list:
			self.calc_one_skill_effect(user, effect_id)

	def calc_one_skill_effect(self, user, effect_id):
		effect = data.skill_effect[effect_id]

		execute_infos = effect.execute_infos
		if not execute_infos:
			return

		for execute_info in execute_infos:
			self.calc_one_execute_info(user, effect, execute_info)
	
	def calc_one_execute_info(self, user, effect, execute_info):
		targets = self.get_skill_target(user, effect, execute_info)
		for target in targets:
			self.calc_one_target_effect(user, effect, target, execute_info)

	def get_skill_target(self, user, effect, execute_info):
		print '         execute_info',execute_info
		execute_type, target_func, execute_argv = execute_info
		distance = float(execute_argv.get('distance', 1))
		targets = []
		for target in self.entity_infos.itervalues():
			func = getattr(user, target_func)
			if not func(target):
				continue
			dis = self.calc_distance(user, target)
			if dis > distance:
				continue
			targets.append(target)

		if not targets:
			return targets

		target_num = int(execute_argv.get('target_num', 1))
		if not target_num or target_num >= len(targets):
			return targets

		return random.sample(targets, target_num)
	
	def calc_distance(self, user, target):
		return abs(user.get_attr('pos') - target.get_attr('pos'))

	def calc_one_target_effect(self, user, effect, target, execute_info):
		execute_type, target_func, execute_argv = execute_info
		func = getattr(self, execute_type)
		func(user, effect, target, execute_argv)
