-- Create database hbtn_0d_usa (if it doesn't already exist)
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;

-- Create table states within hbtn_0d_usa (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`states` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`)
);
