# -*- coding:utf-8 -*-

import random
import battle_common

class SkillLogic(object):
	"""技能相关代码"""

	def use_skill(self, user, skill_id):
		skill_struct = battle_common.SkillStruct(user, skill_id)
		# 如果技能需要准备
		skill = skill_struct.skill
		if skill.prepare_round > 0:
			self.use_prepare_skill(skill_struct)
			return

		if skill_struct.is_miss():
			return

		self.real_use_skill(skill_struct)

	def use_prepare_skill(self, skill_struct):
		skill = skill_struct.skill
		if skill.left_round == 0:
			if not skill_struct.is_miss():
				self.start_preapre(skill_struct)
			return

		skill.left_round -= 1
		if skill.left_round == 0:
			self.real_use_skill(skill_struct)
		else:
			self.continue_preapre(skill_struct)

	def start_preapre(self, skill_struct):
		skill_struct.skill.left_round = skill_struct.skill.prepare_round
		self.on_prepare_skill(skill_struct)

	def continue_preapre(self, skill_struct):
		self.on_continue_preapre(skill_struct)

	def on_prepare_skill(self, skill_struct):
		pass

	def on_before_real_use_skill(self, skill_struct):
		pass
	
	def real_use_skill(self, skill_struct):
		self.on_before_real_use_skill(skill_struct)
		effect_list = skill_struct.skill.skill_effect_list
		if not effect_list:
			return
		for effect_id in effect_list:
			effect_struct = battle_common.EffectStruct(skill_struct.user, skill_struct.skill_id, effect_id)
			self.calc_one_skill_effect(effect_struct)
		self.one_after_use_skill(skill_struct)

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

		if not targets:
			self.on_not_exist_targets(effect_struct)
			return

		for execute_info in execute_infos:
			for target in effect_struct.targets:
				if target.dead:
					continue
				self.calc_one_target_effect(user, effect, target, execute_info)

	def on_not_exist_targets(self, effect_struct):
		pass

	def get_skill_target(self, user, effect):
		target_func = effect.target_func
		target_num = max(effect.target_num,1)
		distance = effect.distance
		targets = []
		for target in self.iter_undead_entity_infos():
			if not user.have_state('charm'):
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
			entity = self.get_entity_by_pos(pos)
			dis += bool(entity and not entity.dead)
		return dis

	def calc_one_target_effect(self, user, effect, target, execute_info):
		hit = self.check_hit(user, effect, target)
		if not hit:
			self.on_effect_not_hit(user, effect, target)
			return
		execute_type, execute_argv = execute_info
		if not execute_type:
			return
		func = getattr(self, 'execute_type_%s'%execute_type)
		func(user, effect, target, execute_argv)

	def check_hit(self, user, effect, target):
		if user == target:
			return True
		hit_rate = user.get_attr('hit_rate', 1)
		r = random.random()
		return r < hit_rate

	def on_effect_not_hit(self, user, effect, target):
		pass