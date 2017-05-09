#encoding:utf-8
import unittest
from appium import webdriver
from ddt import ddt,data,unpack
import time
import MySQLdb
import  re

@ddt
class JingWei_Registered(unittest.TestCase):
    
    def setUp(self):
        desired_caps={}
        desired_caps['platformName']='Android'
        desired_caps['platformVesion']='6.0'
        desired_caps['deviceName']='HUAWEI MT7-TL10'
        desired_caps['appPackage']='com.jingwei.card'
        desired_caps['appActivity']='com.jingwei.card.LogoActivity'
        desired_caps['unicodeKeyboard']='True'
        desired_caps['resetKeyboard']='True'
    
        self.wb=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        time.sleep(5)
    
        self.conn=MySQLdb.Connect(host='10.8.64.53',
                                  port=3306,
                                  user='work@RR',
                                  passwd='Geeker4ZolZ',
                                  db='card',
                                  charset='utf8')
        self.cursor=self.conn.cursor()

    #判断格式是否正确
    def account_format(self,account):
        mark=True #声明一个标识，用于判断账号格式是否正确
        if re.match(r'1(3|5|7|8)\d\d{8}',account): #判断账号是否为手机
            mark=True
        elif re.match(r'\d+@\w+.com',account): #判断账号是否为邮箱
            mark=True
        else:
            mark=False #mark为FALSE标识账号格式不正确
        return mark

    #判断账号是否注册
    def account_if_login(self,account):
        mark=True #声明一个标识，用于判断账号是否已注册
        if '@' in account: #以是否包含@判断账号为手机还有邮箱账号
            sql="select email from account_email where email='%s'"%account #查询email表，以此判断邮箱是否注册
            self.cursor.execute(sql) #执行sql
            self.conn.commit() #提交查询
            if self.cursor.fetchall() !=1:#若查询结果不为1，说明查询结果为空，邮箱未注册
                mark=True
            else:
                mark=False
        else:
            print account
            sql = "SELECT * from account_mobile where mobile=%s" % account#查询mobile表，以此判断手机是否注册
            self.cursor.execute(sql) #执行sql
            self.conn.commit() #提交查询
            if self.cursor.fetchall() <1: #若查询结果不为1，说明查询结果为空，邮箱未注册
                print len(self.cursor.fetchall())
                mark = True
            else:
                mark = False #mark为false说明账号已注册
        return mark
    
    #判断验证码是否正确

    @data(('18012341234','1234'),('357637340@qq.com','1234'))
    @unpack
    #登录页面-注册
    def test_registered(self,account,verifycode):
        self.wb.find_element_by_id('activity_login_regist').click() #点击‘注册’按钮
        self.wb.find_element_by_id('fragment_verify_user_name').send_keys(account) # 输入注册号码
        if self.account_format(account):
            if self.account_if_login(account):
                self.wb.find_element_by_id('include_get_verification_code_button').click() #获取验证码
                self.wb.find_element_by_id('fragment_verify_verify_code').send_keys(verifycode) #输入验证码
                self.wb.find_element_by_id('fragment_verify_commit').click() #点击注册
                print '注册成功'
            else:
                print '该账号已注册'
        else:
            print '账号格式不正确'


    #清除方法
    def tearDown(self):
        self.wb.quit()
        self.cursor.close()
        self.conn.close()

if __name__=='__main__':
    unittest.main()