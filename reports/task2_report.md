# Task 2 — Query Understanding (Decomposition) Report

**Database:** ClassicModels (PostgreSQL)
**Total Questions:** 50
**Format:** Intent · Tables · Columns · Filters · Joins

---

## Part 2A — Simple SELECT Queries (Q1–Q20)

### Q1: List all products

**Intent:** Retrieve all columns and records from the products table
**Tables:** products
**Columns:** productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP
**Filters:** None
**Joins:** None

---

### Q2: Get all customers

**Intent:** Retrieve all columns and records from the customers table
**Tables:** customers
**Columns:** customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressLine2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit
**Filters:** None
**Joins:** None

---

### Q3: Show all orders

**Intent:** Retrieve all columns and records from the orders table
**Tables:** orders
**Columns:** orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber
**Filters:** None
**Joins:** None

---

### Q4: List all employees

**Intent:** Retrieve all columns and records from the employees table
**Tables:** employees
**Columns:** employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle
**Filters:** None
**Joins:** None

---

### Q5: Get all offices

**Intent:** Retrieve all columns and records from the offices table
**Tables:** offices
**Columns:** officeCode, city, phone, addressLine1, addressLine2, state, country, postalCode, territory
**Filters:** None
**Joins:** None

---

### Q6: Show all product lines

**Intent:** Retrieve all columns and records from the productlines table
**Tables:** productlines
**Columns:** productLine, textDescription, htmlDescription, image
**Filters:** None
**Joins:** None

---

### Q7: List all payments

**Intent:** Retrieve all columns and records from the payments table
**Tables:** payments
**Columns:** customerNumber, checkNumber, paymentDate, amount
**Filters:** None
**Joins:** None

---

### Q8: Get product names and prices

**Intent:** Retrieve the name and buy price of every product
**Tables:** products
**Columns:** productName, buyPrice
**Filters:** None
**Joins:** None

---

### Q9: Get customer names and cities

**Intent:** Retrieve the name and city of every customer
**Tables:** customers
**Columns:** customerName, city
**Filters:** None
**Joins:** None

---

### Q10: List employee first and last names

**Intent:** Retrieve the first name and last name of every employee
**Tables:** employees
**Columns:** firstName, lastName
**Filters:** None
**Joins:** None

---

### Q11: Get all order dates

**Intent:** Retrieve the order number and order date for every order
**Tables:** orders
**Columns:** orderNumber, orderDate
**Filters:** None
**Joins:** None

---

### Q12: Show product vendor list

**Intent:** Retrieve the distinct list of product vendors across all products
**Tables:** products
**Columns:** productVendor
**Filters:** None
**Joins:** None

---

### Q13: Get all product codes

**Intent:** Retrieve the product code of every product
**Tables:** products
**Columns:** productCode
**Filters:** None
**Joins:** None

---

### Q14: List all countries from offices

**Intent:** Retrieve the distinct list of countries where offices are located
**Tables:** offices
**Columns:** country
**Filters:** None
**Joins:** None

---

### Q15: Show all order statuses

**Intent:** Retrieve the distinct list of statuses across all orders
**Tables:** orders
**Columns:** status
**Filters:** None
**Joins:** None

---

### Q16: Get all payment amounts

**Intent:** Retrieve the customer number and payment amount for every payment record
**Tables:** payments
**Columns:** customerNumber, amount
**Filters:** None
**Joins:** None

---

### Q17: List all job titles

**Intent:** Retrieve the distinct list of job titles held by employees
**Tables:** employees
**Columns:** jobTitle
**Filters:** None
**Joins:** None

---

### Q18: Get customer phone numbers

**Intent:** Retrieve the name and phone number of every customer
**Tables:** customers
**Columns:** customerName, phone
**Filters:** None
**Joins:** None

---

### Q19: Show product MSRP values

**Intent:** Retrieve the name and MSRP of every product
**Tables:** products
**Columns:** productName, MSRP
**Filters:** None
**Joins:** None

---

### Q20: List order numbers

**Intent:** Retrieve the order number of every order
**Tables:** orders
**Columns:** orderNumber
**Filters:** None
**Joins:** None

