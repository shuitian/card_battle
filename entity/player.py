# -*- coding:utf-8 -*-

import gworld
import base_entity
import player_components
from utils.class_utils import components

@components(*player_components.import_all())
class Player(base_entity.BaseEntity):
	"""玩家"""
	def __init__(self):
		super(Player, self).__init__()

		self.init()

	def init(self):
		pass

	def start_battle(self, cards, enemy_cards):
		battle_info = {}
		entity_infos = {}
		step = 0
		for card_list in (cards, enemy_cards):
			for card in card_list:
				if card:
					attrs = card.get_battle_attrs()
					attrs['eid'] = step
					attrs['pos'] = step
					
					entity_infos[step] = attrs

				step += 1

		battle_info['entity_infos'] = entity_infos
		_battle = gworld.battle_mgr.new_battle(battle_info)
		gworld.battle_mgr.start_battle(_battle.battle_id)