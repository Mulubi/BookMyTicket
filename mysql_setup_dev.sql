-- this script prepares a MySQL server for BMT development stage

CREATE DATABASE IF NOT EXISTS bmt_dev_db;
CREATE USER IF NOT EXISTS 'bmt_dev'@'localhost' IDENTIFIED BY 'bmt_dev_pwd2023!';
GRANT ALL PRIVILEGES ON `bmt_dev_db`.* TO 'bmt_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'bmt_dev'@'localhost';
FLUSH PRIVILEGES;
