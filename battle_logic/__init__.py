# -*- coding:utf-8 -*-

def import_all():
	from battle_logic import BattleLogic
	from battle_utils import BattleUtils
	from battle_report import BattleReport


	rets = locals().values()
	return rets