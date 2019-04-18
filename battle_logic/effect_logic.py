# -*- coding:utf-8 -*-

import const
import random
from utils import utils

class EffectLogic(object):
	"""技能效果相关代码"""

	def execute_type_add_buff(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_value_by_execute_args(execute_args, user, target)
		
		self.add_buff_to_target(user, target, buff_id, turn, value)

	def execute_type_damage(self, user, effect, target, execute_args):
		hit = self.check_hit(user, effect, target)
		if not hit:
			self.on_effect_not_hit(user, effect, target)
			return

		be_evade = self.check_evade(user, effect, target)
		if be_evade:
			self.on_damage_be_evade(user, effect, target)
			return

		value = utils.get_value_by_execute_args(execute_args, user, target)

		_damage_struct = self.create_damage(user, target, effect, value)

		absorb_hp_rate = float(execute_args.get('absorb_hp_rate', 0))
		if absorb_hp_rate:
			_real_value = _damage_struct.get_real_value()

			self.create_cure(user, user, effect, _real_value * absorb_hp_rate)

	def execute_type_cure(self, user, effect, target, execute_args):
		rate = float(execute_args.get('rate', 1.0))
		effect_base = execute_args.get('effect_base', 'atk')

		value = utils.get_value_by_execute_args(execute_args, user, target)

		self.create_cure(user, target, effect, value)

	def execute_type_add_dot(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_value_by_execute_args(execute_args, user, target)

		damage_struct = self.create_damage_struct(user, target, value, {})
		damage_struct = self.fill_damage_rate(damage_struct, effect)

		user_property = damage_struct.get_expect_value()
		self.add_buff_to_target(user, target, buff_id, turn, user_property)

	def execute_type_add_hot(self, user, effect, target, execute_args):
		buff_id = int(execute_args.get('buff_id'))
		turn = int(execute_args.get('turn', 1))

		value = utils.get_value_by_execute_args(execute_args, user, target)

		cure_struct = self.create_cure_struct(user, target, value, {})
		user_property = cure_struct.get_expect_value()

		self.add_buff_to_target(user, target, buff_id, turn, user_property)

	def execute_type_remove_buff(self, user, effect, target, execute_args):
		buff_tag = int(execute_args.get('buff_tag'))
		buff_number = int(execute_args.get('buff_number', 0))


		buff_ids = target.get_buff_ids_by_tag(buff_tag)
		if not buff_ids:
			return

		number = len(buff_ids)
		if buff_number:
			number = min(buff_number, number)

		del_buff_ids = random.sample(buff_ids, number)
		for buff_id in del_buff_ids:
			self.remove_buff_from_target(user, target, buff_id, const.REASON_EFFECT)
