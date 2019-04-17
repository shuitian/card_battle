# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('ability_level','level_hp_rate','level_atk_rate','level_defence_rate','level_speed_rate',)
	def __init__(self,k0,k1,k2,k3,k4):
		self.ability_level=k0
		self.level_hp_rate=k1
		self.level_atk_rate=k2
		self.level_defence_rate=k3
		self.level_speed_rate=k4
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1:Record(1,1.0,0.1,0.1,0.1),
	2:Record(2,2.0,0.2,0.2,0.2),
	3:Record(3,3.0,0.3,0.3,0.3),
	4:Record(4,4.0,0.4,0.4,0.4),
	5:Record(5,5.0,0.5,0.5,0.5),
	6:Record(6,6.0,0.6,0.6,0.6),
	7:Record(7,7.0,0.7,0.7,0.7),
	8:Record(8,8.0,0.8,0.8,0.8),
	9:Record(9,9.0,0.9,0.9,0.9),
	10:Record(10,10.0,1.0,1.0,1.0)
}
