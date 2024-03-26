CREATE TABLE IF NOT EXISTS t (
  id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
  smth varchar(256) NOT NULL
);

INSERT INTO t(smth) VALUES ("This"), ("is"), ("very"), ("strange"), ("database");
