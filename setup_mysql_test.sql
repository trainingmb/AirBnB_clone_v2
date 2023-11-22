-- Create database hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Drop Test User If Exists
DROP USER IF EXISTS 'hbnb_test'@'localhost';

-- Create New Test User
CREATE USER 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Give Priveleges to New User on Created Database
GRANT ALL ON hbnb_test_db.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;

-- Grant SELECT Privileges on perfomance_schema to the New User
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost' WITH GRANT OPTION;
