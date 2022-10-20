## SQL CRUD

+ INSERT one data where has to be the word 'test' in both username and password columns, and other four free data into the "member" table.
> ![SQL INSERT INTO](3-1.png)       
  
+ Use SELECT to see all data from the "member" table
> ![SQL SELECT](3-2.png)  
  
+ SELECT all data from the "memeber" table and sort them in descending oder by the "time" column.
> ![SQL SELECT BY ORDER](3-3.png)

+ SELECT data 2~4 from the "member" table and sort them by the "time" column in descending order.
> ![SQL SELECT BY ORDER LIMIT OFFSET](3-4.png)

+ SELECT the data where username is 'test' from the "member" table
> ![SQL SELECT WHERE](3-5.png)

+ SELECT the data where both username & passord are 'test'.
> ![SQL SELECT WHERE](3-6.png)

+ UPDATE "test2" on the "name" coloumn whose username is 'test'.
> ![SQL UPDATE](3-7.png)
> ![SQL UPDATE](3-7-1.png)

## SQL Aggregate Functions
#### Update "follower_count" column for later calculation
> ![SQL UPDATE folower_count](4-0.png)

+ How many members in the "member" table?
> ![SQL COUNT](4-1.png)

+ The sum of "follower_count" column in the "member" table.
> ![SQL SUM](4-2.png)

+ The Average of "follower_count" column in the "member" table.
> ![SQL SUM](4-3.png)

## SQL JOIN
+ CREATE "message" table
> ![SQL CREATE TABLE](5-1.png)

+ The "message" table after INSERT some data
> ![SQL SELECT INNER JOIN](5-1-1.png)

+ SELECT members' name and their message content by JOIN the "member" & "message" table.
> ![SQL SELECT INNER JOIN](5-2.png)

+ SELET the name and the content by JOIN the "member" & "message" table ON whose username is "test".
> ![SQL SELECT INNER JOIN](5-3.png)

+ SELECT and JOIN to get the average "like_count" of the username "test".
> ![SQL SELECT INNER JOIN](5-4.png)

