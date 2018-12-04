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
STOCK = []
IMG_URL = []
PRODUCT_URL =[]

#setting dataset

for x in myresult:
    P_SN.append(x[0])
    TYPE.append(x[1])
    COLOR.append(x[2])
    NAME.append(x[3])
    PRICE.append(x[4])
    STOCK.append(x[5])
    IMG_URL.append(x[6])
    PRODUCT_URL.append(x[7])

#product : dict 
product_dict = {"P_SN":P_SN,"TYPE":TYPE,"COLOR":COLOR,"PRICE":PRICE,"STOCK":STOCK,"IMG_URL":IMG_URL,"PRODUCT_URL":PRODUCT_URL}
print("product_dict")
display(pd.DataFrame(product_dict))


#User array
mycursor.execute("SELECT * FROM member")
myresult = mycursor.fetchall()

U_SN = []
ID = []
PW = []
NAME = []
IMG_URL = []
NICKNAME = []
ADDRESS = []
PHONE_NUMBER= []

#setting dataset
for x in myresult:
    U_SN.append(x[0])
    ID.append(x[1])
    PW.append(x[2])
    NAME.append(x[3])
    IMG_URL.append(x[4])
    NICKNAME.append(x[5])
    ADDRESS.append(x[6])
    PHONE_NUMBER.append(x[7])

#member : dict 
member_dict = {"U_SN":U_SN,"ID":ID,"PW":PW,"NAME":NAME,"IMG_URL":IMG_URL,"NICKNAME":NICKNAME,"ADDRESS":ADDRESS,"PHONE_NUMBER":PHONE_NUMBER}
print("member_dict")
display(pd.DataFrame(member_dict))
attr_list = ["항공점퍼","바지","니트","티셔츠","red","blue","black","brown","ivory","yellow","white"]


#user_Attribute array
#user 갯수만큼 array 생성
U_A_dict = {x:[0,0,0] for x in attr_list}
print("U_A_dict")
display(pd.DataFrame(U_A_dict))


for i in range(len(UID)):
    #rating_dict['UID'][0]=0번째 UID
    #rating_dict['PID'][0]=0번째 PID
    #rating_dict['RATE'][0]=0번째 RATING
    #product_dict["TYPE"][i]에 해당하는 행에 ++를 한다
    U_A_dict[product_dict["TYPE"][i]][rating_dict['UID'][i]]+=rating_dict['RATE'][i]
    U_A_dict[product_dict["COLOR"][i]][rating_dict['UID'][i]]+=rating_dict['RATE'][i]
print("U_A_dict")
display(pd.DataFrame(U_A_dict))

#user-Product table;
U_P_dict={x:[0,0,0] for x in PID}
print("U_P_dict")
display(pd.DataFrame(U_P_dict))
for j in PID:
    for i in range(3):
        U_P_dict[j][i]+=U_A_dict[product_dict['TYPE'][j]][i]
        U_P_dict[j][i]+=U_A_dict[product_dict['COLOR'][j]][i]
print("U_P_dict")
display(pd.DataFrame(U_P_dict))

#ranking
a=[[],[],[]]
for i in UID:
        a[i]={x:U_P_dict[x][i] for x in U_P_dict.keys()}

#서버로 보내는 sorted 된 product 리스트 #1에 UID
sorted(a[1],key=lambda k: a[1][k],reverse=True)
