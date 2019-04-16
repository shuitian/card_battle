# -*- coding:utf-8 -*-

import gworld
def init():
	import setup
	setup.setup()

def test():
	import data
	import random
	from utils import utils

	battle_info = {}
	entity_infos = {}
	key_data = (1,None,None,None,None,4)
	for x in xrange(6):
		role_id = random.choice(data.role_info.keys())
		level = random.randrange(100,101)
		role_id = key_data[x]

		if not role_id:
			continue
			
		entity_info = utils.create_role(role_id, level)
		entity_info['eid'] = x
		entity_info['pos'] = x
		
		entity_infos[x] = entity_info

	battle_info['entity_infos'] = entity_infos
	_battle = gworld.battle_mgr.new_battle(battle_info)
	gworld.battle_mgr.start_battle(_battle.battle_id)

if __name__ == '__main__':
	init()
	test()

	while True:
		pass