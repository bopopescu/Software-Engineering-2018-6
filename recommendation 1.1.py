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
    def __init__(self):
        rate.__init__(self)
        product.__init__(self)
        user.__init__(self)

    def userarray(self):
        attr_lists = []

        for element in attr1:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in attr2:
            if element not in attr_lists:
                attr_lists.append(element) 
        for element in attr3:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in attr4:
            if element not in attr_lists:
                attr_lists.append(element)
        for element in attr5:
            if element not in attr_lists:
                attr_lists.append(element)
        user_blank=[]
        for i in range(len(U_SN)+1):
            user_blank.append(0)
            
        #user 갯수만큼 array 생성
        U_A_dict = {x:list(tuple(user_blank)) for x in attr_list}   #변수 차단 tuple로 변환한순간 변수x
            
        print("U_A_dict")
        display(pd.DataFrame(U_A_dict))
        #rating to User-Attribute table

        for i in range(len(UID)):
            #rating_dict['UID'][0]=0번째 UID
            #rating_dict['PID'][0]=0번째 PID
            #rating_dict['RATE'][0]=0번째 RATING
            #product_dict["TYPE"][i]에 해당하는 행에 ++를 한다
            U_A_dict[product_dict["TYPE"][rating_dict['PID'][i]]][rating_dict['UID'][i]]+=rating_dict['RATE'][i]
            U_A_dict[product_dict["COLOR"][rating_dict['PID'][i]]][rating_dict['UID'][i]]+=rating_dict['RATE'][i]
        print("U_A_dict")
        display(pd.DataFrame(U_A_dict))

        #User-Product table;
        U_P_dict={x:list(tuple(user_blank)) for x in range(len(P_SN)+1)}
        print("U_P_dict")
        display(pd.DataFrame(U_P_dict))
        for j in PID:
            for i in range(len(U_SN)+1):
                U_P_dict[j][i]+=U_A_dict[product_dict['TYPE'][j]][i]
                U_P_dict[j][i]+=U_A_dict[product_dict['COLOR'][j]][i]
        print("U_P_dict")
        display(pd.DataFrame(U_P_dict))

        #Ranking
        user_rank=[]
        for i in range(len(U_SN)+1):
            user_rank.append([])
        for i in UID:
                user_rank[i]={x:U_P_dict[x][i] for x in U_P_dict.keys()}

        #서버로 보내는 sorted 된 product 리스트 #1에 UID
        sorted(user_rank[1],key=lambda k: user_rank[1][k],reverse=True)

        
mydb = DBConnection('localhost','root','gnsdl10','faredy_db')
# change host/name/passwd/DB according to Server
mydbconn = mydb.get_conn()
mycursor = mydbconn.cursor()

pd.options.display.max_columns = None

test1, test2, test3, test4 = rate(mycursor).result()
print(test4)


