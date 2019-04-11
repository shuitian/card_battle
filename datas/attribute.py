# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('attribute','normal','fighting','flying','poison','ground','rock','bug','ghost','fire','water','grass','electric','psychic','ice','dragon',)
	def __init__(self,k0,k1,k2,k3,k4,k5,k6,k7,k8,k9,ka,kb,kc,kd,ke,kf):
		self.attribute=k0
		self.normal=k1
		self.fighting=k2
		self.flying=k3
		self.poison=k4
		self.ground=k5
		self.rock=k6
		self.bug=k7
		self.ghost=k8
		self.fire=k9
		self.water=ka
		self.grass=kb
		self.electric=kc
		self.psychic=kd
		self.ice=ke
		self.dragon=kf
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	'bug':Record('bug',1.0,0.8,0.8,1.25,1.0,1.0,1.0,0.8,0.8,1.0,1.25,1.0,1.25,1.0,1.0),
	'dragon':Record('dragon',1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.25),
	'electric':Record('electric',1.0,1.0,1.25,1.0,0.5,1.0,1.0,1.0,1.0,1.25,1.0,0.8,1.0,1.0,0.8),
	'fighting':Record('fighting',1.25,1.0,0.8,0.8,1.0,1.25,0.8,0.5,1.0,1.0,1.0,1.0,0.8,1.25,1.0),
	'fire':Record('fire',1.0,1.0,1.0,1.0,1.0,0.8,1.25,1.0,0.8,0.8,1.25,1.0,1.0,1.25,0.8),
	'flying':Record('flying',1.0,1.25,1.0,1.0,1.0,0.8,1.25,1.0,1.0,1.0,1.25,0.8,1.0,1.0,1.0),
	'ghost':Record('ghost',0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.25,1.0,1.0,1.0,1.0,0.5,1.0,1.0),
	'grass':Record('grass',1.0,1.0,0.8,0.8,1.25,1.25,0.8,1.0,0.8,1.25,0.8,1.0,1.0,1.0,0.8),
	'ground':Record('ground',1.0,1.0,0.5,1.25,1.0,1.25,0.8,1.0,1.25,1.0,0.8,1.25,1.0,1.0,1.0),
	'ice':Record('ice',1.0,1.0,1.25,1.0,2.0,1.0,1.0,1.0,1.0,0.8,1.25,1.0,1.0,0.8,1.25),
	'normal':Record('normal',1.0,1.0,1.0,1.0,1.0,0.8,1.0,0.5,1.0,1.0,1.0,1.0,1.0,1.0,1.0),
	'poison':Record('poison',1.0,1.0,1.0,0.8,0.8,0.8,1.25,0.8,1.0,1.0,1.25,1.0,1.0,1.0,1.0),
	'psychic':Record('psychic',1.0,1.25,1.0,1.25,1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0,0.8,1.0,1.0),
	'rock':Record('rock',1.0,0.8,1.25,1.0,0.8,1.0,1.25,1.0,1.25,1.0,1.0,1.0,1.0,1.25,1.0),
	'water':Record('water',1.0,1.0,1.0,1.0,1.25,1.25,1.0,1.0,1.25,0.8,0.8,1.0,1.0,1.0,0.8)
}
