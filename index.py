import requests
import json
from tqdm import tqdm
import pandas as pd
import folium
from folium.plugins import MarkerCluster, MiniMap


url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"

req = requests.get(url)

json = req.json()


def AllMaskStoreInfo():
    url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=1"

    req = requests.get(url)

    total_pages = req.json()['totalPages']

    addr = []
    code = []
    lat = []
    lng = []
    name = []
    types = [] # type class alreay exist so...

    for page_num in tqdm(range(1, total_pages + 1)):
        url = "https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1/stores/json?page=" + str(page_num)

        req = requests.get(url)

        json_data = req.json()

        store_infos = json_data['storeInfos']

        for info in range(len(store_infos)):
            try:
                addr.append(store_infos[info]['addr'])
            except:
                print("add", info)
            try:
                code.append(store_infos[info]['code'])
            except:
                print("code", info)
            try:
                lat.append(store_infos[info]['lat'])
            except:
                print("lat", info)
            try:
                lng.append(store_infos[info]['lng'])
            except:
                print("lng", info)
            try:
                name.append(store_infos[info]['name'])
            except:
                print("name", info)    
            try:
                types.append(store_infos[info]['type'])
            except:
                print("types", info) 


          


    mask_store_info_dt = pd.DataFrame({"addr":addr, "code":code, "latitude":lat, "longitude":lng, "name":name, "type":types}) 
    
    
    return mask_store_info_dt


my_info_df = AllMaskStoreInfo()


save_csv= AllMaskStoreInfo()
my_info_df.to_csv("mask_store_info.csv", index=False)


data_for_draw = my_info_df.loc[:, ['name', 'latitude', 'longitude']]



data_for_draw