# -*- coding:utf-8 -*-

class SkillEvent(object):
	"""技能事件代码"""

	def init(self):
		self.execute_tasks = {} # execute_time : [task_info, task_info]
		self._msg_dic = {}
		
	def register_event(self, msg_id, func):
		'''注册事件'''
		self._msg_dic.setdefault(msg_id,[]).append(func)

	def unregister_event(self, msg_id, func):
		'''删除事件'''
		l = self._msg_dic.get(msg_id,[])
		if func in l:
			l.remove(func)

	def on_event(self, msg_id, *data, **kwd):
		'''触发事件'''
		for f in self._msg_dic.get(msg_id,[]):
			f(*data, **kwd)