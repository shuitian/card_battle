# -*- coding:utf-8 -*-

import sys
import gworld
import threading

def init_battle_mgr():
	'''初始化战斗管理器，开启战斗线程'''
	from entity import battle_mgr
	_battle_thread = battle_mgr.BattleThread()
	_battle_thread.start()

	from entity import battle_report_mgr
	gworld.battler_report_mgr = battle_report_mgr.BattleReportMgr()

def setup_data_mgr():
	assert 'data' not in sys.modules

	from utils import data_mgr
	sys.modules['data'] = data_mgr.data_mgr()

def init_logger():
	'''初始化异步日志线程'''
	from utils import log_manager
	_log_thread = log_manager.LogThread()
	_log_thread.start()

def setup_encode():
	reload(sys)
	sys.setdefaultencoding('utf-8')

def setup():
	# 初始化编码
	setup_encode()

	# 初始化日志
	init_logger()

	# 初始化导表文件
	setup_data_mgr()

	# 初始化战斗管理器
	init_battle_mgr()
