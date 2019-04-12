# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','attribute','distance','target_func','target_num','execute_infos',)
	def __init__(self,k0,k1,k2,k3,k4,k5):
		self._id=k0
		self.attribute=k1
		self.distance=k2
		self.target_func=k3
		self.target_num=k4
		self.execute_infos=k5
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'normal',3,'is_enemy',1,(('damage',{'rate':'0.5'}),(None,{}),(None,{}))),
	2001:Record(2001,'grass',3,'is_enemy',1,(('damage',{'rate':'1'}),('add_buff',{'base_value':'30','buff_id':'202','turn':'2'}),(None,{}))),
	3001:Record(3001,'fire',3,'is_enemy',1,(('damage',{'rate':'1'}),(None,{}),(None,{}))),
	4001:Record(4001,'water',3,'is_enemy',1,(('damage',{'rate':'0.5'}),('add_buff',{'base_value':'20','buff_id':'203','turn':'1'}),('add_buff',{'base_value':'10','buff_id':'202','turn':'2'})))
}
