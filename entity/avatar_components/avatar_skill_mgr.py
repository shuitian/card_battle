# -*- coding:utf-8 -*-

import data
import random
from utils import utils
from passive_effect import PassiveEffect

class skill(object):

	def __init__(self, skill_id, owner):
		super(skill, self).__init__()
		self.skill_id = skill_id
		self.owner = owner
		self.skill_data = data.skill[self.skill_id]
		self.left_round = 0

		if self.passive_args:
			self.passive_effect = PassiveEffect(self.owner.battle, self.owner, self.passive_args)

	def destroy(self):
		if self.passive_effect:
			self.passive_effect.destroy()
		self.owner = None
		self.skill_data = None

	def __getattr__(self, name):
		value = self.skill_data.get(name)
		setattr(self, name, value)

		return value

class AvatarSkillMgr(object):
	"""战斗角色技能管理器"""
	
	def init(self):
		self.skills = {}

	def setup_skills(self):
		# 添加默认技能
		default_skill = self.role_info.default_skill
		default_skill and self.add_skill(default_skill)

		# 添加技能列表
		for skill_id in self.role_info.skill_list or []:
			self.add_skill(skill_id)

	def add_skill(self, skill_id):
		_skill = skill(skill_id, self)
		self.skills[skill_id] = _skill

	def do_action(self, current_round):
		if self.have_state('confusion'):
			self.battle.on_pass_action(self, current_round)
			self.interrupt_prepare_skills()
			return 

		skill_ids = self.skills.keys()
		if not skill_ids:
			return

		random.shuffle(skill_ids)
		for skill_id in skill_ids:
			if self.battle.is_finish:
				continue
			_skill = self.get_skill(skill_id)
			if _skill.passive_flag:
				continue
			if self.have_state('confusion'):
				self.battle.on_pass_action(self, current_round)
				self.interrupt_prepare_skills()
				return 
			self.battle.use_skill(self, skill_id)

	def get_skill(self, skill_id):
		return self.skills.get(skill_id, None)

	def interrupt_prepare_skills(self):
		skills = []
		for skill in self.skills.itervalues():
			if skill.left_round:
				skill.left_round = 0
				skills.append(skill)
		self.battle.on_interrupt_prepare_skills(self, skills)