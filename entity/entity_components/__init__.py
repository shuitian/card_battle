# -*- coding:utf-8 -*-

def import_all():
	from avatar_buff_mgr import AvatarBuffMgr
	from avatar_camp import AvatarCamp
	from avatar_skill_mgr import AvatarSkillMgr

	rets = locals().values()
	return rets