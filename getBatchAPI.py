import requests as r
import json as j

url = "https://epxt-dev3.fa.s1649817.oraclecloudatcustomer.com/fscmRestApi/resources/11.13.18.05/journalBatches"

payload={}
headers = {
  'Content-Type': 'application/vnd.oracle.adf.resourcecollection+json',
  'Authorization': 'Basic aGVjdG9ybmF2YTpPcmFjbGUxMjMh'
}

response = r.request("GET", url, headers=headers, data=payload)

print(response.text)
