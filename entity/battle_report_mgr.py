# -*- coding:utf-8 -*-

import os
import re
import base_entity

class BattleReportMgr(base_entity.BaseEntity):
	"""战报管理器"""
	def __init__(self):
		super(BattleReportMgr, self).__init__()
		self.logger.info('BattleReportMgr __init__!')
		self.report_id = self.get_report_id()
		
	def get_report_id(self):
		if not os.path.exists('report'):
			return 

		path = 'report'
		file_list = os.listdir(path)

		pattern = re.compile(r'(\w+).log')
		max_number = 0
		for filename in file_list:
			rets = pattern.findall(filename)
			if not rets:
				continue
			max_number = max(max_number, int(rets[0]))

		return max_number

	def recode_report(self, battle_report):
		if not battle_report:
			return

		self.remove_outdate_files()
		self.report_id += 1
		report_file_name = 'report/{:0>4}.log'.format(str(self.report_id))
		with open(report_file_name, 'w') as f:
			f.write(str(battle_report))

	def remove_outdate_files(self):
		if not os.path.exists('report'):
			return 

		path = 'report'
		file_list = os.listdir(path)
		if not file_list:
			return

		new_file_list = []
		for filename in file_list:
			filename = os.path.join(path, filename)
			if not os.path.isfile(filename):
				continue

			new_file_list.append(filename)
		
		new_file_list.sort()
		new_file_list = new_file_list[:-20]
		for filename in new_file_list:
			os.remove(filename)
