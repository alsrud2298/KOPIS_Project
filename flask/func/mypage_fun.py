### 마이페이지 선호 공연 관련 함수

import pandas as pd
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

# 마이페이지 선호 오픈 공연 관련 함수
def open_like_all(user_info):
    from website import mysql
    # 좋아하는 오픈 공연 정보 가져오기 
    sql = """SELECT op.show_id, op.name, op.detail_url, op.image_url, op.open_date 
             FROM OpenInfo AS op 
             JOIN OpenLiked AS ol 
             ON op.show_id = ol.show_id 
             WHERE ol.u_id = '%s'""" %(user_info)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    open_like = []
    for i in range(len(data)):
        id = data[i][0]
        title = data[i][1]
        url = data[i][2]
        date = data[i][4]
        image = data[i][3]
        open_info = {
            '_id' : id,
            'title' : title,
            'url' : url,
            'date' : date,
            'image' : image
        }
        open_like.append(open_info)
    return open_like

# 마이페이지 선호 상영 중 공연 관련 함수
def new_like_all(user_info):
    from website import mysql
    # 좋아하는 오픈 공연 정보 가져오기 
    sql = """SELECT ns.id, ns.show_name as title, ns.show_url, ns.img_url, ns.show_date 
             FROM NewShow AS ns 
             JOIN NewLiked AS nl 
             ON ns.id = nl.show_id 
             WHERE nl.u_id = '%s'""" %(user_info)
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    conn.close()

    new_like = []
    for i in range(len(data)):
        id = data[i][0]
        title = data[i][1]
        url = data[i][2]
        date = data[i][4]
        image = data[i][3]
        new_info = {
            '_id' : id,
            'title' : title,
            'url' : url,
            'date' : date,
            'image' : image
        }
        new_like.append(new_info)
    return new_like

