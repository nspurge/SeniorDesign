-- MySQL dump 10.13  Distrib 5.7.21, for Linux (x86_64)
--
-- Host: localhost    Database: seniordesign
-- ------------------------------------------------------
-- Server version	5.7.21-0ubuntu0.16.04.1

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
-- Table structure for table `Assets`
--

DROP TABLE IF EXISTS `Assets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Assets` (
  `AssetIdKey` int(11) NOT NULL AUTO_INCREMENT,
  `Description` varchar(45) DEFAULT NULL,
  `SerialNumber` varchar(45) DEFAULT NULL,
  `StorageLocation` varchar(45) DEFAULT NULL,
  `Model` varchar(45) DEFAULT NULL,
  `Manufacturer` varchar(45) DEFAULT NULL,
  `WarrantyNumber` int(11) DEFAULT NULL,
  `WarrantyExpiration` date DEFAULT NULL,
  `Lost` tinyint(1) DEFAULT NULL,
  `Stolen` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`AssetIdKey`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `IssuedAssets`
--

DROP TABLE IF EXISTS `IssuedAssets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `IssuedAssets` (
  `Users_UserIdKey` int(11) NOT NULL,
  `Assets_AssetIdKey` int(11) NOT NULL,
  `IAKey` varchar(45) DEFAULT NULL,
  `TimeIssued` datetime DEFAULT NULL,
  PRIMARY KEY (`Users_UserIdKey`,`Assets_AssetIdKey`),
  KEY `fk_Users_has_Assets_Assets1_idx` (`Assets_AssetIdKey`),
  KEY `fk_Users_has_Assets_Users_idx` (`Users_UserIdKey`),
  CONSTRAINT `fk_Users_has_Assets_Assets1` FOREIGN KEY (`Assets_AssetIdKey`) REFERENCES `Assets` (`AssetIdKey`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Assets_Users` FOREIGN KEY (`Users_UserIdKey`) REFERENCES `Users` (`UserIdKey`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Log`
--

DROP TABLE IF EXISTS `Log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Log` (
  `LogKey` int(11) NOT NULL AUTO_INCREMENT,
  `Users_UserIdKey` int(11) DEFAULT NULL,
  `Assets_AssetIdKey` int(11) DEFAULT NULL,
  `TimeStamp` varchar(45) DEFAULT NULL,
  `EventDescription` varchar(200) DEFAULT NULL,
  `EventImage` mediumblob,
  PRIMARY KEY (`LogKey`),
  KEY `fk_Users_has_Assets_Assets2_idx` (`Assets_AssetIdKey`),
  KEY `fk_Users_has_Assets_Users1_idx` (`Users_UserIdKey`),
  CONSTRAINT `fk_Users_has_Assets_Assets2` FOREIGN KEY (`Assets_AssetIdKey`) REFERENCES `Assets` (`AssetIdKey`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Users_has_Assets_Users1` FOREIGN KEY (`Users_UserIdKey`) REFERENCES `Users` (`UserIdKey`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `UserIdKey` int(11) NOT NULL AUTO_INCREMENT,
  `Rfid_Id` bigint(20) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Deactivate` tinyint(1) DEFAULT NULL,
  `Admin` tinyint(1) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `PhoneNumber` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`UserIdKey`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-11 17:43:27
