# Task 1 — SQL Benchmark Ground Truth Report

**Database:** ClassicModels (PostgreSQL)
**Total Questions:** 50
**All Queries Verified:** ✅

---

## Part 1A — Simple SELECT Queries (Q1–Q20)

### Q1: List all products

**SQL Query:**
```sql
SELECT * FROM products;
```

**Rows Returned:** 110

**Sample Output:**

| productCode | productName | productLine | productScale | productVendor | productDescription | quantityInStock | buyPrice | MSRP |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| S10_1678 | 1969 Harley Davidson Ultimate Chopper | Motorcycles | 1:10 | Min Lin Diecast | This replica features working kickstand, front suspension, gear-shift lever, footbrake lever, drive chain, wheels and steering. All parts are particularly delicate due to their precise scale and require special care and attention. | 7933 | 48.81 | 95.70 |
| S10_1949 | 1952 Alpine Renault 1300 | Classic Cars | 1:10 | Classic Metal Creations | Turnable front wheels; steering function; detailed interior; detailed engine; opening hood; opening trunk; opening doors; and detailed chassis. | 7305 | 98.58 | 214.30 |
| S10_2016 | 1996 Moto Guzzi 1100i | Motorcycles | 1:10 | Highway 66 Mini Classics | Official Moto Guzzi logos and insignias, saddle bags located on side of motorcycle, detailed engine, working steering, working suspension, two leather seats, luggage rack, dual exhaust pipes, small saddle bag located on handle bars, two-tone paint with chrome accents, superior die-cast detail , rotating wheels , working kick stand, diecast metal with plastic parts and baked enamel finish. | 6625 | 68.99 | 118.94 |

**Explanation:** Returns all 110 products with full details from the products table.

---

### Q2: Get all customers

**SQL Query:**
```sql
SELECT * FROM customers;
```

**Rows Returned:** 122

**Sample Output:**

| customerNumber | customerName | contactLastName | contactFirstName | phone | addressLine1 | addressLine2 | city | state | postalCode | country | salesRepEmployeeNumber | creditLimit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 103 | Atelier graphique | Schmitt | Carine  | 40.32.2555 | 54, rue Royale | None | Nantes | None | 44000 | France | 1370 | 21000.00 |
| 112 | Signal Gift Stores | King | Jean | 7025551838 | 8489 Strong St. | None | Las Vegas | NV | 83030 | USA | 1166 | 71800.00 |
| 114 | Australian Collectors, Co. | Ferguson | Peter | 03 9520 4555 | 636 St Kilda Road | Level 3 | Melbourne | Victoria | 3004 | Australia | 1611 | 117300.00 |

**Explanation:** Returns all 122 customer records including contact info and credit limits.

---

### Q3: Show all orders

**SQL Query:**
```sql
SELECT * FROM orders;
```

**Rows Returned:** 326

**Sample Output:**

| orderNumber | orderDate | requiredDate | shippedDate | status | comments | customerNumber |
| --- | --- | --- | --- | --- | --- | --- |
| 10100 | 2003-01-06 | 2003-01-13 | 2003-01-10 | Shipped | None | 363 |
| 10101 | 2003-01-09 | 2003-01-18 | 2003-01-11 | Shipped | Check on availability. | 128 |
| 10102 | 2003-01-10 | 2003-01-18 | 2003-01-14 | Shipped | None | 181 |

**Explanation:** Returns all 326 orders with dates, status, and customer references.

---

### Q4: List all employees

**SQL Query:**
```sql
SELECT * FROM employees;
```

**Rows Returned:** 23

**Sample Output:**

| employeeNumber | lastName | firstName | extension | email | officeCode | reportsTo | jobTitle |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1002 | Murphy | Diane | x5800 | dmurphy@classicmodelcars.com | 1 | None | President |
| 1056 | Patterson | Mary | x4611 | mpatterso@classicmodelcars.com | 1 | 1002 | VP Sales |
| 1076 | Firrelli | Jeff | x9273 | jfirrelli@classicmodelcars.com | 1 | 1002 | VP Marketing |

**Explanation:** Returns all 23 employees with job titles and office assignments.

---

### Q5: Get all offices

**SQL Query:**
```sql
SELECT * FROM offices;
```

**Rows Returned:** 7

**Sample Output:**

