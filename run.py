<<<<<<< HEAD
from fbparser import Account
from fbparser import function
from fbparser import sorting
from getpass import getpass
import os, time, random, fbparser, sys
=======
from murtanto import Account
from murtanto import function
from murtanto import sorting
from getpass import getpass
import os, time, random, murtanto, sys
>>>>>>> cc763dd... bug fixed

ses = None
count = 0

D = '\033[90m'
W = '\033[1;97m'
R = '\033[1;91m'
G = '\033[1;92m'
Y = '\033[1;93m'
B = '\033[1;94m'
P = '\033[1;95m'
C = '\033[1;96m'
r = '\033[0;91m'
g = '\033[0;92m'
y = '\033[0;93m'
b = '\033[0;94m'
p = '\033[0;95m'
c = '\033[0;96m'
w = '\033[0;97m'
panah = C + "    > " + w

def banner(author = False):
	os.system("cls" if os.name == "nt" else "clear")
	print(f"""
{p}________________ {c} ___________{p}_____   
{p}\__    ___/  _  \ {c}\_   _____/{p}  _  \ {c}v1.2{D}dev
{p}  |    | /  /_\  \{c} |    __){p}/  /_\  \ 
{p}  |    |/    |    \{c}|     \{p}/    |    \\
{p}  |____|\____|__  /{c}\___  /{p}\____|__  /
{c}        {w}   {c}     {p}\/ {c}    \/ {p}        \/""")
	if author:
<<<<<<< HEAD
		print(w + "   by: SalisM3 ft Njank")
=======
		print(w + f"   by: {getMyName()} ft Njank")
		
def getMyName():
  return random.choice(["SalisM3", "RomaKelapa"])
>>>>>>> cc763dd... bug fixed

def input2(teks):
	kata = input(teks + p)
	return kata if kata != "" else ":)"

def hitung_proses(jumlah):
	global count
	count += 1
	hitung = str(count * 100 / jumlah)
	hitung = g + hitung.split(".")[0] + "." + hitung.split(".")[1][:2].ljust(2, " ") + w
	sys.stdout.write(f"\r   ->> Process {hitung} %")
	sys.stdout.flush()

def enter(to = "home"):
	global count
	count = 0
	getpass(f"\n   {w}->> {c}Enter To Back ")
	exec(to + "()")

def confirm_execute():
	angka = random.randint(1,999)
	angka = str(angka).zfill(3)
	if input2(f"   {p}[?]{w} type 'yes{angka}' to confirm: ") != "yes" + angka:
		print()
		print(f"   {p}[!]{w} Operation Cancelled")
		enter()
		exit()

def select(min, max, msg_error = None, teks = "->>"):
	for _ in range(7):
		try:
			pilih = int(input2(f"   {w}{teks} "))
			if pilih < min or pilih > max:
				raise Exception
			return pilih
		except KeyboardInterrupt:
			exit(f"  [!]{w} Oke Sob !!!")
		except:
			if msg_error:
				print(f"    {msg_error}")
	else:
		print(f"   {w}->> {p}Salah mulu tolol!")
		enter()
		exit()

def home():
	banner(author = True)
	print('')
	print(f"{y}   1). {w}Go To Menu")
	print(f"{y}   2). {w}Login")
	print(f"{y}   3). {w}Logout")
	print(f"{y}   0). {w}Exit\n")
	pilih = select(0,3)
	if pilih == 0:
		banner()
		print(f"{p}  ->>{w} Thanks for using our tool")
		print(f"{p}     {c} -------------------------")
		print(f"{p}     {w} Copyright: Salis Mazaya\n")
		exit()
	elif pilih == 1:
		menu1()
	elif pilih == 2:
		login()
	elif pilih == 3:
		logout()

def menu1():
	global ses
	check_login()
	banner()
	if not ses.logged:
		print()
		print(f"   {p}[!]{w} You must login")
		enter()
	else:
		print(f"   {w}Login as {g}{ses.name[:22]}")
		print(f"   {w}Please use it naturally!")
		print(f"   {w}Don't use it for crime!\n")
		print(f"   {p}No. {w}Menu")
		print(f"   {c}--- ----")
		print(f"   {p}1). {w}Like")
		print(f"   {p}2). {w}React")
		print(f"   {p}3). {w}Comment")
		print(f"   {p}4). {w}Friend")
		print(f"   {p}5). {w}Chat")
		print(f"   {p}6). {w}Other")
		print(f"   {p}0). {w}Back\n")
		pilih = select(0,6)
		if pilih == 0:
			home()
		elif pilih == 1:
			menu2()
		elif pilih == 2:
			menu3()
		elif pilih == 3:
			menu4()
		elif pilih == 4:
			menu5()
		elif pilih == 5:
			menu6()
		elif pilih == 6:
			menu7()

