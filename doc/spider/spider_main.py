# -*- coding:utf-8 -*-

import urllib2
import time
import re
import gzip
import codecs

def unzip(text):
	try:
		import io
		buf = io.BytesIO(text)
		gf = gzip.GzipFile(fileobj=buf)
		text = gf.read()
	except Exception as e:
		print e
	
	return text

def get_pokemon_info(index, url):
	print '        get_pokemon_info',index,url
	text = urllib2.urlopen(url).read()

	text =unzip(text)
	# with open('%s.log'%index,'w') as f1:
	# 	f1.write(text)
	
	text = text.decode('utf-8')

	pattern = u'''wgPageName":"([\u4e00-\u9fa5]+)","wgTitle'''
	find = re.findall(pattern, text)
	if find:
		name = find[0]

	pattern = u'''<th class="bgl-HP" width="30">(\d+)\n</th>'''
	find = re.findall(pattern, text)
	if find:
		hp = find[0]

	pattern = u'''<th class="bgl-攻击" width="30">(\d+)\n</th>'''
	find = re.findall(pattern, text)
	if find:
		attack = find[0]

	pattern = u'''<th class="bgl-防御" width="30">(\d+)\n</th>'''
	find = re.findall(pattern, text)
	if find:
		defence = find[0]

	pattern = u'''<th class="bgl-速度" width="30">(\d+)\n</th>'''
	find = re.findall(pattern, text)
	if find:
		speed = find[0]

	pattern = u'"(/wiki/.+)" title="[\u4e00-\u9fa5]+">No.{:0>3}'.format(str(index + 1))
	find = re.findall(pattern, text)
	if find:
		next_url = find[0]

	next_url = 'https://wiki.52poke.com' + next_url

	return name, (hp, attack, defence, speed), next_url

def main():
	with open('output.csv', 'w'):pass
	url = 'https://wiki.52poke.com/wiki/%E5%A6%99%E8%9B%99%E7%A7%8D%E5%AD%90'
	for index in xrange(1,152):
		time.sleep(1)
		name, info, url = get_pokemon_info(index, url)
		with codecs.open('output.csv', 'a', encoding='gbk') as f:
			f.write(name + u','  + ','.join(info) + '\n')


if __name__ == '__main__':
	main()