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
  `quantity` INT NULL,
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
  `sell_name` VARCHAR(50) NOT NULL,
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

CREATE TABLE `csc3170`.`review` (
  `orderID` INT NOT NULL,
  `itemID` INT NOT NULL,
  `rating` INT NOT NULL,
  PRIMARY KEY (`orderID`, `itemID`));

