import mysql.connector
import pandas as pd
import numpy as np
#from IPython.display import display
import time
from datetime import date
today = str(date.today())

class DBConnection:
    def __init__(self, DB_HOST, DB_USER, DB_PASSWORD, DB_NAME):
        self.host = DB_HOST
        self.database = DB_NAME
        self.user = DB_USER
        self.password = DB_PASSWORD
        self.conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = mysql.connector.connect(
                                    host = self.host,
                                    db = self.database,
                                    user = self.user,
                                    passwd = self.password)
        return self.conn

class rate:
    def __init__(self, cursor):
        self.cursor = cursor
        
    def insert(self,uid, pid, rate):
        input_string = "insert into rating(U_SN,P_SN,rate,date) values (" + uid +',' + pid +',' + rate + ',' + NOW()+ ");"
        self.cursor.execute(input_string)
        
    def result(self):
        self.cursor.execute("SELECT * FROM product_mgr_app_rating")
        myresult = mycursor.fetchall()
        rating_id = []
        rate = []
        date = []
        account_id = []
        product_id = []
        for x in myresult:
            rating_id.append(x[0])
            rate.append(x[1])
            date.append(x[2])
            account_id.append(x[3])
            product_id.append(x[4])
        rating_dict = {"UID": account_id, "PID": product_id, "RATE": rate}
        return (rating_id, rate, date, account_id, product_id, rating_dict)

class product:
    def __self__(self,cursor):
        self.cursor = cursor
    def result(self):
        self.cursor.execute("SELECT * FROM product_mgr_app_product")
        myresult = mycursor.fetchall()
        P_SN = []
        attr1 = []
        attr2 = []
        attr3 = []
        attr4 = []
        attr5 = []
        NAME = []
        PRICE = []
        IMG_URL = []
        PRODUCT_URL =[]
        VIEW = []
        for x in myresult:
            P_SN.append(x[0])
            attr1.append(x[1])
            attr2.append(x[2])
            attr3.append(x[3])
            attr4.append(x[4])
            attr5.append(x[5])
            NAME.append(x[6])
            PRICE.append(x[7])
            IMG_URL.append(x[8])
            PRODUCT_URL.append(x[9])
            VIEW.append(x[10])
        product_dict = {"P_SN":P_SN,"attr1":attr1,"attr2":attr2,"attr3":attr3,"attr4":attr4,"attr5":attr5 ,"PRICE":PRICE,"IMG_URL":IMG_URL,"PRODUCT_URL":PRODUCT_URL,"VIEW":VIEW}
        return (P_SN, attr1 , attr2, attr3, attr4, attr5, NAME, PRICE, IMG_URL, PRODUCT_URL, VIEW, product_dict)

class user:
    def __self__(self, cursor):
        self.cursor = cursor
    def result(self):
        self.cursor.execute("SELECT * FROM account_app_account")
        myresult = mycursor.fetchall()
        U_SN = []
        ID = []
        # modified according to main DB
        for x in myresult:
            U_SN.append(x[0])
            ID.append(x[5])
        return (U_SN, ID)

class table(rate, product, user):
    def __init__(self,cursor, db):
        self.db = db
        self.cursor = cursor
        #self.UID, self.PID, self.RATE= rate.result(self)
        self.rating_id, self.rate, self.date, self.account_id, self.product_id, self.rating_dict = rate.result(self)
        self.P_SN, self.attr1 ,self.attr2, self.attr3, self.attr4, self.attr5, self.NAME, self.PRICE, self.IMG_URL, self.PRODUCT_URL, self.VIEW, self.product_dict = product.result(self)
        self.U_SN, self.ID = user.result(self)

    def userarray(self):
        attr_lists = []
        for element in self.attr1:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in self.attr2:
            if element not in attr_lists:
                attr_lists.append(element) 
        for element in self.attr3:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in self.attr4:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in self.attr5:
            if element not in attr_lists:
                attr_lists.append(element)
        user_blank=[]
        for i in range(len(self.U_SN)+1):
            user_blank.append(0)
            
        #user 갯수만큼 array 생성
        U_A_dict = {x:list(tuple(user_blank)) for x in attr_lists}   #변수 차단 tuple로 변환한순간 변수x
            
        
        #rating to User-Attribute table
        for i in range(len(self.rating_id)):
            #rating_dict['UID'][0]=0번째 UID
            #rating_dict['PID'][0]=0번째 PID
            #rating_dict['RATE'][0]=0번째 RATING
            #product_dict["TYPE"][i]에 해당하는 행에 ++를 한다
            U_A_dict[self.product_dict["attr1"][self.rating_dict['PID'][i]-1]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr2"][self.rating_dict['PID'][i]-1]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr3"][self.rating_dict['PID'][i]-1]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr4"][self.rating_dict['PID'][i]-1]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr5"][self.rating_dict['PID'][i]-1]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
        U_A_dict['NULL'] = list(tuple(user_blank))
        #User-Product table;
        U_P_dict={x:list(tuple(user_blank)) for x in range(len(self.P_SN)+1)}
        for j in range(1,len(self.P_SN) + 1):
            for i in range(len(self.U_SN)+1):
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr1'][j-1]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr2'][j-1]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr3'][j-1]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr4'][j-1]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr5'][j-1]][i]
        
        #Ranking
        
        user_rank=[]
        for i in range(len(self.U_SN)+1):
            user_rank.append([])
        for i in range(1,len(self.U_SN)+1):
                user_rank[i]={x:U_P_dict[x][i] for x in U_P_dict.keys()}
        error=0
        for i in range(1,len(self.U_SN)+1):
            t = sorted(user_rank[i], key = lambda k : user_rank[i][k], reverse = True)
            for j in range(min(20,len(self.P_SN))):
                input_string = "insert into recommend_app_recommend (date, account_id, product_id) values (NOW(), %s, %s)"
                if t[min(20,len(self.P_SN))-j]==0:
                    error=1
                    continue
                self.cursor.execute(input_string,(i ,t[min(20,len(self.P_SN))-j]))
                if error==1:
                    self.cursor.execute(input_string,(i ,t[0]))
                error=0
        self.db.commit()
        
        #filter searching
        #self.cursor.execute("select * from product_mgr_app_product where fabric='knit'")
        #print(mycursor.fetchall())
        

        
mydb = DBConnection('localhost','faredy_02','faredy','faredy_db_02').get_conn()

mycursor = mydb.cursor()
# option for displaying all columns using <display>

#pd.options.display.max_columns = None
test = table(mycursor, mydb).userarray()
