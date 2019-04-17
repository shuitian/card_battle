# -*- coding:utf-8 -*-

import data
import battle_common

class DamageLogic(object):
	"""伤害相关代码"""

	# 吸取生命
	def absorb_hp(self, user, target, value, extra_info=None):
		damage_struct = battle_common.DamageStruct(user, target, value, extra_info)

		self.apply_damage(damage_struct)
		cure_struct = battle_common.CureStruct(user, user, damage_struct.get_real_value(), extra_info)
		self.apply_cure(cure_struct)

	# 持续伤害
	def create_dot(self, user, target, value, extra_info=None):
		damage_struct = self.create_damage_struct(user, target, value, extra_info)

		self.apply_damage(damage_struct)
		return damage_struct

	# 持续治疗
	def create_hot(self, user, target, value, extra_info=None):
		cure_struct = self.create_cure_struct(user, target, value, extra_info)

		self.apply_cure(cure_struct)
		return cure_struct

	# 伤害
	def create_damage(self, user, target, effect, value, extra_info=None):
		damage_struct = self.create_damage_struct(user, target, value, extra_info)
		damage_struct = self.fill_damage_rate(damage_struct, effect)
		self.apply_damage(damage_struct)
		return damage_struct

	def create_damage_struct(self, user, target, value, extra_info):
		damage_struct = battle_common.DamageStruct(user, target, value, extra_info)
		return damage_struct

	def fill_damage_rate(self, damage_struct, effect):
		user = damage_struct.user
		target = damage_struct.target
		damage_struct.set_rate('damage_add_rate', user.get_attr('damage_add_rate', 1))
		damage_struct.set_rate('damaged_add_rate', target.get_attr('damaged_add_rate', 1))
		damage_struct.set_rate('defence', 1000.0/(1000 + target.get_attr("defence")))

		if effect:
			damage_struct.set_rate('attribute', self.get_attribute_rate(user, target, effect))
		return damage_struct

	def get_attribute_rate(self, user, target, effect):
		rate = 1.0
		for target_attr in target.role_info.attribute_list:
			rate *= getattr(data.attribute[effect.attribute], target_attr)

		return rate

	def apply_damage(self, damage_struct):
		target = damage_struct.target
		target.sub_attr('hp', damage_struct.get_real_value())
		self.on_damage(damage_struct)
		if target.get_attr('hp') <= 0:
			self.make_entity_die(damage_struct.user, target)

	def on_damage(self, damage_struct):
		pass

	def make_entity_die(self, killer, dead):
		dead.dead = True
		self.on_entity_die(killer, dead)

	def on_entity_die(self, killer, dead):
		pass

	# 治疗
	def create_cure(self, user, target, effect, value, extra_info=None):
		cure_struct = self.create_cure_struct(user, target, value, extra_info)
		cure_struct = self.fill_cure_rate(cure_struct)
		self.apply_cure(cure_struct)
		return cure_struct

	def create_cure_struct(self, user, target, value, extra_info):
		cure_struct = battle_common.CureStruct(user, target, value, extra_info)
		return cure_struct

	def fill_cure_rate(self, cure_struct):
		user = cure_struct.user
		target = cure_struct.target
		cure_struct.set_rate('cure_add_rate', user.get_attr('cure_add_rate', 1))
		cure_struct.set_rate('be_cure_add_rate', target.get_attr('be_cure_add_rate', 1))
		return cure_struct

	def apply_cure(self, cure_struct):
		cure_struct.target.add_attr('hp', cure_struct.get_real_value())
		self.on_cure(cure_struct)

	def on_cure(self, cure_struct):
		pass