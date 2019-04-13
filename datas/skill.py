# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','trigger_prob','prepare_round','skill_effect_list',)
	def __init__(self,k0,k1,k2,k3,k4):
		self._id=k0
		self.name=k1
		self.trigger_prob=k2
		self.prepare_round=k3
		self.skill_effect_list=k4
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'撞击',1.0,0,(1001,)),
	1002:Record(1002,'叫声',0.4,0,(1002,)),
	1003:Record(1003,'生长',0.35,0,(1003,)),
	1004:Record(1004,'抓',1.0,0,(1004,)),
	1005:Record(1005,'烟雾',0.35,0,(1005,)),
	1006:Record(1006,'乱抓',0.5,0,(1006,1006,1006,1006)),
	1007:Record(1007,'摇尾巴',0.35,0,(1007,)),
	1008:Record(1008,'头槌',0.4,1,(1008,)),
	1009:Record(1009,'火箭头槌',0.45,1,(1009,)),
	2001:Record(2001,'藤鞭',0.5,0,(2001,)),
	2002:Record(2002,'飞叶快刀',0.35,1,(2002,)),
	2003:Record(2003,'日光术',0.4,1,(2003,200301)),
	2004:Record(2004,'寄生种子',0.35,1,(2004,)),
	2005:Record(2005,'花瓣舞',0.35,1,(2005,200501,200502)),
	3001:Record(3001,'火花',0.45,0,(3001,)),
	3002:Record(3002,'喷射火焰',0.35,1,(3002,)),
	4001:Record(4001,'泡沫',0.35,0,(4001,)),
	4002:Record(4002,'缩入壳中',0.4,0,(4002,)),
	4003:Record(4003,'水枪',0.5,1,(4003,)),
	4004:Record(4004,'泡沫光线',0.35,0,(4004,)),
	4005:Record(4005,'水流喷射',0.45,1,(4005,)),
	5001:Record(5001,'毒粉',0.3,1,(5001,)),
	6001:Record(6001,'龙怒',0.8,2,(6001,)),
	7001:Record(7001,'翅膀攻击',0.3,0,(7001,)),
	8001:Record(8001,'地球上投',0.5,3,(8001,800101))
}
