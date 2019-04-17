# -*- coding:utf-8 -*-

import card
from utils import utils

class PlayerCardMgr(object):
	"""卡牌管理"""
	
	def init(self):
		self.cards = {}

	def add_card(self, card_id, level = 1):
		_card = utils.create_card(card_id, level)

		self.cards[uuid] = _card
		return _card