def menu2():
	banner()
	print(f"   {p}1). {w}Spam Like in Home")
	print(f"   {p}2). {w}Spam Like in Friend Timeline")
	print(f"   {p}3). {w}Spam Like in Group")
	print(f"   {p}4). {w}Spam Like in Fanspage")
	print(f"   {p}0). {w}Back\n")
	pilih = select(0,4)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		banner()
		print(f"   {p}1). {w}Spam Like in Home")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.like_post_home, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.like_post_home, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 2:
		banner()
		print(f"   {p}2). {w}Spam Like in Friend Timeline")
		id_ = input2(f"   {panah}Id Friend: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.like_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
=======
		data = dump(murtanto.like_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 3:
		banner()
		print(f"   {p}3). {w}Spam Like in Group")
		id_ = input2(f"   {panah}Id Group: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.like_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
=======
		data = dump(murtanto.like_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 4:
		banner()
		print(f"   {p}4). {w}Spam Like in Fanspage")
		id_ = input2(f"   {panah}Username Fanspage: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.like_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
=======
		data = dump(murtanto.like_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

def menu3():
	banner()
	print(f"   {p}1).{w} Spam React in Home")
	print(f"   {p}2).{w} Spam React in Friend Timeline")
	print(f"   {p}3).{w} Spam React in Group")
	print(f"   {p}4).{w} Spam React in Fanspage")
	print(f"   {p}0).{w} Back")
	pilih = select(0,4)
	print()
	if pilih == 0:
		menu1()
	
	print(f"{y}   1).{w} Love")
	print(f"{y}   2).{w} Haha")
	print(f"{y}   3).{w} Wow")
	print(f"{y}   4).{w} Sad")
	print(f"{y}   5).{w} Angry")
	type = ["love", "haha", "wow", "sad", "angry"]
	type = type[select(1,5) - 1]
	
	if pilih == 1:
		banner()
		print(f"   {p}1).{w} Spam React in Home: {type.capitalize()}")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.react_post_home, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.react_post_home, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 2:
		banner()
		print(f"   {p}2).{w} Spam React in Friend Timeline: {type.capitalize()}")
		id_ = input2(f"   {panah}Id Friend: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.react_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
=======
		data = dump(murtanto.react_post_friend, args = (ses,), kwargs = {"id":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 3:
		banner()
		print(f"   {p}3).{w} Spam React in Friend Group: {type.capitalize()}")
		id_ = input2(f"   {panah}Id Group: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.react_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
=======
		data = dump(murtanto.react_post_grup, args = (ses,), kwargs = {"id":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 4:
		banner()
		print(f"   {p}4).{w} Spam React in Fanspage: {type.capitalize()}")
		id_ = input2(f"   {panah}Username Fanspage: ")
		limit = select(1,500, msg_error = f"   {C}> {w}min: 1, max: 500", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.react_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
=======
		data = dump(murtanto.react_post_fanspage, args = (ses,), kwargs = {"username":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.react(ses, url, type = type)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

def menu4():
	banner()
	print(f"   {p}1).{w} Spam Comment in Home")
	print(f"   {p}2).{w} Spam Comment in Friend Timeline")
	print(f"   {p}3).{w} Spam Comment in Group")
	print(f"   {p}4).{w} Spam Comment in Fanspage")
	print(f"   {p}0).{w} Back")
	pilih = select(0,4)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		banner()
		print(f"   {p}1).{w} Spam Comment in Home")
		msg = input2(f"   {panah}Comment value: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.comment_post_home, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.comment_post_home, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.comment(ses, url, msg)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

	elif pilih in [2,3,4]:
		banner()
		if pilih == 2:
			print(f"   {p}2).{w} Spam Comment in Friend Timeline")
		elif pilih == 3:
			print(f"   {p}3).{w} Spam Comment in Group")
		elif pilih == 4:
			print(f"   {p}4).{w} Spam Comment in Fanspage")
		id_ = input2(f"   {panah}" + ("Id" if pilih != 4 else "Username") + " Target: ")
		msg = input2(f"   {panah}Comment value: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", teks = f"    {C}> {w}Limit:")
<<<<<<< HEAD
		data = dump(fbparser.comment_post_friend if pilih == 2 else fbparser.comment_post_grup if pilih == 3 else fbparser.comment_post_fanspage, args = (ses,), kwargs = {"id" if pilih != 4 else "username":id_}, limit = limit)
=======
		data = dump(murtanto.comment_post_friend if pilih == 2 else murtanto.comment_post_grup if pilih == 3 else murtanto.comment_post_fanspage, args = (ses,), kwargs = {"id" if pilih != 4 else "username":id_}, limit = limit)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.comment(ses, url, msg)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

def menu5():
	banner()
	print(f"   {p}1).{w} Mass Accept Request")
	print(f"   {p}2).{w} Mass Reject Friend")
	print(f"   {p}3).{w} Mass Unadd (not Unfriend)")
	print(f"   {p}4).{w} Mass Unfriend")
	print(f"   {p}0).{w} Back")
	pilih = select(0,4)
	if pilih == 0:
		menu1()
	elif pilih == 1 or pilih == 2:
		banner()
		print(f"   {p}1).{w} Mass Accept Request" if pilih == 1 else f"   {p}2).{w} Mass Reject Friend")
		limit = select(1,9999999, teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.friend_request, args = (ses,), limit = limit, show_target = False)
		for url in data:
			url = url["confirm"] if pilih == 1 else url["reject"]
=======
		data = dump(murtanto.friend_request, args = (ses,), limit = limit, show_target = False)
		for url in data:
			url = url[0] if pilih == 1 else url[1]
>>>>>>> cc763dd... bug fixed
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
		
	elif pilih == 3:
		banner()
		print(f"   {p}3).{w} Mass Unadd (not Unfriend)")
		limit = select(1,9999999, teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.friend_requested, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.friend_requested, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.open_url(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

	elif pilih == 4:
		banner()
		print(f"   {p}4).{w} Mass Unfriend")
		limit = select(1,350, msg_error = f"   {C}> {w}min: 1, max: 350", teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.myFriend, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.myFriend, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for name, username, img in data:
			function.unfriend(ses, username)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()


def menu6():
	banner()
	print(f"   {p}1). {w}Mass Chat Friend")
	print(f"   {p}2). {w}Mass Chat Online Friend")
	print(f"   {p}3). {w}Mass Delete Chat")
	print(f"   {p}0). {w}Back\n")
	pilih = select(0,3)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		banner()
		print(f"   {p}1).{w} Mass Chat Friend")
		msg = input2(f"   {panah}Message: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.myFriend, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.myFriend, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for name, username, img in data:
			function.send_msg(ses, username, msg)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 2:
		banner()
		print(f"   {p}2).{w} Mass Chat Online Friend")
		msg = input2(f"   {panah}Message: ")
		limit = select(1,100, msg_error = f"   {C}> {w}min: 1, max: 100", teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.onlineFriend, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.onlineFriend, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for name, username in data:
			function.send_msg(ses, username, msg)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()
	elif pilih == 3:
		banner()
		print(f"   {p}3).{w} Mass Delete Chat")
		# msg = input2(f"   {panah}Message: ")
		limit = select(1,400, msg_error = f"   {C}> {w}min: 1, max: 400", teks = f"    {C}> {w}Limit:")
		confirm_execute()
<<<<<<< HEAD
		data = dump(fbparser.msgUrl, args = (ses,), limit = limit, show_target = False)
=======
		data = dump(murtanto.msgUrl, args = (ses,), limit = limit, show_target = False)
>>>>>>> cc763dd... bug fixed
		for url in data:
			function.deleteMsg(ses, url)
			hitung_proses(len(data))
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

def menu7():
	banner()
	print(f"   {p}1).{w} Find Id Friend")
	print(f"   {p}2).{w} Find Id Group")
	print(f"   {p}3).{w} Request Feature")
	print(f"   {p}0).{w} Back")
	pilih = select(0,3)
	if pilih == 0:
		menu1()
	elif pilih == 1:
		banner()
		print(f"   {p}1).{w} Find Id Friend")
		name = input2(f" {w}  {panah}Full Name: ")
		print(w)
<<<<<<< HEAD
		data = fbparser.find_id_friend(ses, name)
=======
		data = murtanto.find_id_friend(ses, name)
>>>>>>> cc763dd... bug fixed
		if None in data:
			print(f"   {p}[+]{w} Not Found !!!")
		else:
			print(f"   {p}[+]{w} Name : " + data[0][:22])
			print(f"   {p}[+]{w} ID : " + data[1])
		enter()
	elif pilih == 2:
		banner()
		print(f"   {p}1).{w} Find Id Friend")
		name = input2(f" {w}  {panah}Group Name: ")
		print(w)
<<<<<<< HEAD
		data = fbparser.find_id_group(ses, name)
=======
		data = murtanto.find_id_group(ses, name)
>>>>>>> cc763dd... bug fixed
		if None in data:
			print(f"   {p}[+]{w} Not Found !!!")
		else:
			print(f"   {p}[+]{w} Name : " + data[0][:22])
			print(f"   {p}[+]{w} ID : " + data[1])
		enter()
	elif pilih == 3:
		banner()
		print(f"   {p}3).{w} Request Feature")
		print(f"   {r}   [info]{w} Your message will be sent via comments to the author's profile photo")
		msg = input2(f" {w}  {panah} Message: ")
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", msg)
		print(f"\n   {p}[+]{w} Done !!!")
		enter()

	
def dump(func, args = [], kwargs = {}, limit = 100, show_target = True):
	print(w)
	rv = []
	kwargs = kwargs.copy()
	lanjut = True
	data = func(*args, **kwargs)
	for x in data.items:
		rv.append(x)
		if len(rv) == limit:
			lanjut = False
			break
	kwargs["next"] = data.next
	if show_target:
		print(f"   {p}[!]{w} Target: {data.bs4().find('title').text}")
	print(f"   {p}[+]{w} Getting Data")
	if data.next and lanjut:
		rv += function.dump(func, args = args, kwargs = kwargs, limit = limit - len(rv))
	print(f"   {p}[+]{w} Succes Getting Data")
	time.sleep(0.5)
	print(f"   {p}[+]{w} Total: {len(rv)}\n")

	return rv

def comment_toAuthor():
<<<<<<< HEAD
	kata = random.choice(["gw support lu bro", "Hello I'M TAFA User", "gw user tafa bro, buset toolnya mantap bener", "Halo bro gw user Tafa"])
	kata2 = "gw support lu bro"
=======
	kata = random.choice(["gw support lu bro", "Hello I'M TAFA User", "gw user tafa bro, buset toolnya mantap bener", "Halo bro gw user Tafa", "be yourself and never surrender"])
	kata2 = random.choice(["gw support lu bro", "be yourself and never surrender"])
>>>>>>> cc763dd... bug fixed
	try:
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465", kata)
		function.comment(ses, "https://mbasic.facebook.com/photo.php?fbid=150664556427292&id=10004451246330", kata2)
		function.follow(ses, "100041106940465")
		function.follow(ses, "100044512463308")
	except:
		pass

def check_login():
	global ses
	
	try:
		kuki = eval(open("data.json").read())["cookies"]
		
	except:
		kuki = ""
	
	ses = Account(kuki)
	return ses.logged

def login():
	global ses
	
	if check_login():
		print(w)
		print(f"   {p}[!]{w} You have logged in")
		enter()
	else:
		os.system("cls" if os.name == "nt" else "clear")
		print(f"   [!]{w} Don't Know? https://www.youtube.com/watch?v=hjrnR80ABIA")
		print(f"   {r}[info]{w} if you successfully login you will automatically comment to the author profile photo")
		kuki = input2(f"\n   {p}[?]{w} Your Facebook Cookies: ")
		ses = Account(kuki)
		if ses.logged:
			comment_toAuthor()
			data = dict(name = ses.name, id = ses.id, cookies = ses.cookies)
			open("data.json", "w").write(str(data))
			print()
			print(f"   {p}[!]{w} Login Success")
			enter()
		else:
			print()
			print(f"   {p}[!]{w} Login Failed")
			enter()

def logout():
	confirm_execute()
	try:
		os.remove("data.json")
	except:
		pass
	print()
	print(f"   {p}[!]{w} Logout Success")
	enter()

try:
	home()
except KeyboardInterrupt:
	exit(f"   {p}[!]{w} Oke Sob !!!")
<<<<<<< HEAD
except Exception as e:
	print("   [err] " + str(e))
	enter()
=======
#except Exception as e:
#	print("   [err] " + str(e))
#	enter()
>>>>>>> cc763dd... bug fixed
