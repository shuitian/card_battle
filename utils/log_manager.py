# -*- coding:utf-8 -*-

import os
import time
import logging
import threading

log_path = 'log/'
log_list = []
class LogThread(threading.Thread):
	"""日志线程"""
	def __init__(self):
		super(LogThread, self).__init__()
		self.log_handle = open(os.path.join(log_path, time.strftime("%Y%m%d") + '.log'), 'w')

	def run(self):
		while True:
			if not log_list:
				continue

			log_data = log_list.pop(0)
			log_text = time.strftime("%Y-%m-%d %H:%M:%S") + ' - %s - %s - %s\n'%(log_data)
			self.log_handle.write(log_text)
			self.log_handle.flush()

class MyLog(object):
	"""docstring for MyLog"""
	def __init__(self, module_name):
		super(MyLog, self).__init__()
		self.module_name = module_name

	def info(self, content):
		log_list.append((self.module_name, 'INFO', content))

	def error(self, content):
		log_list.append((self.module_name, 'ERROR', content))

	def debug(self, content):
		log_list.append((self.module_name, 'DEBUG', content))

	def error(self, content):
		log_list.append((self.module_name, 'ERROR', content))

class LogManager(object):
	"""日志管理器"""

	created_modules = {}
	def __init__(self):
		super(LogManager, self).__init__()
		
	@staticmethod
	def get_logger(module_name):
		'''获取日志对象'''
		if module_name in LogManager.created_modules:
			return LogManager.created_modules[module_name]

		logger = MyLog(module_name)
		LogManager.created_modules[module_name] = logger

		return logger

# -------------------------------
# -*- coding:utf-8 -*-

# import os
# import time
# import logging
# import threading

# log_list = []
# class LogThread(threading.Thread):
# 	"""日志线程"""
# 	def __init__(self):
# 		super(LogThread, self).__init__()

# 	def run(self):
# 		while True:
# 			if not log_list:
# 				continue

# 			log_data = log_list.pop(0)
# 			_logging_func, content = log_data
# 			_logging_func(content)


# class MyLog(object):
# 	"""docstring for MyLog"""
# 	def __init__(self, module_name):
# 		super(MyLog, self).__init__()
# 		self._logging = logging.getLogger(module_name)

# 	def info(self, content):
# 		log_list.append((self._logging.info, content))

# 	def error(self, content):
# 		log_list.append((self._logging.error, content))

# 	def debug(self, content):
# 		log_list.append((self._logging.debug, content))

# 	def error(self, content):
# 		log_list.append((self._logging.error, content))

# 	def __getattr__(self, name):
# 		return getattr(self._logging, name)

# class LogManager(object):
# 	"""日志管理器"""

# 	created_modules = set()
# 	log_level = logging.DEBUG
# 	log_path = ''

# 	def __init__(self):
# 		super(LogManager, self).__init__()
		
# 	@staticmethod
# 	def get_logger(module_name):
# 		'''获取日志对象'''
# 		if module_name in LogManager.created_modules:
# 			return MyLog(module_name)

# 		logger = MyLog(module_name)
# 		logger.setLevel(LogManager.log_level)
# 		logger.addHandler(LogManager._create_handler(logger))
# 		LogManager.created_modules.add(module_name)

# 		return logger

# 	@staticmethod
# 	def _create_handler(logger):
# 		formatlist = ['%(asctime)s', '%(name)s', '%(levelname)s', '%(message)s']
# 		ch = logging.FileHandler(os.path.join(LogManager.log_path, time.strftime("%Y%m%d") + '.log'), encoding='utf8')
# 		ch.setLevel(LogManager.log_level)
# 		formatter = logging.Formatter(' - '.join(formatlist))
# 		ch.setFormatter(formatter)

# 		return ch