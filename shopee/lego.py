import requests

reqUrl = "https://shopee.tw/api/v4/search/search_items?by=relevancy&keyword=lego&limit=60&newest=0&official_mall=1&order=desc&page_type=search&scenario=PAGE_MALL_SEARCH&version=2"

headersList = {
 "authority": "shopee.tw",
 "accept": "application/json",
 "accept-language": "en",
 "af-ac-enc-dat": "AAUyLjEuMAAAAYC9pMDgAAAAAAJvAAAAAAAAAAD0QDTiApo7K9b1Yi6qzNTIBArdYoBm4EAptVeQ13pLsCwXX5ID+ztsEP/7AsdJKI3M4SLjLj1IaryUBdsuJ65EqeGHUbhLD/u6nR6VMG1RjQu4xLU304Pju76x0w1/n55wcAxo8e5J+F/U44MIyTcjDJpdAOVTakbvaXTvhjGG+PFUkbvNB7LJVts6M69ifE1OAYY9PV3srD9xiXKZs3rL3kNlLhlSglbewa9Gq0Q3p5Fjs4yw8pGWNnYQjtmnppaU9NUSOxXIonWiNMfggadfXCamkDQ75QwOyIib6RbIKXiCsMfJviqmohBFkgGLSmwyEAxDajyCJeqG5mqDrj7++xhpe28iS3zrEtxrnqOCiqFrHNYvZoJOy99HV52IaFBREP7vME1DZD1aLJtbhECpVKy54uYqF/6KFSsRJsiltx2Cm/cXdcaOT6st6ZmonfvzzPXjviuJ8YXd4ZDvchevGH0dFr4BNqSRFEryKlpQoG9chiRHRY/hFXjlCV1a1IyxXGa7fllzZUHTANI/7IwxZJzQFfB+1pjgc0ZQTGAy6RFh+xMnjHq5UH81XSyaqDuRY7OMsPKRljZ2EI7Zp6aWkWOzjLDykZY2dhCO2aemlsoY9/ByyEdZrA7TDa0Km6yo52Taa8i2RDDJAlpz1hDHylMPmhAK6FNr61LGy8m7swgNpB83sKnmyXiHS//FQj5drJVo+OISaWPcKQD+20MhstUQVlhgcaKjeoxwUElE1/Fo9hCMFoSXxid7g5y/8RXVVRGW3rt7N4K7cJHFtPUOctR7Qv8IIzX95EM9LHnyaw9i9FIyBRQKklb+Vj1jNtM=",
 "content-type": "application/json",
 "cookie": "__LOCALE__null=TW; _gcl_au=1.1.1349897812.1652268588; _fbp=fb.1.1652268589558.1662591438; csrftoken=tpeB99zsbaJduoXx8FHN8d527UkcVIXW; _QPWSDCXHZQA=369c5dce-8bc4-4cf2-b7ac-cf242fe39090; SPC_IA=-1; SPC_EC=-; SPC_F=jkiThxbc5ezEjePjSySCePDYgPc9zK55; REC_T_ID=aba170f6-d11d-11ec-a1fe-ee0c4d9244e1; SPC_U=-; SPC_SI=mall.62ALutmLrDnUe34LKwMWGz7pcfzbdzF4; _gid=GA1.2.194882880.1652443378; __BWfp=c1652443388505x74fb5034a; language=en; _ga=GA1.1.749637619.1652268622; shopee_webUnique_ccd=ZU8odcuc2HcJHyVq5xjL9w%3D%3D%7CeBd%2FVhpAAqncczrOYimTTp25ZCFftbL96uapQivT3cdhD3HkCsAdk1wdihaG926i9%2FhxPPg4nJrFbzDc71Q%3D%7Cmhw6z8SdOD%2BE1TkU%7C04%7C3; _dc_gtm_UA-61915057-6=1; cto_bundle=WPsLBF9Ea1lYdHJpUXVOT1V0QUcydnJ0UExCTGx0THphNU41bjVmRjdVdVdiZzRoNGlRZE1vVzEyRUFId2JMRXRkMlRWU2paTmdmcjJHVk5XSnJtZ3RUN0s4SndBNHBpOVF3bFAzaHRSbjZOaUxJYnB5S21SRmV1cU9pa0klMkZVUlRQVFRJbXVGUjVvOUhHJTJCd2ZTM0dvMndsV3NBJTNEJTNE; _ga_RPSBE3TQZZ=GS1.1.1652449119.4.1.1652449130.49; SPC_T_IV="2016Pe1bFwfL2cTJbgoCOA=="; SPC_T_ID="lPaWTMulXzaeKkspWuqnUB8x3us7KX18PdYe8sjRR2GGgUmFD4m4fLwr/f0GUz/s39f1K78/CN2L4WEn6VWtM18aTrWC/tDsOrEM/doCdnk="; SPC_R_T_ID=lPaWTMulXzaeKkspWuqnUB8x3us7KX18PdYe8sjRR2GGgUmFD4m4fLwr/f0GUz/s39f1K78/CN2L4WEn6VWtM18aTrWC/tDsOrEM/doCdnk=; SPC_R_T_IV=2016Pe1bFwfL2cTJbgoCOA==; SPC_T_ID=lPaWTMulXzaeKkspWuqnUB8x3us7KX18PdYe8sjRR2GGgUmFD4m4fLwr/f0GUz/s39f1K78/CN2L4WEn6VWtM18aTrWC/tDsOrEM/doCdnk=; SPC_T_IV=2016Pe1bFwfL2cTJbgoCOA==",
 "referer": "https://shopee.tw/mall/search?keyword=lego",
 "sec-ch-ua": " Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101",
 "sec-ch-ua-mobile": "?0",
 "sec-ch-ua-platform": "Linux",
 "sec-fetch-dest": "empty",
 "sec-fetch-mode": "cors",
 "sec-fetch-site": "same-origin",
 "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36",
 "x-api-source": "pc",
 "x-csrftoken": "tpeB99zsbaJduoXx8FHN8d527UkcVIXW",
 "x-requested-with": "XMLHttpRequest",
 "x-sap-access-f": "3.2.101.4.|13|2.1.0_5.1.0_0_123|16816efdfdfc48208d8d35a1dc976e61b6e02f10b81a4c|10900|1100",
 "x-sap-access-s": "VezxAJ_RnjDyjO-GsN2S_8C9ExckFI8bR_-ZQa6nC7I=",
 "x-sap-access-t": "1652449133",
 "x-shopee-language": "en" 
}

payload = ""

response = requests.request("GET", reqUrl, data=payload,  headers=headersList)

print(response.text)