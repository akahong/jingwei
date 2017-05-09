#encoding:utf-8
import unittest
import requests
import ssl
from ddt import ddt, data, unpack
import MySQLdb as ms
import re


class jingweiAPI(unittest.TestCase):

    #连接数据库
    def setUp(self):
        self.conn = ms.Connect(host='10.8.64.53',
                          port=3306,
                          user='work@RR',
                          passwd='Geeker4ZolZ',
                          db='card',
                          charset='utf8')
        self.cursor = self.conn.cursor()
    """
    #登录接口
    def test_newlogin(self):
        url='https://mobiletest.jingwei.com/newlogin' #接口地址
        sql = 'select mobile,password from account_mobile limit 20' #数据库查询语句
        self.cursor.execute(sql) #执行查询语句
        self.conn.commit() #提交查询语句
        for element in self.cursor.fetchall(): #便利查询结果
            username = element[0] #取出用户名
            password = element[1] #取出用户密码
            data={'username':username,'secret':password} #设置请求参数
            response=requests.post(url,data,verify=False) #发送post请求，https需要将verify值设为False
            print response.status_code #打印服务器返回的状态码
    """

    #分组接口
    def test_getgroup(self):
        url='https://mobiletest.jingwei.com/getgroup' #接口地址
        sql = 'select user_id,access_token from token limit 1' #数据库查询语句
        self.cursor.execute(sql) #执行查询语句
        self.conn.commit() #提交查询语句
        for element in self.cursor.fetchall(): #便利查询结果
            user_id = element[0]  #取出userid值
            token = element[1] #取出token值
            data = {'userId': user_id, 'token': token} #设置请求参数
            response = requests.post(url, data, verify=False) #发送post请求，https需要将verify值设为False
            print response.text #打印服务器返回的结果
            ma=re.search(r'groupid',response.text,re.I) #定义正则表达式匹配groupid模式
            print ma.group() #打印匹配结果


    def tearDown(self):
        self.cursor.close() #关闭游标
        self.conn.close() #关闭数据库连接

if __name__ == '__main__':
    unittest.main()
