-- Establishes the database 'hbtn_0d_2' along with the user 'user_0d_2'.
-- Assigns 'user_0d_2' with SELECT privilege exclusively in the 'hbtn_0d_2' database.
-- Sets the password for 'user_0d_2' to 'user_0d_2_pwd'.
-- Ensures the script does not fail if the database 'hbtn_0d_2' or the user 'user_0d_2' already exists.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
