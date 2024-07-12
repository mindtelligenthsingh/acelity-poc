CREATE OR REPLACE FUNCTION hello_world()
RETURNS text AS
$$
DECLARE
  output  VARCHAR(20);
BEGIN
  /* Query the string into a local variable. */
  SELECT 'Hello World!' INTO output;
 
  /* Return the output text variable. */
  RETURN output;

END
$$ LANGUAGE plpgsql;

CREATE TABLE cars (
  brand VARCHAR(255),
  model VARCHAR(255),
  year INT
);

insert into cars(brand, model, year) values('HONDA', 'CIVIC', 1996);
insert into cars(brand, model, year) values('HONDA', 'ACCORD', 2000);