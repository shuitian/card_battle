# -*- coding:utf-8 -*-

import time

class BattleReport(object):
	"""战报存储"""
	def init(self):
		self.report_data = ''

	def on_prepare_battle(self):
		self.report_data += u'战斗开始！\n'

	def on_next_round(self, current_round):
		self.report_data += u'第%s回合\n'%current_round

	def on_end_battle(self):
		self.report_data += u'战斗结束！\n'
		self.battle_result['battle_report'] = self.report_data