| officeCode | city | phone | addressLine1 | addressLine2 | state | country | postalCode | territory |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | San Francisco | +1 650 219 4782 | 100 Market Street | Suite 300 | CA | USA | 94080 | NA |
| 2 | Boston | +1 215 837 0825 | 1550 Court Place | Suite 102 | MA | USA | 02107 | NA |
| 3 | NYC | +1 212 555 3000 | 523 East 53rd Street | apt. 5A | NY | USA | 10022 | NA |

**Explanation:** Returns all 7 office locations with address and territory info.

---

### Q6: Show all product lines

**SQL Query:**
```sql
SELECT * FROM productlines;
```

**Rows Returned:** 7

**Sample Output:**

| productLine | textDescription | htmlDescription | image |
| --- | --- | --- | --- |
| Classic Cars | Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office. | None | None |
| Motorcycles | Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity. | None | None |
| Planes | Unique, diecast airplane and helicopter replicas suitable for collections, as well as home, office or classroom decorations. Models contain stunning details such as official logos and insignias, rotating jet engines and propellers, retractable wheels, and so on. Most come fully assembled and with a certificate of authenticity from their manufacturers. | None | None |

**Explanation:** Returns all 7 product line categories with descriptions.

---

### Q7: List all payments

**SQL Query:**
```sql
SELECT * FROM payments;
```

**Rows Returned:** 273

**Sample Output:**

| customerNumber | checkNumber | paymentDate | amount |
| --- | --- | --- | --- |
| 103 | HQ336336 | 2004-10-19 | 6066.78 |
| 103 | JM555205 | 2003-06-05 | 14571.44 |
| 103 | OM314933 | 2004-12-18 | 1676.14 |

**Explanation:** Returns all 273 payment records with amounts and dates.

---

### Q8: Get product names and prices

**SQL Query:**
```sql
SELECT "productName", "buyPrice" FROM products;
```

**Rows Returned:** 110

**Sample Output:**

| productName | buyPrice |
| --- | --- |
| 1969 Harley Davidson Ultimate Chopper | 48.81 |
| 1952 Alpine Renault 1300 | 98.58 |
| 1996 Moto Guzzi 1100i | 68.99 |

**Explanation:** Selects only product name and buy price columns from products.

---

### Q9: Get customer names and cities

**SQL Query:**
```sql
SELECT "customerName", city FROM customers;
```

**Rows Returned:** 122

**Sample Output:**

| customerName | city |
| --- | --- |
| Atelier graphique | Nantes |
| Signal Gift Stores | Las Vegas |
| Australian Collectors, Co. | Melbourne |

**Explanation:** Selects customer name and city for all 122 customers.

---

### Q10: List employee first and last names

**SQL Query:**
```sql
SELECT "firstName", "lastName" FROM employees;
```

**Rows Returned:** 23

**Sample Output:**

| firstName | lastName |
| --- | --- |
| Diane | Murphy |
| Mary | Patterson |
| Jeff | Firrelli |

**Explanation:** Returns first and last name of all 23 employees.

---

### Q11: Get all order dates

**SQL Query:**
```sql
SELECT "orderNumber", "orderDate" FROM orders;
```

**Rows Returned:** 326

**Sample Output:**

| orderNumber | orderDate |
| --- | --- |
| 10100 | 2003-01-06 |
| 10101 | 2003-01-09 |
| 10102 | 2003-01-10 |

**Explanation:** Returns order number and order date for all 326 orders.

---

### Q12: Show product vendor list

**SQL Query:**
```sql
SELECT DISTINCT "productVendor" FROM products;
```

**Rows Returned:** 13

**Sample Output:**

| productVendor |
| --- |
| Welly Diecast Productions |
| Motor City Art Classics |
| Classic Metal Creations |

**Explanation:** Returns distinct list of product vendors using DISTINCT keyword.

---

### Q13: Get all product codes

**SQL Query:**
```sql
SELECT "productCode" FROM products;
```

**Rows Returned:** 110

**Sample Output:**

| productCode |
| --- |
| S10_1678 |
| S10_1949 |
| S10_2016 |

**Explanation:** Returns all product codes from the products table.

---

### Q14: List all countries from offices

**SQL Query:**
```sql
SELECT DISTINCT country FROM offices;
```

**Rows Returned:** 5

**Sample Output:**

| country |
| --- |
| USA |
| France |
| Japan |

**Explanation:** Returns distinct countries where offices are located (5 countries).

---

### Q15: Show all order statuses

