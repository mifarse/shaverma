import vk, time
session = vk.Session()
api = vk.API(session)
api.access_token="f85ea1ea7d6958ee6e29ae94ed369cbd9a03af6aa28214cb20fb956f1f300a30b8127d2654a7c4db613d7"
domain = input("PUBLIC: ")
key = input("WORD: ")
flag = True
while flag:
	try:
		time.sleep(0.5)
		posts = api.wall.get(domain=domain, count=2)
		if key in posts[2]['text']:
			if posts[2]['comments']['count']<7:
				print ("in time")
				time.sleep(1)
				api.wall.addComment(owner_id=posts[2]['from_id'], post_id=posts[2]['id'], text = "shaverma moya", access_token=api.access_token)
				flag = False
	except:
		continue




