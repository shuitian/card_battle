# -*- coding:utf-8 -*-

import data

class Card(object):
	"""卡牌信息"""
	def __init__(self, uuid, card_id, level = 1):
		super(Card, self).__init__()
		self.uuid = uuid
		self.card_id = card_id
		self.level = level
		self.card_info = data.card_info[card_id]

		self.hp_level = None
		self.atk_level = None
		self.defence_level = None
		self.speed_level = None

	def get_base_hp(self):
		return self.card_info.base_hp

	def get_real_hp(self):
		base_hp = self.get_base_hp()
		if self.hp_level:
			base_hp += (self.level - 1) * self.get_hp_rate()
		return base_hp

	def get_hp_rate(self):
		return data.ability[self.hp_level].level_hp_rate

	def get_base_atk(self):
		return self.card_info.base_atk

	def get_real_atk(self):
		base_atk = self.get_base_atk()
		if self.atk_level:
			base_atk += (self.level - 1) * self.get_atk_rate()
		return base_atk

	def get_atk_rate(self):
		return data.ability[self.atk_level].level_atk_rate

	def get_base_defence(self):
		return self.card_info.base_defence

	def get_real_defence(self):
		base_defence = self.get_base_defence()
		if self.defence_level:
			base_defence += (self.level - 1) * self.get_defence_rate()
		return base_defence

	def get_defence_rate(self):
		return data.ability[self.defence_level].level_defence_rate

	def get_base_speed(self):
		return self.card_info.base_speed

	def get_real_speed(self):
		base_speed = self.get_base_speed()
		if self.speed_level:
			base_speed += (self.level - 1) * self.get_speed_rate()
		return base_speed

	def get_speed_rate(self):
		return data.ability[self.speed_level].level_speed_rate
		

	def set_hp_level(self, level):
		self.hp_level = level

	def set_atk_level(self, level):
		self.atk_level = level

	def set_defence_level(self, level):
		self.defence_level = level

	def set_speed_level(self, level):
		self.speed_level = level

	def get_battle_attrs(self):
		attrs = {}

		attrs['card_id'] = self.card_id
		attrs['level'] = self.level


		attrs['hp_level'] = self.hp_level
		attrs['atk_level'] = self.atk_level
		attrs['defence_level'] = self.defence_level
		attrs['speed_level'] = self.speed_level

		attrs['hp'] = int(self.get_real_hp())
		attrs['atk'] = self.get_real_atk()
		attrs['defence'] = self.get_real_defence()
		attrs['speed'] = self.get_real_speed()

		attrs['max_hp'] =attrs['hp']

		return attrs