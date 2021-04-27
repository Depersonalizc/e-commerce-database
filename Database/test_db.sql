CREATE TABLE `csc3170`.`orders` (
  `orderID` INT NOT NULL,
  `custID` INT NOT NULL,
  `sellerID` INT NOT NULL,
  `time` DATETIME NULL,
  `address` VARCHAR(50) NULL,
  `status` INT NULL,
  PRIMARY KEY (`orderID`));

CREATE TABLE `csc3170`.`order_item` (
  `orderID` INT NOT NULL,
  `itemID` INT NOT NULL,
  `quantity` INT NOT NULL,
  `rating` INT NOT NULL,
  PRIMARY KEY (`orderID`, `itemID`));

CREATE TABLE `csc3170`.`items` (
  `itemID` INT NOT NULL,
  `sellerID` INT NOT NULL,
  `type` VARCHAR(50) NOT NULL,
  `description` VARCHAR(200) NULL,
  `stock` INT NOT NULL,
  PRIMARY KEY (`itemID`));

CREATE TABLE `csc3170`.`sellers` (
  `sellerID` INT NOT NULL,
  `seller_name` VARCHAR(50) NOT NULL,
  PRIMARY KEY (`sellerID`));

CREATE TABLE `csc3170`.`customers` (
  `custID` INT NOT NULL,
  `cust_name` VARCHAR(50) NOT NULL,
  `cust_gender` VARCHAR(6) NOT NULL,
  `cust_age` INT NOT NULL,
  PRIMARY KEY (`custID`));

CREATE TABLE `csc3170`.`addresses` (
  `custID` INT NOT NULL,
  `address` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`custID`, `address`));
  
