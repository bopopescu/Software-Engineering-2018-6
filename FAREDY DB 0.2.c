/*Table ����*/
 
CREATE TABLE Member ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
ID varchar(30) NOT NULL, 
PW varchar(45) NOT NULL, 
name varchar(45) NOT NULL, 
nickname varchar(45) NOT NULL, 
address varchar(100) DEFAULT NULL, 
phone_number varchar(15) NOT NULL, 
PRIMARY KEY (SN), 
UNIQUE KEY ID_UNIQUE (ID), 
UNIQUE KEY nickname_UNIQUE (nickname) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Product ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
type varchar(7) NOT NULL, 
color varchar(7) NOT NULL, 
name varchar(45) NOT NULL, 
price int(11) NOT NULL, 
img_url varchar(100) NOT NULL, 
product_url varchar(100) NOT NULL,
view int(5) DEFAULT NULL,
PRIMARY KEY (SN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS rating (
U_SN int(11) NOT NULL,
P_SN int(11) NOT NULL,
rate int(1) NOT NULL,
date DATE NOT NULL,
PRIMARY KEY (U_SN, P_SN),
FOREIGN KEY (U_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION, 
FOREIGN KEY (P_SN) REFERENCES Product (SN) ON DELETE NO ACTION ON UPDATE NO ACTION
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_Notice ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
title varchar(45) NOT NULL, 
date datetime NOT NULL, 
views int(11) NOT NULL, 
contents varchar(1000) DEFAULT NULL, 
writer_SN int(11) NOT NULL, 
PRIMARY KEY (SN), 
KEY w1_idx (writer_SN), 
CONSTRAINT w1 FOREIGN KEY (writer_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE CASCADE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_News ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
title varchar(45) NOT NULL, 
date datetime NOT NULL, 
views int(11) NOT NULL, 
contents varchar(1000) DEFAULT NULL, 
writer_SN int(11) NOT NULL, 
PRIMARY KEY (SN), 
KEY w2_idx (writer_SN), 
CONSTRAINT w2 FOREIGN KEY (writer_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE CASCADE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_Free ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
title varchar(45) NOT NULL, 
date datetime NOT NULL, 
views int(11) NOT NULL, 
contents varchar(1000) DEFAULT NULL, 
writer_SN int(11) NOT NULL, 
PRIMARY KEY (SN), 
KEY w3_idx (writer_SN), 
CONSTRAINT w3 FOREIGN KEY (writer_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE CASCADE 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_Comment_Notice ( 
SN int(11) NOT NULL, 
contents varchar(300) NOT NULL, 
wirter_SN int(11) NOT NULL, 
community_SN int(11) NOT NULL, 
date datetime DEFAULT NULL, 
PRIMARY KEY (SN), 
KEY fk_Community_Comment_Notice_1_idx (wirter_SN), 
KEY fk_Community_Comment_Notice_2_idx (community_SN), 
CONSTRAINT fk_Community_Comment_Notice_1 FOREIGN KEY (wirter_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION, 
CONSTRAINT fk_Community_Comment_Notice_2 FOREIGN KEY (community_SN) REFERENCES Community_Notice (SN) ON DELETE NO ACTION ON UPDATE NO ACTION 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_Comment_News ( 
SN int(11) NOT NULL, 
contents varchar(300) NOT NULL, 
wirter_SN int(11) NOT NULL, 
community_SN int(11) NOT NULL, 
date datetime DEFAULT NULL, 
PRIMARY KEY (SN), 
KEY fk_Community_Comment_News_1_idx (wirter_SN), 
KEY fk_Community_Comment_News_2_idx (community_SN), 
CONSTRAINT fk_Community_Comment_News_1 FOREIGN KEY (wirter_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION, 
CONSTRAINT fk_Community_Comment_News_2 FOREIGN KEY (community_SN) REFERENCES Community_News (SN) ON DELETE NO ACTION ON UPDATE NO ACTION 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE Community_Comment_Free ( 
SN int(11) NOT NULL, 
contents varchar(300) NOT NULL, 
wirter_SN int(11) NOT NULL, 
community_SN int(11) NOT NULL, 
date datetime DEFAULT NULL, 
PRIMARY KEY (SN), 
KEY fk_Community_Comment_Free_1_idx (wirter_SN), 
KEY fk_Community_Comment_Free_2_idx (community_SN), 
CONSTRAINT fk_Community_Comment_Free_1 FOREIGN KEY (wirter_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION, 
CONSTRAINT fk_Community_Comment_Free_2 FOREIGN KEY (community_SN) REFERENCES Community_Free (SN) ON DELETE NO ACTION ON UPDATE NO ACTION 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



/*DB ����*/

/*
CREATE TABLE Product ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
type varchar(7) NOT NULL, 
color varchar(7) NOT NULL, 
name varchar(45) NOT NULL, 
price int(11) NOT NULL, 
stock int(11) NOT NULL, 
img_url varchar(100) NOT NULL, 
product_url varchar(100) NOT NULL,
PRIMARY KEY (SN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/

INSERT INTO product(type,color,name,price,img_url,product_url)
values('�װ�����','red','�װ�����1','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('�װ�����','blue','�װ�����2','60000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('�װ�����','black','�װ�����3','70000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('����','blue','û����1','30000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('����','black','û����2','40000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('����','brown','�����1','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('��Ʈ','brown','��Ʈ1','80000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('��Ʈ','ivory','��Ʈ2','70000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('��Ʈ','white','��Ʈ3','100000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('Ƽ����','blue','����1','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('Ƽ����','red','����2','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('Ƽ����','blue','����1','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');
INSERT INTO product(type,color,name,price,img_url,product_url) 
values('Ƽ����','yellow','����2','50000','https://image.musinsa.com/mfile_s01//_lookbook/list5bee4f0b4549e','https://image.musinsa.com');

/*
CREATE TABLE Member ( 
SN int(11) NOT NULL AUTO_INCREMENT, 
ID varchar(30) NOT NULL, 
PW varchar(45) NOT NULL, 
name varchar(45) NOT NULL, 
img_url varchar(45) DEFAULT NULL, 
nickname varchar(45) NOT NULL, 
address varchar(100) DEFAULT NULL, 
phone_number int(11) DEFAULT NULL, 
PRIMARY KEY (SN), 
UNIQUE KEY ID_UNIQUE (ID), 
UNIQUE KEY nickname_UNIQUE (nickname) 
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/

insert into member(ID,PW,name,nickname,address,phone_number) values('aaaaa','1234','â��','nickname1','address1','01012341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('bbbbb','2234','����','nickname2','address2','01022341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('ccccc','1234','����','nickname3','address1','01032341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('ddddd','1234','���','nickname4','address1','01032341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('eeeee','1234','��ö','nickname5','address1','01032341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('fffff','1234','��ȯ','nickname6','address1','01032341234');
insert into member(ID,PW,name,nickname,address,phone_number) values('ggggg','1234','aproov','nickname7','address1','01032341234');
/*
CREATE TABLE IF NOT EXISTS rating (
U_SN int(11) NOT NULL,
P_SN int(11) NOT NULL,
rate int(1) NOT NULL,
date DATE NOT NULL,
PRIMARY KEY (U_SN, P_SN),
FOREIGN KEY (U_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION, 
FOREIGN KEY (P_SN) REFERENCES Product (SN) ON DELETE NO ACTION ON UPDATE NO ACTION
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/

insert into rating(U_SN,P_SN,rate,date) values('1','1','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','2','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','3','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','4','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','5','2',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','6','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','7','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','8','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','9','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','10','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','11','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('1','12','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','1','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','2','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','3','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','4','2',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','5','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','6','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','7','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','8','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','9','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','10','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','11','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('2','12','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','1','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','2','0',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','3','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','4','2',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','5','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','6','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','7','5',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','8','1',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','9','2',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','10','3',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','11','4',NOW());
insert into rating(U_SN,P_SN,rate,date) values('3','12','5',NOW());

/*Query*/


