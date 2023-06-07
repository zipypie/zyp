CREATE DATABASE  IF NOT EXISTS `mobile_purchases_db` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;
USE `mobile_purchases_db`;
-- MariaDB dump 10.19  Distrib 10.4.28-MariaDB, for Win64 (AMD64)
--
-- Host: localhost    Database: mobile_purchases_db
-- ------------------------------------------------------
-- Server version	10.4.28-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `atm`
--

DROP TABLE IF EXISTS `atm`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `atm` (
  `atm_id` int(11) NOT NULL AUTO_INCREMENT,
  `atm_number` varchar(45) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`atm_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10032 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `atm`
--

LOCK TABLES `atm` WRITE;
/*!40000 ALTER TABLE `atm` DISABLE KEYS */;
INSERT INTO `atm` VALUES (10001,'1000111121',1),(10002,'1000111122',2),(10003,'1000111123',3),(10004,'1000111124',4),(10005,'1000111125',5),(10006,'1000111121',6),(10007,'1000111125',7),(10008,'1000111126',8),(10009,'1000111149',9),(10010,'1000111142',10),(10011,'1000111129',11),(10012,'1000111166',12),(10013,'1000111128',13),(10014,'1000111127',14),(10015,'1000111128',15),(10016,'1000111134',16),(10017,'1000111137',17),(10018,'1000111134',18),(10019,'1000111131',19),(10020,'1000111128',20),(10021,'1000111123',21),(10022,'1000111126',22),(10023,'1000111128',23),(10024,'1000111131',24),(10025,'1000111135',25),(10026,'1000111142',26),(10027,'1000111132',27),(10028,'1000111121',28);
/*!40000 ALTER TABLE `atm` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `customer_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `customer_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES (1,'Juan ','Dela Cruz','123 Main Street, Quezon City, Metro Manila'),(2,'Maria ','Santos','456 Elm Street, Makati City, Metro Manila'),(3,'Pedro ','Gonzales','789 Oak Street, Cebu City, Cebu'),(4,'Luisa ','Reyes','321 Pine Street, Davao City, Davao del Sur'),(5,'Ramon ','Torres','654 Maple Street, Iloilo City, Iloilo'),(6,'Carmen ','Garcia','987 Birch Street, Baguio City, Benguet'),(7,'Antonio ','Santos','246 Cedar Street, Pasig City, Metro Manila'),(8,'Sofia ','Hernandez','135 Walnut Street, Parañaque City, Metro Manila'),(9,'Emilio ','Ramirez','864 Cherry Street, Mandaluyong City, Metro Manila'),(10,'Andres',' Gonzales','753 Oak Street, Bacoor City, Cavite'),(11,'Cristina',' Reyes','982 Pine Street, Santa Rosa City, Laguna'),(12,'Manuel',' Torres','321 Elm Street, Cagayan de Oro City, Misamis Oriental'),(13,'Elena',' Garcia','654 Maple Street, San Fernando City, La Union'),(14,'Jose ','Santos','987 Birch Street, Legazpi City, Albay'),(15,'Ana ','Hernandez','246 Cedar Street, Tacloban City, Leyte'),(16,'Carlos ','Ramirez','135 Walnut Street, Naga City, Camarines Sur'),(17,'Mariano ','Gonzales','864 Cherry Street, Lipa City, Batangas'),(18,'Rosario ','Reyes','753 Oak Street, Butuan City, Agusan del Norte'),(19,'Fernando ','Torres','982 Pine Street, Ozamiz City, Misamis Occidental'),(20,'Angelita ','Garcia','321 Elm Street, Laoag City, Ilocos Norte'),(21,'Roberto ','Santos','654 Maple Street, General Santos City, South Cotabato'),(22,'Aurora ','Hernandez','987 Birch Street, Pagadian City, Zamboanga del Sur'),(23,'Felipe ','Ramirez','246 Cedar Street, Lucena City, Quezon'),(24,'Carmela ','Gonzales','135 Walnut Street, Angeles City, Pampanga'),(25,'Feliciano ','Reyes','864 Cherry Street, Zamboanga City, Zamboanga del Sur'),(26,'Gloria ','Torres','753 Oak Street, Bacolod City, Negros Occidental'),(27,'Rogelio ','Garcia','982 Pine Street, Tarlac City, Tarlac'),(28,'Alicia ','Santos','321 Elm Street, Puerto Princesa City, Palawan');
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `payment`
--

DROP TABLE IF EXISTS `payment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `phone_id` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  `product_price_id` int(11) DEFAULT NULL,
  `atm_id` int(11) DEFAULT NULL,
  `payment_method` varchar(15) DEFAULT NULL,
  `date_of_payment` date DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `FK_Phone_TO_Payments` (`phone_id`),
  KEY `FK_Products_TO_Payments` (`product_id`),
  KEY `FK_Product_price_TO_Payments` (`product_price_id`),
  KEY `FK_Atm_TO_Payments` (`atm_id`),
  CONSTRAINT `FK_Atm_TO_Payments` FOREIGN KEY (`atm_id`) REFERENCES `atm` (`atm_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Phone_TO_Payments` FOREIGN KEY (`phone_id`) REFERENCES `phone` (`phone_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Product_price_TO_Payments` FOREIGN KEY (`product_price_id`) REFERENCES `product_price` (`product_price_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `FK_Products_TO_Payments` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=50031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `payment`
--

LOCK TABLES `payment` WRITE;
/*!40000 ALTER TABLE `payment` DISABLE KEYS */;
INSERT INTO `payment` VALUES (50001,1014,20016,15012,10014,'Credit Card','2023-05-01',14),(50003,1004,20015,15011,10004,'Credit Card','2023-05-03',4),(50004,1001,20009,15005,10001,'Credit Card','2023-05-04',1),(50005,1004,20029,15025,10004,'Debit Card','2023-05-05',4),(50006,1003,20007,15003,10003,'Cash','2023-05-06',3),(50007,1010,20014,15010,10010,'Cash','2023-05-07',10),(50008,1026,20029,15025,10026,'Cash','2023-05-08',26),(50009,1003,20014,15010,10003,'Credit Card','2023-05-09',3),(50010,1007,20023,15019,10007,'Debit Card','2023-05-10',7),(50011,1004,20006,15002,10004,'Debit Card','2023-05-11',4),(50013,1011,20006,15002,10011,'Cash','2023-05-13',11),(50014,1017,20007,15003,10017,'Credit Card','2023-05-14',17),(50015,1014,20025,15021,10014,'Debit Card','2023-05-15',14),(50016,1005,20009,15005,10005,'Credit Card','2023-05-16',5),(50018,1014,20016,15012,10014,'Debit Card','2023-05-18',14),(50019,1022,20010,15006,10022,'Debit Card','2023-05-19',22),(50020,1014,20014,15010,10014,'Cash','2023-05-20',14),(50023,1012,20028,15024,10012,'Cash','2023-05-23',12),(50024,1025,20006,15002,10025,'Cash','2023-05-24',25),(50025,1023,20027,15025,10023,'Cash','2023-05-25',23),(50026,1019,20026,15022,10017,'Cash','2023-05-26',17),(50027,1005,20027,15023,10005,'Credit Card','2023-05-27',5),(50028,1016,20029,15025,10016,'Cash','2023-05-28',16),(50029,1024,20012,15008,10024,'Credit Card','2023-05-29',24),(50030,1025,20013,15009,10025,'Debit Card','2023-05-30',25);
/*!40000 ALTER TABLE `payment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone`
--

DROP TABLE IF EXISTS `phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phone` (
  `phone_id` int(11) NOT NULL AUTO_INCREMENT,
  `customer_id` int(11) DEFAULT NULL,
  `phone_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`phone_id`),
  KEY `FK_Customer_TO_Phone` (`customer_id`),
  CONSTRAINT `FK_Customer_TO_Phone` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`customer_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=1031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone`
--

LOCK TABLES `phone` WRITE;
/*!40000 ALTER TABLE `phone` DISABLE KEYS */;
INSERT INTO `phone` VALUES (1001,1,'+639329012345'),(1002,2,'+639274567890'),(1003,3,'+639359876543'),(1004,4,'+639361234567'),(1005,5,'+639478901234'),(1006,6,'+639156789012'),(1007,7,'+639323456789'),(1008,8,'+639356789012'),(1009,9,'+639174567890'),(1010,10,'+639277890123'),(1011,11,'+639328901234'),(1012,12,'+639369012345'),(1013,13,'+639472345678'),(1014,14,'+639355678901'),(1015,15,'+639176789012'),(1016,16,'+639279012345'),(1017,17,'+639321234567'),(1018,18,'+639364567890'),(1019,19,'+639477890123'),(1020,20,'+639158901234'),(1021,21,'+639359012345'),(1022,22,'+639172345678'),(1023,23,'+639275678901'),(1024,24,'+639326789012'),(1025,25,'+639369012345'),(1026,26,'+639471234567'),(1027,27,'+639354567890'),(1028,28,'+639177890123');
/*!40000 ALTER TABLE `phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product` (
  `product_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_name` varchar(65) DEFAULT NULL,
  `quantity` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=20031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (20001,'Bananas',50),(20002,'Apples',30),(20003,'Milk',20),(20004,'Bread',40),(20005,'Eggs',60),(20006,'Chicken',25),(20007,'Rice',100),(20008,'Pasta',35),(20009,'Tomatoes',45),(20010,'Potatoes',55),(20011,'Onions',40),(20012,'Carrots',30),(20013,'Spinach',20),(20014,'Oranges',60),(20015,'Lettuce',35),(20016,'Cucumbers',45),(20017,'Cheese',50),(20018,'Yogurt',40),(20019,'Salmon',30),(20020,'Beef',20),(20021,'Pork',35),(20022,'Shrimp',25),(20023,'Coffee',50),(20024,'Tea',60),(20025,'Sugar',45),(20026,'Salt',55),(20027,'Olive Oil',40),(20028,'Vinegar',30),(20029,'Cereal',20);
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_price`
--

DROP TABLE IF EXISTS `product_price`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `product_price` (
  `product_price_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_price` int(11) DEFAULT NULL,
  `product_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_price_id`),
  KEY `FK_Products_TO_Product_price` (`product_id`),
  CONSTRAINT `FK_Products_TO_Product_price` FOREIGN KEY (`product_id`) REFERENCES `product` (`product_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=15035 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_price`
--

LOCK TABLES `product_price` WRITE;
/*!40000 ALTER TABLE `product_price` DISABLE KEYS */;
INSERT INTO `product_price` VALUES (15001,100,20001),(15002,200,20002),(15003,150,20003),(15004,120,20004),(15005,80,20005),(15006,250,20006),(15007,180,20007),(15008,300,20008),(15009,130,20009),(15010,90,20010),(15011,170,20011),(15012,220,20012),(15013,140,20013),(15014,190,20014),(15015,110,20015),(15016,160,20016),(15017,270,20017),(15018,230,20018),(15019,260,20019),(15020,210,20020),(15021,240,20021),(15022,175,20022),(15023,120,20023),(15024,200,20024),(15025,150,20025),(15026,130,20026),(15027,100,20027),(15028,180,20028),(15029,160,20029);
/*!40000 ALTER TABLE `product_price` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-07 13:41:39
