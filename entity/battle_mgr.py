# -*- coding:utf-8 -*-

import os
import battle
import gworld
import threading
import base_entity

class BattleThread(threading.Thread):
	"""战斗管理器线程"""
	def __init__(self):
		super(BattleThread, self).__init__()
		gworld.battle_mgr = BattleMgr()

	def run(self):
		while True:
			if not gworld.battle_mgr.need_start_battles:
				continue

			_battle = gworld.battle_mgr.need_start_battles.pop(0)
			_battle.run()
		
class BattleMgr(base_entity.BaseEntity):
	"""战斗管理器"""
	def __init__(self):
		super(BattleMgr, self).__init__()
		self.logger.info('BattleMgr __init__!')
		self.battles = {}
		self.need_start_battles = []

	def new_battle(self, battle_info):
		'''创建一场战斗'''
		self.logger.info('new_battle %s'%(battle_info))
		battle_id = gworld.gen_object_id()
		_battle = battle.Battle(self, battle_id, battle_info)
		self.battles[battle_id] = _battle
		return _battle

	def start_battle(self, battle_id):
		'''开启一场战斗'''
		self.logger.info('start_battle %s'%(battle_id))
		_battle = self.battles.get(battle_id, None)
		self.need_start_battles.append(_battle)
		_battle.start()

	def finish_battle(self, battle_id, battle_result):
		'''结束一场战斗'''
		self.logger.info('finish_battle %s %s'%(battle_id, battle_result))
		_battle = self.battles.pop(battle_id, None)
		gworld.battler_report_mgr.recode_report(battle_result.get('battle_report',None))