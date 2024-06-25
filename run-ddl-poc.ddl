CREATE TABLE consultants(
  id serial NOT NULL,
  first_name varchar(100) NOT NULL,
  last_name varchar(100) NOT NULL,
  email varchar(200),
  departments_id integer NOT NULL,
  contract_date date
    CONSTRAINT check_contract_date CHECK ((contract_date <= CURRENT_DATE)),
  CONSTRAINT consultants_pkey PRIMARY KEY(id),
  CONSTRAINT email UNIQUE(email)
);

CREATE INDEX consultants_last_name_idx ON consultants(last_name);
