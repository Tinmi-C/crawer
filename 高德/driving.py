# -*- coding: utf-8 -*-
"""
@Time ： 2022/6/2 14:03
@Auth ： 陈子晗
@File ：driving.py
@IDE ：PyCharm
"""
import json

import requests


def driving_distance(place1, place2):
    url = "https://lbs.amap.com/service/api/restapi?origin=%s&destination=%s&extensions=all&strategy=0" % (
        place1, place2)

    payload = "type=direction%2Fdriving&version=v3"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'cna=wc0cGwmPpgUCAa8JjXBgZ0ec; _uab_collina=165414236412774589520908; xlly_s=1; passport_login=MjcwMDIxOTA1LGFtYXBfMTM4NzM4Njk0MjNCbGVBaHhYS2IsZG12NTdzYWVxeGZ1YXBjdDNpbjV0andidWZkcTdrbGcsMTY1NDE0OTA5MyxZMlU1WlRCbE4ySTRPVGMzTjJRNFlUaGlZV1JrTTJReE1UTTVOV1V4TmpVPQ%3D%3D; oauth_state=76585e0b872100d55c1093f247e5c9e4; gray_auth=2; tfstk=ct6NBuidOKbC8g9bwd94fokSthcOaf6lH2-Xsz5saGys8jRHzs0xkHmmoBRSYqAG.; l=eBgfKPwuLArtvdZWBO5ahurza7795BAjfsPzaNbMiIncC6als8JpV_KQ0FJCEpxRR8XATiY94ZZDt9eO-OtfifIsw2XSsEWmeYnMB; isg=BGZmy76xOGn8lezNteMUm7sXt9roR6oBsFlyHlAJMQse0xHtvde6ESjlK8_f-6IZ; x5secdata=xb7cb21b94244b69ec5ba40d2991f7adab1654149752a463660787a1203358675aaaac2aaa__bx__lbs.amap.com%3A443%2Fservice%2Fapi%2Frestapi'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

def get_coor(place1):
    url = "https://restapi.amap.com/v3/place/text?keywords=%s&city=四川&types=风景名胜&offset=1&page=1&key=2bba2b9b636a590d4f28e6c8c8ba71cb" %(place1)
    payload = "type=direction%2Fdriving&version=v3"
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'cna=wc0cGwmPpgUCAa8JjXBgZ0ec; _uab_collina=165414236412774589520908; xlly_s=1; passport_login=MjcwMDIxOTA1LGFtYXBfMTM4NzM4Njk0MjNCbGVBaHhYS2IsZG12NTdzYWVxeGZ1YXBjdDNpbjV0andidWZkcTdrbGcsMTY1NDE0OTA5MyxZMlU1WlRCbE4ySTRPVGMzTjJRNFlUaGlZV1JrTTJReE1UTTVOV1V4TmpVPQ%3D%3D; oauth_state=76585e0b872100d55c1093f247e5c9e4; gray_auth=2; tfstk=ct6NBuidOKbC8g9bwd94fokSthcOaf6lH2-Xsz5saGys8jRHzs0xkHmmoBRSYqAG.; l=eBgfKPwuLArtvdZWBO5ahurza7795BAjfsPzaNbMiIncC6als8JpV_KQ0FJCEpxRR8XATiY94ZZDt9eO-OtfifIsw2XSsEWmeYnMB; isg=BGZmy76xOGn8lezNteMUm7sXt9roR6oBsFlyHlAJMQse0xHtvde6ESjlK8_f-6IZ; x5secdata=xb7cb21b94244b69ec5ba40d2991f7adab1654149752a463660787a1203358675aaaac2aaa__bx__lbs.amap.com%3A443%2Fservice%2Fapi%2Frestapi'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text


if __name__ == '__main__':
    coor_list = []
    with open('poi_title.txt','r') as f:
        for name in f:
            poi = name.split(',')
            poiname = poi[0].replace('\n','')
            poiid = poi[1].replace('\n','')
            coor_json = json.loads(get_coor(poiname))
            coor_json["poiName"] = poiname
            coor_json["poiId"] = poiid
            print(coor_json)
            coor_list.append(coor_json)

    with open('coor_res.txt','w',encoding='utf-8') as a:
        for row in coor_list:
            txt = json.dumps(row,ensure_ascii=False)
            a.write(txt+'\n')
    #et_coor('宽窄巷子','四川')
    # with open('Hongkong_poi.txt') as f:
    #     for line in f:
    #         line = line.replace('\n', '').split('\t')
    #         poiId = line[0]
    #         poiName = line[2]
    #         poiLon = line[3]
    #         poiLat = line[4]
    #         js = {'poiId': poiId, 'poiName': poiName, 'lon': poiLon, 'lat': poiLat}
    #         js = json.dumps(js, ensure_ascii=False)
    #         print(js)
