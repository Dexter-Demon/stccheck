import urllib3

import requests
import threading
	
print('\033[1;33;40m------------[+] Status Code Checker By RC [+]----------\n')
input('\033[1;37;40mEnter The File Name Which Contains The Subdomains \n\n\033[1;32;40mroot@rc #~ ')
def full(a):
	http = urllib3.PoolManager()
	f = open('domains.txt')
	for i in f:
		pass
		i = i.replace('\n','')
		try:
			'''resp = http.request(
			'GET',
			i ,
			headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',})'''
			resp=requests.get(i)
			if resp.status_code==200:
				print(f'\033[1;33;40m{i}  200 OK')
			elif resp.status_code==301:
				print(f'\033[1;32;40m;;{i} Redirected 301')
			elif resp.status_code==404:
				print(f'\033[1;31;40m{i} 404 Not Found')
			else:
				print("\033[1;34;40m" + i + " Unknown Status Code")
		except requests.ConnectionError:
			print("\033[1;31;40m" + i + " 404 Not Found")
o = [1]
for i in o:
	thread = threading.Thread(target=full,args=(1,))
	thread.start()
