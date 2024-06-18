-- Create table unique_id (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS `{{ database_name }}`.`unique_id` (
  `id` INT NOT NULL AUTO_INCREMENT,  -- Use AUTO_INCREMENT for unique IDs
  `name` VARCHAR(256),
  PRIMARY KEY (`id`)
);
