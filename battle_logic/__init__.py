# -*- coding:utf-8 -*-

def import_all():
	from battle_entity_mgr import BattleEntityMgr
	from battle_logic import BattleLogic
	from battle_report import BattleReport
	from buff_logic import BuffLogic
	from damage_logic import DamageLogic
	from effect_logic import EffectLogic
	from execute_task import ExecuteTask
	from skill_logic import SkillLogic

	rets = locals().values()
	return rets