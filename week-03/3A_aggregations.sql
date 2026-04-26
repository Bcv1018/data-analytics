USE northwind;

/*1)Write a query to find the price of the cheapest item that Northwind sells. Then write a
second query to find the name of the product that has that price.*/
 SELECT MIN(UnitPrice) AS LowestUnitPrice FROM products;
 SELECT 
	 MIN(UnitPrice) AS LowestUnitPrice
	 ,ProductName 
 FROM products
GROUP BY ProductName
ORDER BY LowestUnitPrice
LIMIT 1
;

/*2. Write a query to find the average price of all items that Northwind sells.
(Bonus: Once you have written a working query, try asking Claude or ChatGPT for help
using the ROUND function to round the average price to the nearest cent.)*/
SELECT ROUND(AVG(UnitPrice),2) AS AVG_Items_Price FROM products;

/*3. Write a query to find the price of the most expensive item that Northwind sells. Then
write a second query to find the name of the product with that price, plus the name of
the supplier for that product.*/
SELECT MAX(UnitPrice) AS Highest_Product_Price FROM products;
SELECT 
	  CompanyName
	 ,ProductName
     ,MAX(UnitPrice) AS Highest_Product_Price
FROM products
JOIN suppliers ON products.SupplierID = suppliers.SupplierID
GROUP BY CompanyName, ProductName
ORDER BY Highest_Product_Price DESC
LIMIT 1
;

/*4. Write a query to find total monthly payroll (the sum of all the employees’ monthly
salaries).*/
SELECT ROUND(SUM(Salary),2) FROM employees;

/*5. Write a query to identify the highest salary and the lowest salary amounts which any
employee makes. (Just the amounts, not the specific employees!)*/
SELECT MAX(Salary) AS HighestSalary, MIN(Salary) AS LowestSalary FROM employees;

/*6. Write a query to find the name and supplier ID of each supplier and the number of
items they supply. Hint: Join is your friend here.*/
-- Going to need these tables: Suppliers, products
-- Columns I need: CompanyName SupplierID, ProductName, 
SELECT
	 s.CompanyName
    ,s.SupplierID
    ,Count(p.ProductName) as NumOfItemsSupply
		FROM suppliers as s
JOIN products as p
	ON s.SupplierID = p.SupplierId
GROUP BY CompanyName, SupplierID;

/*7. Write a query to find the list of all category names and the average price for items in
each category.*/
-- Tables I would need for this is categories and products
-- Columns I need are CategoryName,CategoryID,UnitPrice
SELECT 
	 c.CategoryID
    ,c.CategoryName
    ,ROUND(AVG(p.UnitPrice),2) AS AVG_Price
FROM categories as c
JOIN products as p 
	on c.CategoryID = p.CategoryID
GROUP BY CategoryID, CategoryName
;
/*8. Write a query to find, for all suppliers that provide at least 5 items to Northwind, what
is the name of each supplier and the number of items they supply.*/
-- Tables: suppliers, products, 
-- Columnns:CompanyName, ProductName
SELECT 
      s.CompanyName
     ,COUNT(ProductName) AS NumOfItemsSupply
FROM suppliers as s
JOIN products as p
	ON s.SupplierID = p.SupplierID
GROUP BY CompanyName
HAVING NumOfItemsSupply >= 5;

/*9. Write a query to list products currently in inventory by the product id, product name,
and inventory value (calculated by multiplying unit price by the number of units on
hand). Sort the results in descending order by value. If two or more have the same
value, order by product name. If a product is not in stock, leave it off the list.*/
-- Table I need: Products
-- Columns: productID,productName, UnitPrice, UnitsInStock
SELECT 
	 ProductID
    ,ProductName
    ,UnitPrice * UnitsInStock AS InventoryValue 
FROM products
WHERE UnitsInStock > 1
ORDER BY InventoryValue DESC, ProductName
;
