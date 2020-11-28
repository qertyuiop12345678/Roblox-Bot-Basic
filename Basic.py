import requests
from colorama import Fore,init
print('Created by Faveish on Roblox copyright https://github.com/qertyuiop12345678')
#Current X-CSRF token endpoint URL:
currentxcsrfurl = 'https://auth.roblox.com'
ses = requests.session()
cookies = open('cookies.txt').read().splitlines()
#If it's only one cookie:
#ses.cookies['.ROBLOSECURITY'] = cookies
x = ses.post(currentxcsrfurl)
#Do this to check if the X-CSRF token input is working,if there is an KeyError regarding this then find an new endpoint or try with an .ROBLOSECURITY set as an cookie.
#print(x.headers['x-csrf-token']) #(only for debugging/dev-mode)
#You can just global x and use x.headers for the x-csrf token.
for line in cookies:
  print(Fore.GREEN + 'Trying (Action here)')
  hed = x.headers
  #Do requests and set the headers to hed!