**SQL Query:**
```sql
SELECT DISTINCT status FROM orders;
```

**Rows Returned:** 6

**Sample Output:**

| status |
| --- |
| Shipped |
| In Process |
| Disputed |

**Explanation:** Returns distinct order status values (6 statuses: Shipped, In Process, etc).

---

### Q16: Get all payment amounts

**SQL Query:**
```sql
SELECT "customerNumber", amount FROM payments;
```

**Rows Returned:** 273

**Sample Output:**

| customerNumber | amount |
| --- | --- |
| 103 | 6066.78 |
| 103 | 14571.44 |
| 103 | 1676.14 |

**Explanation:** Returns customer number and payment amount for all 273 payments.

---

### Q17: List all job titles

**SQL Query:**
```sql
SELECT DISTINCT "jobTitle" FROM employees;
```

**Rows Returned:** 7

**Sample Output:**

| jobTitle |
| --- |
| VP Sales |
| Sales Manager (APAC) |
| Sale Manager (EMEA) |

**Explanation:** Returns distinct job titles across all employees.

---

### Q18: Get customer phone numbers

**SQL Query:**
```sql
SELECT "customerName", phone FROM customers;
```

**Rows Returned:** 122

**Sample Output:**

| customerName | phone |
| --- | --- |
| Atelier graphique | 40.32.2555 |
| Signal Gift Stores | 7025551838 |
| Australian Collectors, Co. | 03 9520 4555 |

**Explanation:** Returns customer name and phone number for all customers.

---

### Q19: Show product MSRP values

**SQL Query:**
```sql
SELECT "productName", "MSRP" FROM products;
```

**Rows Returned:** 110

**Sample Output:**

| productName | MSRP |
| --- | --- |
| 1969 Harley Davidson Ultimate Chopper | 95.70 |
| 1952 Alpine Renault 1300 | 214.30 |
| 1996 Moto Guzzi 1100i | 118.94 |

**Explanation:** Returns product name and MSRP (retail price) for all products.

---

### Q20: List order numbers

**SQL Query:**
```sql
SELECT "orderNumber" FROM orders;
```

**Rows Returned:** 326

**Sample Output:**

| orderNumber |
| --- |
| 10100 |
| 10101 |
| 10102 |

**Explanation:** Returns just the order number column from the orders table.

---

## Part 1B — JOIN Queries (Q21–Q30)

### Q21: Get orders with customer names

**SQL Query:**
```sql
SELECT o."orderNumber", o."orderDate", c."customerName"
            FROM orders o
            JOIN customers c ON o."customerNumber" = c."customerNumber";
```

**Rows Returned:** 326

**Sample Output:**

| orderNumber | orderDate | customerName |
| --- | --- | --- |
| 10100 | 2003-01-06 | Online Diecast Creations Co. |
| 10101 | 2003-01-09 | Blauer See Auto, Co. |
| 10102 | 2003-01-10 | Vitachrome Inc. |

**Explanation:** JOINs orders and customers tables on customerNumber to show order dates with customer names.

---

### Q22: Get employees with office city

**SQL Query:**
```sql
SELECT e."firstName", e."lastName", o.city
            FROM employees e
            JOIN offices o ON e."officeCode" = o."officeCode";
```

**Rows Returned:** 23

**Sample Output:**

| firstName | lastName | city |
| --- | --- | --- |
| Diane | Murphy | San Francisco |
| Mary | Patterson | San Francisco |
| Jeff | Firrelli | San Francisco |

**Explanation:** JOINs employees and offices tables on officeCode to show which city each employee works in.

---

### Q23: Get payments with customer names

**SQL Query:**
```sql
SELECT c."customerName", p.amount, p."paymentDate"
            FROM payments p
            JOIN customers c ON p."customerNumber" = c."customerNumber";
```

**Rows Returned:** 273

**Sample Output:**

| customerName | amount | paymentDate |
| --- | --- | --- |
| Atelier graphique | 6066.78 | 2004-10-19 |
| Atelier graphique | 14571.44 | 2003-06-05 |
| Atelier graphique | 1676.14 | 2004-12-18 |

**Explanation:** JOINs payments and customers tables to show payment amounts alongside customer names.

---

### Q24: Get order details with product names

**SQL Query:**
```sql
SELECT od."orderNumber", p."productName", od."quantityOrdered", od."priceEach"
            FROM orderdetails od
            JOIN products p ON od."productCode" = p."productCode";
```

