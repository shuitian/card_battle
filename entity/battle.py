# -*- coding:utf-8 -*-

import base_entity
import battle_logic
from utils.class_utils import components

@components(*battle_logic.import_all())
class Battle(base_entity.BaseEntity):
	"""战场"""
	def __init__(self, battle_mgr, battle_id, battle_info):
		super(Battle, self).__init__()
		self.logger.info('Battle __init__!')
		self.battle_mgr = battle_mgr
		self.battle_id = battle_id
		self.battle_info = battle_info

		self.init()

	def init(self):
		self.is_start = False
		self.is_finish = False

	def start(self):
		self.is_start = True

	def run(self):
		self.logger.info('Battle run!')

	def finish(self, result):
		self.logger.info('Battle finish!')
		self.is_finish = True
		self.battle_mgr.finish_battle(self.battle_id, result)
		self.destroy()

	def destroy(self):
		self.logger.info('Battle destroy!')
		self.battle_mgr = None
		self.battle_info = None
