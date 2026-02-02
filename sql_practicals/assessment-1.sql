create table students(student_id int,name varchar(50),department varchar(30),year int, marks int);
insert into students values(4,'jiya','IT',1,90),(5,'piya','CSE',1,95),(3,'jinal','brs',1,96);
select * from students;
select name, department from students;
select * from students where marks> 75;
select * from students where department ='CSE';
select * from students order by marks desc;
select name,marks from students order by marks desc limit 3; 
