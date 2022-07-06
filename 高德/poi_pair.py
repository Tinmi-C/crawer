# -*- coding: utf-8 -*-
import json

import requests
from copy import deepcopy
from loguru import logger

paths = []

def get_dsp_pair(file_name):
    with open(file_name,'r',encoding='utf-8') as f:
        global paths
        idx = 0
        zuobiao = f.readlines()
        max_idx = len(zuobiao)
        for idx in range(0,max_idx):
            zuobiao_json = json.loads(zuobiao[idx])
            origin_coor = zuobiao_json["route"]["origin"].split(',')
            dest_coor = zuobiao_json["route"]["destination"].split(',')
            #ori_poi_id = zuobiao_json["start_poi_id"]
            origin_poi = zuobiao_json["start_poi_title"]
            #dest_poi_id = zuobiao_json["end_poi_id"]
            dest_poi = zuobiao_json["end_poi_title"]
            distance = round(int(zuobiao_json["route"]["paths"][0]["distance"])/1000)
            duration = round(int(zuobiao_json["route"]["paths"][0]["duration"])/60)
            #if origin_poi == '成都大熊猫繁育研究基地' and dest_poi =='三星堆博物馆':
            dest_json = {
                "iconUrl": "icon/20220613/poi_car.jpg",
                "distance":'全程'+str(distance)+'km',
                #"poi_id":dest_poi_id,
                #"poi_type":'景点',
                "duration":'预计'+str(duration)+'分钟'
            }
            paths.append(dest_json)

def write_pair(file_name):
    get_dsp_pair(file_name)
    with open ('file/pair.txt', 'w', encoding='utf-8') as f:
        txt = ','.join(json.dumps(i,ensure_ascii=False) for i in paths)
        f.write('['+txt+']')
