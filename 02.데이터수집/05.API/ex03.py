import json
import os
import folium

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

def createMap():
    y = 37.5511225714939
    x = 126.987867837993
    location = (y, x)
    
    map = folium.Map(location, zoom_start=15, width='100%', height='100%')
    popup=folium.Popup('남산타워')
    folium.Marker(
        location,
        popup,
        icon=folium.Icon(color='blue', icon='glyphicon-road')
    ).add_to(map)

    map.save('data/map/남산타워.html')

if __name__=='__main__':
    createMap()
    # os.system('cls')
    # while True:        
    #     print()
    #     address = input("매장주소>")
    #     if address=='':break
    #     search_list=searchAddress(address)
    #     if len(search_list)==0:
    #         print('검색한 매장이 없습니다.')