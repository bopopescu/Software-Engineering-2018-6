/*Table 생성*/

CREATE TABLE account_app_account(
id int(11) NOT NULL AUTO_INCREMENT,
nickname varchar(20) NOT NULL,
address varchar(100),
phone varchar(20),
registration_date datetime(6) NOT NULL,
user_id int(11) NOT NULL,
PRIMARY KEY(id),
UNIQUE KEY(nickname),
UNIQUE KEY(user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE product_mgr_app_product(
id int(11) NOT NULL AUTO_INCREMENT,
texture varchar(50),
fabric varchar(50),
shape varchar(50),
part varchar(50),
style varchar(50),
name varchar(100) NOT NULL,
price int(11) NOT NULL,
img_url varchar(256),
product_url varchar(256),
view int(11),
PRIMARY KEY(id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE product_mgr_app_rating(
id int(11) NOT NULL AUTO_INCREMENT,
rate int(11) NOT NULL,
date datetime(6) NOT NULL,
account_id int(11) NOT NULL,
product_id int(11) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (account_id) REFERENCES account_app_account (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (product_id) REFERENCES product_mgr_app_product (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE recommend_app_recommend(
id int(11) NOT NULL AUTO_INCREMENT,
date datetime(6) NOT NULL,
account_id int(11) NOT NULL,
product_id int(11) NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (account_id) REFERENCES account_app_account (id) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (product_id) REFERENCES product_mgr_app_product (id) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*server로 넘기기 전
CREATE TABLE Member (
SN int(11) NOT NULL AUTO_INCREMENT,
ID varchar(30) NOT NULL,
PRIMARY KEY (SN),
UNIQUE KEY ID_UNIQUE (ID)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE Product (
SN int(11) NOT NULL AUTO_INCREMENT,
texture varchar(50) DEFAULT NULL,
fabric varchar(50) DEFAULT NULL,
shape varchar(50) DEFAULT NULL,
part varchar(50) DEFAULT NULL,
style varchar(50) DEFAULT NULL,
name varchar(100) NOT NULL,
price int(11) NOT NULL,
img_url varchar(100) NOT NULL,
product_url varchar(100) NOT NULL,
view int(5) DEFAULT '0',
PRIMARY KEY (SN)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE rating (
U_SN int(11) NOT NULL,
P_SN int(11) NOT NULL,
rate int(1) NOT NULL,
date DATE NOT NULL,
PRIMARY KEY (U_SN, P_SN),
FOREIGN KEY (U_SN) REFERENCES Member (SN) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (P_SN) REFERENCES Product (SN) ON DELETE NO ACTION ON UPDATE NO ACTION
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


CREATE TABLE recommend(
ID varchar(30) NOT NULL,
P_SN int(11) NOT NULL,
PRIMARY KEY (ID,P_SN),
FOREIGN KEY (ID) REFERENCES Member (ID) ON DELETE NO ACTION ON UPDATE NO ACTION,
FOREIGN KEY (P_SN) REFERENCES Product (SN) ON DELETE NO ACTION ON UPDATE NO ACTION,
rec_date DATE NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
*/

/*
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
*/


/*DB 삽입*/



/*Query*/


