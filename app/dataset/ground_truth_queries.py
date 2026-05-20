GROUND_TRUTH = [
    (1,  "List all products",
         "SELECT * FROM products;"),

    (2,  "Get all customers",
         "SELECT * FROM customers;"),

    (3,  "Show all orders",
         "SELECT * FROM orders;"),

    (4,  "List all employees",
         "SELECT * FROM employees;"),

    (5,  "Get all offices",
         "SELECT * FROM offices;"),

    (6,  "Show all product lines",
         "SELECT * FROM productlines;"),

    (7,  "List all payments",
         "SELECT * FROM payments;"),

    (8,  "Get product names and prices",
         'SELECT "productName", "buyPrice" FROM products;'),

    (9,  "Get customer names and cities",
         'SELECT "customerName", city FROM customers;'),

    (10, "List employee first and last names",
         'SELECT "firstName", "lastName" FROM employees;'),

    (11, "Get all order dates",
         'SELECT "orderNumber", "orderDate" FROM orders;'),

    (12, "Show product vendor list",
         'SELECT DISTINCT "productVendor" FROM products;'),

    (13, "Get all product codes",
         'SELECT "productCode" FROM products;'),

    (14, "List all countries from offices",
         "SELECT DISTINCT country FROM offices;"),

    (15, "Show all order statuses",
         "SELECT DISTINCT status FROM orders;"),

    (16, "Get all payment amounts",
         'SELECT "customerNumber", amount FROM payments;'),

    (17, "List all job titles",
         'SELECT DISTINCT "jobTitle" FROM employees;'),

    (18, "Get customer phone numbers",
         'SELECT "customerName", phone FROM customers;'),

    (19, "Show product MSRP values",
         'SELECT "productName", "MSRP" FROM products;'),

    (20, "List order numbers",
         'SELECT "orderNumber" FROM orders;'),

    # ── JOIN queries ───────────────────────────────────────────
    (21, "Get orders with customer names",
         """SELECT o."orderNumber", o."orderDate", c."customerName"
            FROM orders o
            JOIN customers c ON o."customerNumber" = c."customerNumber";"""),

    (22, "Get employees with office city",
         """SELECT e."firstName", e."lastName", o.city
            FROM employees e
            JOIN offices o ON e."officeCode" = o."officeCode";"""),

    (23, "Get payments with customer names",
         """SELECT c."customerName", p.amount, p."paymentDate"
            FROM payments p
            JOIN customers c ON p."customerNumber" = c."customerNumber";"""),

    (24, "Get order details with product names",
         """SELECT od."orderNumber", p."productName", od."quantityOrdered", od."priceEach"
            FROM orderdetails od
            JOIN products p ON od."productCode" = p."productCode";"""),

    (25, "Get products with product line description",
         """SELECT p."productName", pl."textDescription"
            FROM products p
            JOIN productlines pl ON p."productLine" = pl."productLine";"""),

    (26, "Get customers with sales rep names",
         """SELECT c."customerName", e."firstName", e."lastName"
            FROM customers c
            JOIN employees e ON c."salesRepEmployeeNumber" = e."employeeNumber";"""),

    (27, "Get orders with customer city",
         """SELECT o."orderNumber", o."orderDate", c.city
            FROM orders o
            JOIN customers c ON o."customerNumber" = c."customerNumber";"""),

    (28, "Get employees and their manager",
         """SELECT e."firstName" AS employee, m."firstName" AS manager
            FROM employees e
            LEFT JOIN employees m ON e."reportsTo" = m."employeeNumber";"""),

    (29, "Get orderdetails with product vendor",
         """SELECT od."orderNumber", p."productVendor", od."quantityOrdered"
            FROM orderdetails od
            JOIN products p ON od."productCode" = p."productCode";"""),

    (30, "Get payments with customer country",
         """SELECT c."customerName", c.country, p.amount
            FROM payments p
            JOIN customers c ON p."customerNumber" = c."customerNumber";"""),

    # ── GROUP BY + Aggregation ─────────────────────────────────
    (31, "Count customers per country",
         """SELECT country, COUNT(*) AS customer_count
            FROM customers
            GROUP BY country
            ORDER BY customer_count DESC;"""),

    (32, "Total payments per customer",
         """SELECT "customerNumber", SUM(amount) AS total_paid
            FROM payments
            GROUP BY "customerNumber"
            ORDER BY total_paid DESC;"""),

    (33, "Number of orders per status",
         """SELECT status, COUNT(*) AS order_count
            FROM orders
            GROUP BY status;"""),

    (34, "Products per product line",
         """SELECT "productLine", COUNT(*) AS product_count
            FROM products
            GROUP BY "productLine";"""),

    (35, "Employees per office",
         """SELECT "officeCode", COUNT(*) AS employee_count
            FROM employees
            GROUP BY "officeCode";"""),

    (36, "Total stock per product vendor",
         """SELECT "productVendor", SUM("quantityInStock") AS total_stock
            FROM products
            GROUP BY "productVendor"
            ORDER BY total_stock DESC;"""),

    (37, "Average buy price per product line",
         """SELECT "productLine", ROUND(AVG("buyPrice"), 2) AS avg_buy_price
            FROM products
            GROUP BY "productLine";"""),

    (38, "Orders per customer",
         """SELECT "customerNumber", COUNT(*) AS order_count
            FROM orders
            GROUP BY "customerNumber"
            ORDER BY order_count DESC;"""),

    (39, "Max MSRP per product line",
         """SELECT "productLine", MAX("MSRP") AS max_msrp
            FROM products
            GROUP BY "productLine";"""),

    (40, "Min buy price per vendor",
         """SELECT "productVendor", MIN("buyPrice") AS min_buy_price
            FROM products
            GROUP BY "productVendor";"""),

    # ── Aggregate functions ────────────────────────────────────
    (41, "Total number of customers",
         "SELECT COUNT(*) AS total_customers FROM customers;"),

    (42, "Total number of products",
         "SELECT COUNT(*) AS total_products FROM products;"),

    (43, "Total revenue from payments",
         "SELECT SUM(amount) AS total_revenue FROM payments;"),

    (44, "Average product price",
         'SELECT ROUND(AVG("buyPrice"), 2) AS avg_buy_price FROM products;'),

    (45, "Max payment amount",
         "SELECT MAX(amount) AS max_payment FROM payments;"),

    (46, "Min payment amount",
         "SELECT MIN(amount) AS min_payment FROM payments;"),

    (47, "Count total orders",
         "SELECT COUNT(*) AS total_orders FROM orders;"),

    (48, "Total quantity in stock",
         'SELECT SUM("quantityInStock") AS total_stock FROM products;'),

    (49, "Average MSRP",
         'SELECT ROUND(AVG("MSRP"), 2) AS avg_msrp FROM products;'),

    (50, "Number of employees",
         "SELECT COUNT(*) AS total_employees FROM employees;"),
]