-- creates  tyrell_crop with nexus6 table
CREATE database tyrell_crop;
use tyrell_crop;
CREATE TABLE nexus6 (
        id INT,
        name VARCHAR(60)
);
INSERT INTO nexus6 VALUES(1, "Leon");
GRANT SELECT ON tyrell_crop.nexus6 TO 'holberton_user'@'localhost';

