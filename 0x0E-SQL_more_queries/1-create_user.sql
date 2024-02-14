-- Establishes the MySQL server user 'user_0d_1' with full privileges.
-- Sets the password for 'user_0d_1' to 'user_0d_1_pwd'.
-- Safely ensures that the script does not fail if 'user_0d_1' already exists

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
