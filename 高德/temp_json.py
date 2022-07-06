# coding=utf-8
import json
import logging

gaode_list = []
paths = []

def step_split(gaode_json,paths):
    for step in gaode_json:
        if "polyline" in step:
            step_list = step["polyline"].split(';')
            for step_coor in step_list:
                coor_list = step_coor.split(',')
                step_json = {
                    "longitude":coor_list[0],
                    "latitude":coor_list[1]
                }
                paths.append(step_json)
        else:
            logging.info(step)
    return paths


file_name = '驾车路径规划.txt'
def get_distance_json(file_name):
    global paths
    with open(file_name,'r',encoding='utf-8') as f:
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
            steps = zuobiao_json["route"]["paths"][0]["steps"]
            #if origin_poi == '成都大熊猫繁育研究基地' and dest_poi =='三星堆博物馆':
            if idx == 0:
                ori_json = {
                    "longitude": origin_coor[0],
                    "latitude": origin_coor[1],
                    #"poi_id":ori_poi_id,
                    #"poi_type":'景点',
                    "title":origin_poi
                }
                paths.append(ori_json)
            paths = step_split(steps,paths)
            dest_json = {
                "longitude": dest_coor[0],
                "latitude": dest_coor[1],
                #"poi_id":dest_poi_id,
                #"poi_type":'景点',
                "title":dest_poi
            }
            paths.append(dest_json)

def write_dsp(file_name):
    get_distance_json(file_name)
    with open ('file/dsp.txt', 'w', encoding='utf-8') as f:
        txt = ','.join(json.dumps(i,ensure_ascii=False) for i in paths)
        f.write('['+txt+']')
