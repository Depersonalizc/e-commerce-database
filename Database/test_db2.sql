CREATE TABLE `csc3170_2`.`orders` (
  `orderID` INT NOT NULL,
  `custID` INT NOT NULL,
  `sellerID` INT NOT NULL,
  `time` DATETIME NULL,
  `address` VARCHAR(50) NULL,
  `status` INT NULL,
  PRIMARY KEY (`orderID`));

CREATE TABLE `csc3170_2`.`order_item` (
  `orderID` INT NOT NULL,
  `itemID` INT NOT NULL,
  `quantity` INT NOT NULL,
  `rating` INT NOT NULL,
  PRIMARY KEY (`orderID`, `itemID`));

CREATE TABLE `csc3170_2`.`items` (
  `itemID` INT NOT NULL,
  `sellerID` INT NOT NULL,
  `type` VARCHAR(50) NOT NULL,
  `description` VARCHAR(200) NULL,
  `stock` INT NOT NULL,
  PRIMARY KEY (`itemID`));

CREATE TABLE `csc3170_2`.`sellers` (
  `sellerID` INT NOT NULL,
  `seller_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`sellerID`));

CREATE TABLE `csc3170_2`.`customers` (
  `custID` INT NOT NULL,
  `cust_name` VARCHAR(50) NOT NULL,
  `cust_gender` VARCHAR(6) NOT NULL,
  `cust_age` INT NOT NULL,
  PRIMARY KEY (`custID`));

CREATE TABLE `csc3170_2`.`addresses` (
  `custID` INT NOT NULL,
  `address` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`custID`, `address`));

insert into addresses(custID,address) values('1','Guangdong');
insert into addresses(custID,address) values('2','Guangdong');
insert into addresses(custID,address) values('3','Guangdong');
insert into addresses(custID,address) values('4','Guangdong');
insert into addresses(custID,address) values('5','Beijing');
insert into addresses(custID,address) values('6','Anhui');
insert into addresses(custID,address) values('7','Hebei');
insert into addresses(custID,address) values('8','Shanghai');
insert into addresses(custID,address) values('9','Jiangsu');
insert into addresses(custID,address) values('10','Henan');
insert into items(itemID,sellerID,type,description,stock) values('1','4','Car','Benz','85');
insert into items(itemID,sellerID,type,description,stock) values('2','8','Jewelry','diamond','20');
insert into items(itemID,sellerID,type,description,stock) values('3','7','Home improvement products','Safeguard shower gel','62');
insert into items(itemID,sellerID,type,description,stock) values('4','5','Car','BMW','57');
insert into items(itemID,sellerID,type,description,stock) values('5','9','Medicine','cold cure','100');
insert into items(itemID,sellerID,type,description,stock) values('6','2','Digital appliance','computer','93');
insert into items(itemID,sellerID,type,description,stock) values('7','10','Food','vegetable','82');
insert into items(itemID,sellerID,type,description,stock) values('8','7','Food','BESTORE dried pork slices ','81');
insert into items(itemID,sellerID,type,description,stock) values('9','1','Food','mutton','18');
insert into items(itemID,sellerID,type,description,stock) values('10','10','Food','milk','55');
insert into items(itemID,sellerID,type,description,stock) values('11','8','Digital appliance','heatset','32');
insert into items(itemID,sellerID,type,description,stock) values('12','3','Wear','shirt','36');
insert into items(itemID,sellerID,type,description,stock) values('13','9','Home improvement products','laundry detergent','32');
insert into items(itemID,sellerID,type,description,stock) values('14','6','Jewelry','gold','90');
insert into items(itemID,sellerID,type,description,stock) values('15','4','Digital appliance','camera','40');
insert into items(itemID,sellerID,type,description,stock) values('16','10','Car','VW','64');
insert into items(itemID,sellerID,type,description,stock) values('17','3','Packaging','hop-pocket','71');
insert into items(itemID,sellerID,type,description,stock) values('18','2','Articles of luxury','PRADA','46');
insert into items(itemID,sellerID,type,description,stock) values('19','7','Food','BE&CHEERY snacks','20');
insert into items(itemID,sellerID,type,description,stock) values('20','2','Food','coffee','48');
insert into items(itemID,sellerID,type,description,stock) values('21','7','Food','Lapsang souchong','38');
insert into items(itemID,sellerID,type,description,stock) values('22','10','Medicine','digestive','72');
insert into items(itemID,sellerID,type,description,stock) values('23','6','Car','BYD','17');
insert into items(itemID,sellerID,type,description,stock) values('24','9','Medicine','hypotensor','92');
insert into items(itemID,sellerID,type,description,stock) values('25','1','Mother and baby products','baby diapers','62');
insert into items(itemID,sellerID,type,description,stock) values('26','4','Home improvement products','wallpaper','45');
insert into items(itemID,sellerID,type,description,stock) values('27','8','Mother and baby products','milk powder','29');
insert into items(itemID,sellerID,type,description,stock) values('28','8','Food','instant food','17');
insert into items(itemID,sellerID,type,description,stock) values('29','6','Phone','Iphone','33');
insert into items(itemID,sellerID,type,description,stock) values('30','4','Jewelry','ring','20');
insert into items(itemID,sellerID,type,description,stock) values('31','9','Articles of luxury','VALENTINO','68');
insert into items(itemID,sellerID,type,description,stock) values('32','5','Home improvement products','light','24');
insert into items(itemID,sellerID,type,description,stock) values('33','3','Food','chocolate','30');
insert into items(itemID,sellerID,type,description,stock) values('34','6','Food','candies','67');
insert into items(itemID,sellerID,type,description,stock) values('35','7','Phone','MIUI','90');
insert into items(itemID,sellerID,type,description,stock) values('36','7','Food','NongFu Spring','34');
insert into items(itemID,sellerID,type,description,stock) values('37','9','Food','wine','31');
insert into items(itemID,sellerID,type,description,stock) values('38','2','Food','rice noodles','72');
insert into items(itemID,sellerID,type,description,stock) values('39','8','Car','Ford','94');
insert into items(itemID,sellerID,type,description,stock) values('40','10','Mother and baby products','children toys','81');
insert into items(itemID,sellerID,type,description,stock) values('41','6','Jewelry','necklace','65');
insert into items(itemID,sellerID,type,description,stock) values('42','7','Jewelry','DW bracelet','57');
insert into items(itemID,sellerID,type,description,stock) values('43','8','Articles of luxury','BALENGIAGA','87');
insert into items(itemID,sellerID,type,description,stock) values('44','7','Wear','playboy pants','91');
insert into items(itemID,sellerID,type,description,stock) values('45','8','Home improvement products','bed','17');
insert into items(itemID,sellerID,type,description,stock) values('46','5','Packaging','bag','27');
insert into items(itemID,sellerID,type,description,stock) values('47','10','Digital appliance','xbox','92');
insert into items(itemID,sellerID,type,description,stock) values('48','6','Mother and baby products','feeder','18');
insert into items(itemID,sellerID,type,description,stock) values('49','7','Food','Oreo cookie','60');
insert into items(itemID,sellerID,type,description,stock) values('50','1','Phone','SAMSUNG','14');
insert into orders(orderID,custID,sellerID,time,address,status) values('1','2','1','20140423','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('2','8','2','20140428','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('3','3','1','20120923','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('4','7','1','20150413','Hebei','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('5','4','6','20170209','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('6','8','2','20210828','Shanghai','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('7','3','6','20191125','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('8','6','10','20171203','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('9','5','10','20190315','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('10','6','4','20160817','Anhui','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('11','3','7','20201116','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('12','9','9','20151216','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('13','3','5','20140717','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('14','2','8','20181212','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('15','10','4','20160817','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('16','9','8','20161126','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('17','5','6','20120807','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('18','2','4','20130812','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('19','9','6','20211118','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('20','4','4','20120724','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('21','2','4','20150423','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('22','8','7','20161102','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('23','1','6','20141114','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('24','6','7','20141215','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('25','7','6','20200404','Hebei','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('26','10','4','20130904','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('27','2','4','20140326','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('28','7','5','20160103','Hebei','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('29','9','6','20190308','Jiangsu','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('30','5','6','20160505','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('31','8','8','20141101','Shanghai','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('32','4','6','20141204','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('33','3','10','20180817','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('34','9','7','20170223','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('35','8','5','20170810','Shanghai','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('36','2','9','20161001','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('37','6','10','20100814','Anhui','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('38','5','4','20150504','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('39','5','9','20180328','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('40','3','2','20100119','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('41','8','1','20100923','Shanghai','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('42','8','4','20130418','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('43','1','4','20160626','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('44','3','6','20150608','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('45','3','6','20130625','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('46','2','5','20140112','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('47','9','9','20160301','Jiangsu','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('48','10','8','20100610','Henan','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('49','6','10','20100609','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('50','6','8','20131223','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('51','3','8','20120712','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('52','3','5','20130507','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('53','8','2','20210917','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('54','1','5','20110805','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('55','5','1','20110921','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('56','10','4','20110328','Henan','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('57','1','3','20110309','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('58','9','1','20100410','Jiangsu','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('59','4','6','20120325','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('60','6','10','20181105','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('61','7','2','20170523','Hebei','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('62','1','8','20110517','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('63','4','7','20200515','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('64','10','2','20161026','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('65','2','10','20140527','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('66','9','3','20120521','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('67','7','8','20121024','Hebei','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('68','10','9','20160804','Henan','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('69','5','3','20161223','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('70','3','2','20100122','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('71','6','4','20170409','Anhui','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('72','5','4','20140724','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('73','4','6','20210707','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('74','4','7','20100928','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('75','7','1','20191021','Hebei','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('76','9','2','20120228','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('77','10','10','20210814','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('78','6','9','20200424','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('79','2','10','20140415','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('80','3','1','20120126','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('81','8','3','20111011','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('82','1','9','20140923','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('83','2','9','20210213','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('84','5','5','20160913','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('85','3','4','20200616','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('86','10','1','20140907','Henan','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('87','6','6','20140625','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('88','2','1','20140701','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('89','5','9','20210422','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('90','9','6','20120207','Jiangsu','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('91','4','3','20170726','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('92','3','10','20171009','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('93','2','5','20150605','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('94','6','6','20121221','Anhui','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('95','10','8','20110220','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('96','9','4','20150301','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('97','8','4','20180728','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('98','7','2','20160628','Hebei','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('99','2','6','20140920','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('100','5','8','20200421','Beijing','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('101','1','7','20200211','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('102','3','7','20200104','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('103','4','7','20201022','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('104','5','7','20201214','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('105','6','7','20201028','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('106','8','7','20200804','Shanghai','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('107','1','7','20200805','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('108','2','7','20201128','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('109','10','7','20200205','Henan','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('110','8','7','20201117','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('111','9','7','20201127','Jiangsu','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('112','6','7','20201108','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('113','5','7','20200201','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('114','3','7','20200324','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('115','2','7','20200625','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('116','1','7','20200511','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('117','4','7','20200302','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('118','6','7','20200710','Anhui','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('119','7','7','20200811','Hebei','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('120','8','7','20211022','Shanghai','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('121','5','7','20211225','Beijing','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('122','3','7','20210422','Guangdong','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('123','4','7','20210522','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('124','2','7','20210710','Guangdong','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('125','3','7','20210919','Guangdong','1');
insert into order_item(orderID,itemID,quantity,rating) values('1','9','1','4');
insert into order_item(orderID,itemID,quantity,rating) values('1','25','6','4');
insert into order_item(orderID,itemID,quantity,rating) values('2','6','4','7');
insert into order_item(orderID,itemID,quantity,rating) values('2','18','9','2');
insert into order_item(orderID,itemID,quantity,rating) values('3','17','2','10');
insert into order_item(orderID,itemID,quantity,rating) values('4','9','8','8');
insert into order_item(orderID,itemID,quantity,rating) values('4','25','10','1');
insert into order_item(orderID,itemID,quantity,rating) values('4','50','4','5');
insert into order_item(orderID,itemID,quantity,rating) values('5','14','8','3');
insert into order_item(orderID,itemID,quantity,rating) values('6','6','8','1');
insert into order_item(orderID,itemID,quantity,rating) values('6','18','9','6');
insert into order_item(orderID,itemID,quantity,rating) values('6','20','5','3');
insert into order_item(orderID,itemID,quantity,rating) values('7','23','6','6');
insert into order_item(orderID,itemID,quantity,rating) values('8','7','4','3');
insert into order_item(orderID,itemID,quantity,rating) values('9','10','4','10');
insert into order_item(orderID,itemID,quantity,rating) values('10','1','6','2');
insert into order_item(orderID,itemID,quantity,rating) values('11','3','9','8');
insert into order_item(orderID,itemID,quantity,rating) values('11','8','8','6');
insert into order_item(orderID,itemID,quantity,rating) values('12','5','6','6');
insert into order_item(orderID,itemID,quantity,rating) values('13','4','7','1');
insert into order_item(orderID,itemID,quantity,rating) values('14','2','8','6');
insert into order_item(orderID,itemID,quantity,rating) values('15','15','3','3');
insert into order_item(orderID,itemID,quantity,rating) values('15','26','5','2');
insert into order_item(orderID,itemID,quantity,rating) values('16','11','5','3');
insert into order_item(orderID,itemID,quantity,rating) values('17','29','5','8');
insert into order_item(orderID,itemID,quantity,rating) values('18','30','6','1');
insert into order_item(orderID,itemID,quantity,rating) values('19','34','2','4');
insert into order_item(orderID,itemID,quantity,rating) values('20','1','5','9');
insert into order_item(orderID,itemID,quantity,rating) values('20','15','2','10');
insert into order_item(orderID,itemID,quantity,rating) values('21','26','9','10');
insert into order_item(orderID,itemID,quantity,rating) values('22','19','9','9');
insert into order_item(orderID,itemID,quantity,rating) values('23','41','6','3');
insert into order_item(orderID,itemID,quantity,rating) values('24','21','3','10');
insert into order_item(orderID,itemID,quantity,rating) values('25','48','2','8');
insert into order_item(orderID,itemID,quantity,rating) values('26','1','2','8');
insert into order_item(orderID,itemID,quantity,rating) values('27','15','2','7');
insert into order_item(orderID,itemID,quantity,rating) values('28','32','8','2');
insert into order_item(orderID,itemID,quantity,rating) values('29','41','8','5');
insert into order_item(orderID,itemID,quantity,rating) values('30','48','7','7');
insert into order_item(orderID,itemID,quantity,rating) values('31','27','2','9');
insert into order_item(orderID,itemID,quantity,rating) values('32','14','2','3');
insert into order_item(orderID,itemID,quantity,rating) values('33','16','9','1');
insert into order_item(orderID,itemID,quantity,rating) values('34','35','2','7');
insert into order_item(orderID,itemID,quantity,rating) values('35','46','3','9');
insert into order_item(orderID,itemID,quantity,rating) values('35','4','6','2');
insert into order_item(orderID,itemID,quantity,rating) values('36','13','10','10');
insert into order_item(orderID,itemID,quantity,rating) values('37','22','8','10');
insert into order_item(orderID,itemID,quantity,rating) values('38','26','10','4');
insert into order_item(orderID,itemID,quantity,rating) values('39','24','6','5');
insert into order_item(orderID,itemID,quantity,rating) values('39','31','1','1');
insert into order_item(orderID,itemID,quantity,rating) values('40','38','3','4');
insert into order_item(orderID,itemID,quantity,rating) values('40','6','9','5');
insert into order_item(orderID,itemID,quantity,rating) values('40','18','6','2');
insert into order_item(orderID,itemID,quantity,rating) values('41','9','7','8');
insert into order_item(orderID,itemID,quantity,rating) values('41','25','4','8');
insert into order_item(orderID,itemID,quantity,rating) values('42','30','8','3');
insert into order_item(orderID,itemID,quantity,rating) values('42','1','1','2');
insert into order_item(orderID,itemID,quantity,rating) values('43','15','5','2');
insert into order_item(orderID,itemID,quantity,rating) values('44','23','5','7');
insert into order_item(orderID,itemID,quantity,rating) values('44','14','7','10');
insert into order_item(orderID,itemID,quantity,rating) values('44','48','7','6');
insert into order_item(orderID,itemID,quantity,rating) values('45','41','7','8');
insert into order_item(orderID,itemID,quantity,rating) values('46','4','4','6');
insert into order_item(orderID,itemID,quantity,rating) values('47','37','4','6');
insert into order_item(orderID,itemID,quantity,rating) values('48','28','2','9');
insert into order_item(orderID,itemID,quantity,rating) values('49','40','8','10');
insert into order_item(orderID,itemID,quantity,rating) values('50','39','7','8');
insert into order_item(orderID,itemID,quantity,rating) values('51','43','1','10');
insert into order_item(orderID,itemID,quantity,rating) values('52','4','3','9');
insert into order_item(orderID,itemID,quantity,rating) values('53','6','9','1');
insert into order_item(orderID,itemID,quantity,rating) values('53','20','4','5');
insert into order_item(orderID,itemID,quantity,rating) values('54','32','2','3');
insert into order_item(orderID,itemID,quantity,rating) values('55','50','4','9');
insert into order_item(orderID,itemID,quantity,rating) values('56','15','3','3');
insert into order_item(orderID,itemID,quantity,rating) values('57','12','10','7');
insert into order_item(orderID,itemID,quantity,rating) values('57','17','4','7');
insert into order_item(orderID,itemID,quantity,rating) values('58','9','3','2');
insert into order_item(orderID,itemID,quantity,rating) values('59','41','6','4');
insert into order_item(orderID,itemID,quantity,rating) values('60','47','6','9');
insert into order_item(orderID,itemID,quantity,rating) values('60','7','4','4');
insert into order_item(orderID,itemID,quantity,rating) values('60','10','6','1');
insert into order_item(orderID,itemID,quantity,rating) values('60','16','3','10');
insert into order_item(orderID,itemID,quantity,rating) values('60','22','1','7');
insert into order_item(orderID,itemID,quantity,rating) values('61','38','9','8');
insert into order_item(orderID,itemID,quantity,rating) values('62','45','1','3');
insert into order_item(orderID,itemID,quantity,rating) values('63','36','3','6');
insert into order_item(orderID,itemID,quantity,rating) values('64','18','9','6');
insert into order_item(orderID,itemID,quantity,rating) values('65','40','6','7');
insert into order_item(orderID,itemID,quantity,rating) values('66','12','1','5');
insert into order_item(orderID,itemID,quantity,rating) values('67','43','6','5');
insert into order_item(orderID,itemID,quantity,rating) values('68','5','10','8');
insert into order_item(orderID,itemID,quantity,rating) values('69','17','5','7');
insert into order_item(orderID,itemID,quantity,rating) values('70','18','10','8');
insert into order_item(orderID,itemID,quantity,rating) values('71','26','3','9');
insert into order_item(orderID,itemID,quantity,rating) values('71','30','7','7');
insert into order_item(orderID,itemID,quantity,rating) values('72','1','4','6');
insert into order_item(orderID,itemID,quantity,rating) values('73','23','5','3');
insert into order_item(orderID,itemID,quantity,rating) values('73','41','6','10');
insert into order_item(orderID,itemID,quantity,rating) values('73','48','5','5');
insert into order_item(orderID,itemID,quantity,rating) values('74','49','7','10');
insert into order_item(orderID,itemID,quantity,rating) values('74','44','9','9');
insert into order_item(orderID,itemID,quantity,rating) values('74','42','8','7');
insert into order_item(orderID,itemID,quantity,rating) values('75','9','10','9');
insert into order_item(orderID,itemID,quantity,rating) values('76','18','10','3');
insert into order_item(orderID,itemID,quantity,rating) values('76','20','1','9');
insert into order_item(orderID,itemID,quantity,rating) values('77','7','5','1');
insert into order_item(orderID,itemID,quantity,rating) values('78','13','10','7');
insert into order_item(orderID,itemID,quantity,rating) values('78','24','3','1');
insert into order_item(orderID,itemID,quantity,rating) values('78','31','6','9');
insert into order_item(orderID,itemID,quantity,rating) values('79','22','3','9');
insert into order_item(orderID,itemID,quantity,rating) values('80','25','5','2');
insert into order_item(orderID,itemID,quantity,rating) values('81','12','6','1');
insert into order_item(orderID,itemID,quantity,rating) values('82','37','5','8');
insert into order_item(orderID,itemID,quantity,rating) values('83','5','10','3');
insert into order_item(orderID,itemID,quantity,rating) values('84','46','2','5');
insert into order_item(orderID,itemID,quantity,rating) values('85','26','2','3');
insert into order_item(orderID,itemID,quantity,rating) values('86','50','3','7');
insert into order_item(orderID,itemID,quantity,rating) values('87','29','7','3');
insert into order_item(orderID,itemID,quantity,rating) values('88','9','6','4');
insert into order_item(orderID,itemID,quantity,rating) values('89','31','6','6');
insert into order_item(orderID,itemID,quantity,rating) values('90','34','5','1');
insert into order_item(orderID,itemID,quantity,rating) values('90','14','3','9');
insert into order_item(orderID,itemID,quantity,rating) values('91','33','1','3');
insert into order_item(orderID,itemID,quantity,rating) values('92','40','3','8');
insert into order_item(orderID,itemID,quantity,rating) values('93','32','9','9');
insert into order_item(orderID,itemID,quantity,rating) values('93','46','3','7');
insert into order_item(orderID,itemID,quantity,rating) values('94','48','6','9');
insert into order_item(orderID,itemID,quantity,rating) values('95','2','8','9');
insert into order_item(orderID,itemID,quantity,rating) values('96','1','1','5');
insert into order_item(orderID,itemID,quantity,rating) values('97','15','3','3');
insert into order_item(orderID,itemID,quantity,rating) values('97','26','2','2');
insert into order_item(orderID,itemID,quantity,rating) values('97','30','4','3');
insert into order_item(orderID,itemID,quantity,rating) values('98','20','9','7');
insert into order_item(orderID,itemID,quantity,rating) values('98','18','4','7');
insert into order_item(orderID,itemID,quantity,rating) values('99','41','10','7');
insert into order_item(orderID,itemID,quantity,rating) values('100','11','9','4');
insert into order_item(orderID,itemID,quantity,rating) values('101','3','5','9');
insert into order_item(orderID,itemID,quantity,rating) values('102','8','4','10');
insert into order_item(orderID,itemID,quantity,rating) values('103','19','2','9');
insert into order_item(orderID,itemID,quantity,rating) values('104','21','6','2');
insert into order_item(orderID,itemID,quantity,rating) values('105','35','2','10');
insert into order_item(orderID,itemID,quantity,rating) values('106','36','5','5');
insert into order_item(orderID,itemID,quantity,rating) values('107','42','9','10');
insert into order_item(orderID,itemID,quantity,rating) values('108','44','4','2');
insert into order_item(orderID,itemID,quantity,rating) values('109','49','7','7');
insert into order_item(orderID,itemID,quantity,rating) values('110','3','8','7');
insert into order_item(orderID,itemID,quantity,rating) values('111','3','1','9');
insert into order_item(orderID,itemID,quantity,rating) values('112','8','10','9');
insert into order_item(orderID,itemID,quantity,rating) values('113','8','4','6');
insert into order_item(orderID,itemID,quantity,rating) values('114','19','8','10');
insert into order_item(orderID,itemID,quantity,rating) values('115','19','5','7');
insert into order_item(orderID,itemID,quantity,rating) values('116','44','6','7');
insert into order_item(orderID,itemID,quantity,rating) values('117','49','3','4');
insert into order_item(orderID,itemID,quantity,rating) values('118','49','10','8');
insert into order_item(orderID,itemID,quantity,rating) values('119','42','1','4');
insert into order_item(orderID,itemID,quantity,rating) values('120','35','6','6');
insert into order_item(orderID,itemID,quantity,rating) values('121','36','10','9');
insert into order_item(orderID,itemID,quantity,rating) values('122','36','2','9');
insert into order_item(orderID,itemID,quantity,rating) values('123','21','1','5');
insert into order_item(orderID,itemID,quantity,rating) values('124','3','10','4');
insert into order_item(orderID,itemID,quantity,rating) values('125','42','1','4');
insert into sellers(sellerID,seller_name) values('1','Wade');
insert into sellers(sellerID,seller_name) values('2','Gail');
insert into sellers(sellerID,seller_name) values('3','Gallagher');
insert into sellers(sellerID,seller_name) values('4','Calvin');
insert into sellers(sellerID,seller_name) values('5','Babs');
insert into sellers(sellerID,seller_name) values('6','Babington');
insert into sellers(sellerID,seller_name) values('7','Oakley');
insert into sellers(sellerID,seller_name) values('8','Olive');
insert into sellers(sellerID,seller_name) values('9','Una');
insert into sellers(sellerID,seller_name) values('10','Gage');