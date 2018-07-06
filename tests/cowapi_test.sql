-- MySQL dump 10.13  Distrib 8.0.11, for Linux (x86_64)
--
-- Host: localhost    Database: cowapi
-- ------------------------------------------------------
-- Server version	8.0.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `state_codes`
--

DROP TABLE IF EXISTS `state_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `state_codes` (
  `state_abbr` char(10) DEFAULT NULL,
  `state_id` int(11) DEFAULT NULL,
  `state_name` char(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `state_codes`
--

LOCK TABLES `state_codes` WRITE;
/*!40000 ALTER TABLE `state_codes` DISABLE KEYS */;
INSERT INTO `state_codes` VALUES ('USA',2,'United States of America'),('CAN',20,'Canada'),('BHM',31,'Bahamas'),('CUB',40,'Cuba'),('CUB',40,'Cuba'),('HAI',41,'Haiti'),('HAI',41,'Haiti'),('DOM',42,'Dominican Republic'),('DOM',42,'Dominican Republic'),('JAM',51,'Jamaica'),('TRI',52,'Trinidad and Tobago'),('BAR',53,'Barbados'),('DMA',54,'Dominica'),('GRN',55,'Grenada'),('SLU',56,'St. Lucia'),('SVG',57,'St. Vincent and the Grenadines'),('AAB',58,'Antigua & Barbuda'),('SKN',60,'St. Kitts and Nevis'),('MEX',70,'Mexico'),('BLZ',80,'Belize'),('GUA',90,'Guatemala'),('HON',91,'Honduras'),('SAL',92,'El Salvador'),('NIC',93,'Nicaragua'),('COS',94,'Costa Rica'),('PAN',95,'Panama'),('COL',100,'Colombia'),('VEN',101,'Venezuela'),('GUY',110,'Guyana'),('SUR',115,'Suriname'),('ECU',130,'Ecuador'),('PER',135,'Peru'),('BRA',140,'Brazil'),('BOL',145,'Bolivia'),('PAR',150,'Paraguay'),('PAR',150,'Paraguay'),('CHL',155,'Chile'),('ARG',160,'Argentina'),('URU',165,'Uruguay'),('UKG',200,'United Kingdom'),('IRE',205,'Ireland'),('NTH',210,'Netherlands'),('NTH',210,'Netherlands'),('BEL',211,'Belgium'),('BEL',211,'Belgium'),('LUX',212,'Luxembourg'),('LUX',212,'Luxembourg'),('FRN',220,'France'),('FRN',220,'France'),('MNC',221,'Monaco'),('LIE',223,'Liechtenstein'),('SWZ',225,'Switzerland'),('SPN',230,'Spain'),('AND',232,'Andorra'),('POR',235,'Portugal'),('HAN',240,'Hanover'),('BAV',245,'Bavaria'),('GMY',255,'Germany'),('GMY',255,'Germany'),('GFR',260,'German Federal Republic'),('GDR',265,'German Democratic Republic'),('BAD',267,'Baden'),('SAX',269,'Saxony'),('WRT',271,'Wuerttemburg'),('HSE',273,'Hesse Electoral'),('HSG',275,'Hesse Grand Ducal'),('MEC',280,'Mecklenburg Schwerin'),('POL',290,'Poland'),('POL',290,'Poland'),('AUH',300,'Austria-Hungary'),('AUS',305,'Austria'),('AUS',305,'Austria'),('HUN',310,'Hungary'),('CZE',315,'Czechoslovakia'),('CZE',315,'Czechoslovakia'),('CZR',316,'Czech Republic'),('SLO',317,'Slovakia'),('ITA',325,'Italy'),('PAP',327,'Papal States'),('SIC',329,'Two Sicilies'),('SNM',331,'San Marino'),('MOD',332,'Modena'),('PMA',335,'Parma'),('TUS',337,'Tuscany'),('MLT',338,'Malta'),('ALB',339,'Albania'),('ALB',339,'Albania'),('MNG',341,'Montenegro'),('MAC',343,'Macedonia'),('CRO',344,'Croatia'),('YUG',345,'Yugoslavia'),('YUG',345,'Yugoslavia'),('BOS',346,'Bosnia and Herzegovina'),('KOS',347,'Kosovo'),('SLV',349,'Slovenia'),('GRC',350,'Greece'),('GRC',350,'Greece'),('CYP',352,'Cyprus'),('BUL',355,'Bulgaria'),('MLD',359,'Moldova'),('ROM',360,'Romania'),('RUS',365,'Russia'),('EST',366,'Estonia'),('EST',366,'Estonia'),('LAT',367,'Latvia'),('LAT',367,'Latvia'),('LIT',368,'Lithuania'),('LIT',368,'Lithuania'),('UKR',369,'Ukraine'),('BLR',370,'Belarus'),('ARM',371,'Armenia'),('GRG',372,'Georgia'),('AZE',373,'Azerbaijan'),('FIN',375,'Finland'),('SWD',380,'Sweden'),('NOR',385,'Norway'),('NOR',385,'Norway'),('DEN',390,'Denmark'),('DEN',390,'Denmark'),('ICE',395,'Iceland'),('CAP',402,'Cape Verde'),('STP',403,'Sao Tome and Principe'),('GNB',404,'Guinea-Bissau'),('EQG',411,'Equatorial Guinea'),('GAM',420,'Gambia'),('MLI',432,'Mali'),('SEN',433,'Senegal'),('BEN',434,'Benin'),('MAA',435,'Mauritania'),('NIR',436,'Niger'),('CDI',437,'Ivory Coast'),('GUI',438,'Guinea'),('BFO',439,'Burkina Faso'),('LBR',450,'Liberia'),('SIE',451,'Sierra Leone'),('GHA',452,'Ghana'),('TOG',461,'Togo'),('CAO',471,'Cameroon'),('NIG',475,'Nigeria'),('GAB',481,'Gabon'),('CEN',482,'Central African Republic'),('CHA',483,'Chad'),('CON',484,'Congo'),('DRC',490,'Democratic Republic of the Congo'),('UGA',500,'Uganda'),('KEN',501,'Kenya'),('TAZ',510,'Tanzania'),('ZAN',511,'Zanzibar'),('BUI',516,'Burundi'),('RWA',517,'Rwanda'),('SOM',520,'Somalia'),('DJI',522,'Djibouti'),('ETH',530,'Ethiopia'),('ETH',530,'Ethiopia'),('ERI',531,'Eritrea'),('ANG',540,'Angola'),('MZM',541,'Mozambique'),('ZAM',551,'Zambia'),('ZIM',552,'Zimbabwe'),('MAW',553,'Malawi'),('SAF',560,'South Africa'),('NAM',565,'Namibia'),('LES',570,'Lesotho'),('BOT',571,'Botswana'),('SWA',572,'Swaziland'),('MAG',580,'Madagascar'),('COM',581,'Comoros'),('MAS',590,'Mauritius'),('SEY',591,'Seychelles'),('MOR',600,'Morocco'),('MOR',600,'Morocco'),('ALG',615,'Algeria'),('TUN',616,'Tunisia'),('TUN',616,'Tunisia'),('LIB',620,'Libya'),('SUD',625,'Sudan'),('SSD',626,'South Sudan'),('IRN',630,'Iran'),('TUR',640,'Turkey'),('IRQ',645,'Iraq'),('EGY',651,'Egypt'),('EGY',651,'Egypt'),('SYR',652,'Syria'),('SYR',652,'Syria'),('LEB',660,'Lebanon'),('JOR',663,'Jordan'),('ISR',666,'Israel'),('SAU',670,'Saudi Arabia'),('YAR',678,'Yemen Arab Republic'),('YEM',679,'Yemen'),('YPR',680,'Yemen People\'s Republic'),('KUW',690,'Kuwait'),('BAH',692,'Bahrain'),('QAT',694,'Qatar'),('UAE',696,'United Arab Emirates'),('OMA',698,'Oman'),('AFG',700,'Afghanistan'),('TKM',701,'Turkmenistan'),('TAJ',702,'Tajikistan'),('KYR',703,'Kyrgyzstan'),('UZB',704,'Uzbekistan'),('KZK',705,'Kazakhstan'),('CHN',710,'China'),('MON',712,'Mongolia'),('TAW',713,'Taiwan'),('KOR',730,'Korea'),('PRK',731,'North Korea'),('ROK',732,'South Korea'),('JPN',740,'Japan'),('JPN',740,'Japan'),('IND',750,'India'),('BHU',760,'Bhutan'),('PAK',770,'Pakistan'),('BNG',771,'Bangladesh'),('MYA',775,'Myanmar'),('SRI',780,'Sri Lanka'),('MAD',781,'Maldives'),('NEP',790,'Nepal'),('THI',800,'Thailand'),('CAM',811,'Cambodia'),('LAO',812,'Laos'),('DRV',816,'Vietnam'),('RVN',817,'Republic of Vietnam'),('MAL',820,'Malaysia'),('SIN',830,'Singapore'),('BRU',835,'Brunei'),('PHI',840,'Philippines'),('INS',850,'Indonesia'),('ETM',860,'East Timor'),('AUL',900,'Australia'),('PNG',910,'Papua New Guinea'),('NEW',920,'New Zealand'),('VAN',935,'Vanuatu'),('SOL',940,'Solomon Islands'),('KIR',946,'Kiribati'),('TUV',947,'Tuvalu'),('FIJ',950,'Fiji'),('TON',955,'Tonga'),('NAU',970,'Nauru'),('MSI',983,'Marshall Islands'),('PAL',986,'Palau'),('FSM',987,'Federated States of Micronesia'),('WSM',990,'Samoa');
/*!40000 ALTER TABLE `state_codes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-05  2:36:45
