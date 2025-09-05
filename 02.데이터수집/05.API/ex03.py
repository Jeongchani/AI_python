import json
import os

def getAddress():
    with open('data/hollys_location.json', 'r', encoding='utf8') as file:
        data=json.load(file)
        return data

def searchAddress(address):
    list = getAddress()
    search_list = []
    for store in list:
        if store['address'].find(address)!=-1:
            print(f"{store['name']}, {store['address']}, {store['phone']}")
            search_list.append(store)
    return search_list

if __name__=='__main__':
    os.system('cls')
    print()
    address = input("매장주소>")
    search_list=searchAddress(address)
    if len(search_list)==0:
        print('검색한 매장이 없습니다.')