CREATE TABLE users(
  id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(64) NOT NULL UNIQUE,
  first_name VARCHAR(64) NOT NULL,
  last_name VARCHAR(64) NOT NULL
);
