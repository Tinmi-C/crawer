# -*- coding: utf-8 -*-
import json

import requests
from copy import deepcopy
from loguru import logger
import temp_json
import poi_pair

"""
0：直线距离

1：驾车导航距离（仅支持国内坐标）

3：步行规划距离（仅支持5km之间的距离）
"""

file_name='驾车路径规划.txt'





def get_one_distance(place1, place2,start_poi_title,end_poi_title):
    url = "https://restapi.amap.com/v3/direction/driving?origin=%s&destination=%s&originid=%s&destinationid=%s&extensions=all&strategy=0&key=2bba2b9b636a590d4f28e6c8c8ba71cb" % (
        place1, place2,start_poi_title,end_poi_title)
    response = requests.post(url)
    logger.info(start_poi_title, end_poi_title)
    response = json.loads(response.text)
    response['start_poi_title'] = start_poi_title
    #response['end_poi_id'] = end_poi_id
    response['end_poi_title'] = end_poi_title
    response = json.dumps(response, ensure_ascii=False)
    return str(response)



if __name__ == '__main__':
    with open('file/rout_list.txt', 'r') as f:
        data_list = f.readlines()
    distance_list = []
    for data in data_list:
        data_l = data.split('\t')
        stat_poi = data_l[0]
        end_poi = data_l[1]
        start_coor = data_l[2]
        end_coor = data_l[3].replace('\n','')
        distance_list.append(get_one_distance(start_coor,end_coor,stat_poi,end_poi))
    with open(file_name, 'w', encoding='utf-8') as f:
        for distance in distance_list:
            f.write(distance + '\n')

    temp_json.write_dsp(file_name)
    poi_pair.write_pair(file_name)