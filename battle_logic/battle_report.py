# -*- coding:utf-8 -*-

import data
import const

class BattleReport(object):
	"""战报记录"""
	def init(self):
		self.report_data = ''

	def on_prepare_battle(self):
		self.report_data += u'战斗开始！\n'
		self.report_data += '\n'

		self.report_data += u'【攻方阵容】\n'
		entity = self.left_infos[0]
		self.report_data += u'(大营)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[1]
		self.report_data += u'(中军)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[2]
		self.report_data += u'(前锋)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		self.report_data += '\n'

		self.report_data += u'【守方阵容】\n'
		entity = self.right_infos[0]
		self.report_data += u'(前锋)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[1]
		self.report_data += u'(中军)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[2]
		self.report_data += u'(大营)【%s】 %s级 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		self.report_data += '\n'

	def on_begin_next_round(self, current_round):
		self.report_data += u'\n第%s回合\n'%current_round

	def on_end_battle(self):
		self.report_data += u'战斗结束！\n'
		if self.winner is None:
			self.report_data += u'平局！\n\n'
		elif self.winner == const.WINNER_LEFT:
			self.report_data += u'攻方胜利！\n\n'
		else:
			self.report_data += u'守方胜利！\n\n'

		entity = self.left_infos[0]
		self.report_data += u'(大营)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[1]
		self.report_data += u'(中军)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[2]
		self.report_data += u'(前锋)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		self.report_data += '\n'

		self.report_data += u'【守方阵容】\n'
		entity = self.right_infos[0]
		self.report_data += u'(前锋)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[1]
		self.report_data += u'(中军)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[2]
		self.report_data += u'(大营)【%s】 %s级别 生命:%s\n'%(entity.role_info.name, entity.level, entity.get_attr('hp'))

		self.battle_result['battle_report'] = self.report_data

	# def on_action(self, avatar_info, current_round):
	# 	self.report_data += u'%s行动结束！\n'%avatar_info.role_info.name

	def on_damage(self, damage_struct):
		user, target, _damage = damage_struct.user, damage_struct.target, damage_struct.get_real_value()
		self.report_data += u'\t【%s】(%s)对【%s】造成%s点伤害，【%s】剩余生命%s\n'%(user.role_info.name, user.get_attr('hp'), target.role_info.name, _damage, target.role_info.name, target.get_attr('hp'))

	def on_before_use_skill(self, skill_struct):
		self.report_data += u'【%s】发动技能【%s】\n'%(skill_struct.user.role_info.name, skill_struct.skill.name)

	def on_entity_die(self, killer, dead):
		self.report_data += u'\t【%s】无法再战\n'%(dead.role_info.name)