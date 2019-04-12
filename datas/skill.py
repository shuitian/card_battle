# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','trigger_prob','skill_effect_list',)
	def __init__(self,k0,k1,k2,k3):
		self._id=k0
		self.name=k1
		self.trigger_prob=k2
		self.skill_effect_list=k3
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'撞击',1.0,(1001,)),
	2001:Record(2001,'藤鞭',1.0,(2001,)),
	3001:Record(3001,'火花',1.0,(3001,)),
	4001:Record(4001,'泡沫',1.0,(4001,))
}
