-- Create table unique_id (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS unique_id (
  `id` INT DEFAULT 1,
  `name` VARCHAR(256) NOT NULL
);