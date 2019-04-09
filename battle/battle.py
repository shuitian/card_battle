# -*- coding:utf-8 -*-

class Battle(object):
	"""战场"""
	def __init__(self, battle_mgr, battle_id, battle_info):
		super(Battle, self).__init__()
		self.battle_mgr = battle_mgr
		self.battle_id = battle_id
		self.battle_info = battle_info
		self.is_start = False
		self.is_finish = False

	def start(self):
		self.is_start = True

	def run(self):
		self.finish({})

	def finish(self, result):
		self.is_finish = True
		self.battle_mgr.finish_battle(self.battle_id, result)
		self.destroy()

	def destroy(self):
		self.battle_mgr = None
		self.battle_info = None
