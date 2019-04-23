# -*- coding:utf-8 -*-

import gworld
def init():
	import setup
	setup.setup()

def test():
	import data
	import random
	from utils import utils

	key_data = (3,2,1,1,2,6,3,2,4)
	key_data = (11,None,None,None,None,10,6,5,4)
	cards = []
	for x in xrange(6):
		# card_id = random.choice(data.card_info.keys())
		level = random.randrange(100,101)
		card_id = key_data[x]

		if card_id:
			card = utils.create_card(card_id, level)
		else:
			card = None
		cards.append(card)

	gworld.player.start_battle(cards[:3], cards[3:])

if __name__ == '__main__':
	init()
	test()

	while True:
		pass