import urllib.request , socket
fname = input("[?] Name of file with Proxies? > ")
with open(fname) as f:
    proxyList = f.readlines()
proxyList = [x.strip() for x in proxyList]
socket.setdefaulttimeout(1)

def is_bad_proxy(pip):   
    try:       
        proxy_handler = urllib.request.ProxyHandler({'http': pip})       
        opener = urllib.request.build_opener(proxy_handler)
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)       
        sock=urllib.request.urlopen('http://www.google.com')
    except urllib.error.HTTPError as e:       
        return e.code
    except Exception as detail:
        return 1
    return 0

for item in proxyList:
    if is_bad_proxy(item):
        print("[LOG] Прокси не валидный:", item)
    else:
        print("[LOG] Прокси валидный:", item)
