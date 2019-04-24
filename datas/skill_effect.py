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
	1001:Record(1001,'normal','撞击',1,'is_enemy',1,(('damage',{'rate':'0.5'}),)),
	1002:Record(1002,'normal','叫声',4,'is_enemy',2,(('add_buff',{'buff_id':'201','rate':'0.1','turn':'2'}),)),
	1003:Record(1003,'normal','生长',1,'is_self',1,(('add_buff',{'buff_id':'104','rate':'0.001','turn':'10'}),)),
	1004:Record(1004,'normal','抓',1,'is_enemy',1,(('damage',{'rate':'1'}),)),
	1005:Record(1005,'normal','烟雾',5,'is_enemy',2,(('add_buff',{'buff_id':'208','effect_base':'speed','rate':'0.001','turn':'3'}),)),
	1006:Record(1006,'normal','乱抓',5,'is_enemy',1,(('damage',{'absorb_hp_rate':'0.5','rate':'0.5'}),)),
	1007:Record(1007,'normal','摇尾巴',4,'is_enemy',2,(('add_buff',{'buff_id':'202','rate':'0.2','turn':'2'}),)),
	1008:Record(1008,'normal','头槌',4,'is_enemy',1,(('damage',{'rate':'2.1'}),)),
	1009:Record(1009,'normal','火箭头槌',5,'is_enemy',1,(('damage',{'rate':'2.5'}),)),
	1010:Record(1010,'normal','高速旋转-伤害',5,'is_enemy',1,(('damage',{'rate':'1.5'}),)),
	1011:Record(1011,'normal','变硬',1,'is_self',1,(('add_buff_user_property',{'buff_id':'105','effect_base':'defence','rate':'0.001','turn':'10'}),)),
	2001:Record(2001,'grass','藤鞭',3,'is_enemy',1,(('damage',{'rate':'1.5'}),)),
	2002:Record(2002,'grass','飞叶快刀',5,'is_enemy',2,(('damage',{'rate':'1.5'}),)),
	2003:Record(2003,'grass','日光术',4,'is_enemy',1,(('damage',{'rate':'2.2'}),)),
	2004:Record(2004,'grass','寄生种子',5,'is_enemy',3,(('add_dot',{'buff_id':'1001','effect_base':'max_hp','rate':'0.05','turn':'10'}),)),
	2005:Record(2005,'grass','花瓣舞',5,'is_enemy',3,(('damage',{'rate':'1.5'}),)),
	2006:Record(2006,'grass','麻痹粉',5,'is_enemy',1,(('add_buff',{'buff_id':'203','rate':'0.1','turn':'2'}),('add_buff',{'buff_id':'306','execute_prob':'0.5','turn':'2'}))),
	3001:Record(3001,'fire','火花',3,'is_enemy',1,(('damage',{'rate':'1.5'}),('add_dot',{'buff_id':'1002','effect_base':'atk','turn':'2'}))),
	3002:Record(3002,'fire','喷射火焰',4,'is_enemy',2,(('damage',{'rate':'1.5'}),('add_dot',{'buff_id':'1002','effect_base':'atk','turn':'2'}))),
	4001:Record(4001,'water','泡沫',4,'is_enemy',1,(('damage',{'rate':'0.5'}),('add_buff',{'buff_id':'203','rate':'0.2','turn':'1'}))),
	4002:Record(4002,'water','缩入壳中',1,'is_self',1,(('add_buff',{'buff_id':'105','effect_base':'defence','rate':'0.002','turn':'2'}),)),
	4003:Record(4003,'water','水枪',5,'is_enemy',2,(('damage',{'rate':'1.4'}),)),
	4004:Record(4004,'water','泡沫光纤',5,'is_enemy',2,(('damage',{'rate':'1'}),('add_buff',{'buff_id':'203','rate':'0.2','turn':'2'}))),
	4005:Record(4005,'water','水流喷射',5,'is_enemy',2,(('damage',{'rate':'1.5'}),('add_buff',{'buff_id':'303','turn':'2'}))),
	5001:Record(5001,'poison','毒粉',4,'is_enemy',2,()),
	6001:Record(6001,'dragon','龙怒',1,'is_self',1,(('add_buff',{'buff_id':'305','turn':'10'}),)),
	6002:Record(6002,'dragon','龙威',5,'is_enemy',3,(('add_buff',{'buff_id':'204','rate':'0.001','turn':'10'}),)),
	7001:Record(7001,'flying','翅膀攻击',4,'is_enemy',2,(('damage',{'rate':'1.2'}),)),
	7002:Record(7002,'flying','顺风',5,'is_teammate_or_self',3,(('add_buff',{'buff_id':'103','effect_base':'speed','rate':'0.2','turn':'3'}),)),
	8001:Record(8001,'fighting','地球上投',5,'is_enemy',1,(('damage',{'rate':'5'}),('add_buff',{'buff_id':'304','turn':'1'}))),
	9001:Record(9001,'bug','吐丝',5,'is_enemy',2,(('damage',{'rate':'0.25'}),('add_buff',{'buff_id':'203','rate':'0.3','turn':'1'}),('add_buff',{'buff_id':'304','execute_prob':'0.5','turn':'1'}))),
	9002:Record(9002,'bug','虫咬',4,'is_enemy',1,(('damage',{'rate':'1.2'}),('add_buff',{'buff_id':'1003','effect_base':'atk','rate':'0.4','turn':'3'}))),
	9003:Record(9003,'bug','蝶舞+伤',1,'is_self',1,(('add_buff',{'buff_id':'104','effect_base':'speed','execute_prob':'0.5','rate':'0.002','turn':'2'}),)),
	9004:Record(9004,'bug','银色旋风',5,'is_enemy',3,(('damage',{'effect_base':'speed','rate':'1.5'}),)),
	10001:Record(10001,'rock','滚动',4,'is_enemy',1,(('damage',{'rate':'1.5'}),)),
	11001:Record(11001,'psychic','幻象光线',5,'is_enemy',2,(('damage',{'rate':'2'}),('add_buff',{'buff_id':'301','execute_prob':'0.25','turn':'2'}))),
	101001:Record(101001,'normal','高速旋转-驱散',1,'is_self',1,(('remove_buff',{'buff_tag':'21'}),)),
	200301:Record(200301,'grass','日光术回血',1,'is_self',1,(('cure',{'effect_base':'max_hp','rate':'0.05'}),)),
	200501:Record(200501,'grass','花瓣舞回血',4,'is_teammate_or_self',2,(('cure',{'effect_base':'max_hp','rate':'0.1'}),)),
	200502:Record(200502,'grass','花瓣舞负面',1,'is_self',1,(('add_buff',{'buff_id':'302','turn':'3'}),)),
	600101:Record(600101,'dragon','龙怒+伤害',1,'is_self',1,(('add_buff',{'buff_id':'104','rate':'0.003','turn':'10'}),)),
	800101:Record(800101,'fighting','地球上投负面',1,'is_self',1,(('damage',{'rate':'0.5'}),('add_buff',{'buff_id':'304','turn':'2'}))),
	900301:Record(900301,'bug','蝶舞+闪避',1,'is_self',1,(('add_buff',{'buff_id':'108','effect_base':'speed','execute_prob':'0.5','rate':'0.001','turn':'2'}),)),
	900401:Record(900401,'bug','银色旋风+三维',3,'is_teammate_or_self',2,(('cure',{'effect_base':'speed','rate':'0.5'}),))
}
