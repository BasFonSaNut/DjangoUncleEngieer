BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "myapp_bookproduct" (
	"id"	integer NOT NULL,
	"bookname"	varchar(100) NOT NULL,
	"price"	varchar(100) NOT NULL,
	"author"	varchar(100) NOT NULL,
	"description"	varchar(500),
	"imageurl"	varchar(500),
	"imagefilename"	varchar(500),
	"instock"	bool NOT NULL,
	"unit"	varchar(200) NOT NULL,
	"quantity"	integer NOT NULL,
	"image"	varchar(100),
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "myapp_bookproduct" VALUES (1,'Eakwckmdx','1581','Sjpecd Esjkpw','','myapp/images/book/icon/100.jpg','100.jpg',0,'เล่ม',6,'books/100.jpg');
INSERT INTO "myapp_bookproduct" VALUES (2,'Snwoyxg','2384','Dlywd Ebcva','','myapp/images/book/icon/b10.jpg','b10.jpg',1,'ลัง',10,'books/b10.jpg');
INSERT INTO "myapp_bookproduct" VALUES (3,'Qvjfbqsgtv','1050','Clvn Ztle','','myapp/images/book/icon/b11.jpg','b11.jpg',0,'ลัง',10,'books/b11.jpg');
INSERT INTO "myapp_bookproduct" VALUES (4,'Xdsady','1936','Wofxcl Alvvky','','myapp/images/book/icon/b12.jpg','b12.jpg',1,'เล่ม',3,'books/b12.jpg');
INSERT INTO "myapp_bookproduct" VALUES (5,'Cayutc','2040','Ovckn Uugdv','','myapp/images/book/icon/b13.jpg','b13.jpg',1,'เล่ม',10,'books/b13.jpg');
INSERT INTO "myapp_bookproduct" VALUES (6,'Qyailwno','2197','Lmw Bon','','myapp/images/book/icon/b14.jpg','b14.jpg',1,'ลัง',8,'books/b14.jpg');
INSERT INTO "myapp_bookproduct" VALUES (7,'Lkzxpcg','2973','Iqaic Rzwtp','','myapp/images/book/icon/b15.jpg','b15.jpg',1,'เล่ม',9,'books/b15.jpg');
INSERT INTO "myapp_bookproduct" VALUES (8,'Ijpmfgzstxq','1626','Hgf Nwv','','myapp/images/book/icon/b16.jpg','b16.jpg',1,'ลัง',4,'books/b16.jpg');
INSERT INTO "myapp_bookproduct" VALUES (9,'Tjcretjjrqy','2686','Dbukkp Tpqsnz','','myapp/images/book/icon/b17.jpg','b17.jpg',1,'ลัง',5,'books/b17.jpg');
INSERT INTO "myapp_bookproduct" VALUES (10,'Rjuuvrrcm','2585','Roozw Qtfks','','myapp/images/book/icon/b19.jpg','b19.jpg',0,'ลัง',8,'books/b19.jpg');
INSERT INTO "myapp_bookproduct" VALUES (11,'Wsverimbz','1238','Unqxn Ehkio','','myapp/images/book/icon/b2.jpg','b2.jpg',1,'ลัง',5,'books/b2.jpg');
INSERT INTO "myapp_bookproduct" VALUES (12,'Dfgmxfgjvms','2698','Rnxl Sfnh','','myapp/images/book/icon/b20.jpg','b20.jpg',0,'ลัง',5,'books/b20.jpg');
INSERT INTO "myapp_bookproduct" VALUES (13,'Scaltcqhnv','1780','Louhnw Zktecn','','myapp/images/book/icon/b22.jpg','b22.jpg',0,'เล่ม',9,'books/b22.jpg');
INSERT INTO "myapp_bookproduct" VALUES (14,'Pnuzjhwolu','1478','Bpw Lej','','myapp/images/book/icon/b24.jpg','b24.jpg',0,'เล่ม',3,'books/b24.jpg');
INSERT INTO "myapp_bookproduct" VALUES (15,'Pjevjkisxrb','2281','Swh Cri','','myapp/images/book/icon/b25.jpg','b25.jpg',1,'ลัง',3,'books/b25.jpg');
INSERT INTO "myapp_bookproduct" VALUES (16,'Ebjnpwjiw','2221','Kyrlxz Cchinm','','myapp/images/book/icon/b26.jpg','b26.jpg',0,'ลัง',10,'books/b26.jpg');
INSERT INTO "myapp_bookproduct" VALUES (17,'Xgvvrldjahi','1282','Twwo Wfoz','','myapp/images/book/icon/b27.jpg','b27.jpg',0,'เล่ม',8,'books/b27.jpg');
INSERT INTO "myapp_bookproduct" VALUES (18,'Snqvqokddsr','2431','Pyxv Bpvh','','myapp/images/book/icon/b29.jpg','b29.jpg',1,'เล่ม',10,'books/b29.jpg');
INSERT INTO "myapp_bookproduct" VALUES (19,'Ourlncxj','1711','Iyzdm Qwibw','','myapp/images/book/icon/b3.jpg','b3.jpg',1,'เล่ม',8,'books/b3.jpg');
INSERT INTO "myapp_bookproduct" VALUES (20,'Webqdgl','2210','Ukwqj Qmaaa','','myapp/images/book/icon/b30.jpg','b30.jpg',0,'ลัง',4,'books/b30.jpg');
INSERT INTO "myapp_bookproduct" VALUES (21,'Yussoyebeds','2571','Nkalv Pnioq','','myapp/images/book/icon/b31.jpg','b31.jpg',0,'เล่ม',7,'books/b31.jpg');
INSERT INTO "myapp_bookproduct" VALUES (22,'Rppqnktldxc','2054','Bxboc Dmlec','','myapp/images/book/icon/b32.jpg','b32.jpg',0,'เล่ม',3,'books/b32.jpg');
INSERT INTO "myapp_bookproduct" VALUES (23,'Xayxonfs','2394','Nbyuy Dykpn','','myapp/images/book/icon/b33.jpg','b33.jpg',0,'เล่ม',5,'books/b33.jpg');
INSERT INTO "myapp_bookproduct" VALUES (24,'Ixcrzw','1321','Lfk Xbk','','myapp/images/book/icon/b34.jpg','b34.jpg',0,'เล่ม',7,'books/b34.jpg');
INSERT INTO "myapp_bookproduct" VALUES (25,'Rkkqyxqnudz','1265','Qdn Aex','','myapp/images/book/icon/b35.jpg','b35.jpg',0,'ลัง',7,'books/b35.jpg');
INSERT INTO "myapp_bookproduct" VALUES (26,'Npndfxxu','2153','Zzgok Qeftn','','myapp/images/book/icon/b36.jpg','b36.jpg',0,'ลัง',10,'books/b36.jpg');
INSERT INTO "myapp_bookproduct" VALUES (27,'Ermebpdivr','1600','Zynqi Cutrl','','myapp/images/book/icon/b37.jpg','b37.jpg',1,'เล่ม',9,'books/b37.jpg');
INSERT INTO "myapp_bookproduct" VALUES (28,'Xlpftrrd','1289','Tqd Jlk','','myapp/images/book/icon/b38.jpg','b38.jpg',1,'ลัง',6,'books/b38.jpg');
INSERT INTO "myapp_bookproduct" VALUES (29,'Nayjrlo','1673','Row Vne','','myapp/images/book/icon/b39.jpg','b39.jpg',1,'ลัง',7,'books/b39.jpg');
INSERT INTO "myapp_bookproduct" VALUES (30,'Ngrlgkab','2602','Jirtf Jxtly','','myapp/images/book/icon/b40.jpg','b40.jpg',0,'เล่ม',6,'books/b40.jpg');
INSERT INTO "myapp_bookproduct" VALUES (31,'Lxfrbzb','1341','Xbxig Ekris','','myapp/images/book/icon/b41.jpg','b41.jpg',1,'ลัง',10,'books/b41.jpg');
INSERT INTO "myapp_bookproduct" VALUES (32,'Aatwmzv','1367','Hfpc Bhdt','','myapp/images/book/icon/b42.jpg','b42.jpg',1,'เล่ม',3,'books/b42.jpg');
INSERT INTO "myapp_bookproduct" VALUES (33,'Itqjadqmf','1117','Slerg Fbeep','','myapp/images/book/icon/b43.jpg','b43.jpg',1,'เล่ม',6,'books/b43.jpg');
INSERT INTO "myapp_bookproduct" VALUES (34,'Svagkez','1579','Wkgyom Lwdunf','','myapp/images/book/icon/b44.jpg','b44.jpg',1,'ลัง',3,'books/b44.jpg');
INSERT INTO "myapp_bookproduct" VALUES (35,'Nunyoiafg','1960','Crhzlx Lnyvcj','','myapp/images/book/icon/b45.jpg','b45.jpg',1,'ลัง',7,'books/b45.jpg');
INSERT INTO "myapp_bookproduct" VALUES (36,'Poiyjs','2641','Mnawti Vjjyce','','myapp/images/book/icon/b46.jpg','b46.jpg',0,'ลัง',8,'books/b46.jpg');
INSERT INTO "myapp_bookproduct" VALUES (37,'Cufxodbt','1662','Yjp Ppd','','myapp/images/book/icon/b47.jpg','b47.jpg',1,'เล่ม',10,'books/b47.jpg');
INSERT INTO "myapp_bookproduct" VALUES (38,'Rilxsw','1191','Qivlyj Nwxnww','','myapp/images/book/icon/b48.jpg','b48.jpg',1,'เล่ม',4,'books/b48.jpg');
INSERT INTO "myapp_bookproduct" VALUES (39,'Kadnzh','2500','Iofl Hfyn','','myapp/images/book/icon/b49.jpg','b49.jpg',0,'ลัง',3,'books/b49.jpg');
INSERT INTO "myapp_bookproduct" VALUES (40,'Kokrsofjody','1050','Vlrbg Xfzne','','myapp/images/book/icon/b5.jpg','b5.jpg',1,'เล่ม',3,'books/b5.jpg');
INSERT INTO "myapp_bookproduct" VALUES (41,'Cdallnjqy','2590','Cuh Reu','','myapp/images/book/icon/b50.jpg','b50.jpg',0,'ลัง',4,'books/b50.jpg');
INSERT INTO "myapp_bookproduct" VALUES (42,'Cnetdrcr','1142','Giis Ugqk','','myapp/images/book/icon/b51.jpg','b51.jpg',0,'ลัง',9,'books/b51.jpg');
INSERT INTO "myapp_bookproduct" VALUES (43,'Qqmgvokrn','1966','Ibm Sku','','myapp/images/book/icon/b52.jpg','b52.jpg',0,'เล่ม',5,'books/b52.jpg');
INSERT INTO "myapp_bookproduct" VALUES (44,'Rufobad','1282','Ihapvo Lgrnsu','','myapp/images/book/icon/b53.jpg','b53.jpg',1,'ลัง',6,'books/b53.jpg');
INSERT INTO "myapp_bookproduct" VALUES (45,'Mtyqprwqhwo','1520','Bkcg Usvu','','myapp/images/book/icon/b54.jpg','b54.jpg',1,'เล่ม',8,'books/b54.jpg');
INSERT INTO "myapp_bookproduct" VALUES (46,'Qyqybewd','1755','Dysjqf Thmkbp','','myapp/images/book/icon/b55.jpg','b55.jpg',1,'เล่ม',7,'books/b55.jpg');
INSERT INTO "myapp_bookproduct" VALUES (47,'Ndbhciymekl','1295','Mbws Qese','','myapp/images/book/icon/b56.jpg','b56.jpg',1,'ลัง',6,'books/b56.jpg');
INSERT INTO "myapp_bookproduct" VALUES (48,'Tdtysxtmeer','1221','Xuhk Cwyf','','myapp/images/book/icon/b58.jpg','b58.jpg',1,'ลัง',6,'books/b58.jpg');
INSERT INTO "myapp_bookproduct" VALUES (49,'Sihppamhvmq','2443','Rarag Yoghq','','myapp/images/book/icon/b59.jpg','b59.jpg',1,'ลัง',8,'books/b59.jpg');
INSERT INTO "myapp_bookproduct" VALUES (50,'Tjhilyoivjd','1628','Jzhmiq Wwxvcs','','myapp/images/book/icon/b6.jpg','b6.jpg',0,'ลัง',9,'books/b6.jpg');
INSERT INTO "myapp_bookproduct" VALUES (51,'Ttsadre','2448','Iexf Tgjm','','myapp/images/book/icon/b60.jpg','b60.jpg',0,'เล่ม',3,'books/b60.jpg');
INSERT INTO "myapp_bookproduct" VALUES (52,'Flltuxojec','2450','Wqmwvt Isvnci','','myapp/images/book/icon/b61.jpg','b61.jpg',0,'ลัง',5,'books/b61.jpg');
INSERT INTO "myapp_bookproduct" VALUES (53,'Gnwkdim','2489','Dtc Eki','','myapp/images/book/icon/b62.jpg','b62.jpg',1,'ลัง',3,'books/b62.jpg');
INSERT INTO "myapp_bookproduct" VALUES (54,'Quxtqtluoai','1786','Rkvwu Gbcus','','myapp/images/book/icon/b63.jpg','b63.jpg',1,'ลัง',3,'books/b63.jpg');
INSERT INTO "myapp_bookproduct" VALUES (55,'Bhdgjhfn','1230','Qbc Pwd','','myapp/images/book/icon/b64.jpg','b64.jpg',1,'เล่ม',6,'books/b64.jpg');
INSERT INTO "myapp_bookproduct" VALUES (56,'Ltcxciazxz','1619','Nxid Uemo','','myapp/images/book/icon/b65.jpg','b65.jpg',1,'เล่ม',8,'books/b65.jpg');
INSERT INTO "myapp_bookproduct" VALUES (57,'Tzresaowqmh','1347','Btseyv Xvmdpe','','myapp/images/book/icon/b66.jpg','b66.jpg',0,'ลัง',3,'books/b66.jpg');
INSERT INTO "myapp_bookproduct" VALUES (58,'Ghvydceumb','2176','Nbxfkk Vktsjj','','myapp/images/book/icon/b67.jpg','b67.jpg',1,'ลัง',3,'books/b67.jpg');
INSERT INTO "myapp_bookproduct" VALUES (59,'Qlydshqzak','1368','Xlh Rjh','','myapp/images/book/icon/b68.jpg','b68.jpg',1,'เล่ม',9,'books/b68.jpg');
INSERT INTO "myapp_bookproduct" VALUES (60,'Hsksqan','1911','Blmqr Ujctr','','myapp/images/book/icon/b69.jpg','b69.jpg',0,'ลัง',6,'books/b69.jpg');
INSERT INTO "myapp_bookproduct" VALUES (61,'Xmmmgnbcfai','1509','Cxkwh Dkfuh','','myapp/images/book/icon/b7.jpg','b7.jpg',0,'เล่ม',9,'books/b7.jpg');
INSERT INTO "myapp_bookproduct" VALUES (62,'Inacui','1808','Cjc Cdd','','myapp/images/book/icon/b70.jpg','b70.jpg',0,'ลัง',8,'books/b70.jpg');
INSERT INTO "myapp_bookproduct" VALUES (63,'Pzbjntfa','1132','Bdzp Oglh','','myapp/images/book/icon/b72.jpg','b72.jpg',0,'เล่ม',8,'books/b72.jpg');
INSERT INTO "myapp_bookproduct" VALUES (64,'Gsbmsnsb','1836','Cuwr Ixay','','myapp/images/book/icon/b73.jpg','b73.jpg',1,'ลัง',10,'books/b73.jpg');
INSERT INTO "myapp_bookproduct" VALUES (65,'Ltewmnquum','1379','Syepx Qrtgi','','myapp/images/book/icon/b74.jpg','b74.jpg',1,'เล่ม',9,'books/b74.jpg');
INSERT INTO "myapp_bookproduct" VALUES (66,'Nfourkcx','2206','Zmoguh Aprhaj','','myapp/images/book/icon/b75.jpg','b75.jpg',1,'เล่ม',8,'books/b75.jpg');
INSERT INTO "myapp_bookproduct" VALUES (67,'Irsmpeyyy','2782','Msfs Cycy','','myapp/images/book/icon/b76.jpg','b76.jpg',0,'เล่ม',4,'books/b76.jpg');
INSERT INTO "myapp_bookproduct" VALUES (68,'Vurlbvdpey','1516','Uyibbv Rmksma','','myapp/images/book/icon/b77.jpg','b77.jpg',1,'ลัง',5,'books/b77.jpg');
INSERT INTO "myapp_bookproduct" VALUES (69,'Suksqjid','1228','Svdzcw Equvij','','myapp/images/book/icon/b79.jpg','b79.jpg',1,'เล่ม',7,'books/b79.jpg');
INSERT INTO "myapp_bookproduct" VALUES (70,'Yyjbhyfw','1798','Kqkx Whmh','','myapp/images/book/icon/b8.jpg','b8.jpg',0,'เล่ม',3,'books/b8.jpg');
INSERT INTO "myapp_bookproduct" VALUES (71,'Iqvzytuu','1698','Hoirtf Mkifkv','','myapp/images/book/icon/b81.jpg','b81.jpg',0,'ลัง',9,'books/b81.jpg');
INSERT INTO "myapp_bookproduct" VALUES (72,'Aeuildtvc','2805','Dhvaz Zclhr','','myapp/images/book/icon/b82.jpg','b82.jpg',0,'ลัง',7,'books/b82.jpg');
INSERT INTO "myapp_bookproduct" VALUES (73,'Hyxlwo','2169','Iqa Lky','','myapp/images/book/icon/b84.jpg','b84.jpg',1,'เล่ม',9,'books/b84.jpg');
INSERT INTO "myapp_bookproduct" VALUES (74,'Zmdedxcnj','2158','Iey Tnc','','myapp/images/book/icon/b85.jpg','b85.jpg',0,'เล่ม',5,'books/b85.jpg');
INSERT INTO "myapp_bookproduct" VALUES (75,'Rcsaydvu','1601','Xjvnmc Ijeyrh','','myapp/images/book/icon/b86.jpg','b86.jpg',0,'เล่ม',5,'books/b86.jpg');
INSERT INTO "myapp_bookproduct" VALUES (76,'Ijckikzg','1702','Wrk Tcp','','myapp/images/book/icon/b87.jpg','b87.jpg',1,'เล่ม',5,'books/b87.jpg');
INSERT INTO "myapp_bookproduct" VALUES (77,'Nmbqyjjql','2943','Ugp Fsx','','myapp/images/book/icon/b88.jpg','b88.jpg',1,'เล่ม',9,'books/b88.jpg');
INSERT INTO "myapp_bookproduct" VALUES (78,'Kzidmqqhgbe','2130','Vzlcn Vtprh','','myapp/images/book/icon/b89.jpg','b89.jpg',1,'ลัง',7,'books/b89.jpg');
INSERT INTO "myapp_bookproduct" VALUES (79,'Bawiytciw','1897','Lorl Egza','','myapp/images/book/icon/b9.jpg','b9.jpg',1,'ลัง',7,'books/b9.jpg');
INSERT INTO "myapp_bookproduct" VALUES (80,'Vqpgrnnfkr','2281','Ebowhu Xhdiix','','myapp/images/book/icon/b90.jpg','b90.jpg',0,'ลัง',10,'books/b90.jpg');
INSERT INTO "myapp_bookproduct" VALUES (81,'Nvlfqlw','1030','Bgss Bsns','','myapp/images/book/icon/b91.jpg','b91.jpg',0,'ลัง',5,'books/b91.jpg');
INSERT INTO "myapp_bookproduct" VALUES (82,'Kuzjjrr','2181','Jex Svu','','myapp/images/book/icon/b92.jpg','b92.jpg',1,'เล่ม',7,'books/b92.jpg');
INSERT INTO "myapp_bookproduct" VALUES (83,'Uqerksgdmtt','2110','Ohu Nvo','','myapp/images/book/icon/b93.jpg','b93.jpg',0,'ลัง',5,'books/b93.jpg');
INSERT INTO "myapp_bookproduct" VALUES (84,'Epnvcfzwaw','2507','Ajph Jfkg','','myapp/images/book/icon/b94.jpg','b94.jpg',1,'เล่ม',5,'books/b94.jpg');
INSERT INTO "myapp_bookproduct" VALUES (85,'Xfrzpxm','1122','Sszi Wbto','','myapp/images/book/icon/b96.jpg','b96.jpg',1,'ลัง',7,'books/b96.jpg');
INSERT INTO "myapp_bookproduct" VALUES (86,'Mxsohekd','2043','Kvjyq Nputl','','myapp/images/book/icon/b97.jpg','b97.jpg',1,'เล่ม',10,'books/b97.jpg');
INSERT INTO "myapp_bookproduct" VALUES (87,'Wjnkeruzjmz','1499','Yber Qzbq','','myapp/images/book/icon/b98.jpg','b98.jpg',1,'ลัง',3,'books/b98.jpg');
INSERT INTO "myapp_bookproduct" VALUES (88,'Aeztbdfyhq','2284','Uhxt Timx','','myapp/images/book/icon/b99.jpg','b99.jpg',0,'ลัง',5,'books/b99.jpg');
COMMIT;
