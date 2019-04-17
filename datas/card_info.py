# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','attribute_list','base_hp','base_atk','base_defence','base_speed','skill_list',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6,k7):
		self._id=k0
		self.name=k1
		self.attribute_list=k2
		self.base_hp=k3
		self.base_atk=k4
		self.base_defence=k5
		self.base_speed=k6
		self.skill_list=k7
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1:Record(1,'妙蛙种子',('grass','poison'),450.0,49.0,49.0,45.0,(1002,2001,2002,2004)),
	2:Record(2,'妙蛙草',('grass','poison'),600.0,62.0,63.0,60.0,(1003,2001,2002,2003)),
	3:Record(3,'妙蛙花',('grass','poison'),800.0,82.0,83.0,80.0,(1003,2001,2003,2005)),
	4:Record(4,'小火龙',('fire',),390.0,52.0,43.0,65.0,(1002,1005,3001,3002)),
	5:Record(5,'火恐龙',('fire',),580.0,64.0,58.0,80.0,(1006,3001,3002,6001)),
	6:Record(6,'喷火龙',('fire','flying'),780.0,84.0,78.0,100.0,(1006,3002,6002,8001)),
	7:Record(7,'杰尼龟',('water',),440.0,48.0,65.0,43.0,(1001,1007,4001,4002,4003)),
	8:Record(8,'卡咪龟',('water',),590.0,63.0,80.0,58.0,(1007,1008,4002,4003,4004)),
	9:Record(9,'水箭龟',('water',),790.0,83.0,100.0,78.0,(1008,1009,4002,4004,4005)),
	10:Record(10,'绿毛虫',('bug',),450.0,30.0,35.0,45.0,(1001,))
}
