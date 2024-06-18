-- Create table force_name (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS `{{ database_name }}`.`force_name` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(256) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;