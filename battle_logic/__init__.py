# -*- coding:utf-8 -*-

def import_all():
	from battle_logic import BattleLogic

	rets = locals().values()
	return rets