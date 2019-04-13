# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','attribute','name','distance','target_func','target_num','execute_infos',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6):
		self._id=k0
		self.attribute=k1
		self.name=k2
		self.distance=k3
		self.target_func=k4
		self.target_num=k5
		self.execute_infos=k6
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	1001:Record(1001,'normal','撞击',1,'is_enemy',1,(('damage',{'rate':'0.5'}),(None,{}),(None,{}))),
	1002:Record(1002,'normal','叫声',4,'is_enemy',2,(('add_buff',{'base_value':'15','buff_id':'201','turn':'2'}),(None,{}),(None,{}))),
	1003:Record(1003,'normal','生长',1,'is_self',1,(('add_buff',{'base_value':'15','buff_id':'101','turn':'2'}),(None,{}),(None,{}))),
	2001:Record(2001,'grass','藤鞭',3,'is_enemy',1,(('damage',{'rate':'1.5'}),('add_buff',{'base_value':'20','buff_id':'202','turn':'2'}),(None,{}))),
	2002:Record(2002,'grass','飞叶快刀',5,'is_enemy',2,(('damage',{'rate':'1.5'}),(None,{}),(None,{}))),
	2003:Record(2003,'grass','日光术',4,'is_enemy',1,(('damage',{'rate':'3'}),(None,{}),(None,{}))),
	2004:Record(2004,'grass','寄生种子',4,'is_enemy',1,((None,{}),(None,{}),(None,{}))),
	2005:Record(2005,'grass','花瓣舞',5,'is_enemy',3,(('damage',{'rate':'1.5'}),(None,{}),(None,{}))),
	3001:Record(3001,'fire','火花',3,'is_enemy',1,(('damage',{'rate':'1'}),(None,{}),(None,{}))),
	4001:Record(4001,'water','泡沫',3,'is_enemy',1,(('damage',{'rate':'0.5'}),('add_buff',{'base_value':'20','buff_id':'203','turn':'1'}),('add_buff',{'base_value':'10','buff_id':'202','turn':'2'}))),
	5001:Record(5001,'poison','毒粉',4,'is_enemy',2,((None,{}),(None,{}),(None,{}))),
	200301:Record(200301,'grass','日光术回血',1,'is_self',1,(('cure',{'effect_base':'max_hp','rate':'0.05'}),(None,{}),(None,{}))),
	200501:Record(200501,'grass','花瓣舞回血',4,'is_teammate',2,(('cure',{'effect_base':'max_hp','rate':'0.1'}),(None,{}),(None,{}))),
	200502:Record(200502,'grass','花瓣舞负面',1,'is_self',1,(('add_buff',{'buff_id':'302','turn':'2'}),(None,{}),(None,{})))
}
