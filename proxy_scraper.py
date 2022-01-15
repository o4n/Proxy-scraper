import requests, urllib.request, os

timeout = 10000 #put your timeout here the lower the less proxies

proxytype = ["http","socks4","socks5"] # scrapes http, socks4 and socks5 proxies
for x in proxytype:
    proxies = requests.get('https://api.proxyscrape.com?request=amountproxies&proxytype={}'.format(x))
    url = 'https://api.proxyscrape.com?request=getproxies&proxytype={}&timeout={}'.format(x,timeout)
    print('Scraping '+ proxies.text +'\t' + x + ' proxies.')
    urllib.request.urlretrieve(url, '{}.txt'.format(x))
    print("Saved proxies")