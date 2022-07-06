# coding=utf-8
import json
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y/%m/%d %H:%M:%S')
gaode_list = []

def step_split(gaode_json,idx):
    step_idx = 1
    steps = []
    for row in gaode_json:
        if "polyline" in row:
            poiline = row["polyline"].split(';')
            step_distance = row["distance"]
            if "road" in row:
                road = row["road"]
            else:
                road = ''
            poi_step = {
                "distance":step_distance,
                "poiline":poiline,
                "road":road
            }
            steps.append(poi_step)
            logging.debug('序号：%d 导航序号：%d 成功%s' % (idx, step_idx, row))
        else:
            logging.error('序号：%d 导航序号：%d 报错%s'%(idx, step_idx, row))
            exit()
        step_idx += 1
    return steps


file_name = 'file/gaode_hk2.txt'
with open(file_name,'r',encoding='utf-8') as f:
    idx = 0
    for row in f.readlines():
        try:
            zuobiao = row.replace('\'','\"')
            zuobiao_json = json.loads(zuobiao)
            status = zuobiao_json["status"]
            if status == "1":
                origin_coor = zuobiao_json["route"]["origin"].split(',')
                dest_coor = zuobiao_json["route"]["destination"].split(',')
                origin_poi = zuobiao_json["start_poi_title"]
                dest_poi = zuobiao_json["end_poi_title"]
                steps = zuobiao_json["route"]["paths"][0]["steps"]
                step_list = step_split(steps,idx)
                gaode_json ={
                    "ori_poi_id":zuobiao_json["start_poi_id"],
                    "ori_poi_title":origin_poi,
                    "dest_poi_id":zuobiao_json["end_poi_id"],
                    "dest_poi_title":dest_poi,
                    "ori_lon":origin_coor[0],
                    "ori_lat":origin_coor[1],
                    "dest_lon":dest_coor[0],
                    "dest_lat":dest_coor[1],
                    "steps":step_list
                }
                gaode_list.append(gaode_json)
                logging.info('清洗完成，item=%d,ori_poi_name=%s,dest_poi_name=%s'%(idx,origin_poi,dest_poi))
            idx += 1
        except Exception as e:
            logging.error(zuobiao_json)
            print(e)


with open ('file/gaode4.txt', 'a+', encoding='utf-8') as f:
    wirte_idx = 1
    for gaode in gaode_list:
        txt = json.dumps(gaode,ensure_ascii=False)
        print('序号%d 类型%s'%(wirte_idx,type(txt)))
        f.write(txt+'\n')
        wirte_idx += 1
