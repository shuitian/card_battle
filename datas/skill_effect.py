# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','attribute','execute_info',)
	def __init__(self,k0,k1,k2):
		self._id=k0
		self.attribute=k1
		self.execute_info=k2
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'normal',('damage','is_enemy',{'distance':'3','rate':'1'})),
	2001:Record(2001,'grass',('damage','is_enemy',{'distance':'3','rate':'1'})),
	3001:Record(3001,'fire',('damage','is_enemy',{'distance':'3','rate':'1'})),
	4004:Record(4004,'water',('damage','is_enemy',{'distance':'3','rate':'1'}))
}
