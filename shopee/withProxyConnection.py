 

import requests
from requests.exceptions import ConnectionError, ProxyError
import secrets
import urllib.parse
keywords=['lego 41926', 'hello kitty','lego']


headersList = {
 "authority": "shopee.tw",
 "accept": "application/json",
 "accept-language": "en",
 "af-ac-enc-dat": "AAUyLjEuMAAAAYC9XfdeAAAAAAJvAAAAAAAAAAD0QDTiApo7K9b1Yi6qzNTIGzxsdughJIdGLmxsAphfniwXX5ID+ztsEP/7AsdJKI3M4SLjLj1IaryUBdsuJ65EqeGHUbhLD/u6nR6VMG1RjQu4xLU304Pju76x0w1/n55wcAxo8e5J+F/U44MIyTcjDJpdAOVTakbvaXTvhjGG+PFUkbvNB7LJVts6M69ifE1OAYY9PV3srD9xiXKZs3rL3kNlLhlSglbewa9Gq0Q3p5Fjs4yw8pGWNnYQjtmnppaU9NUSOxXIonWiNMfggadfXCamkDQ75QwOyIib6RbIKXiCsMfJviqmohBFkgGLSmwyEAxDajyCJeqG5mqDrj7++xhpe28iS3zrEtxrnqOCiqFrHNYvZoJOy99HV52IaFBREP7vME1DZD1aLJtbhECpVKy54uYqF/6KFSsRJsiltx2Cm/cXdcaOT6st6ZmonfvzzPXjviuJ8YXd4ZDvchevGH0dFr4BNqSRFEryKlpQoG9chiRHRY/hFXjlCV1a1IyxXGa7fllzZUHTANI/7IwxZJzQFfB+1pjgc0ZQTGAy6RFh+xMnjHq5UH81XSyaqDuRY7OMsPKRljZ2EI7Zp6aWkWOzjLDykZY2dhCO2aemlsoY9/ByyEdZrA7TDa0Km6yo52Taa8i2RDDJAlpz1hDHylMPmhAK6FNr61LGy8m7swgNpB83sKnmyXiHS//FQj5drJVo+OISaWPcKQD+20MhegnDRH/D6LHDWhTm0kCqQQzQv+xVjvxW/0j021RGlHbVVRGW3rt7N4K7cJHFtPUOctR7Qv8IIzX95EM9LHnyaw9i9FIyBRQKklb+Vj1jNtM=",
 "content-type": "application/json",
 "cookie": "__LOCALE__null=TW; _gcl_au=1.1.1349897812.1652268588; _fbp=fb.1.1652268589558.1662591438; csrftoken=tpeB99zsbaJduoXx8FHN8d527UkcVIXW; _QPWSDCXHZQA=369c5dce-8bc4-4cf2-b7ac-cf242fe39090; SPC_IA=-1; SPC_EC=-; SPC_F=jkiThxbc5ezEjePjSySCePDYgPc9zK55; REC_T_ID=aba170f6-d11d-11ec-a1fe-ee0c4d9244e1; SPC_U=-; SPC_SI=mall.62ALutmLrDnUe34LKwMWGz7pcfzbdzF4; AMP_TOKEN=%24NOT_FOUND; _gid=GA1.2.194882880.1652443378; __BWfp=c1652443388505x74fb5034a; language=en; SPC_T_ID=CQy0gvgorolyO5ZZUcOX5hZYzPBqQq66GiJP3euedq1dAqUxIF39NICjpZYNuXH8PaA+6n0H9wuvEnF7wYMMvOvANfBZmH0JyWAPpNJl53k=; SPC_T_IV=6Fg8J0dp9FYjNSR823z5sQ==; _ga=GA1.2.749637619.1652268622; shopee_webUnique_ccd=HsIWvY%2BzBXrAUzLefI0LrQ%3D%3D%7CeBd%2FVhpAAqncczrOYjkrnoKkhRfeEkB4tEZ%2BYuMieYHr80h%2BiutJ5g%2F0majH62QqBj3avkbq0QEGRzGE71c%3D%7Cmhw6z8SdOD%2BE1TkU%7C04%7C3; _gali=shopee-searchbar-listbox; cto_bundle=v7pDXV9Ea1lYdHJpUXVOT1V0QUcydnJ0UExKWHY5a2VIVDlIZk5MZHo1Y2olMkJqRk1XWTk2Mmp5RmdtbkhhTjRlN0xxQUxHQkhBMXoxZXJFJTJGTkFtUW1Gb0lreXlmNkl4aGd6SjZ0ZXZYWHc4Smt4RzNWdnQyVmxEODhDeTclMkZqdEdFZ1RlY0xWVDUyckp2VEp6SGxGWnJpRmh1QVElM0QlM0Q; _ga_RPSBE3TQZZ=GS1.1.1652443377.3.1.1652444492.57; SPC_R_T_ID=GJRMacXx9rjNm3w4vrhyDGYSbvLyEkVJZroGu9KLQwXa+uEdSkr8uEQwySRmejI0Yh6n4WuYVg5XoMdxhlZG5/MilNPvyVUlFEIGtD11euo=; SPC_T_IV=glxB4iskZt2db8W9yiuC0g==; SPC_R_T_IV=glxB4iskZt2db8W9yiuC0g==; SPC_T_ID=GJRMacXx9rjNm3w4vrhyDGYSbvLyEkVJZroGu9KLQwXa+uEdSkr8uEQwySRmejI0Yh6n4WuYVg5XoMdxhlZG5/MilNPvyVUlFEIGtD11euo=",
 "sec-ch-ua-mobile": "?0",
 "sec-ch-ua-platform": "Linux",
 "sec-fetch-dest": "empty",
 "sec-fetch-mode": "cors",
 "sec-fetch-site": "same-origin",
 "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
 "x-api-source": "pc",
 "x-csrftoken": "tpeB99zsbaJduoXx8FHN8d527UkcVIXW",
 "x-requested-with": "XMLHttpRequest",
 "x-sap-access-f": "3.2.101.4.|13|2.1.0_5.1.0_0_130|d6358fb9350848f58d09961f110abee54f2b180bbe0b45|10900|1100",
 "x-sap-access-s": "LOssFK108czQ160JturX4azvC6BG59Edum4qMBT7jo4=",
 "x-sap-access-t": "1652444493",
 "x-shopee-language": "en",
 "referer": "https://shopee.tw/"
}
payload = ""
proxyList =["45.72.88.131:8800","192.186.190.71:8800","45.72.88.91:8800","192.186.156.198:8800","192.186.190.73:8800","192.186.190.66:8800","5.253.162.24:8800","192.186.190.70:8800","5.253.162.203:8800","192.186.156.207:8800"]
ses=requests.Session()
BASE_URL ='https://shopee.tw/'
for mykeyword in keywords:  
     
    # connection =False
    initial_request=''
    while connection==False:
        selected_proxy =secrets.choice(proxyList)#"45.72.88.131:8800"
        myproxies = {
        'http': 'http://'+selected_proxy,
        'https': 'http://'+selected_proxy,
        }
        try:
            ses.proxies=myproxies
            initial_request =ses.get(url=BASE_URL, headers=headersList)
            print(initial_request)            
            connection =True
        except (ProxyError) as error:            
            print('We have a Proxy Errror: ', error)
            # raise ProxyError('A proxy error occurred.')
            #Rotate the Proxy and try again
            # selected_proxy=secrets.choice(proxyList)#"45.72.88.91:8800"

        except (ConnectionError) as connError:            
            print(connError)
                #try request again without changin/rotatting the proxy
        except (Exception) as e:
            print(e)
            
    #continue with the code....
    initial_cooki_jar= initial_request.cookies
    reqUrl = 'https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword='+urllib.parse.quote(mykeyword)+'&limit=60&newest=0&official_mall=1&order=desc&page_type=search&scenario=PAGE_MALL_SEARCH&version=2'
    headersList.update({"referer": "https://shopee.tw/mall/search?keyword="+urllib.parse.quote(mykeyword)})
    response = ses.get(reqUrl, data=payload,  headers=headersList, cookies=initial_cooki_jar)
    
    json_response =response.json()
    products=json_response["items"]
    
    assert products, 'We have empty results'
    
    # results_available=[product["item_basic"]['name'] for product in products if keywords[0].split(' ')[1].strip() in product["item_basic"]['name']]
    json_data=json_response["json_data"]
    
    print(json_data)
    if json_data:
        all_products =[]
        print('Total Products: ',len(products))
        for product in  products:        
            name=product["item_basic"]['name']
            # print(name)
            price=product['item_basic']['price']
            # print(price)
            all_products.append({'name':name, 'price':price})

        lowest =min([prod['price'] for prod in all_products])

        # lowest_products=[]
        # for prod in all_products:
        #     if prod['price']==lowest:
        #         lowest_products.append({prod['name'],prod['price']})

        # print(lowest_products[0])        
                
        product_with_lowest_price=[{prod['name'],prod['price']} for prod in all_products if  prod['price']==lowest] 

        print('product with lowest  price:',product_with_lowest_price[0])
        
        # product url: https://shopee.tw/+productname+shopid.itemid
        #N/B: you need to slugify the product name.
    else:
        print('Looks like we have Empty results from search keyword.')      