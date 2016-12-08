-- Create DB if it doesn't exist
CREATE DATABASE IF NOT EXISTS demodb;

-- Create test db user
-- INSERT INTO mysql.user(User,Host,Password) VALUES(‘demouser’,’localhost’,PASSWORD(‘demopassword’));
INSERT INTO mysql.user(User, Host, Password)
SELECT * FROM (SELECT 'demouser', 'localhost', PASSWORD('helloworld')) AS tmp
WHERE NOT EXISTS (
    SELECT User FROM mysql.user WHERE User = 'demouser'
) LIMIT 1;

-- Apply changes
FLUSH PRIVILEGES;

-- Grant all privileges for our user
GRANT ALL PRIVILEGES ON demodb.* to demouser@localhost;

-- Apply changes
FLUSH PRIVILEGES;

-- Check
SHOW GRANTS FOR demouser@localhost;

-- Current usage
USE demodb;

-- ####################### TABLES ########################
DROP TABLE IF EXISTS Bid;
CREATE TABLE Bid (
  id INTEGER NOT NULL AUTO_INCREMENT DEFAULT NULL,
  ts DATETIME NULL DEFAULT NULL,
  id_Status INTEGER NULL DEFAULT NULL,
  id_Action INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Status;
CREATE TABLE Status (
  id INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  value MEDIUMTEXT NULL DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Bidder;
CREATE TABLE Bidder (
  id INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  firstname VARCHAR(80) NOT NULL,
  lastname VARCHAR(80) NOT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS BiddingMap;
CREATE TABLE BiddingMap (
  id INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  id_Bidder INTEGER NULL DEFAULT NULL,
  id_Bid INTEGER NULL DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS Action;
CREATE TABLE Action (
  id INTEGER NULL AUTO_INCREMENT DEFAULT NULL,
  value MEDIUMTEXT NOT NULL,
  PRIMARY KEY (id)
);

-- ---
-- Foreign Keys 
-- ---
ALTER   TABLE   Bid          ADD   FOREIGN KEY   (id_Status)   REFERENCES   Status(id);
ALTER   TABLE   Bid          ADD   FOREIGN KEY   (id_Action)   REFERENCES   Action(id);
ALTER   TABLE   BiddingMap   ADD   FOREIGN KEY   (id_Bidder)   REFERENCES   Bidder(id);
ALTER   TABLE   BiddingMap   ADD   FOREIGN KEY   (id_Bid)      REFERENCES   Bid(id);

-- ---
-- Table Properties
-- ---
ALTER   TABLE   Bid          ENGINE=InnoDB   DEFAULT   CHARSET=utf8   COLLATE=utf8_bin;
ALTER   TABLE   Status       ENGINE=InnoDB   DEFAULT   CHARSET=utf8   COLLATE=utf8_bin;
ALTER   TABLE   Bidder       ENGINE=InnoDB   DEFAULT   CHARSET=utf8   COLLATE=utf8_bin;
ALTER   TABLE   BiddingMap   ENGINE=InnoDB   DEFAULT   CHARSET=utf8   COLLATE=utf8_bin;
ALTER   TABLE   Action       ENGINE=InnoDB   DEFAULT   CHARSET=utf8   COLLATE=utf8_bin;

-- Statuses
INSERT INTO Status(value) VALUES('Fixed');
INSERT INTO Status(value) VALUES('InProgress');

-- Actions
INSERT INTO Action(value) VALUES('Washing a car');
INSERT INTO Action(value) VALUES('Shopping');

-- Bidders
INSERT INTO Bidder(firstname, lastname) VALUES('Bob', 'Doe');
INSERT INTO Bidder(firstname, lastname) VALUES('Alice', 'Doe');

-- Bids
INSERT INTO Bid(ts, id_Status, id_Action) VALUES('2016-12-05 10:20:00', 1, 1);
INSERT INTO Bid(ts, id_Status, id_Action) VALUES('2016-12-06 10:30:00', 2, 2);
INSERT INTO Bid(ts, id_Status, id_Action) VALUES('2016-12-05 10:20:00', 2, 2);

-- BiddingMaps
INSERT INTO BiddingMap(id_Bidder, id_Bid) VALUES(1, 2);
INSERT INTO BiddingMap(id_Bidder, id_Bid) VALUES(2, 2);
INSERT INTO BiddingMap(id_Bidder, id_Bid) VALUES(2, 3);


-- ---
-- Test Data
-- ---
-- INSERT INTO `Bid` (`id`,`ts`,`id_Status`,`id_Action`) VALUES
-- ('','','','');
-- INSERT INTO `Status` (`id`,`value`) VALUES
-- ('','');
-- INSERT INTO `Bidder` (`id`,`firstname`,`lastname`) VALUES
-- ('','','');
-- INSERT INTO `BiddingMap` (`id`,`id_Bidder`,`id_Bid`) VALUES
-- ('','','');
-- INSERT INTO `Action` (`id`,`value`) VALUES
-- ('','');
