-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: icpep_data
-- ------------------------------------------------------
-- Server version	8.0.35

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
-- Table structure for table `app_aboutpic`
--

DROP TABLE IF EXISTS `app_aboutpic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_aboutpic` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image` varchar(100) NOT NULL,
  `image_title` varchar(50) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_aboutpic`
--

LOCK TABLES `app_aboutpic` WRITE;
/*!40000 ALTER TABLE `app_aboutpic` DISABLE KEYS */;
INSERT INTO `app_aboutpic` VALUES (1,'about-us_kJXdN8E.jpg','Who We Are','The Institute of Computer Engineers of the Philippines BulSU - Meneses Campus shall and developed capable students to become leaders and direct the objectives of the organization and as well uphold the ideals of the Filipino students.\r\n\r\nFormed in 2020, ICpEP.SE BulSU - Meneses Campus shall and has developed capable students to become leaders and direct the objectives of the organization and as well uphold the ideals of the Filipino students in attaining a national, scientific, mass-oriented and global competitive type of education');
/*!40000 ALTER TABLE `app_aboutpic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_banner`
--

DROP TABLE IF EXISTS `app_banner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_banner` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `sub_text` varchar(100) NOT NULL,
  `primary_text` varchar(100) NOT NULL,
  `primary_sub` varchar(100) NOT NULL,
  `description` longtext NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_banner`
--

LOCK TABLES `app_banner` WRITE;
/*!40000 ALTER TABLE `app_banner` DISABLE KEYS */;
INSERT INTO `app_banner` VALUES (1,'Create, Process, Elevate','Computer Engineers','of the Future','\"I can\'t but WE can\"');
/*!40000 ALTER TABLE `app_banner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_highlightsevent`
--

DROP TABLE IF EXISTS `app_highlightsevent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_highlightsevent` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `image` varchar(100) NOT NULL,
  `title` varchar(200) NOT NULL,
  `time` time(6) DEFAULT NULL,
  `date_to` date DEFAULT NULL,
  `date_from` date DEFAULT NULL,
  `location` varchar(255) NOT NULL,
  `desc` longtext,
  `link_desc` varchar(255) NOT NULL,
  `details` varchar(100) NOT NULL,
  `learn_more` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_highlightsevent`
--

LOCK TABLES `app_highlightsevent` WRITE;
/*!40000 ALTER TABLE `app_highlightsevent` DISABLE KEYS */;
INSERT INTO `app_highlightsevent` VALUES (15,'https://forms.gle/mJS5or92gS7H2FbQ6','','Seminar','20:47:00.000000','2024-03-29','2024-03-29','Online via Facebook','','this is link','Documentation team','https://www.facebook.com/photo/?fbid=732267629036871&set=pcb.732267665703534'),(16,'https://forms.gle/mJS5or92gS7H2FbQ6','','BOBONG EVENT','20:57:00.000000','2024-03-29','2024-03-31','Online via Facebook','','this is link','Documentation team','https://www.facebook.com/photo/?fbid=732267629036871&set=pcb.732267665703534'),(17,'https://forms.gle/mJS5or92gS7H2FbQ6','','Sample Event','22:38:00.000000','2024-03-30','2024-03-30','Online via Facebook','HAHAHHAHAHAHAHAHAHAHAHAHHAHHAHHHAHA THIS IS DESCRIPTION','this is link','POGI MARCEL','https://www.facebook.com/photo/?fbid=732267629036871&set=pcb.732267665703534');
/*!40000 ALTER TABLE `app_highlightsevent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_softwaretools`
--

DROP TABLE IF EXISTS `app_softwaretools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_softwaretools` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_softwaretools`
--

LOCK TABLES `app_softwaretools` WRITE;
/*!40000 ALTER TABLE `app_softwaretools` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_softwaretools` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_softwaretoolsresource`
--

DROP TABLE IF EXISTS `app_softwaretoolsresource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_softwaretoolsresource` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `url` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  `desc` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_softwaretoolsresource`
--

LOCK TABLES `app_softwaretoolsresource` WRITE;
/*!40000 ALTER TABLE `app_softwaretoolsresource` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_softwaretoolsresource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user`
--

DROP TABLE IF EXISTS `app_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `username` varchar(100) DEFAULT NULL,
  `email` varchar(254) DEFAULT NULL,
  `orgbox` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `image` varchar(100) DEFAULT NULL,
  `date_joined` datetime(6) NOT NULL,
  `year_section` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user`
--

LOCK TABLES `app_user` WRITE;
/*!40000 ALTER TABLE `app_user` DISABLE KEYS */;
INSERT INTO `app_user` VALUES (1,'pbkdf2_sha256$720000$J99CJey1cxfp7jQdIJaKpq$6w5iVx8XgDHcAqh/5jr6awtL04IP1s3DN7k5Z1DpIwU=','2024-04-11 09:52:24.650401',1,'','','admin','celgamerx123@gmail.com',0,1,1,'','2024-03-29 10:13:56.634379',NULL),(2,'pbkdf2_sha256$720000$yL36riTcoqvI42XJkdQ7ke$d/brcoHkYuoflFvGrtJp0wR+Tv/pTRkk2JK2YBWJX04=','2024-04-11 09:52:08.026618',0,'Aribal','Veniegas','2020400259','marceljames.aribal.v@bulsu.edu.ph',0,1,1,'profile-images/tool-6.png','2024-03-29 10:15:04.408613',NULL),(3,'pbkdf2_sha256$720000$HK7YRsXyr2tXLZ3ThU9HfN$+/IwvYNi295ceN3XkAyiISdwtsEy/C83Ln43SfM/h/Q=',NULL,0,'Evan Justine','Clavecilla','2020400299','evanjustine.clavecilla.g@bulsu.edu.ph',0,0,0,'','2024-03-29 12:57:07.590890',NULL),(4,'pbkdf2_sha256$720000$xJkIeeK2mqHKGZRudx39rW$z2giMVwDL3TgDwdEYqXeadyRGpxiYAfRuPnxFrUAhks=','2024-03-30 14:34:14.454570',0,'','','2020400301','jazzmine.esteve.s@bulsu.edu.ph',0,1,0,'','2024-03-30 14:34:14.445529',NULL),(6,'pbkdf2_sha256$720000$S8jpOS6G1GuYe7unP26qJB$qZg99m3/xLjzeX6JIqBQzNFrGRRchrntFZRTj50513Q=',NULL,0,'Charles ','Espanol','2020400766','charlestrex990@gmail.com',0,0,0,'','2024-03-30 15:02:15.521719',NULL),(7,'pbkdf2_sha256$720000$uHUsAKH8RArCX40WNWLnPe$tbtR3CtExt8ZOFbIcH7y8rqGeu3X1NIQyvdBVo/XNKs=','2024-03-31 10:31:27.553654',0,'','','2021400521','kurtandrei.gutierrez.a@bulsu.edu.ph',1,0,0,'','2024-03-31 10:31:27.541658',NULL);
/*!40000 ALTER TABLE `app_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_groups`
--

DROP TABLE IF EXISTS `app_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_user_groups_user_id_group_id_73b8e940_uniq` (`user_id`,`group_id`),
  KEY `app_user_groups_group_id_e774d92c_fk_auth_group_id` (`group_id`),
  CONSTRAINT `app_user_groups_group_id_e774d92c_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `app_user_groups_user_id_e6f878f6_fk_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_groups`
--

LOCK TABLES `app_user_groups` WRITE;
/*!40000 ALTER TABLE `app_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `app_user_user_permissions`
--

DROP TABLE IF EXISTS `app_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `app_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` bigint NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_user_user_permissions_user_id_permission_id_7c8316ce_uniq` (`user_id`,`permission_id`),
  KEY `app_user_user_permis_permission_id_4ef8e133_fk_auth_perm` (`permission_id`),
  CONSTRAINT `app_user_user_permis_permission_id_4ef8e133_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `app_user_user_permissions_user_id_24780b52_fk_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `app_user_user_permissions`
--

LOCK TABLES `app_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `app_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `app_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add about pic',6,'add_aboutpic'),(22,'Can change about pic',6,'change_aboutpic'),(23,'Can delete about pic',6,'delete_aboutpic'),(24,'Can view about pic',6,'view_aboutpic'),(25,'Can add banner',7,'add_banner'),(26,'Can change banner',7,'change_banner'),(27,'Can delete banner',7,'delete_banner'),(28,'Can view banner',7,'view_banner'),(29,'Can add highlights event',8,'add_highlightsevent'),(30,'Can change highlights event',8,'change_highlightsevent'),(31,'Can delete highlights event',8,'delete_highlightsevent'),(32,'Can view highlights event',8,'view_highlightsevent'),(33,'Can add software tools',9,'add_softwaretools'),(34,'Can change software tools',9,'change_softwaretools'),(35,'Can delete software tools',9,'delete_softwaretools'),(36,'Can view software tools',9,'view_softwaretools'),(37,'Can add software tools resource',10,'add_softwaretoolsresource'),(38,'Can change software tools resource',10,'change_softwaretoolsresource'),(39,'Can delete software tools resource',10,'delete_softwaretoolsresource'),(40,'Can view software tools resource',10,'view_softwaretoolsresource'),(41,'Can add user',11,'add_user'),(42,'Can change user',11,'change_user'),(43,'Can delete user',11,'delete_user'),(44,'Can view user',11,'view_user');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_app_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_app_user_id` FOREIGN KEY (`user_id`) REFERENCES `app_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2024-03-29 13:03:38.384491','1','Who We Are',1,'[{\"added\": {}}]',6,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(6,'app','aboutpic'),(7,'app','banner'),(8,'app','highlightsevent'),(9,'app','softwaretools'),(10,'app','softwaretoolsresource'),(11,'app','user'),(3,'auth','group'),(2,'auth','permission'),(4,'contenttypes','contenttype'),(5,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2024-03-29 10:12:15.510844'),(2,'contenttypes','0002_remove_content_type_name','2024-03-29 10:12:15.590069'),(3,'auth','0001_initial','2024-03-29 10:12:15.900878'),(4,'auth','0002_alter_permission_name_max_length','2024-03-29 10:12:15.971906'),(5,'auth','0003_alter_user_email_max_length','2024-03-29 10:12:15.978902'),(6,'auth','0004_alter_user_username_opts','2024-03-29 10:12:15.985924'),(7,'auth','0005_alter_user_last_login_null','2024-03-29 10:12:15.994919'),(8,'auth','0006_require_contenttypes_0002','2024-03-29 10:12:15.997915'),(9,'auth','0007_alter_validators_add_error_messages','2024-03-29 10:12:16.004513'),(10,'auth','0008_alter_user_username_max_length','2024-03-29 10:12:16.011508'),(11,'auth','0009_alter_user_last_name_max_length','2024-03-29 10:12:16.018504'),(12,'auth','0010_alter_group_name_max_length','2024-03-29 10:12:16.038491'),(13,'auth','0011_update_proxy_permissions','2024-03-29 10:12:16.046486'),(14,'auth','0012_alter_user_first_name_max_length','2024-03-29 10:12:16.053576'),(15,'app','0001_initial','2024-03-29 10:12:16.494911'),(16,'admin','0001_initial','2024-03-29 10:12:16.656883'),(17,'admin','0002_logentry_remove_auto_add','2024-03-29 10:12:16.665877'),(18,'admin','0003_logentry_add_action_flag_choices','2024-03-29 10:12:16.678870'),(19,'sessions','0001_initial','2024-03-29 10:12:16.725841'),(20,'app','0002_user_year_section','2024-03-31 13:50:11.569655');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('8log17szay201idle0ptdbcdd3580uiu','.eJxVjDsOwjAQBe_iGllef3BMSZ8zWOvdNQmgRIqTCnF3iJQC2jcz76UybuuQtyZLHlldFKjT71aQHjLtgO843WZN87QuY9G7og_adD-zPK-H-3cwYBu-dXKx85FtEo8i6C2ShMIExpgOwRG54OgMYhNX8OiKsTVihY4L2BDV-wPshjgW:1rqBfg:K0ZHVCU_QsWUTtDM_h1j_4nQeJinH82KwalSYHi20LA','2024-04-12 12:49:24.493636'),('ao72ynvwe0e6ed777gcv45wadwg6cr6r','.eJxVjDsOwjAQBe_iGllef3BMSZ8zWOvdNQmgRIqTCnF3iJQC2jcz76UybuuQtyZLHlldFKjT71aQHjLtgO843WZN87QuY9G7og_adD-zPK-H-3cwYBu-dXKx85FtEo8i6C2ShMIExpgOwRG54OgMYhNX8OiKsTVihY4L2BDV-wPshjgW:1rqZNG:1410CFc1dRovoV8C8CepGZng4ZksYZWYpZGfWxZeeuU','2024-04-13 14:07:58.776540'),('gbytuf2r31zqygb4wq8gaazuebc5xyx1','.eJxVjDsOwjAQBe_iGllef3BMSZ8zWOvdNQmgRIqTCnF3iJQC2jcz76UybuuQtyZLHlldFKjT71aQHjLtgO843WZN87QuY9G7og_adD-zPK-H-3cwYBu-dXKx85FtEo8i6C2ShMIExpgOwRG54OgMYhNX8OiKsTVihY4L2BDV-wPshjgW:1rur6W:taK_ePBIH09M0EVCdZMTWULHYhtb1kTzxpnSgjrW77w','2024-04-25 09:52:24.654402'),('ppzlzictr3u1j977itwyq7d66h6c5whg','.eJxVjDsOwjAQBe_iGllef3BMSZ8zWOvdNQmgRIqTCnF3iJQC2jcz76UybuuQtyZLHlldFKjT71aQHjLtgO843WZN87QuY9G7og_adD-zPK-H-3cwYBu-dXKx85FtEo8i6C2ShMIExpgOwRG54OgMYhNX8OiKsTVihY4L2BDV-wPshjgW:1rqw1Y:jtSF0Xbzscdn4itZHDuD9ZrcoDo7_-liQfk5GWgn4Q4','2024-04-14 14:19:04.895257');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-04-18 16:05:10
