# -*- coding:utf-8 -*-

import data

class BattleReport(object):
	"""战报记录"""
	def init(self):
		self.report_data = ''

	def on_prepare_battle(self):
		self.report_data += u'战斗开始！\n'

	def on_next_round(self, current_round):
		self.report_data += u'第%s回合\n'%current_round

	def on_end_battle(self):
		self.report_data += u'战斗结束！\n'
		self.battle_result['battle_report'] = self.report_data

	def on_action(self, avatar_info, current_round):
		self.report_data += u'%s行动结束！\n'%avatar_info.role_info.name

	def on_damage(self, user, target, _damage):
		self.report_data += u'%s对%s造成%s点伤害\n'%(user.role_info.name,target.role_info.name,_damage)