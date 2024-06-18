-- Create table force_name (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS `{{ database_name }}`.`force_name` (
  `id` INT,
  `name` VARCHAR(256),
  PRIMARY KEY (`id`)
);
