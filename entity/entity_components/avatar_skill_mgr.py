# -*- coding:utf-8 -*-

import data
from utils import utils

class skill(object):

	def __init__(self, skill_id, owner):
		self.skill_id = skill_id
		self.owner = owner
		self.skill_data = data.skill[self.skill_id]

	def destroy(self):
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
		self.setup_skills()

	def setup_skills(self):
		# 添加主动技能
		for skill_id in self.role_info.skill_list:
			self.add_skill(skill_id)

	def add_skill(self, skill_id):
		_skill = skill(skill_id, self)
		self.skills[skill_id] = _skill

	def do_action(self, current_round):
		for skill in self.skills.itervalues():
			self.battle.use_skill(self, skill)

	def get_skill(self, skill_id):
		return self.skills.get(skill_id, None)