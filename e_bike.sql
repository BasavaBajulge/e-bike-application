CREATE DATABASE IF NOT EXISTS e_bike;

USE e_bike;

CREATE TABLE IF NOT EXISTS DEALER (
    dealer_id varchar(20) primary key,
    dealer_name varchar(20) not null,
    dealer_city varchar(20),
    dealer_pin int(6) not null,
    dealer_street varchar(30)
);
