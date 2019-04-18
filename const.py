# -*- coding:utf-8 -*-

# 默认回合数为10
DEFAULT_TOTAL_ROUND = 10

# 技能效果目标
EXECUTE_TARGET_ENEMY = 1
EXECUTE_TARGET_TEAMMATE = 2
EXECUTE_TARGET_TEAMMATE_OR_SELF = 3
EXECUTE_TARGET_ALL = 3

# 胜利方
WINNER_LEFT = 1
WINNER_RIGHT = 2

# 属性标准
ATTR_BASE = {
	'hp' : 10000,
	'max_hp' : 10000,
	'atk' : 100,
	'defence' : 100,
	'speed' : 100,
}

# 状态消失原因
REASON_EFFECT = 'effect' # 驱散
REASON_TIME = 'time' # 回合结束自动消失