**Rows Returned:** 2996

**Sample Output:**

| orderNumber | productName | quantityOrdered | priceEach |
| --- | --- | --- | --- |
| 10100 | 1917 Grand Touring Sedan | 30 | 136.00 |
| 10100 | 1911 Ford Town Car | 50 | 55.09 |
| 10100 | 1932 Alfa Romeo 8C2300 Spider Sport | 22 | 75.46 |

**Explanation:** JOINs orderdetails and products tables to show product names, quantities, and prices per order.

---

### Q25: Get products with product line description

**SQL Query:**
```sql
SELECT p."productName", pl."textDescription"
            FROM products p
            JOIN productlines pl ON p."productLine" = pl."productLine";
```

**Rows Returned:** 110

**Sample Output:**

| productName | textDescription |
| --- | --- |
| 1969 Harley Davidson Ultimate Chopper | Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity. |
| 1952 Alpine Renault 1300 | Attention car enthusiasts: Make your wildest car ownership dreams come true. Whether you are looking for classic muscle cars, dream sports cars or movie-inspired miniatures, you will find great choices in this category. These replicas feature superb attention to detail and craftsmanship and offer features such as working steering system, opening forward compartment, opening rear trunk with removable spare wheel, 4-wheel independent spring suspension, and so on. The models range in size from 1:10 to 1:24 scale and include numerous limited edition and several out-of-production vehicles. All models include a certificate of authenticity from their manufacturers and come fully assembled and ready for display in the home or office. |
| 1996 Moto Guzzi 1100i | Our motorcycles are state of the art replicas of classic as well as contemporary motorcycle legends such as Harley Davidson, Ducati and Vespa. Models contain stunning details such as official logos, rotating wheels, working kickstand, front suspension, gear-shift lever, footbrake lever, and drive chain. Materials used include diecast and plastic. The models range in size from 1:10 to 1:50 scale and include numerous limited edition and several out-of-production vehicles. All models come fully assembled and ready for display in the home or office. Most include a certificate of authenticity. |

**Explanation:** JOINs products and productlines tables to show each product with its category description.

---

### Q26: Get customers with sales rep names

**SQL Query:**
```sql
SELECT c."customerName", e."firstName", e."lastName"
            FROM customers c
            JOIN employees e ON c."salesRepEmployeeNumber" = e."employeeNumber";
```

**Rows Returned:** 100

**Sample Output:**

| customerName | firstName | lastName |
| --- | --- | --- |
| Atelier graphique | Gerard | Hernandez |
| Signal Gift Stores | Leslie | Thompson |
| Australian Collectors, Co. | Andy | Fixter |

**Explanation:** JOINs customers and employees tables to show which sales rep manages each customer.

---

### Q27: Get orders with customer city

**SQL Query:**
```sql
SELECT o."orderNumber", o."orderDate", c.city
            FROM orders o
            JOIN customers c ON o."customerNumber" = c."customerNumber";
```

**Rows Returned:** 326

**Sample Output:**

| orderNumber | orderDate | city |
| --- | --- | --- |
| 10100 | 2003-01-06 | Nashua |
| 10101 | 2003-01-09 | Frankfurt |
| 10102 | 2003-01-10 | NYC |

**Explanation:** JOINs orders and customers to show the city of the customer who placed each order.

---

### Q28: Get employees and their manager

**SQL Query:**
```sql
SELECT e."firstName" AS employee, m."firstName" AS manager
            FROM employees e
            LEFT JOIN employees m ON e."reportsTo" = m."employeeNumber";
```

**Rows Returned:** 23

**Sample Output:**

| employee | manager |
| --- | --- |
| Diane | None |
| Mary | Diane |
| Jeff | Diane |

**Explanation:** Self-JOIN on employees table using reportsTo to show each employee paired with their manager.

---

### Q29: Get orderdetails with product vendor

**SQL Query:**
```sql
SELECT od."orderNumber", p."productVendor", od."quantityOrdered"
            FROM orderdetails od
            JOIN products p ON od."productCode" = p."productCode";
```

**Rows Returned:** 2996

**Sample Output:**

| orderNumber | productVendor | quantityOrdered |
| --- | --- | --- |
| 10100 | Welly Diecast Productions | 30 |
| 10100 | Motor City Art Classics | 50 |
| 10100 | Exoto Designs | 22 |

**Explanation:** JOINs orderdetails and products to show vendor name alongside order quantities.

