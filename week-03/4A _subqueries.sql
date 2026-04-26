USE northwind;

/*1.What is the product name(s) of the most expensive products?*/
SELECT ProductName FROM products
WHERE UnitPrice =
	(SELECT MAX(UnitPrice) FROM products);

/*2.What is the product name(s) and categories of the least expensive products?*/
SELECT ProductName,CategoryName FROM products AS p
JOIN categories AS c on p.CategoryID = c.CategoryID	
WHERE UnitPrice =
		(SELECT MIN(UnitPrice) FROM products);

/*3.What is the order id, shipping name and shipping address of all orders shipped via
"Federal Shipping"? */
-- Tables: orders, shippers
SELECT o.orderID, o.ShipName, o.ShipAddress FROM orders as o
WHERE ShipVIa =
	(SELECT ShipperID FROM shippers
    WHERE ShipperID = 3);

/*4.What are the order ids of the orders that included "Sasquatch Ale"?*/
SELECT o.OrderID,ProductName FROM `order details` AS o
JOIN (
	SELECT ProductID, ProductName FROM products
    WHERE ProductID = 34) AS p
ON o.ProductID = p.ProductID;
/*5.What is the name of the employee that sold order 10266?*/
SELECT e.LastName, e.FirstName,o.OrderID FROM employees AS e
JOIN (
	SELECT OrderID, EmployeeID FROM orders 
    WHERE OrderID = 10266 ) AS o
ON e.EmployeeID = o.EmployeeID;

/*6.What is the name of the customer that bought order 10266?*/
SELECT c.CompanyName AS Customer,o.OrderID FROM customers AS c
JOIN (
	SELECT OrderID, CustomerID FROM orders
    WHERE OrderId = 10266) AS o
ON o.CustomerID = c.CustomerID; 

