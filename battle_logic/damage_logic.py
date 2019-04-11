# -*- coding:utf-8 -*-

import data
import const
import random
import battle_common

class DamageLogic(object):
	"""伤害相关代码"""

	def damage(self, user, effect, target, execute_argv):
		rate = float(execute_argv.get('rate', 1.0))
		effect_base = execute_argv.get('effect_base', 'atk')
		damage_struct = battle_common.DamageStruct(user, target, user.get_attr(effect_base))
		
		damage_struct.set_rate('defence', 1000.0/(1000 + target.get_attr("defence")))
		damage_struct.set_rate('attribute', self.get_attribute_rate(user, target, effect))

		target.sub_attr('hp', damage_struct.get_real_value())
		self.on_damage(damage_struct)
		if target.get_attr('hp') <= 0:
			self.make_entity_die(user, target)

	def on_damage(self, damage_struct):
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
