# -*- encoding:utf-8 -*-
_reload_all = True

class Record(object):
	__slots__ = ('_id','name','trigger_prob','skill_effect_list',)
	def __init__(self,k0,k1,k2,k3):
		self._id=k0
		self.name=k1
		self.trigger_prob=k2
		self.skill_effect_list=k3
		
	def get(self, key, default=None):
		ret = getattr(self, key, None)
		if ret is None:
			return default
		else:
			return ret
			
	__getitem__ = object.__getattribute__


data = {
	101:Record(101,'藤鞭',1.0,(10101,)),
	201:Record(201,'藤鞭',1.0,(20101,)),
	301:Record(301,'藤鞭',1.0,(30101,)),
	401:Record(401,'火花',1.0,(40101,)),
	501:Record(501,'火花',1.0,(50101,)),
	601:Record(601,'火花',1.0,(60101,)),
	701:Record(701,'泡沫',1.0,(70101,)),
	801:Record(801,'泡沫',1.0,(80101,)),
	901:Record(901,'泡沫',1.0,(90101,))
}
