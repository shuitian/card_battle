# -*- coding:utf-8 -*-

import const
from utils import utils

class BattleReport(object):
	"""战报记录"""
	def init(self):
		self.skill_step = 0
		self.report_data = ''

	def on_battle_start(self):
		self.report_data += u'战斗开始！\n'
		self.report_data += '\n'

		self.report_data += u'【攻方阵容】\n'
		entity = self.left_infos[0]
		self.report_data += u'(大营)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[1]
		if entity:
			self.report_data += u'(中军)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		else:
			self.report_data += u'(中军)无\n'
		entity = self.left_infos[2]
		if entity:
			self.report_data += u'(前锋)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		else:
			self.report_data += u'(前锋)无\n'
		self.report_data += '\n'

		self.report_data += u'【守方阵容】\n'
		entity = self.right_infos[0]
		if entity:
			self.report_data += u'(前锋)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		else:
			self.report_data += u'(前锋)无\n'
		entity = self.right_infos[1]
		if entity:
			self.report_data += u'(中军)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		else:
			self.report_data += u'(中军)无\n'
		entity = self.right_infos[2]
		self.report_data += u'(大营)【%s】 %s级 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
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
		self.report_data += u'(大营)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[1]
		if entity:
			self.report_data += u'(中军)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		entity = self.left_infos[2]
		if entity:
			self.report_data += u'(前锋)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		self.report_data += '\n'

		self.report_data += u'【守方阵容】\n'
		entity = self.right_infos[0]
		if entity:
			self.report_data += u'(前锋)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[1]
		if entity:
			self.report_data += u'(中军)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))
		entity = self.right_infos[2]
		self.report_data += u'(大营)【%s】 %s级别 生命:%s\n'%(entity.eid, entity.level, entity.get_attr('hp'))

		self.replace_eid()
		self.battle_result['battle_report'] = self.report_data

	def replace_eid(self):
		for eid, entity in self.entity_infos.iteritems():
			self.report_data = self.report_data.replace(u'【%s】'%eid, u'【(%s)%s】'%(eid+1,entity.role_info.name))

	def on_damage(self, damage_struct):
		user, target, value = damage_struct.user, damage_struct.target, damage_struct.get_real_value()
		extra_info = damage_struct.extra_info or {}
		buff_obj = extra_info.get('buff_obj', None)
		self.report_data += u'\t' * self.skill_step
		if buff_obj:
			self.report_data += u'【%s】的【%s】对【%s】(%s)造成%s点伤害，【%s】剩余生命%s\n'%(user.eid, buff_obj.buff_data.name, target.eid, target.get_attr('hp') + value, value, target.eid, target.get_attr('hp'))
		else:
			self.report_data += u'【%s】(%s)对【%s】(%s)造成%s点伤害，【%s】剩余生命%s\n'%(user.eid, user.get_attr('hp'), target.eid, target.get_attr('hp') + value, value, target.eid, target.get_attr('hp'))

	def on_cure(self, cure_struct):
		user, target, value = cure_struct.user, cure_struct.target, cure_struct.get_real_value()
		extra_info = cure_struct.extra_info or {}
		buff_obj = extra_info.get('buff_obj', None)
		self.report_data += u'\t' * self.skill_step
		if buff_obj:
			self.report_data += u'【%s】的【%s】为【%s】(%s)恢复%s点生命，【%s】当前生命%s\n'%(user.eid, buff_obj.buff_data.name, target.eid, target.get_attr('hp') - value, value, target.eid, target.get_attr('hp'))
		else:
			self.report_data += u'【%s】(%s)为【%s】(%s)恢复%s点生命，【%s】当前生命%s\n'%(user.eid, user.get_attr('hp'), target.eid, target.get_attr('hp') - value, value, target.eid, target.get_attr('hp'))

	def on_before_real_use_skill(self, skill_struct):
		self.report_data += u'\t' * self.skill_step + u'【%s】发动技能【%s】\n'%(skill_struct.user.eid, skill_struct.skill.name)
		self.skill_step += 1

	def one_after_use_skill(self, skill_struct):
		self.skill_step -= 1

	def on_entity_die(self, killer, dead):
		self.report_data += u'\t' * self.skill_step + u'【%s】无法再战\n'%(dead.eid)

	def on_add_buff_failed(self, target, buff_obj):
		self.report_data += u'\t' * self.skill_step + u'【%s】%s效果\n'%(target.eid, utils.get_buff_exist_desc(target, buff_obj))

	def on_add_buff(self, target, buff_obj):
		add_desc = utils.get_buff_add_desc(target, buff_obj)
		if not add_desc:
			add_desc = u'获得【%s】'%(buff_obj.buff_data.name)
		if add_desc:
			self.report_data += u'\t' * self.skill_step + u'【%s】%s\n'%(target.eid, add_desc)
		desc = utils.get_buff_desc(target, buff_obj)
		if desc:
			self.report_data += u'\t' * (self.skill_step + 1) + u'【%s】%s\n'%(target.eid, desc)

	def on_refresh_buff(self, target, buff_obj):
		self.report_data += u'\t' * self.skill_step + u'【%s】刷新了【%s】\n'%(target.eid, buff_obj.buff_data.name)
		desc = utils.get_buff_desc(target, buff_obj)
		if desc:
			self.report_data += u'\t' * (self.skill_step + 1) + u'【%s】%s\n'%(target.eid, desc)

	def on_remove_buff(self, target, buff_obj):
		self.report_data += u'【%s】来自【%s】的【%s】效果消失了\n'%(target.eid, buff_obj.eid, buff_obj.buff_data.name)

	def on_pass_action(self, avatar, current_round):
		self.report_data += u'【%s】无法行动\n'%(avatar.eid)

	def on_start_action(self, avatar):
		if avatar.have_state('charm'):
			self.report_data += u'【%s】不分敌我目标\n'%(avatar.eid)

	def on_prepare_skill(self, skill_struct):
		self.report_data += u'【%s】的技能【%s】开始准备\n'%(skill_struct.user.eid, skill_struct.skill.name)

	def on_continue_preapre(self, skill_struct):
		self.report_data += u'【%s】的技能【%s】继续准备\n'%(skill_struct.user.eid, skill_struct.skill.name)

	def on_interrupt_prepare_skills(self, avatar, skills):
		for skill in skills:
			self.report_data += u'【%s】的技能【%s】被打断了\n'%(avatar.eid, skill.name)

	def on_not_exist_targets(self, effect_struct):
		self.report_data += u'\t【%s】的【%s】在范围内没有目标\n'%(effect_struct.user.eid, effect_struct.effect.name)

	def on_event_battle_prepare(self):
		self.report_data += u'准备阶段\n'

	def on_effect_not_hit(self, user, effect, target):
		self.report_data += u'\t【%s】没有看清【%s】的位置，效果未命中\n'%(user.eid, target.eid)
		
	def on_damage_be_evade(self, user, effect, target):
		self.report_data += u'\t【%s】敏捷地躲过了伤害\n'%(target.eid)