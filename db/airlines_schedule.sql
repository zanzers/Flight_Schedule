-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: airlines_schedule
-- ------------------------------------------------------
-- Server version	8.0.40

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `airports`
--

DROP TABLE IF EXISTS `airports`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airports` (
  `airports_ID` int NOT NULL AUTO_INCREMENT,
  `airport_name` varchar(250) NOT NULL,
  `airport_location` varchar(250) NOT NULL,
  `airport_latitude` decimal(5,0) NOT NULL,
  `airport_longtitude` decimal(5,0) NOT NULL,
  `airport_elevation` decimal(5,0) NOT NULL,
  PRIMARY KEY (`airports_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airports`
--

LOCK TABLES `airports` WRITE;
/*!40000 ALTER TABLE `airports` DISABLE KEYS */;
INSERT INTO `airports` VALUES (1,'Thompson-Serrano','West Heather',0,-55,2799),(2,'Frazier Inc','Tonyport',26,-59,4583),(3,'Patterson and Sons','West Danielborough',-59,110,3162),(4,'Watson, Walker and Johnson','Vickimouth',41,8,1731),(5,'Johnson-Fletcher','Port Nicholas',-24,-108,3492),(6,'Williams and Sons','Lake Jocelyn',45,79,2024),(7,'Robbins-Hill','Petersonmouth',41,53,769),(8,'Oliver Inc','Kimhaven',-32,80,564),(9,'Hurley, Parks and Kim','Ericmouth',-8,-67,3278),(10,'Smith, Jones and Gill','Robertland',-10,124,1073),(11,'Rivera PLC','Johnsonshire',-61,68,3006),(12,'Lopez-Jones','East Kellymouth',-81,92,4082),(13,'Acevedo-Smith','Toddfort',-72,-137,1898),(14,'Alvarez Ltd','Christinamouth',74,147,3589),(15,'Schmidt-Kirby','Mitchellfort',-43,148,1925),(16,'Freeman-Delgado','Port Joshua',-84,162,579),(17,'James-Mendez','Perryfort',-40,102,3080),(18,'Wells, Joseph and Yang','Kristinberg',6,-67,4175),(19,'Rodriguez, Rogers and Harris','New Christopherborough',-40,137,3932),(20,'Orozco Ltd','Jamesmouth',1,-77,3660),(21,'Cruz-Ray','Jackberg',-9,69,4168),(22,'Hill LLC','West Tammychester',-32,141,1335),(23,'Richardson Group','Mitchellbury',26,100,2530),(24,'Cohen-Mullins','Roberttown',-65,-34,3090),(25,'Horn, Garcia and Moore','Peterfurt',-6,103,2803);
/*!40000 ALTER TABLE `airports` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight_schedule`
--

