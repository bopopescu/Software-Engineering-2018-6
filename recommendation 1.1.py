import mysql.connector
import pandas as pd
import numpy as np
from IPython.display import display

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
        print("Rate in")
        self.cursor.execute("SELECT * FROM rating")
        myresult = mycursor.fetchall()
        UID = []
        PID = []
        RATE = []
        for x in myresult:
            UID.append(x[0])
            PID.append(x[1])
            RATE.append(x[2])
        rating_dict = {"UID": UID, "PID": PID, "RATE": RATE}
        return (UID, PID, RATE, rating_dict)

class product:
    def __self__(self,cursor):
        self.cursor = cursor
    def result(self):
        print("Product in")
        self.cursor.execute("SELECT * FROM product")
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
        print("user in")
        self.cursor.execute("SELECT * FROM member")
        myresult = mycursor.fetchall()
        U_SN = []
        ID = []
        PW = []
        NAME = []
        NICKNAME = []
        ADDRESS = []
        PHONE_NUMBER= []
        for x in myresult:
            U_SN.append(x[0])
            ID.append(x[1])
            PW.append(x[2])
            NAME.append(x[3])
            NICKNAME.append(x[4])
            ADDRESS.append(x[5])
            PHONE_NUMBER.append(x[6])

        member_dict = {"U_SN":U_SN,"ID":ID,"PW":PW,"NAME":NAME,"NICKNAME":NICKNAME,"ADDRESS":ADDRESS,"PHONE_NUMBER":PHONE_NUMBER}
        return (U_SN, ID, PW, NAME, NICKNAME, ADDRESS, PHONE_NUMBER, member_dict)

class table(rate, product, user):
    def __init__(self,cursor):
        self.cursor = cursor
        rate.__init__(self, cursor)
        product.__init__(self)
        user.__init__(self)
        
        self.UID, self.PID, self.RATE, self.rating_dict = rate.result(self)
        self.P_SN, self.attr1 ,self.attr2, self.attr3, self.attr4, self.attr5, self.NAME, self.PRICE, self.IMG_URL, self.PRODUCT_URL, self.VIEW, self.product_dict= product.result(self)
        self.U_SN, self.ID, self.PW, self.NAME2, self.NICKNAME, self.ADDRESS, self.PHONE_NUMBER, self.member_dict = user.result(self)
        print("table init")

    def userarray(self):
        attr_lists = []
        print("userarry in")
        print(self.UID)
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
            
        print("U_A_dict")
        print(U_A_dict)
        display(pd.DataFrame(U_A_dict))
        #rating to User-Attribute table

        for i in range(len(self.UID)):
            #rating_dict['UID'][0]=0번째 UID
            #rating_dict['PID'][0]=0번째 PID
            #rating_dict['RATE'][0]=0번째 RATING
            #product_dict["TYPE"][i]에 해당하는 행에 ++를 한다
            U_A_dict[self.product_dict["attr1"][self.rating_dict['PID'][i]]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr2"][self.rating_dict['PID'][i]]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr3"][self.rating_dict['PID'][i]]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr4"][self.rating_dict['PID'][i]]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
            U_A_dict[self.product_dict["attr5"][self.rating_dict['PID'][i]]][self.rating_dict['UID'][i]]+=self.rating_dict['RATE'][i]
        print("U_A_dict")
        display(pd.DataFrame(U_A_dict))

        #User-Product table;
        U_P_dict={x:list(tuple(user_blank)) for x in range(len(self.P_SN)+1)}
        print("U_P_dict")
        display(pd.DataFrame(U_P_dict))
        for j in self.PID:
            for i in range(len(self.U_SN)+1):
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr1'][j]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr2'][j]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr3'][j]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr4'][j]][i]
                U_P_dict[j][i]+=U_A_dict[self.product_dict['attr5'][j]][i]
        print("U_P_dict")
        display(pd.DataFrame(U_P_dict))

        #Ranking
        user_rank=[]
        for i in range(len(self.U_SN)+1):
            user_rank.append([])
        for i in self.UID:
                user_rank[i]={x:U_P_dict[x][i] for x in U_P_dict.keys()}

        #서버로 보내는 sorted 된 product 리스트 #1에 UID
        sorted(user_rank[1],key=lambda k: user_rank[1][k],reverse=True)
        print(sorted)

        
mydb = DBConnection('localhost','root','gnsdl10','faredy_db')
# change host/name/passwd/DB according to Server
mydbconn = mydb.get_conn()
mycursor = mydbconn.cursor()

pd.options.display.max_columns = None

test = table(mycursor).userarray()

