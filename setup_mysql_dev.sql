-- Create database hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Drop User
DROP USER IF EXISTS 'hbnb_dev'@'localhost';

-- Create New User
CREATE USER 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Give Priveleges to New User on Created Database
GRANT ALL ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;

-- Grant SELECT Privileges on perfomance_schema to the New User
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost' WITH GRANT OPTION;
