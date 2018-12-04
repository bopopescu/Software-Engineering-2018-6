import mysql.connector
import pandas as pd
import numpy as np
# 1. Create Pandas Dataframe
from IPython.display import display

#log in
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="2a4u8d60",
    database="faredy_db"
)
print(mydb)

mycursor = mydb.cursor()

#rating
mycursor.execute("SELECT * FROM rating")
myresult = mycursor.fetchall()

UID = []
PID = []
RATE = []


#setting dataset

for x in myresult:
    UID.append(x[0])
    PID.append(x[1])
    RATE.append(x[2])

print("UID\tPID\tRATE")

#rating : query 
#for i in range(len(UID)):
#    print(str(UID[i]) + '\t' + str(PID[i]) + '\t' + str(RATE[i])+ '\n',end="")

#rating : dict
rating_dict = {"UID": UID, "PID": PID, "RATE": RATE}
print("rating_dict")
display(pd.DataFrame(rating_dict))

#product

mycursor.execute("SELECT * FROM product")
myresult = mycursor.fetchall()

P_SN = []
TYPE = []
COLOR = []
NAME = []
PRICE = []
IMG_URL = []
PRODUCT_URL =[]
VIEW = []

#setting dataset

for x in myresult:
    P_SN.append(x[0])
    TYPE.append(x[1])
    COLOR.append(x[2])
    NAME.append(x[3])
    PRICE.append(x[4])
    IMG_URL.append(x[5])
    PRODUCT_URL.append(x[6])
    VIEW.append(x[7])
    

#product : dict 
product_dict = {"P_SN":P_SN,"TYPE":TYPE,"COLOR":COLOR,"PRICE":PRICE,"IMG_URL":IMG_URL,"PRODUCT_URL":PRODUCT_URL,"VIEW":VIEW}
print("product_dict")
display(pd.DataFrame(product_dict))


#User array
mycursor.execute("SELECT * FROM member")
myresult = mycursor.fetchall()

U_SN = []
ID = []
PW = []
NAME = []
NICKNAME = []
ADDRESS = []
PHONE_NUMBER= []

#setting dataset
for x in myresult:
    U_SN.append(x[0])
    ID.append(x[1])
    PW.append(x[2])
    NAME.append(x[3])
    NICKNAME.append(x[4])
    ADDRESS.append(x[5])
    PHONE_NUMBER.append(x[6])

#member : dict 
member_dict = {"U_SN":U_SN,"ID":ID,"PW":PW,"NAME":NAME,"NICKNAME":NICKNAME,"ADDRESS":ADDRESS,"PHONE_NUMBER":PHONE_NUMBER}
print("member_dict")
display(pd.DataFrame(member_dict))
attr_list = ["항공점퍼","바지","니트","티셔츠","red","blue","black","brown","ivory","yellow","white","asdf"]


#User_Attribute array
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
