# -*- coding:utf-8 -*-

import random
class EffectLogic(object):
	"""技能效果相关代码"""

	def execute_type_add_buff(self, user, effect, target, execute_argv):
		buff_id = int(execute_argv.get('buff_id'))
		turn = int(execute_argv.get('turn', 1))

		base_value = float(execute_argv.get('base_value', 0))

		rate = float(execute_argv.get('rate', 1.0))
		user_property = base_value * rate
		self.add_buff_to_target(user, target, buff_id, turn, user_property)

	def execute_type_damage(self, user, effect, target, execute_argv):
		be_evade = self.check_evade(user, effect, target)
		if be_evade:
			self.on_damage_be_evade(user, effect, target)
			return

		rate = float(execute_argv.get('rate', 1.0))
		effect_base = execute_argv.get('effect_base', 'atk')
		self.create_damage(user, target, effect, user.get_attr(effect_base) * rate)

	def execute_type_cure(self, user, effect, target, execute_argv):
		rate = float(execute_argv.get('rate', 1.0))
		effect_base = execute_argv.get('effect_base', 'atk')
		self.create_cure(user, target, effect, user.get_attr(effect_base) * rate)

	def check_evade(self, user, effect, target):
		evade_rate = user.get_attr('evade_rate', 0)
		r = random.random()
		return r < evade_rate

	def on_damage_be_evade(self, user, effect, target):
		pass
