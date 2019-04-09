# -*- coding:utf-8 -*-

import gworld
def init():
	import setup
	setup.setup()

def test():
	_battle = gworld.battle_mgr.new_battle({})
	gworld.battle_mgr.start_battle(_battle.battle_id)

if __name__ == '__main__':
	init()
	test()
	test()
	test()
	test()

	while True:
		pass