-- Create MySQL server user user_0d_1 with all privileges and password user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL ON *.* TO 'user_0d_1'@'localhost';

