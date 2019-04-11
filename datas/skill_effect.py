# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','execute_infos',)
	def __init__(self,k0,k1):
		self._id=k0
		self.execute_infos=k1
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	10101:Record(10101,(('damage','is_enemy',{'distance':'3','rate':'0.8'}),)),
	20101:Record(20101,(('damage','is_enemy',{'distance':'3','rate':'0.9'}),)),
	30101:Record(30101,(('damage','is_enemy',{'distance':'3','rate':'1'}),)),
	40101:Record(40101,(('damage','is_enemy',{'distance':'3','rate':'0.8'}),)),
	50101:Record(50101,(('damage','is_enemy',{'distance':'3','rate':'0.9'}),)),
	60101:Record(60101,(('damage','is_enemy',{'distance':'3','rate':'1'}),)),
	70101:Record(70101,(('damage','is_enemy',{'distance':'3','rate':'0.8'}),)),
	80101:Record(80101,(('damage','is_enemy',{'distance':'3','rate':'0.9'}),)),
	90101:Record(90101,(('damage','is_enemy',{'distance':'3','rate':'1'}),))
}