DROP TABLE IF EXISTS `flight_schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight_schedule` (
  `flight_schedule_ID` int NOT NULL AUTO_INCREMENT,
  `ref_aircraft_Types_ID` int NOT NULL,
  `ref_airlines_ID` int NOT NULL,
  `airline_code` varchar(50) NOT NULL,
  `first_airport_code` varchar(10) NOT NULL,
  `final_airport_code` varchar(10) NOT NULL,
  `departure_date_time` datetime NOT NULL,
  `arraval_date_time` datetime NOT NULL,
  PRIMARY KEY (`flight_schedule_ID`),
  KEY `fk_Flight_Schedule_Ref_Aircraft_Types1_idx` (`ref_aircraft_Types_ID`),
  KEY `fk_Flight_Schedule_Ref_Airlines1_idx` (`ref_airlines_ID`),
  CONSTRAINT `fk_Flight_Schedule_Ref_Aircraft_Types1` FOREIGN KEY (`ref_aircraft_Types_ID`) REFERENCES `ref_aircraft_types` (`ref_aircraft_Types_ID`),
  CONSTRAINT `fk_Flight_Schedule_Ref_Airlines1` FOREIGN KEY (`ref_airlines_ID`) REFERENCES `ref_airlines` (`ref_airlines_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight_schedule`
--

LOCK TABLES `flight_schedule` WRITE;
/*!40000 ALTER TABLE `flight_schedule` DISABLE KEYS */;
INSERT INTO `flight_schedule` VALUES (1,23,2,'VFW','VSR','KCV','2024-03-21 03:20:09','2024-03-21 05:20:09'),(2,5,9,'MLB','PXA','LKM','2024-04-08 18:21:04','2024-04-08 21:21:04'),(3,22,19,'NUR','HAH','NQJ','2024-01-02 07:01:36','2024-01-02 09:01:36'),(4,24,22,'KAX','SKK','WYU','2024-01-01 11:02:01','2024-01-01 15:02:01'),(5,23,6,'ADP','KQW','ZRN','2024-09-17 23:56:56','2024-09-18 03:56:56'),(6,11,15,'XGN','SJI','LGB','2024-03-03 17:14:12','2024-03-03 22:14:12'),(7,5,18,'MCU','MQV','TCU','2024-06-21 20:46:33','2024-06-22 01:46:33'),(8,17,17,'NZJ','IBZ','IWO','2024-06-25 15:18:13','2024-06-25 21:18:13'),(9,11,6,'LBL','HJT','XXJ','2024-04-04 20:26:25','2024-04-05 00:26:25'),(10,5,24,'IVN','YIV','URS','2024-04-14 05:59:56','2024-04-14 08:59:56'),(11,4,6,'SVW','XRR','HEV','2024-05-10 13:13:28','2024-05-10 17:13:28'),(12,14,14,'YQD','UOU','EGD','2024-06-27 00:38:11','2024-06-27 04:38:11'),(13,7,13,'WKV','XUJ','QIQ','2024-11-12 14:08:58','2024-11-12 17:08:58'),(14,13,6,'NBZ','UMN','YCB','2024-02-09 22:04:58','2024-02-10 02:04:58'),(15,13,12,'DAT','XNC','FWD','2024-12-04 23:47:49','2024-12-05 04:47:49'),(16,21,21,'OJA','XCT','EFQ','2024-09-27 22:06:42','2024-09-28 01:06:42'),(17,10,13,'XLE','SDH','ZKN','2024-11-05 15:08:15','2024-11-05 21:08:15'),(18,22,17,'WRX','LAE','CRM','2024-02-21 18:07:53','2024-02-21 23:07:53'),(19,23,14,'FTC','ZDE','DAW','2024-04-10 19:01:00','2024-04-10 22:01:00'),(20,24,22,'DEJ','ZQA','QIB','2024-07-11 20:57:57','2024-07-11 22:57:57'),(21,3,9,'XJQ','KWM','DAS','2024-08-27 02:07:04','2024-08-27 08:07:04'),(22,22,3,'GUR','LDO','ZJH','2024-10-11 08:55:15','2024-10-11 14:55:15'),(23,12,16,'DRU','BSB','IPR','2024-04-01 06:33:31','2024-04-01 08:33:31'),(24,22,17,'MLQ','HIX','ZRU','2024-03-19 15:48:52','2024-03-19 19:48:52'),(25,3,18,'DBY','MTQ','NEU','2024-03-06 04:29:45','2024-03-06 08:29:45');
/*!40000 ALTER TABLE `flight_schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `legs`
--

DROP TABLE IF EXISTS `legs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `legs` (
  `legs_ID` int NOT NULL AUTO_INCREMENT,
  `flight_schedule_ID` int NOT NULL,
  `Airports_airports_ID` int NOT NULL,
  `departure_time` datetime NOT NULL,
  `arrival_time` datetime NOT NULL,
  PRIMARY KEY (`legs_ID`),
  KEY `fk_Legs_Flight_Schedule_idx` (`flight_schedule_ID`),
  KEY `fk_Legs_Airports1_idx` (`Airports_airports_ID`),
  CONSTRAINT `fk_Legs_Airports1` FOREIGN KEY (`Airports_airports_ID`) REFERENCES `airports` (`airports_ID`),
  CONSTRAINT `fk_Legs_Flight_Schedule` FOREIGN KEY (`flight_schedule_ID`) REFERENCES `flight_schedule` (`flight_schedule_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `legs`
--

LOCK TABLES `legs` WRITE;
/*!40000 ALTER TABLE `legs` DISABLE KEYS */;
INSERT INTO `legs` VALUES (1,3,19,'2024-12-07 22:35:25','2024-12-08 04:35:25'),(2,9,2,'2024-03-28 09:40:50','2024-03-28 15:40:50'),(3,20,4,'2024-09-18 07:14:18','2024-09-18 13:14:18'),(4,10,23,'2024-03-22 13:54:29','2024-03-22 18:54:29'),(5,14,22,'2024-07-04 06:21:50','2024-07-04 08:21:50'),(6,2,11,'2024-03-24 07:56:03','2024-03-24 12:56:03'),(7,21,21,'2024-03-22 13:34:23','2024-03-22 16:34:23'),(8,8,25,'2024-11-10 10:25:06','2024-11-10 14:25:06'),(9,9,10,'2024-01-03 21:45:37','2024-01-03 23:45:37'),(10,20,18,'2024-01-20 13:17:48','2024-01-20 19:17:48');
/*!40000 ALTER TABLE `legs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref_aircraft_types`
--

DROP TABLE IF EXISTS `ref_aircraft_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ref_aircraft_types` (
  `ref_aircraft_Types_ID` int NOT NULL AUTO_INCREMENT,
  `aircraft_type_name` varchar(100) NOT NULL,
  `aircraft_type_capacity` varchar(100) NOT NULL,
  PRIMARY KEY (`ref_aircraft_Types_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref_aircraft_types`
--

LOCK TABLES `ref_aircraft_types` WRITE;
/*!40000 ALTER TABLE `ref_aircraft_types` DISABLE KEYS */;
INSERT INTO `ref_aircraft_types` VALUES (1,'Boeing 787','500'),(2,'Bombardier Q400','500'),(3,'Airbus A380','350'),(4,'Pilatus PC-12','180'),(5,'Boeing 787','350'),(6,'Boeing 787','180'),(7,'Boeing 737','400'),(8,'Boeing 777','500'),(9,'Airbus A380','200'),(10,'Embraer E175','200'),(11,'Boeing 787','220'),(12,'Boeing 787','180'),(13,'Boeing 787','180'),(14,'Airbus A320','220'),(15,'Boeing 787','400'),(16,'Airbus A350','400'),(17,'Cessna 172','220'),(18,'Pilatus PC-12','250'),(19,'Cessna 172','200'),(20,'Boeing 737','400'),(21,'Airbus A320','500'),(22,'Bombardier Q400','400'),(23,'Boeing 737','400'),(24,'Airbus A320','180'),(25,'Pilatus PC-12','220');
/*!40000 ALTER TABLE `ref_aircraft_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ref_airlines`
--

DROP TABLE IF EXISTS `ref_airlines`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ref_airlines` (
  `ref_airlines_ID` int NOT NULL AUTO_INCREMENT,
  `airlines_name` varchar(150) NOT NULL,
  `airlines_country` varchar(150) NOT NULL,
  PRIMARY KEY (`ref_airlines_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ref_airlines`
--

LOCK TABLES `ref_airlines` WRITE;
/*!40000 ALTER TABLE `ref_airlines` DISABLE KEYS */;
INSERT INTO `ref_airlines` VALUES (1,'Baker Inc','Egypt'),(2,'Roberts, Bell and Owens','Germany'),(3,'King, Brown and Humphrey','France'),(4,'Davis-Williams','Italy'),(5,'Preston Inc','South Africa'),(6,'Jones Ltd','Egypt'),(7,'Sharp-Miller','India'),(8,'Wagner Group','Australia'),(9,'Flores, Heath and Riley','Brazil'),(10,'Sanchez, Patel and Stewart','China'),(11,'Smith, Carpenter and Wright','USA'),(12,'Williams, Walker and Short','Italy'),(13,'Howard-Watkins','Canada'),(14,'Peterson, Doyle and Ortiz','Japan'),(15,'Dyer Ltd','Mexico'),(16,'Glass-Jones','Germany'),(17,'Brown-Villarreal','Australia'),(18,'Rose PLC','Mexico'),(19,'Miller PLC','France'),(20,'Warner and Sons','Australia'),(21,'Cobb, Deleon and George','Egypt'),(22,'Jordan and Sons','France'),(23,'Sullivan, Smith and Reyes','Egypt'),(24,'West-Richmond','Brazil'),(25,'Long LLC','Egypt');
/*!40000 ALTER TABLE `ref_airlines` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-14  0:21:20
