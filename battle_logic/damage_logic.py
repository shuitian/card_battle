# -*- coding:utf-8 -*-

import data
import battle_common

class DamageLogic(object):
	"""伤害相关代码"""

	def apply_damage(self, damage_struct):
		target = damage_struct.target
		target.sub_attr('hp', damage_struct.get_real_value())
		self.on_damage(damage_struct)
		if target.get_attr('hp') <= 0:
			self.make_entity_die(damage_struct.user, target)

	def apply_cure(self, cure_struct):
		cure_struct.target.add_attr('hp', cure_struct.get_real_value())
		self.on_cure(cure_struct)

	def absorb_hp(self, user, target, value, extra_info=None):
		damage_struct = battle_common.DamageStruct(user, target, value, extra_info)

		self.apply_damage(damage_struct)

		cure_struct = battle_common.CureStruct(user, user, damage_struct.get_real_value(), extra_info)
		self.apply_cure(cure_struct)

	def create_damage(self, user, target, effect, value, extra_info=None):
		damage_struct = battle_common.DamageStruct(user, target, value, extra_info)

		damage_struct.set_rate('defence', 1000.0/(1000 + target.get_attr("defence")))
		damage_struct.set_rate('attribute', self.get_attribute_rate(user, target, effect))

		self.apply_damage(damage_struct)

	def create_cure(self, user, target, effect, value, extra_info=None):
		cure_struct = battle_common.CureStruct(user, target, value, extra_info)
		
		self.apply_cure(cure_struct)

	def on_damage(self, damage_struct):
		pass

	def on_cure(self, cure_struct):
		pass

	def make_entity_die(self, killer, dead):
		dead.dead = True
		self.on_entity_die(killer, dead)

	def on_entity_die(self, killer, dead):
		pass

	def get_attribute_rate(self, user, target, effect):
		rate = 1.0
		for target_attr in target.role_info.attribute_list:
			rate *= getattr(data.attribute[effect.attribute], target_attr)

		return rate