---

## Part 2B — JOIN Queries (Q21–Q30)

### Q21: Get orders with customer names

**Intent:** Retrieve each order's number and date along with the name of the customer who placed it
**Tables:** orders, customers
**Columns:** orders.orderNumber, orders.orderDate, customers.customerName
**Filters:** None
**Joins:** orders.customerNumber = customers.customerNumber

---

### Q22: Get employees with office city

**Intent:** Retrieve each employee's first and last name along with the city of their assigned office
**Tables:** employees, offices
**Columns:** employees.firstName, employees.lastName, offices.city
**Filters:** None
**Joins:** employees.officeCode = offices.officeCode

---

### Q23: Get payments with customer names

**Intent:** Retrieve each payment's amount and date along with the name of the customer who made it
**Tables:** payments, customers
**Columns:** customers.customerName, payments.amount, payments.paymentDate
**Filters:** None
**Joins:** payments.customerNumber = customers.customerNumber

---

### Q24: Get order details with product names

**Intent:** Retrieve each order detail record along with the name, quantity ordered, and price of the corresponding product
**Tables:** orderdetails, products
**Columns:** orderdetails.orderNumber, products.productName, orderdetails.quantityOrdered, orderdetails.priceEach
**Filters:** None
**Joins:** orderdetails.productCode = products.productCode

---

### Q25: Get products with product line description

**Intent:** Retrieve each product's name along with the text description of its product line
**Tables:** products, productlines
**Columns:** products.productName, productlines.textDescription
**Filters:** None
**Joins:** products.productLine = productlines.productLine

---

### Q26: Get customers with sales rep names

**Intent:** Retrieve each customer's name along with the first and last name of their assigned sales representative
**Tables:** customers, employees
**Columns:** customers.customerName, employees.firstName, employees.lastName
**Filters:** None
**Joins:** customers.salesRepEmployeeNumber = employees.employeeNumber

---

### Q27: Get orders with customer city

**Intent:** Retrieve each order's number and date along with the city of the customer who placed it
**Tables:** orders, customers
**Columns:** orders.orderNumber, orders.orderDate, customers.city
**Filters:** None
**Joins:** orders.customerNumber = customers.customerNumber

---

### Q28: Get employees and their manager

**Intent:** Retrieve each employee's first name alongside their manager's first name using a self-join on the employees table
**Tables:** employees (self-join)
**Columns:** employees.firstName, employees.reportsTo, employees.employeeNumber
**Filters:** None
**Joins:** employees.reportsTo = employees.employeeNumber

---

### Q29: Get orderdetails with product vendor

**Intent:** Retrieve each order detail record along with the vendor of the corresponding product
**Tables:** orderdetails, products
**Columns:** orderdetails.orderNumber, products.productVendor, orderdetails.quantityOrdered
**Filters:** None
**Joins:** orderdetails.productCode = products.productCode

---

### Q30: Get payments with customer country

**Intent:** Retrieve each payment's amount along with the customer's name and country
**Tables:** payments, customers
**Columns:** customers.customerName, customers.country, payments.amount
**Filters:** None
**Joins:** payments.customerNumber = customers.customerNumber

---

## Part 2C — GROUP BY + Aggregation Queries (Q31–Q40)

### Q31: Count customers per country

**Intent:** Count the number of customers grouped by each country using COUNT
**Tables:** customers
**Columns:** country, customerNumber
**Filters:** None
**Joins:** None

---

### Q32: Total payments per customer

**Intent:** Calculate the total payment amount per customer using SUM grouped by customerNumber
**Tables:** payments
**Columns:** customerNumber, amount
**Filters:** None
**Joins:** None

---

### Q33: Number of orders per status

**Intent:** Count the number of orders for each distinct status value using COUNT grouped by status
**Tables:** orders
**Columns:** status, orderNumber
**Filters:** None
**Joins:** None

---

### Q34: Products per product line

**Intent:** Count the number of products in each product line using COUNT grouped by productLine
**Tables:** products
**Columns:** productLine, productCode
**Filters:** None
**Joins:** None

