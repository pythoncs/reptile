# @Time    : 18-7-25 下午7:02
# @Author  : cuishu
# @Site    : 
# @File    : process_item_mongodb.py
# @Software: PyCharm

import pymysql
import json
import redis


def get_redis_data():
    redisCli = redis.StrictRedis(host='192.168.43.175', port='6379', db=0)
    mysqlCli = pymysql.Connection(host='127.0.0.1', user='root', passwd='1227bing', db='baiduly', port=3306,
                                  use_unicode=True)

    while True:
        source, data = redisCli.blpop('csbaiduly:dupefilter')
        item = json.loads(data.dncode('utf-8'))
        insert_data(data)
        insert_sql, params = insert_data()
        mysqlCli.connect(insert_sql, params)

def insert_data(data):
    insert_sql = """
        INSERT INTO article(%s) VALUES (%s)
        """ % (','.join([key for key, value in data.item()]),
               ','.join(['%s' for key, value in data.item()]))

    params = [value for key, value in data.item()]

    return insert_sql, params

if __name__ == '__main__':
    get_redis_data()
