/*
a) The information that is included in columns under actor is the actor id,first and last name, and last update.
b) The information that is included in columns under film is film id and title,description,release year, langauge id, og language,rental duration and rate, length, replacement_cost, rating, special feature, and last update.alter
c) The other table in sakila that contains clomuns for both film id and actor id is column film_actor.
d) The information in the rental table is info about the rental process of a film. It has information such as when it was rented, when it was returned, customer id, staff id, invetory id,and last update. I think this table could be hard to read because the date and time is really long and for that looks a lot more 
busy than it really is. Other than just the visualization of the table making it look like a lot I think it is relatively easy to read because all the information is formatted good and the column names match with the data making it easy to find when a film was rented.
f) The tables that you will need to understand the names of all films that were rented on a specific date are film, rental,inventory, customer and payment. I chose film because in this table it has the information of the film id and title of the film which you will need to find what film is being rented. I chose rental because in this
table it has the information on the rental date, inventory id, and customer id. I chose invetory, customer, and payment tables because you can use these to fact check and verify the information is correct on the film and rental tables. For example in the film table you will find the film id and title and go into 
the rental to see what film was rented and what date and you can go into payment, customer, and inventory tables to verify that yes this customer did rent this film and the payment date matches the rental date.
*/

select * from film;
select * from rental;
select * from payment;
select * from inventory;
select * from customer;