---

### Q30: Get payments with customer country

**SQL Query:**
```sql
SELECT c."customerName", c.country, p.amount
            FROM payments p
            JOIN customers c ON p."customerNumber" = c."customerNumber";
```

**Rows Returned:** 273

**Sample Output:**

| customerName | country | amount |
| --- | --- | --- |
| Atelier graphique | France | 6066.78 |
| Atelier graphique | France | 14571.44 |
| Atelier graphique | France | 1676.14 |

**Explanation:** JOINs payments and customers to show payment amounts grouped with customer country.

---

## Part 1C — GROUP BY and Aggregation (Q31–Q40)

### Q31: Count customers per country

**SQL Query:**
```sql
SELECT country, COUNT(*) AS customer_count
            FROM customers
            GROUP BY country
            ORDER BY customer_count DESC;
```

**Rows Returned:** 28

**Sample Output:**

| country | customer_count |
| --- | --- |
| USA | 36 |
| Germany | 13 |
| France | 12 |

**Explanation:** Groups customers by country and counts how many are in each, ordered by count descending.

---

### Q32: Total payments per customer

**SQL Query:**
```sql
SELECT "customerNumber", SUM(amount) AS total_paid
            FROM payments
            GROUP BY "customerNumber"
            ORDER BY total_paid DESC;
```

**Rows Returned:** 98

**Sample Output:**

| customerNumber | total_paid |
| --- | --- |
| 141 | 715738.98 |
| 124 | 584188.24 |
| 114 | 180585.07 |

**Explanation:** Groups payments by customerNumber and sums the total amount paid per customer.

---

### Q33: Number of orders per status

**SQL Query:**
```sql
SELECT status, COUNT(*) AS order_count
            FROM orders
            GROUP BY status;
```

**Rows Returned:** 6

**Sample Output:**

| status | order_count |
| --- | --- |
| Shipped | 303 |
| In Process | 6 |
| Disputed | 3 |

**Explanation:** Groups orders by status and counts how many orders are in each status category.

---

### Q34: Products per product line

**SQL Query:**
```sql
SELECT "productLine", COUNT(*) AS product_count
            FROM products
            GROUP BY "productLine";
```

**Rows Returned:** 7

**Sample Output:**

| productLine | product_count |
| --- | --- |
| Classic Cars | 38 |
| Trains | 3 |
| Planes | 12 |

**Explanation:** Groups products by productLine and counts how many products belong to each line.

---

### Q35: Employees per office

**SQL Query:**
```sql
SELECT "officeCode", COUNT(*) AS employee_count
            FROM employees
            GROUP BY "officeCode";
```

**Rows Returned:** 7

**Sample Output:**

| officeCode | employee_count |
| --- | --- |
| 6 | 4 |
| 2 | 2 |
| 4 | 5 |

**Explanation:** Groups employees by officeCode and counts staff per office location.

---

### Q36: Total stock per product vendor

**SQL Query:**
```sql
SELECT "productVendor", SUM("quantityInStock") AS total_stock
            FROM products
            GROUP BY "productVendor"
            ORDER BY total_stock DESC;
```

**Rows Returned:** 13

**Sample Output:**

| productVendor | total_stock |
| --- | --- |
| Gearbox Collectibles | 60495 |
| Min Lin Diecast | 50089 |
| Classic Metal Creations | 45408 |

**Explanation:** Groups products by vendor and sums total quantity in stock per vendor.

---

### Q37: Average buy price per product line

**SQL Query:**
```sql
SELECT "productLine", ROUND(AVG("buyPrice"), 2) AS avg_buy_price
            FROM products
            GROUP BY "productLine";
```

**Rows Returned:** 7

**Sample Output:**

| productLine | avg_buy_price |
| --- | --- |
| Classic Cars | 64.45 |
| Trains | 43.92 |
| Planes | 49.63 |

**Explanation:** Groups products by product line and calculates the average buy price for each.

---

### Q38: Orders per customer

**SQL Query:**
```sql
SELECT "customerNumber", COUNT(*) AS order_count
            FROM orders
            GROUP BY "customerNumber"
            ORDER BY order_count DESC;
```

**Rows Returned:** 98

**Sample Output:**

| customerNumber | order_count |
| --- | --- |
| 141 | 26 |
| 124 | 17 |
| 148 | 5 |

