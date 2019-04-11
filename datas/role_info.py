# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','base_hp','base_atk','base_defence','base_speed','level_hp_rate','level_atk_rate','level_defence_rate','level_speed_rate','skill_list',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,ka):
		self._id=k0
		self.name=k1
		self.base_hp=k2
		self.base_atk=k3
		self.base_defence=k4
		self.base_speed=k5
		self.level_hp_rate=k6
		self.level_atk_rate=k7
		self.level_defence_rate=k8
		self.level_speed_rate=k9
		self.skill_list=ka
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1:Record(1,'妙蛙种子',450.0,49.0,49.0,45.0,4.5,0.49,0.49,0.45,(101,)),
	2:Record(2,'妙蛙草',600.0,62.0,63.0,60.0,6.0,0.62,0.63,0.6,(201,)),
	3:Record(3,'妙蛙花',800.0,82.0,83.0,80.0,8.0,0.82,0.83,0.8,(301,)),
	4:Record(4,'小火龙',390.0,52.0,43.0,65.0,3.9,0.52,0.43,0.65,(401,)),
	5:Record(5,'火恐龙',580.0,64.0,58.0,80.0,5.8,0.64,0.58,0.8,(501,)),
	6:Record(6,'喷火龙',780.0,84.0,78.0,100.0,7.8,0.84,0.78,1.0,(601,)),
	7:Record(7,'杰尼龟',440.0,48.0,65.0,43.0,4.4,0.48,0.65,0.43,(701,)),
	8:Record(8,'卡咪龟',590.0,63.0,80.0,58.0,5.9,0.63,0.8,0.58,(801,)),
	9:Record(9,'水箭龟',790.0,83.0,100.0,78.0,7.9,0.83,1.0,0.78,(901,))
}
