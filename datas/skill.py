# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','trigger_prob','prepare_round','skill_effect_list','passive_flag','passive_args',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6):
		self._id=k0
		self.name=k1
		self.trigger_prob=k2
		self.prepare_round=k3
		self.skill_effect_list=k4
		self.passive_flag=k5
		self.passive_args=k6
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'撞击',1.0,0,(1001,),None,{}),
	1002:Record(1002,'叫声',0.4,0,(1002,),None,{}),
	1003:Record(1003,'生长',None,None,(1003,),1,{'execute_id':'1003','execute_task':'execute_skill','execute_time':'battle_prepare'}),
	1004:Record(1004,'抓',1.0,0,(1004,),None,{}),
	1005:Record(1005,'烟雾',0.5,0,(1005,),None,{}),
	1006:Record(1006,'乱抓',0.35,0,(1006,1006,1006),None,{}),
	1007:Record(1007,'摇尾巴',0.35,0,(1007,),None,{}),
	1008:Record(1008,'头槌',0.4,1,(1008,),None,{}),
	1009:Record(1009,'火箭头槌',0.45,1,(1009,),None,{}),
	1010:Record(1010,'高速旋转',0.25,0,(1010,101001),None,{}),
	2001:Record(2001,'藤鞭',0.5,0,(2001,),None,{}),
	2002:Record(2002,'飞叶快刀',0.35,1,(2002,),None,{}),
	2003:Record(2003,'日光术',0.4,1,(2003,200301),None,{}),
	2004:Record(2004,'寄生种子',None,None,(2004,),1,{'execute_id':'2004','execute_task':'execute_skill','execute_time':'battle_prepare'}),
	2005:Record(2005,'花瓣舞',0.35,1,(2005,200501,200502),None,{}),
	3001:Record(3001,'火花',0.45,0,(3001,),None,{}),
	3002:Record(3002,'喷射火焰',0.35,1,(3002,),None,{}),
	4001:Record(4001,'泡沫',0.35,0,(4001,),None,{}),
	4002:Record(4002,'缩入壳中',0.4,0,(4002,),None,{}),
	4003:Record(4003,'水枪',0.5,1,(4003,),None,{}),
	4004:Record(4004,'泡沫光线',0.35,0,(4004,),None,{}),
	4005:Record(4005,'水流喷射',0.45,1,(4005,),None,{}),
	5001:Record(5001,'毒粉',0.3,1,(5001,),None,{}),
	6001:Record(6001,'龙怒',None,None,(6001,600101),1,{'execute_id':'6001','execute_task':'execute_skill','execute_time':'battle_prepare'}),
	6002:Record(6002,'龙威',None,None,(6002,),1,{'execute_id':'6002','execute_task':'execute_skill','execute_time':'battle_prepare'}),
	7001:Record(7001,'翅膀攻击',0.3,0,(7001,),None,{}),
	8001:Record(8001,'地球上投',0.5,3,(8001,800101),None,{})
}
