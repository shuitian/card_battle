# -*- coding:utf-8 -*-

import gworld
from utils.log_manager import LogManager
class BaseEntity(object):
	"""entity基类"""
	def __init__(self):
		super(BaseEntity, self).__init__()
		self.logger = LogManager.get_logger(self.__class__.__name__)
		
	def destroy(self):
		pass
	
		