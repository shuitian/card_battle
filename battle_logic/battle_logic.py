# -*- coding:utf-8 -*-

import data
import const

class BattleLogic(object):
	"""战斗主逻辑"""
	def init(self):
		self.total_round = self.battle_info.get('total_round', const.DEFAULT_TOTAL_ROUND)
		self.current_round = None
		self.battle_result = {}
		self.entity_infos = {}

	def run(self):
		self.create_entity_infos()
		self.prepare_battle()
		for _ in xrange(self.total_round):
			self.next_round()
		self.end_battle()
		self.finish(self.battle_result)

	def create_entity_infos(self):
		pass

	def prepare_battle(self):
		self.current_round = 0
		self.on_prepare_battle()

	def on_prepare_battle(self):
		pass

	def next_round(self):
		self.current_round += 1
		self.on_next_round(self.current_round)

	def on_next_round(self, current_round):
		pass

	def end_battle(self):
		self.on_end_battle()

	def on_end_battle(self):
		pass
