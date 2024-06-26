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


