CREATE TABLE users
(
  user_id  SERIAL NOT NULL
    CONSTRAINT users_pkey
    PRIMARY KEY,
  username VARCHAR(3000),
  password VARCHAR(3000)
);

CREATE UNIQUE INDEX users_user_id_uindex
  ON users (user_id);

CREATE UNIQUE INDEX users_username_uindex
  ON users (username);


