
create table Employees
(id integer not null, 
Name VARCHAR(100) not null, 
Salary integer not null, 
manager_id integer);

insert into Employees (id,Name,Salary,manager_id) VALUES 
(1,'John',300,3), 
(2,'Mike',200,3), 
(3,'Sally',550,4),
(4,'Jane',500,7),
(5,'Joe',600,7),
(6,'Dan',600,3),
(7,'Phil',550,NULL);

//part a

select
     a.NAME as Employees
from Employee as a JOIN Employee as b
     on a.ManagerId = b.Id
     and a.Salary > b.Salary
;

//part b

select AVG(t1.salary) as AVG_SALARY
from Employees as t1
LEFT JOIN Employees t2 on t1.id=t2.manager_id
where t2.id is NULL;
