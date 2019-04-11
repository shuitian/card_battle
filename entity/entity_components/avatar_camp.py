# -*- coding:utf-8 -*-

import data
from utils import utils


class AvatarCamp(object):
	"""战斗角色阵营管理"""
	
	def init(self):
		self.camp_id = self.attrs.get('pos') / 3
	
	def is_enemy(self, info):
		return self.camp_id != info.camp_id

	def is_teammate(self, info):
		return self.camp_id == info.camp_id and self.eid != info.eid

	def is_teammate_or_self(self, info):
		return self.camp_id == info.camp_id

	def is_camp_all(self, info):
		return True