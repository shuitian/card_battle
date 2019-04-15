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
	1003:Record(1003,'normal','生长',1,'is_self',1,(('add_buff',{'base_value':'0.1','buff_id':'104','turn':'10'}),(None,{}),(None,{}))),
	1004:Record(1004,'normal','抓',1,'is_enemy',1,(('damage',{'rate':'0.5'}),(None,{}),(None,{}))),
	1005:Record(1005,'normal','烟雾',4,'is_enemy',2,((None,{}),(None,{}),(None,{}))),
	1006:Record(1006,'normal','乱抓',5,'is_enemy',1,(('damage',{'rate':'0.5'}),(None,{}),(None,{}))),
	1007:Record(1007,'normal','摇尾巴',4,'is_enemy',2,(('add_buff',{'base_value':'15','buff_id':'202','turn':'2'}),(None,{}),(None,{}))),
	1008:Record(1008,'normal','头槌',4,'is_enemy',1,(('damage',{'rate':'2.1'}),(None,{}),(None,{}))),
	1009:Record(1009,'normal','火箭头槌',5,'is_enemy',1,(('damage',{'rate':'2.3'}),(None,{}),(None,{}))),
	2001:Record(2001,'grass','藤鞭',3,'is_enemy',1,(('damage',{'rate':'1.5'}),(None,{}),(None,{}))),
	2002:Record(2002,'grass','飞叶快刀',5,'is_enemy',2,(('damage',{'rate':'1.5'}),('add_buff',{'base_value':'10','buff_id':'202','turn':'2'}),(None,{}))),
	2003:Record(2003,'grass','日光术',4,'is_enemy',1,(('damage',{'rate':'2.2'}),(None,{}),(None,{}))),
	2004:Record(2004,'grass','寄生种子',5,'is_enemy',3,(('add_buff',{'base_value':'15','buff_id':'1001','turn':'10'}),(None,{}),(None,{}))),
	2005:Record(2005,'grass','花瓣舞',5,'is_enemy',3,(('damage',{'rate':'1.5'}),(None,{}),(None,{}))),
	3001:Record(3001,'fire','火花',3,'is_enemy',1,(('damage',{'rate':'1.5'}),(None,{}),(None,{}))),
	3002:Record(3002,'fire','喷射火焰',4,'is_enemy',2,(('damage',{'rate':'1.3'}),(None,{}),(None,{}))),
	4001:Record(4001,'water','泡沫',4,'is_enemy',1,(('damage',{'rate':'0.5'}),('add_buff',{'base_value':'20','buff_id':'203','turn':'1'}),(None,{}))),
	4002:Record(4002,'water','缩入壳中',1,'is_self',1,(('add_buff',{'base_value':'10','buff_id':'102','turn':'2'}),(None,{}),(None,{}))),
	4003:Record(4003,'water','水枪',5,'is_enemy',2,(('damage',{'rate':'1.4'}),(None,{}),(None,{}))),
	4004:Record(4004,'water','泡沫光纤',5,'is_enemy',2,(('damage',{'rate':'0.5'}),('add_buff',{'base_value':'10','buff_id':'203','turn':'2'}),(None,{}))),
	4005:Record(4005,'water','水流喷射',5,'is_enemy',2,(('damage',{'rate':'1.1'}),('add_buff',{'buff_id':'303','turn':'2'}),(None,{}))),
	5001:Record(5001,'poison','毒粉',4,'is_enemy',2,((None,{}),(None,{}),(None,{}))),
	6001:Record(6001,'dragon','龙怒',5,'is_enemy',1,(('damage',{'rate':'3.5'}),(None,{}),(None,{}))),
	7001:Record(7001,'flying','翅膀攻击',4,'is_enemy',2,(('damage',{'rate':'1.2'}),(None,{}),(None,{}))),
	8001:Record(8001,'fighting','地球上投',5,'is_enemy',1,(('damage',{'rate':'5'}),('add_buff',{'buff_id':'304','turn':'1'}),(None,{}))),
	200301:Record(200301,'grass','日光术回血',1,'is_self',1,(('cure',{'effect_base':'max_hp','rate':'0.05'}),(None,{}),(None,{}))),
	200501:Record(200501,'grass','花瓣舞回血',4,'is_teammate',2,(('cure',{'effect_base':'max_hp','rate':'0.1'}),(None,{}),(None,{}))),
	200502:Record(200502,'grass','花瓣舞负面',1,'is_self',1,(('add_buff',{'buff_id':'302','turn':'3'}),(None,{}),(None,{}))),
	800101:Record(800101,'fighting','地球上投负面',1,'is_self',1,(('damage',{'rate':'0.5'}),('add_buff',{'buff_id':'304','turn':'2'}),(None,{})))
}
