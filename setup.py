# -*- coding:utf-8 -*-

import gworld
import threading

def init_battle_mgr():
	'''初始化战斗管理器，开启战斗线程'''
	from entity import battle_mgr
	_battle_thread = battle_mgr.BattleThread()
	_battle_thread.start()

def init_logger():
	'''初始化异步日志线程'''
	from utils import log_manager
	_log_thread = log_manager.LogThread()
	_log_thread.start()

def setup():
	init_logger()

	setup_logic()

def setup_logic():
	init_battle_mgr()
