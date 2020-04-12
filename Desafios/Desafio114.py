import urllib
import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('\033[0;31mO site Pudim não está acessivel no computador.\033[m')
else:
    print('\033[0;32mO site Pudim está acessivel no computador.\033[m')
    print(site.read())
