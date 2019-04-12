# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','buff_tags','name','desc','buff_refresh','special_effect','special_effect_args',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6):
		self._id=k0
		self.buff_tags=k1
		self.name=k2
		self.desc=k3
		self.buff_refresh=k4
		self.special_effect=k5
		self.special_effect_args=k6
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	101:Record(101,(10,11,12),'加攻','攻击增加$value$',1,'add_attr',{'attr':'atk'}),
	102:Record(102,(10,11,12),'加防','防御增加$value$',1,'add_attr',{'attr':'defence'}),
	103:Record(103,(10,11,12),'加速','速度增加$value$',1,'add_attr',{'attr':'speed'}),
	104:Record(104,(10,11,12),'增伤','造成的伤害增加$value$',1,'add_attr',{'attr':'damage_add_rate'}),
	105:Record(105,(10,11,12),'减受伤','受到的伤害减少$value$',1,'sub_attr',{'attr':'damaged_add_rate','max_value':'0.9'}),
	106:Record(106,(10,11,12),'增治疗','施加的治疗增加$value$',1,'add_attr',{'attr':'cure_add_rate'}),
	107:Record(107,(10,11,12),'增受治疗','受到的治疗增加$value$',1,'add_attr',{'attr':'be_cure_add_rate'}),
	201:Record(201,(20,21,22),'减攻','攻击减少$value$',1,'sub_attr',{'attr':'atk'}),
	202:Record(202,(20,21,22),'减防','防御减少$value$',1,'sub_attr',{'attr':'defence'}),
	203:Record(203,(20,21,22),'减速','速度减少$value$',1,'sub_attr',{'attr':'speed'}),
	204:Record(204,(20,21,22),'减伤','造成的伤害减少$value$',1,'sub_attr',{'attr':'damage_add_rate','max_value':'0.9'}),
	205:Record(205,(20,21,22),'增受伤','受到的伤害增加$value$',1,'add_attr',{'attr':'damaged_add_rate'}),
	206:Record(206,(20,21,22),'减治疗','施加的治疗减少$value$',1,'sub_attr',{'attr':'cure_add_rate','max_value':'0.9'}),
	207:Record(207,(20,21,22),'减受治疗','受到的治疗减少$value$',1,'sub_attr',{'attr':'be_cure_add_rate','max_value':'0.9'}),
	301:Record(301,(20,21,30),'混乱','无法行动',None,'add_control',{'effect':'confusion'}),
	302:Record(302,(20,21,30),'暴走','无差别攻击',None,'add_control',{'effect':'charm'}),
	303:Record(303,(20,21,30),'禁疗','无法收到治疗',None,'add_control',{'effect':'forbid_cure'})
}
