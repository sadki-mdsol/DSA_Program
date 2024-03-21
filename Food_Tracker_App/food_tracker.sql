create table log_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    entry_date DATE NOT NULL
);


CREATE table food(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    food_name text NOT NULL,
    protein integer NOT NULL,
    carbohydrates integer NOT NULL,
    fat integer NOT NULL,
    calories integer NOT NULL
);


CREATE table food_date(
    food_id integer NOT NULL,
    log_date_id integer NOT NULL,
    primary key(food_id,log_date_id)
);