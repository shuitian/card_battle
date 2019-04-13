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
	2001:Record(2001,'藤鞭',0.5,0,(2001,)),
	2002:Record(2002,'飞叶快刀',0.35,1,(2002,)),
	2003:Record(2003,'日光术',0.4,1,(2003,200301)),
	2004:Record(2004,'寄生种子',0.35,1,(2004,)),
	2005:Record(2005,'花瓣舞',0.35,1,(2005,200501,200502)),
	5001:Record(5001,'毒粉',0.3,1,(5001,))
}
