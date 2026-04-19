USE northwind;


-- 4) a) The name of the table that holds the items Northwind sells is the Products Table 
-- b) The name of the table that holds the types/categories of the items Northwind sells is the Categories Table

SELECT * FROM northwind.employees;
-- 5) The Northwind employee whose name makes it look like she's a bird is Margaret Peacock

SELECT * FROM northwind.products;
-- 6) a) The records that my query returned was 77. You can use the dropdown menu where it says Limit to * rows and you can choose from 10 to 50,000.
-- b) SELECT * FROM northwind.products LIMIT 10; I asked this question in google but it didn't give me exactly this script, it gave me options using limit and other various commands I can use, but I decided to just try adding LIMIT to the end of the select query with a number and bang it works.

SELECT * FROM northwind.categories;
-- 7) The category id of seafood is 8


-- 8) 
SELECT OrderID, OrderDate,ShipName,ShipCountry FROM orders LIMIT 50;
