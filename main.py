import requests
from requests.structures import CaseInsensitiveDict
import json

headers = CaseInsensitiveDict()
headers["apiKey"] = "" #enter the API key generated from https://currencyapi.com/

def get_currency(currencyName, **kwargs):

    re = requests.get(url="https://api.currencyapi.com/v3/latest",headers=headers)
    parse_response = re.json()
    euro = []

    for key,value in parse_response.items():
        for k,val in value.items():
            if currencyName == k:
                euro.append(val)

    for element in range(len(euro)):
        print(euro[element])

def get_status():
    re = requests.get(url="https://api.currencyapi.com/v3/status", headers=headers)
    print(re.json())

if __name__ == '__main__':
    curr_name = str(input("Enter currency to search (Note: Default value is in USD): "))
    get_currency(curr_name)
    get_status()
