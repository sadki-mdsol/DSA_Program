create table users(
    id integer primary key autoincrement,
    user_name  text not null,
    password text not null,
    expert boolean,
    admin boolean
);

create table questions(
    id integer primary key autoincrement,
    question_test text not null,
    answer_text text,
    asked_by_id integer not null,
    expert_id integer not null
);