---

### Q35: Employees per office

**Intent:** Count the number of employees in each office using COUNT grouped by officeCode
**Tables:** employees
**Columns:** officeCode, employeeNumber
**Filters:** None
**Joins:** None

---

### Q36: Total stock per product vendor

**Intent:** Sum the quantity in stock for products grouped by each product vendor using SUM
**Tables:** products
**Columns:** productVendor, quantityInStock
**Filters:** None
**Joins:** None

---

### Q37: Average buy price per product line

**Intent:** Calculate the average buy price of products grouped by each product line using AVG
**Tables:** products
**Columns:** productLine, buyPrice
**Filters:** None
**Joins:** None

---

### Q38: Orders per customer

**Intent:** Count the number of orders placed by each customer using COUNT grouped by customerNumber
**Tables:** orders
**Columns:** customerNumber, orderNumber
**Filters:** None
**Joins:** None

---

### Q39: Max MSRP per product line

**Intent:** Find the maximum MSRP value among products grouped by each product line using MAX
**Tables:** products
**Columns:** productLine, MSRP
**Filters:** None
**Joins:** None

---

### Q40: Min buy price per vendor

**Intent:** Find the minimum buy price among products grouped by each product vendor using MIN
**Tables:** products
**Columns:** productVendor, buyPrice
**Filters:** None
**Joins:** None

---

## Part 2D — Single Aggregate Queries (Q41–Q50)

### Q41: Total number of customers

**Intent:** Count the total number of customer records in the customers table using COUNT
**Tables:** customers
**Columns:** customerNumber
**Filters:** None
**Joins:** None

---

### Q42: Total number of products

**Intent:** Count the total number of product records in the products table using COUNT
**Tables:** products
**Columns:** productCode
**Filters:** None
**Joins:** None

---

### Q43: Total revenue from payments

**Intent:** Sum the amount across all payment records to get total revenue using SUM
**Tables:** payments
**Columns:** amount
**Filters:** None
**Joins:** None

---

### Q44: Average product price

**Intent:** Calculate the average buy price across all products using AVG
**Tables:** products
**Columns:** buyPrice
**Filters:** None
**Joins:** None

---

### Q45: Max payment amount

**Intent:** Find the single largest payment amount across all payment records using MAX
**Tables:** payments
**Columns:** amount
**Filters:** None
**Joins:** None

---

### Q46: Min payment amount

**Intent:** Find the single smallest payment amount across all payment records using MIN
**Tables:** payments
**Columns:** amount
**Filters:** None
**Joins:** None

---

### Q47: Count total orders

**Intent:** Count the total number of order records in the orders table using COUNT
**Tables:** orders
**Columns:** orderNumber
**Filters:** None
**Joins:** None

---

### Q48: Total quantity in stock

**Intent:** Sum the quantity in stock across all products to get the total inventory using SUM
**Tables:** products
**Columns:** quantityInStock
**Filters:** None
**Joins:** None

---

### Q49: Average MSRP

**Intent:** Calculate the average MSRP value across all products using AVG
**Tables:** products
**Columns:** MSRP
**Filters:** None
**Joins:** None

---

### Q50: Number of employees

**Intent:** Count the total number of employee records in the employees table using COUNT
**Tables:** employees
**Columns:** employeeNumber
**Filters:** None
**Joins:** None

---

## Summary

| Category | Questions | Tables Used | Joins Required |
|---|---|---|---|
| Simple SELECT (all columns) | Q1–Q7 | 1 table each | None |
| Simple SELECT (specific columns) | Q8–Q20 | 1 table each | None |
| JOIN queries | Q21–Q30 | 2 tables each | Yes (1 join each) |
| GROUP BY + Aggregation | Q31–Q40 | 1 table each | None |
| Single Aggregate (COUNT/SUM/AVG/MAX/MIN) | Q41–Q50 | 1 table each | None |

**Total questions decomposed:** 50 / 50
**Questions requiring joins:** 10 (Q21–Q30)
**Questions using aggregation:** 20 (Q31–Q50)
**Questions with filters:** 0 (all benchmark questions are unfiltered)
