# -*- coding:utf-8 -*-

import data
import const
import random
import battle_common

class SkillLogic(object):
	"""技能相关代码"""

	def use_skill(self, user, skill_id):
		skill_struct = battle_common.SkillStruct(user, skill_id)
		if skill_struct.is_miss():
			return
		
		self.on_before_use_skill(skill_struct)
		self.real_use_skill(skill_struct)
		self.one_after_use_skill(skill_struct)

	def on_before_use_skill(self, skill_struct):
		pass
	
	def real_use_skill(self, skill_struct):
		effect_list = skill_struct.skill.skill_effect_list
		if not effect_list:
			return
		for effect_id in effect_list:
			effect_struct = battle_common.EffectStruct(skill_struct.user, skill_struct.skill_id, effect_id)
			self.calc_one_skill_effect(effect_struct)

	def one_after_use_skill(self, skill_struct):
		pass

	def calc_one_skill_effect(self, effect_struct):
		user = effect_struct.user
		effect = effect_struct.effect
		execute_infos = effect.execute_infos
		if not execute_infos:
			return

		targets = self.get_skill_target(user, effect)
		effect_struct.set_targets(targets)

		for execute_info in execute_infos:
			for target in effect_struct.targets:
				if target.dead:
					continue
				self.calc_one_target_effect(user, effect, target, execute_info)

	def get_skill_target(self, user, effect):
		target_func = effect.target_func
		target_num = max(effect.target_num,1)
		distance = effect.distance
		targets = []
		for target in self.iter_undead_entity_infos():
			func = getattr(user, target_func)
			if not func(target):
				continue
			dis = self.calc_distance(user, target)
			if dis > distance:
				continue
			targets.append(target)

		if not targets:
			return targets

		if target_num >= len(targets):
			return targets

		return random.sample(targets, target_num)
	
	def calc_distance(self, user, target):
		pos_1 = user.get_attr('pos')
		pos_2 = target.get_attr('pos')
		if pos_1 > pos_2:
			pos_1, pos_2 = pos_2, pos_1

		dis = 1
		for pos in xrange(pos_1+1, pos_2):
			dis += not self.get_entity_by_pos(pos).dead
		return dis

	def calc_one_target_effect(self, user, effect, target, execute_info):
		execute_type, execute_argv = execute_info
		if not execute_type:
			return
		func = getattr(self, 'execute_type_%s'%execute_type)
		func(user, effect, target, execute_argv)
