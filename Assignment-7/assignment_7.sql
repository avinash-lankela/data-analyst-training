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
-- Connect to Database
-------------------------------------------------------

-- Open Query Tool for retail_company before executing
-------------------------------------------------------
-- 2. Create Customers Table
-------------------------------------------------------
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    gender VARCHAR(10),
    city VARCHAR(50),
    state VARCHAR(50),
    membership VARCHAR(20),
    email VARCHAR(100),
    phone VARCHAR(20)
);
-------------------------------------------------------
-- 3. Insert Sample Customer Records
-------------------------------------------------------
INSERT INTO customers
(first_name, last_name, age, gender, city, state, membership, email, phone)
VALUES
('Rahul','Sharma',25,'Male','Hyderabad','Telangana','Gold','rahul@gmail.com','9876543210'),
('Priya','Reddy',28,'Female','Hyderabad','Telangana','Silver','priya@gmail.com','9876543211'),
('Amit','Verma',34,'Male','Delhi','Delhi','Gold','amit@gmail.com','9876543212'),
('Sneha','Patil',30,'Female','Mumbai','Maharashtra','Platinum','sneha@gmail.com','9876543213'),
('Arjun','Kumar',26,'Male','Bangalore','Karnataka','Silver','arjun@gmail.com','9876543214'),
('Meena','Singh',45,'Female','Lucknow','Uttar Pradesh','Gold','meena@gmail.com','9876543215'),
('Ravi','Patel',38,'Male','Ahmedabad','Gujarat','Silver','ravi@gmail.com','9876543216'),
('Neha','Joshi',29,'Female','Pune','Maharashtra','Gold','neha@gmail.com','9876543217'),
('Karan','Gupta',40,'Male','Jaipur','Rajasthan','Platinum','karan@gmail.com','9876543218'),
('Divya','Nair',32,'Female','Kochi','Kerala','Silver','divya@gmail.com','9876543219'),
('Suresh','Rao',37,'Male','Chennai','Tamil Nadu','Gold','suresh@gmail.com','9876543220'),
('Anjali','Mishra',24,'Female','Bhopal','Madhya Pradesh','Silver','anjali@gmail.com','9876543221'),
('Vikram','Shah',31,'Male','Surat','Gujarat','Gold','vikram@gmail.com','9876543222'),
('Pooja','Kapoor',27,'Female','Delhi','Delhi','Gold','pooja@gmail.com','9876543223'),
('Ramesh','Yadav',50,'Male','Patna','Bihar','Silver','ramesh@gmail.com','9876543224'),
('Lakshmi','Iyer',35,'Female','Chennai','Tamil Nadu','Platinum','lakshmi@gmail.com','9876543225'),
('Rahul','Sharma',25,'Male','Hyderabad','Telangana','Gold','rahul@gmail.com','9876543210'),
('Neha','Joshi',29,'Female','Pune','Maharashtra','Gold','neha@gmail.com','9876543217'),
('Mohit','Bansal',33,'Male','Noida','Uttar Pradesh','Silver',NULL,'9876543226'),
('Kavya','Rao',22,'Female','Hyderabad','Telangana','Gold','kavya@gmail.com','9876543227');
-------------------------------------------------------
-- Display all customers
-------------------------------------------------------

SELECT * FROM customers;

-------------------------------------------------------
-- Display first name and last name
-------------------------------------------------------

SELECT first_name, last_name
FROM customers;

-------------------------------------------------------
-- Display unique cities
-------------------------------------------------------

SELECT DISTINCT city
FROM customers;

-------------------------------------------------------
-- Customers from Telangana
-------------------------------------------------------

SELECT *
FROM customers
WHERE state = 'Telangana';

-------------------------------------------------------
-- Customers older than 30
-------------------------------------------------------

SELECT *
FROM customers
WHERE age > 30;

-------------------------------------------------------
-- Gold members
-------------------------------------------------------

SELECT *
FROM customers
WHERE membership = 'Gold';

-------------------------------------------------------
-- Customers between age 25 and 35
-------------------------------------------------------

SELECT *
FROM customers
WHERE age BETWEEN 25 AND 35;

-------------------------------------------------------
-- Customers from Delhi or Hyderabad
-------------------------------------------------------

SELECT *
FROM customers
WHERE city IN ('Delhi', 'Hyderabad');

-------------------------------------------------------
-- Customers with NULL email
-------------------------------------------------------

SELECT *
FROM customers
WHERE email IS NULL;

-------------------------------------------------------
-- Names starting with R
-------------------------------------------------------

SELECT *
FROM customers
WHERE first_name LIKE 'R%';

-------------------------------------------------------
-- Gmail users
-------------------------------------------------------

SELECT *
FROM customers
WHERE email LIKE '%gmail.com';

-------------------------------------------------------
-- Order by age (Ascending)
-------------------------------------------------------

SELECT *
FROM customers
ORDER BY age ASC;

-------------------------------------------------------
-- Order by age (Descending)
-------------------------------------------------------

SELECT *
FROM customers
ORDER BY age DESC;

-------------------------------------------------------
-- First 5 customers
-------------------------------------------------------

SELECT *
FROM customers
LIMIT 5;

-------------------------------------------------------
-- Aliases
-------------------------------------------------------

SELECT
first_name AS FirstName,
last_name AS LastName,
membership AS MembershipType
FROM customers;

-------------------------------------------------------
-- Female Gold members
-------------------------------------------------------

SELECT *
FROM customers
WHERE gender = 'Female'
AND membership = 'Gold';

-------------------------------------------------------
-- Platinum members
-------------------------------------------------------

SELECT *
FROM customers
WHERE membership = 'Platinum';

-------------------------------------------------------
-- Customers from Maharashtra
-------------------------------------------------------

SELECT *
FROM customers
WHERE state = 'Maharashtra';

-------------------------------------------------------
-- Customers younger than 30
-------------------------------------------------------

SELECT *
FROM customers
WHERE age < 30;

-------------------------------------------------------
-- Cities in alphabetical order
-------------------------------------------------------

SELECT DISTINCT city
FROM customers
ORDER BY city;

-------------------------------------------------------
-- Challenge Question 1: Count Total Customers
-------------------------------------------------------

SELECT COUNT(*) AS total_customers
FROM customers;

-------------------------------------------------------
-- Challenge Question 2: Count Gold Members
-------------------------------------------------------

SELECT COUNT(*) AS gold_members
FROM customers
WHERE membership = 'Gold';

-------------------------------------------------------
-- Challenge Question 3: Count Customers with NULL Email
-------------------------------------------------------

SELECT COUNT(*) AS null_email_count
FROM customers
WHERE email IS NULL;

-------------------------------------------------------
-- Challenge Question 4: Display Unique States
-------------------------------------------------------

SELECT DISTINCT state
FROM customers;

-------------------------------------------------------
-- Challenge Question 5: Customers from Gujarat or Kerala
-------------------------------------------------------

SELECT *
FROM customers
WHERE state IN ('Gujarat', 'Kerala');