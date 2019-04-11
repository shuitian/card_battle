# -*- coding:utf-8 -*-

import data

def create_role(role_id, level):
	attrs = {}

	attrs['role_id'] = role_id
	attrs['level'] = level


	role_data = data.role_info[role_id]
	attrs['hp'] = int(role_data.base_hp + role_data.level_hp_rate * (level - 1))
	attrs['atk'] = role_data.base_atk + role_data.level_atk_rate * (level - 1)
	attrs['defence'] = role_data.base_defence + role_data.level_defence_rate * (level - 1)
	attrs['speed'] = role_data.base_speed + role_data.level_speed_rate * (level - 1)

	attrs['max_hp'] =attrs['hp']

	return attrs