**Explanation:** Groups orders by customerNumber and counts how many orders each customer has placed.

---

### Q39: Max MSRP per product line

**SQL Query:**
```sql
SELECT "productLine", MAX("MSRP") AS max_msrp
            FROM products
            GROUP BY "productLine";
```

**Rows Returned:** 7

**Sample Output:**

| productLine | max_msrp |
| --- | --- |
| Classic Cars | 214.30 |
| Trains | 100.84 |
| Planes | 157.69 |

**Explanation:** Groups products by product line and finds the highest MSRP in each category.

---

### Q40: Min buy price per vendor

**SQL Query:**
```sql
SELECT "productVendor", MIN("buyPrice") AS min_buy_price
            FROM products
            GROUP BY "productVendor";
```

**Rows Returned:** 13

**Sample Output:**

| productVendor | min_buy_price |
| --- | --- |
| Welly Diecast Productions | 24.23 |
| Motor City Art Classics | 22.57 |
| Classic Metal Creations | 20.61 |

**Explanation:** Groups products by vendor and finds the lowest buy price offered by each vendor.

---

## Part 1D — Aggregate Functions (Q41–Q50)

### Q41: Total number of customers

**SQL Query:**
```sql
SELECT COUNT(*) AS total_customers FROM customers;
```

**Rows Returned:** 1

**Sample Output:**

| total_customers |
| --- |
| 122 |

**Explanation:** Counts the total number of customer records in the customers table.

---

### Q42: Total number of products

**SQL Query:**
```sql
SELECT COUNT(*) AS total_products FROM products;
```

**Rows Returned:** 1

**Sample Output:**

| total_products |
| --- |
| 110 |

**Explanation:** Counts the total number of products in the products table.

---

### Q43: Total revenue from payments

**SQL Query:**
```sql
SELECT SUM(amount) AS total_revenue FROM payments;
```

**Rows Returned:** 1

**Sample Output:**

| total_revenue |
| --- |
| 8853839.23 |

**Explanation:** Sums all payment amounts to get total revenue of $8,853,839.23.

---

### Q44: Average product price

**SQL Query:**
```sql
SELECT ROUND(AVG("buyPrice"), 2) AS avg_buy_price FROM products;
```

**Rows Returned:** 1

**Sample Output:**

| avg_buy_price |
| --- |
| 54.40 |

**Explanation:** Calculates the average buy price across all products.

---

### Q45: Max payment amount

**SQL Query:**
```sql
SELECT MAX(amount) AS max_payment FROM payments;
```

**Rows Returned:** 1

**Sample Output:**

| max_payment |
| --- |
| 120166.58 |

**Explanation:** Finds the single largest payment amount recorded ($120,166.58).

---

### Q46: Min payment amount

**SQL Query:**
```sql
SELECT MIN(amount) AS min_payment FROM payments;
```

**Rows Returned:** 1

**Sample Output:**

| min_payment |
| --- |
| 615.45 |

**Explanation:** Finds the smallest payment amount recorded ($615.45).

---

### Q47: Count total orders

**SQL Query:**
```sql
SELECT COUNT(*) AS total_orders FROM orders;
```

**Rows Returned:** 1

**Sample Output:**

| total_orders |
| --- |
| 326 |

**Explanation:** Counts the total number of orders placed (326 orders).

---

### Q48: Total quantity in stock

**SQL Query:**
```sql
SELECT SUM("quantityInStock") AS total_stock FROM products;
```

**Rows Returned:** 1

**Sample Output:**

| total_stock |
| --- |
| 555131 |

**Explanation:** Sums quantityInStock across all products to get total inventory.

---

### Q49: Average MSRP

**SQL Query:**
```sql
SELECT ROUND(AVG("MSRP"), 2) AS avg_msrp FROM products;
```

**Rows Returned:** 1

**Sample Output:**

| avg_msrp |
| --- |
| 100.44 |

**Explanation:** Calculates the average MSRP (retail price) across all products.

---

### Q50: Number of employees

**SQL Query:**
```sql
SELECT COUNT(*) AS total_employees FROM employees;
```

**Rows Returned:** 1

**Sample Output:**

| total_employees |
| --- |
| 23 |

**Explanation:** Counts the total number of employees in the company (23 employees).

---

## Summary

| Metric | Value |
| --- | --- |
| Total Questions | 50 |
| Successful Queries | 50 |
| Failed Queries | 0 |
| Success Rate | 100% |
