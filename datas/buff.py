# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','buff_tags','name','desc','exist_desc','add_desc','buff_refresh','special_effect','special_effect_args',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6,k7,k8):
		self._id=k0
		self.buff_tags=k1
		self.name=k2
		self.desc=k3
		self.exist_desc=k4
		self.add_desc=k5
		self.buff_refresh=k6
		self.special_effect=k7
		self.special_effect_args=k8
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	101:Record(101,(10,11,12),'加攻','攻击增加$value$($攻击)','已存在同等或更强的攻击增加效果',None,1,'add_attr',{'attr':'atk'}),
	102:Record(102,(10,11,12),'加防','防御增加$value$($防御)','已存在同等或更强的防御增加效果',None,1,'add_attr',{'attr':'defence'}),
	103:Record(103,(10,11,12),'加速','速度增加$value$($速度)','已存在同等或更强的速度增加效果',None,1,'add_attr',{'attr':'speed'}),
	104:Record(104,(10,11,12),'增伤','造成的伤害增加%value%','已存在同等或更强的伤害增加效果',None,1,'add_attr',{'attr':'damage_add_rate'}),
	105:Record(105,(10,11,12),'减受伤','受到的伤害减少%value%','已存在同等或更强的受伤增加效果',None,1,'sub_attr',{'attr':'damaged_add_rate','max_value':'0.9'}),
	106:Record(106,(10,11,12),'增治疗','施加的治疗增加%value%','已存在同等或更强的治疗增加效果',None,1,'add_attr',{'attr':'cure_add_rate'}),
	107:Record(107,(10,11,12),'增受治疗','受到的治疗增加%value%','已存在同等或更强的受治疗增加效果',None,1,'add_attr',{'attr':'be_cure_add_rate'}),
	108:Record(108,(10,11,12),'增闪避','有%value%的概率免疫伤害','已存在同等或更强的闪避增加效果',None,1,'add_attr',{'attr':'evade_rate','max_value':'0.5'}),
	201:Record(201,(20,21,22),'减攻','攻击减少$value$($攻击)','已存在同等或更强的攻击增加效果',None,1,'sub_attr',{'attr':'atk'}),
	202:Record(202,(20,21,22),'减防','防御减少$value$($防御)','已存在同等或更强的防御增加效果',None,1,'sub_attr',{'attr':'defence'}),
	203:Record(203,(20,21,22),'减速','速度减少$value$($速度)','已存在同等或更强的速度增加效果',None,1,'sub_attr',{'attr':'speed'}),
	204:Record(204,(20,21,22),'减伤','造成的伤害减少%value%','已存在同等或更强的伤害增加效果',None,1,'sub_attr',{'attr':'damage_add_rate','max_value':'0.9'}),
	205:Record(205,(20,21,22),'增受伤','受到的伤害增加%value%','已存在同等或更强的受伤增加效果',None,1,'add_attr',{'attr':'damaged_add_rate'}),
	206:Record(206,(20,21,22),'减治疗','施加的治疗减少%value%','已存在同等或更强的治疗增加效果',None,1,'sub_attr',{'attr':'cure_add_rate','max_value':'0.9'}),
	207:Record(207,(20,21,22),'减受治疗','受到的治疗减少%value%','已存在同等或更强的受治疗增加效果',None,1,'sub_attr',{'attr':'be_cure_add_rate','max_value':'0.9'}),
	208:Record(208,(20,21,22),'降命中','使用的技能效果命中概率降低%value%','已存在同等或更强的命中降低效果',None,1,'sub_attr',{'attr':'hit_rate','max_value':'0.5'}),
	301:Record(301,(20,21,30),'混乱',None,'已存在混乱效果','陷入混乱中，无法行动',None,'add_control',{'effect':'confusion'}),
	302:Record(302,(20,21,30),'暴走',None,'已存在暴走效果','陷入暴走中，不分敌我目标',None,'add_control',{'effect':'charm'}),
	303:Record(303,(20,21,30),'禁疗',None,'已存在禁疗效果','无法受到治疗',None,'add_control',{'effect':'forbid_cure'}),
	304:Record(304,(20,21,30),'眩晕',None,'已存在眩晕效果','陷入眩晕中，无法行动',None,'add_control',{'effect':'confusion'}),
	1001:Record(1001,(21,25),'寄生种子',None,'已存在寄生种子效果','的寄生种子效果已施加',None,'execute_effect',{'execute_task':'absorb_hp','execute_time':'round_start'}),
	1002:Record(1002,(21,25),'灼烧',None,'已存在灼烧效果','的灼烧效果已施加',None,'execute_effect',{'execute_task':'damage','execute_time':'round_start'})
}
