# -*- coding:utf-8 -*-

import random
from utils import utils

class EffectLogic(object):
	"""技能效果相关代码"""

	def execute_type_add_buff(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_buff_value(execute_args, user, target)
		
		self.add_buff_to_target(user, target, buff_id, turn, value)

	def execute_type_damage(self, user, effect, target, execute_args):
		be_evade = self.check_evade(user, effect, target)
		if be_evade:
			self.on_damage_be_evade(user, effect, target)
			return

		value = utils.get_damage_value(execute_args, user, target)

		self.create_damage(user, target, effect, value)

	def execute_type_cure(self, user, effect, target, execute_args):
		rate = float(execute_args.get('rate', 1.0))
		effect_base = execute_args.get('effect_base', 'atk')

		value = utils.get_cure_value(execute_args, user, target)

		self.create_cure(user, target, effect, value)

	def execute_type_add_dot(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_damage_value(execute_args, user, target)

		damage_struct = self.create_damage_struct(user, target, value, {})
		damage_struct = self.fill_damage_rate(damage_struct, effect)

		user_property = damage_struct.get_expect_value()
		self.add_buff_to_target(user, target, buff_id, turn, user_property)

	def execute_type_add_hot(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_cure_value(execute_args, user, target)

		cure_struct = self.create_cure_struct(user, target, value, {})
		user_property = cure_struct.get_expect_value()

		self.add_buff_to_target(user, target, buff_id, turn, user_property)

	def check_evade(self, user, effect, target):
		evade_rate = user.get_attr('evade_rate', 0)
		r = random.random()
		return r < evade_rate

	def on_damage_be_evade(self, user, effect, target):
		pass
