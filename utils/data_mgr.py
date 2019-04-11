# -*- coding:utf-8 -*-

import sys

class data_mgr(object):

	def __getattr__(self, name):
		data = self.import_data(name)

		setattr(self, name, data)
		return data

	def import_data(self, name):
		module_name = 'datas.%s'%(name)

		if module_name in sys.modules:
			sys.modules.pop(module_name)
		__import__(module_name)
		module = sys.modules[module_name]

		return module.data