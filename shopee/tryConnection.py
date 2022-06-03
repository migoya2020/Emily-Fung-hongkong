 
import requests
from requests.exceptions import ConnectionError, ProxyError

myproxies = {
   'http': 'http://proxy.example.com:8080',
   'https': 'http://secureproxy.example.com:8090',
}

url = 'https://shopee.tw/mall/search?keyword=lego'
connection =False

while connection==False:
    try:
        response = requests.post(url, proxies=myproxies)
        
    except (ProxyError) as error:
        
            print('We have a Proxy Errror: ', error)
            # raise ProxyError('A proxy error occurred.')
            #Rotate the Proxy and try again

    except (ConnectionError) as connError: 
        if ConnectionError:
            print(connError)
            #try request again without changin/rotatting the proxy
    except (Exception ) as genExcept:
        print(genExcept)