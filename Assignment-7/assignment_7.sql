/*=====================================================
 Assignment 7 - SQL Fundamentals
 Name: Avinash
 Database: retail_company
=====================================================*/


-------------------------------------------------------
-- 1. Create Database
-------------------------------------------------------

CREATE DATABASE retail_company;


-------------------------------------------------------
-- IMPORTANT
-- After creating the database, open a new Query Tool
-- connected to the "retail_company" database before
-- running the remaining sections.
-------------------------------------------------------


-------------------------------------------------------
-- 2. Create Customers Table
-------------------------------------------------------

DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    state VARCHAR(50),
    membership VARCHAR(20),
    signup_date DATE,
    email VARCHAR(100),
    phone VARCHAR(20)
);


-------------------------------------------------------
-- 3. Insert Sample Customer Records
-------------------------------------------------------

INSERT INTO customers
(first_name, last_name, age, gender, city, state, membership, signup_date, email, phone)
VALUES
('Rahul','Sharma',25,'Male','Hyderabad','Telangana','Gold','2025-01-15','rahul@gmail.com','9876543210'),
('Priya','Reddy',28,'Female','Hyderabad','Telangana','Silver','2025-02-20','priya@gmail.com','9876543211'),
('Amit','Verma',34,'Male','Delhi','Delhi','Gold','2025-03-10','amit@gmail.com','9876543212'),
('Sneha','Patil',30,'Female','Mumbai','Maharashtra','Platinum','2025-03-25','sneha@gmail.com','9876543213'),
('Arjun','Kumar',26,'Male','Bangalore','Karnataka','Silver','2025-04-05','arjun@gmail.com','9876543214'),
('Meena','Singh',45,'Female','Lucknow','Uttar Pradesh','Gold','2025-04-18','meena@gmail.com','9876543215'),
('Ravi','Patel',38,'Male','Ahmedabad','Gujarat','Silver','2025-05-02','ravi@gmail.com','9876543216'),
('Neha','Joshi',29,'Female','Pune','Maharashtra','Gold','2025-05-15','neha@gmail.com','9876543217'),
('Karan','Gupta',40,'Male','Jaipur','Rajasthan','Platinum','2025-06-01','karan@gmail.com','9876543218'),
('Divya','Nair',32,'Female','Kochi','Kerala','Silver','2025-06-14','divya@gmail.com','9876543219'),
('Suresh','Rao',37,'Male','Chennai','Tamil Nadu','Gold','2025-06-28','suresh@gmail.com','9876543220'),
('Anjali','Mishra',24,'Female','Bhopal','Madhya Pradesh','Silver','2025-07-10','anjali@gmail.com','9876543221'),
('Vikram','Shah',31,'Male','Surat','Gujarat','Gold','2025-07-22','vikram@gmail.com','9876543222'),
('Pooja','Kapoor',27,'Female','Delhi','Delhi','Gold','2025-08-05','pooja@gmail.com','9876543223'),
('Ramesh','Yadav',50,'Male','Patna','Bihar','Silver','2025-08-18','ramesh@gmail.com','9876543224'),
('Lakshmi','Iyer',35,'Female','Chennai','Tamil Nadu','Platinum','2025-09-01','lakshmi@gmail.com','9876543225'),
('Aarav','Wilson',23,'Male','Austin','Texas','Gold','2025-09-15','aarav@gmail.com','9876543226'),
('Emily','Johnson',42,'Female','Dallas','Texas','Silver','2025-10-03','emily@gmail.com','9876543227'),
('Daniel','Brown',36,'Male','Los Angeles','California','Gold','2025-10-20','daniel@gmail.com','9876543228'),
('Olivia','Anderson',48,'Female',NULL,'Florida','Platinum','2025-11-08','olivia@gmail.com','9876543229');


-------------------------------------------------------
-- 4. REQUIRED QUERIES
-------------------------------------------------------


-- Query 1: Display all customers

SELECT *
FROM customers;


-- Query 2: Display first name, last name and city

SELECT first_name, last_name, city
FROM customers;


-- Query 3: Customers older than 35

SELECT *
FROM customers
WHERE age > 35;


-- Query 4: Customers from Texas

SELECT *
FROM customers
WHERE state = 'Texas';


-- Query 5: Gold members

SELECT *
FROM customers
WHERE membership = 'Gold';


-- Query 6: Customers aged between 25 and 40

SELECT *
FROM customers
WHERE age BETWEEN 25 AND 40;


-- Query 7: Customers from Texas, California or Florida

SELECT *
FROM customers
WHERE state IN ('Texas', 'California', 'Florida');


-- Query 8: First names starting with A

SELECT *
FROM customers
WHERE first_name LIKE 'A%';


-- Query 9: Last names ending with "son"

SELECT *
FROM customers
WHERE last_name LIKE '%son';


-- Query 10: Customers with NULL city

SELECT *
FROM customers
WHERE city IS NULL;


-- Query 11: Display unique states

SELECT DISTINCT state
FROM customers;


-- Query 12: Order customers by age ascending

SELECT *
FROM customers
ORDER BY age ASC;


-- Query 13: Order customers by age descending

SELECT *
FROM customers
ORDER BY age DESC;


-- Query 14: Display five oldest customers

SELECT *
FROM customers
ORDER BY age DESC
LIMIT 5;


-- Query 15: Column aliases

SELECT
    first_name AS "First Name",
    last_name AS "Last Name",
    membership AS "Membership"
FROM customers;


-------------------------------------------------------
-- 5. CHALLENGE QUERIES
-------------------------------------------------------


-- Challenge 1: Gold members younger than 30

SELECT *
FROM customers
WHERE age < 30
AND membership = 'Gold';


-- Challenge 2: Texas customers older than 40

SELECT *
FROM customers
WHERE state = 'Texas'
AND age > 40;


-- Challenge 3: First name contains "e"

SELECT *
FROM customers
WHERE first_name LIKE '%e%';


-- Challenge 4: Customers who are not Platinum

SELECT *
FROM customers
WHERE membership <> 'Platinum';


-- Challenge 5: Customers ordered alphabetically by last name

SELECT *
FROM customers
ORDER BY last_name ASC;


-------------------------------------------------------
-- 6. BONUS QUERIES
-------------------------------------------------------


-- Bonus 1: Count total customers

SELECT COUNT(*) AS total_customers
FROM customers;


-- Bonus 2: Count Gold members

SELECT COUNT(*) AS gold_members
FROM customers
WHERE membership = 'Gold';


-- Bonus 3: Count customers with NULL email

SELECT COUNT(*) AS null_email_count
FROM customers
WHERE email IS NULL;


-- Bonus 4: Display unique cities

SELECT DISTINCT city
FROM customers;


-- Bonus 5: Customers from Gujarat or Kerala

SELECT *
FROM customers
WHERE state IN ('Gujarat', 'Kerala');


-- Bonus 6: Gmail users

SELECT *
FROM customers
WHERE email LIKE '%gmail.com';


-- Bonus 7: Platinum members

SELECT *
FROM customers
WHERE membership = 'Platinum';


-- Bonus 8: Customers from Maharashtra

SELECT *
FROM customers
WHERE state = 'Maharashtra';


-- Bonus 9: Customers younger than 30

SELECT *
FROM customers
WHERE age < 30;


-- Bonus 10: Cities in alphabetical order

SELECT DISTINCT city
FROM customers
ORDER BY city ASC;