insert into addresses(custID,address) values('1','102122');
insert into addresses(custID,address) values('2','102157');
insert into addresses(custID,address) values('3','102415');
insert into addresses(custID,address) values('4','103542');
insert into addresses(custID,address) values('5','235674');
insert into addresses(custID,address) values('6','345795');
insert into addresses(custID,address) values('7','325643');
insert into addresses(custID,address) values('8','385567');
insert into addresses(custID,address) values('9','243156');
insert into addresses(custID,address) values('10','235672');
insert into customers(custID,cust_name,cust_gender,cust_age) values('1','Abia','man','21');
insert into customers(custID,cust_name,cust_gender,cust_age) values('2','Brewster','woman','34');
insert into customers(custID,cust_name,cust_gender,cust_age) values('3','Bridget','man','56');
insert into customers(custID,cust_name,cust_gender,cust_age) values('4','Fabian','woman','12');
insert into customers(custID,cust_name,cust_gender,cust_age) values('5','Pack','woman','67');
insert into customers(custID,cust_name,cust_gender,cust_age) values('6','Tabor','man','28');
insert into customers(custID,cust_name,cust_gender,cust_age) values('7','Halley','woman','31');
insert into customers(custID,cust_name,cust_gender,cust_age) values('8','Eddy','woman','44');
insert into customers(custID,cust_name,cust_gender,cust_age) values('9','Dan','man','52');
insert into customers(custID,cust_name,cust_gender,cust_age) values('10','Zola','man','25');
insert into items(itemID,sellerID,type,description,stock) values('1','4','Toiletries','We use decomposition techniques to quantify the share of employment disparities that is rooted in pre-epidemic sorting across occupations and industries. Such sorting explains a substantial share of many of the disparities in employment outcomes. Further, some of the job and industry factors that protected jobs during the early months of the epidemic are often associated with higher income and job security in normal times.','85');
insert into items(itemID,sellerID,type,description,stock) values('2','8','Imported goods','Our paper examines the distribution of job losses during the early epidemic in a social stratification framework that exploits population subgroups sorting across different jobs.','20');
insert into items(itemID,sellerID,type,description,stock) values('3','7','Women’s wear','A wide range of evidence indicates that the epidemic led to a major decline in social and economic activity in 2020. Large sectors of the economy – transportation, hospitality, and tourism – essentially shut down their normal operations between February and April, as state governments implemented a range of social distancing mandates','62');
insert into items(itemID,sellerID,type,description,stock) values('4','5','Men’s wear','Focusing on recent unemployment allows us to study recent job losses using only cross-sectional models.','57');
insert into items(itemID,sellerID,type,description,stock) values('5','9','Food','We also use data from the 2019 Occupational Information Network (O*NET) Work Context module, which reports summary measures of the tasks used in 968 occupations (O*NET National Center for O*NET Development 2020).','100');
insert into items(itemID,sellerID,type,description,stock) values('6','2','Shoes','These occupational characteristics in the O*NET prior to the epidemic. This means that they do not capture “work practice innovations” that may have been induced by the epidemic, such as the fact that many teachers and professors have transitioned from face-to-face to online instruction during the epidemic','93');
insert into items(itemID,sellerID,type,description,stock) values('7','10','Phone','We also compared our Remote Work and Face-to-Face indices with Dingel and Neiman (2020)’s Telework classification, which might be viewed as a substitute to our Remote Work index.','82');
insert into items(itemID,sellerID,type,description,stock) values('8','7','Bags and suitcases','Finally, the correlation between our Remote Work index, and the Teleworkable variable is 0.51, suggesting that the two measures are indeed fairly similar','81');
insert into items(itemID,sellerID,type,description,stock) values('9','1','Sporting goods','The U.S. Department of Homeland Security (DHS) issued guidance that describes 14 essential critical infrastructure sectors during the COVID-19 epidemic','18');
insert into items(itemID,sellerID,type,description,stock) values('10','10','Jewelry','From the 287 industry categories at the four-digit level, 194 are identified as essential in 17 out of 20 NAICS sectors.','55');
insert into items(itemID,sellerID,type,description,stock) values('11','8','Electric appliance','The light grey lines on the figure show that employment losses during the COVID-19 pandemic dwarf the declines for the other two recessions, which span nine and nineteen months respectively.','32');
insert into items(itemID,sellerID,type,description,stock) values('12','3','Car accessories','Young (ages 18-24) and Hispanic workers fared the worst during the COVID-19 pandemic when compared to older and non-Hispanic workers and to the previous recessions','36');
insert into items(itemID,sellerID,type,description,stock) values('13','9','Health care products','Employment effects are polarized by education: employment declines less for high school dropouts and college graduates compared to the intermediate education groups.','32');
insert into items(itemID,sellerID,type,description,stock) values('14','6','Medicine','Comparing the decrease in employment between February and April (light gray) to that between February and May (dark gray) indicates that there were gains in employment between April and May as states began re-opening.','90');
insert into items(itemID,sellerID,type,description,stock) values('15','4','Car','They did not recover in May as much as would have been expected given the decline in employment in April,','40');
insert into items(itemID,sellerID,type,description,stock) values('16','10','Articles of luxury','The bar charts in this section highlight Hispanics, young workers (between 18 and 24 years old), and single parents to be the most vulnerable workers as a result of the epidemic, and those most in need of policy protection.','64');
insert into items(itemID,sellerID,type,description,stock) values('17','3','Packaging','To examine employment disruptions in the early epidemic, we use data from the March, April, and May waves of the 2020 CPS. The March CPS data were collected largely before the major responses are observed and we view March as a hybrid period.','71');
insert into items(itemID,sellerID,type,description,stock) values('18','2','Digital appliance','Ignoring re-employment, this measure captures employment disruptions since February in each subsequent monthly CPS.','46');
insert into items(itemID,sellerID,type,description,stock) values('19','7','Home improvement products','Table 1 reports estimates from March (left panel), April (middle), and May (right). Column (1) in all three panels shows estimates from models that control for occupation and individual characteristics, but not for the number of COVID-19 cases in the state.','20');
insert into items(itemID,sellerID,type,description,stock) values('20','2','Underwear','In the analysis based on the April CPS, the model in Column (1) implies that recent unemployment rates were 1.6 percentage points higher for people working in jobs that score 1 standard deviation (SD) higher on the Face-to-Face index. The recent unemployment rate in our April sample was 12.6 percent,','48');
insert into items(itemID,sellerID,type,description,stock) values('21','7','Mother and baby products','Working in a job that scores 1 SD higher on Remote Work is associated with a 4.6 percentage point lower risk of recent job loss','38');
insert into items(itemID,sellerID,type,description,stock) values('22','10','Food','which is 44% of the recent unemployment rate in April.','72');
insert into items(itemID,sellerID,type,description,stock) values('23','6','Shoes','The regressions show that recent unemployment rates vary with individual characteristics. Recent unemployment rates are about 3 percentage points higher for women in April and May','17');
insert into items(itemID,sellerID,type,description,stock) values('24','9','Phone','higher for younger workers and decline with age at a decreasing rate. Recent unemployment is lower among college','92');
insert into items(itemID,sellerID,type,description,stock) values('25','1','Bags and suitcases','but on the same level during May. Including occupation and industry fixed effects attenuates the education gradient somewhat','62');
insert into items(itemID,sellerID,type,description,stock) values('26','4','Articles of luxury','Table 2 shows results from models with “employed but absent” as the outcome. Our estimates show that workers jobs relying heavily on face-to-face interactions are more likely to experience absence from work','45');
insert into items(itemID,sellerID,type,description,stock) values('27','8','Packaging','which may indicate that absences precede dismissals. However, classification issues discussed in the data description make this a tentative conclusion.','29');
insert into items(itemID,sellerID,type,description,stock) values('28','8','Toiletries','The education gradient is very similar to the one found for recent unemployment, with education protecting against work absence','17');
insert into items(itemID,sellerID,type,description,stock) values('29','6','Imported goods','n Appendix A.8 we report additional results that explore whether mortality risk from COVID-19 affected labor supply among high-risk groups by estimating regressions that include a measure of COVID-19 mortality risk as a covariate.','33');
insert into items(itemID,sellerID,type,description,stock) values('30','4','Women’s wear','Overall, mortality risk decreases the probability of recent layoff although less so for occupations that can be performed remotely. In April, the coefficient for the index is 1.3 percentage points or 10% of the baseline recent unemployment rate','20');
insert into items(itemID,sellerID,type,description,stock) values('31','9','Men’s wear','In Appendix A.9 (Table A9.1) we report estimates from models where the dependent variable is either recently unemployed or absent from work, combining the two categories examined in the main analysis','68');
insert into items(itemID,sellerID,type,description,stock) values('32','5','Food','In Appendix A.10, we examine the possibility that the relationship between job characteristics and recent unemployment reflects pre-existing patterns of employment instability not related to the epidemic.','24');
insert into items(itemID,sellerID,type,description,stock) values('33','3','Shoes','Appendix A.11 examines the sensitivity of our results to varying the number of weeks used to define recent unemployment. Figures A11.1 and A11.2 show that the the model coefficients are not sensitive to the cutoff used to define “recent” unemployment.','30');
insert into items(itemID,sellerID,type,description,stock) values('34','6','Phone','Recent unemployment rates in April and May varied substantially across sub-populations. As the preceding analysis indicates,','67');
insert into items(itemID,sellerID,type,description,stock) values('35','7','Bags and suitcases','these differences may be explained in large part by the kinds of jobs workers held at the onset of the epidemic.','90');
insert into items(itemID,sellerID,type,description,stock) values('36','7','Sporting goods','In this section, we use a version of the Oaxaca-Blinder decomposition to quantify the role of pre-epidemic sorting more formally','34');
insert into items(itemID,sellerID,type,description,stock) values('37','9','Jewelry','Rather, they reflect differences in the rates at which different groups became unemployed at the start of the pandemic, holding job sorting and other characteristics fixed.','31');
insert into items(itemID,sellerID,type,description,stock) values('38','2','Electric appliance','We examine six aggregate gaps in recent unemployment rates: White vs. Black, High School Graduate vs. High School Drop Out, Female vs. Male, Non-Hispanic vs. Hispanic, College graduate vs. High school graduate','72');
insert into items(itemID,sellerID,type,description,stock) values('39','8','Car accessories','For each gap, we estimate three versions of the pooled decomposition model. Each model includes basic demographic characteristics (','94');
insert into items(itemID,sellerID,type,description,stock) values('40','10','Health care products','Focusing first on Model A for the April data, the explanatory contributions of task-based sorting and essential industry sorting push in different directions across groups.','81');
insert into items(itemID,sellerID,type,description,stock) values('41','6','Medicine','The gender gap displays a different pattern; continuing with the April data, most of the gender gap is unexplained,','65');
insert into items(itemID,sellerID,type,description,stock) values('42','7','Car','However, there remain substantial unexplained differences in employment losses across groups even in these more detailed decompositions','57');
insert into items(itemID,sellerID,type,description,stock) values('43','8','Articles of luxury','The largest gaps we observe are between college graduates and high-school graduates, and between older versus younger workers.','87');
insert into items(itemID,sellerID,type,description,stock) values('44','7','Packaging','All of the patterns we observe are consistent from April to May except one: the gap in recent unemployment between Black and White workers.','91');
insert into items(itemID,sellerID,type,description,stock) values('45','8','Digital appliance','In May, the raw gap is -0.0345 percentage points; double the -0.0171 gap from April.','17');
insert into items(itemID,sellerID,type,description,stock) values('46','5','Home improvement products','Curiously, all of the growth in the gap is from sources that are not explained by the individual or job characteristics included in the model.','27');
insert into items(itemID,sellerID,type,description,stock) values('47','10','Underwear','Consistent with this trend, recent unemployment also fell for White workers. However, recent unemployment rates increased slightly for Black workers. O','92');
insert into items(itemID,sellerID,type,description,stock) values('48','6','Mother and baby products','This finding echoes recent work by Athreya et al. (2020), who find that the service sectors are most vulnerable to social-distancing.','18');
insert into items(itemID,sellerID,type,description,stock) values('49','7','Digital appliance',' Finally, we note that demographic controls do not explain a large part of any of the gaps, suggesting a limited role for labor supply effects in explaining recent job losses.','60');
insert into items(itemID,sellerID,type,description,stock) values('50','1','Jewelry','After only a few months, the COVID-19 job losses are larger than the total multi-year effect of the Great Recession.','14');
insert into orders(orderID,custID,sellerID,time,address,status) values('1','2','1','20140423','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('2','8','2','20140428','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('3','3','1','20120923','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('4','7','1','20150413','325643','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('5','4','6','20170209','103542','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('6','8','2','20210828','385567','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('7','3','6','20191125','102415','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('8','6','10','20171203','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('9','5','10','20190315','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('10','6','4','20160817','345795','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('11','3','7','20201116','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('12','9','9','20151216','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('13','3','5','20140717','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('14','2','8','20181212','102157','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('15','10','4','20160817','235672','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('16','9','8','20161126','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('17','5','6','20120807','235674','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('18','2','4','20130812','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('19','9','6','20211118','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('20','4','4','20120724','103542','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('21','2','4','20150423','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('22','8','7','20161102','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('23','1','6','20141114','102122','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('24','6','7','20141215','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('25','7','6','20200404','325643','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('26','10','4','20130904','235672','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('27','2','4','20140326','102157','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('28','7','5','20160103','325643','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('29','9','6','20190308','243156','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('30','5','6','20160505','235674','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('31','8','8','20141101','385567','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('32','4','6','20141204','103542','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('33','3','10','20180817','102415','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('34','9','7','20170223','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('35','8','5','20170810','385567','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('36','2','9','20161001','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('37','6','10','20100814','345795','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('38','5','4','20150504','235674','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('39','5','9','20180328','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('40','3','2','20100119','102415','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('41','8','1','20100923','385567','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('42','8','4','20130418','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('43','1','4','20160626','102122','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('44','3','6','20150608','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('45','3','6','20130625','102415','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('46','2','5','20140112','102157','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('47','9','9','20160301','243156','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('48','10','8','20100610','235672','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('49','6','10','20100609','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('50','6','8','20131223','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('51','3','8','20120712','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('52','3','5','20130507','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('53','8','2','20210917','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('54','1','5','20110805','102122','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('55','5','1','20110921','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('56','10','4','20110328','235672','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('57','1','3','20110309','102122','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('58','9','1','20100410','243156','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('59','4','6','20120325','103542','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('60','6','10','20181105','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('61','7','2','20170523','325643','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('62','1','8','20110517','102122','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('63','4','7','20200515','103542','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('64','10','2','20161026','235672','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('65','2','10','20140527','102157','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('66','9','3','20120521','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('67','7','8','20121024','325643','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('68','10','9','20160804','235672','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('69','5','3','20161223','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('70','3','2','20100122','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('71','6','4','20170409','345795','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('72','5','4','20140724','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('73','4','6','20210707','103542','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('74','4','7','20100928','103542','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('75','7','1','20191021','325643','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('76','9','2','20120228','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('77','10','10','20210814','235672','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('78','6','9','20200424','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('79','2','10','20140415','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('80','3','1','20120126','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('81','8','3','20111011','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('82','1','9','20140923','102122','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('83','2','9','20210213','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('84','5','5','20160913','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('85','3','4','20200616','102415','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('86','10','1','20140907','235672','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('87','6','6','20140625','345795','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('88','2','1','20140701','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('89','5','9','20210422','235674','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('90','9','6','20120207','243156','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('91','4','3','20170726','103542','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('92','3','10','20171009','102415','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('93','2','5','20150605','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('94','6','6','20121221','345795','0');
insert into orders(orderID,custID,sellerID,time,address,status) values('95','10','8','20110220','235672','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('96','9','4','20150301','243156','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('97','8','4','20180728','385567','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('98','7','2','20160628','325643','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('99','2','6','20140920','102157','1');
insert into orders(orderID,custID,sellerID,time,address,status) values('100','5','8','20200421','235674','0');
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
