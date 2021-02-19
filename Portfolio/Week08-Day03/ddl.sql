create table Teachers(
    id integer primary key,
    image varchar(255),
    teacher_first_name varchar(255),
    teacher_last_name varchar(255),
    description text(255),
    email ,
    phone integer(30),
    gender varchar(20)
);

create table Categories(
    id integer primary key,
    category_name varchar(50)
);


create table Courses(
    id integer primary key,
    course_title varchar(60),
    description text(255),
    teacher_id integer not null,
    FOREIGN KEY (teacher_id)
    REFERENCES Teachers(id),
    category_id integer not null,
    FOREIGN KEY (category_id)
    REFERENCES Categories(id)
    level_id integer NOT NULL,
    FOREIGN KEY (level_id)
    REFERENCES Levels(id)
);

create table Levels(
    id integer primary key,
    level_name varchar(255)
)

CREATE TABLE Contact(
id integer primary key,
person_name varcher(255),
subject varchar (255),
description text(255),
person_phone integer(20),
person_email varchar(255),
city_id inete
)