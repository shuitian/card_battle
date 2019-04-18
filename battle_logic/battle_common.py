# -*- coding:utf-8 -*-

import data
import random

skill_event_list = (

'BATTLE_PREPARE', # 战斗准备
'ROUND_START', # 回合开始
'BEFORE_ACTION', # 行动前

)

for key in skill_event_list:
 	locals()[key] = key.lower()


class SkillStruct(object):
	"""技能释放结构"""
	def __init__(self, user, skill_id):
		super(SkillStruct, self).__init__()
		self.user = user
		self.skill_id = skill_id
		self.skill = user.get_skill(skill_id)
		self._is_miss = None

	def is_miss(self):
		if self._is_miss is None:
			self._is_miss = random.random() >= self.skill.trigger_prob
		return self._is_miss

class EffectStruct(object):
	"""技能效果数据结构"""
	def __init__(self, user, skill_id, effect_id):
		super(EffectStruct, self).__init__()
		self.user = user
		self.skill_id = skill_id
		self.skill = user.get_skill(skill_id)
		self.effect_id = effect_id
		self.effect = data.skill_effect[self.effect_id]

		self.targets = []

	def set_targets(self, targets):
		self.targets = targets

class HpStruct(object):
	"""生命值变化数据结构"""
	def __init__(self, user, target, base_value, extra_info):
		super(HpStruct, self).__init__()
		self.user = user
		self.target = target
		self._base_value = base_value
		self.extra_info = extra_info

		self.rates = {}
		self._real_value = None

	def get_base_value(self):
		return self._base_value

	def get_real_value(self):
		if self._real_value:
			return self._real_value

		self._real_value = self._get_real_value()
		self._real_value = int(self._real_value)
		return self._real_value

	def _get_real_value(self):
		return self.get_expect_value()

	def get_expect_value(self):
		value = self.get_base_value()
		if not value:
			return 0

		for rate in self.rates.itervalues():
			if rate == 0:
				return 0
			value = value * rate

		return max(int(round(value)), 1)

	def set_rate(self, name, rate):
		self.rates[name] = rate

class DamageStruct(HpStruct):
	"""伤害数据结构"""
	
	def _get_real_value(self):
		value = super(DamageStruct, self)._get_real_value()
		value = min(value, self.target.get_attr('hp'))
		return value
	

class CureStruct(HpStruct):
	"""治疗数据结构"""

	def _get_real_value(self):
		value = super(CureStruct, self)._get_real_value()
		value = min(self.target.get_attr("max_hp") - self.target.get_attr("hp"), value)
		return value