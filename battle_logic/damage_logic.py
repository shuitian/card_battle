# -*- coding:utf-8 -*-

import const
import random

class DamageLogic(object):
	"""伤害相关代码"""

	def damage(self, user, effect, target, execute_argv):
		rate = float(execute_argv.get('rate', 1.0))
		effect_base = execute_argv.get('effect_base', 'atk')
		_damage = user.get_attr(effect_base) * 1000.0/(1000 + target.get_attr("defence"))
		target.sub_attr('hp', _damage)

		self.on_damage(user, target, _damage)

	def on_damage(self, user, target, _damage):
		pass