begin;
create table accounts (acc_id int primary key,name varchar(50),balance int);
insert into accounts values (1,'amit',5000);
insert into accounts values (2,'rahul',3000);
insert into accounts values (3,'arjun',7000);
insert into accounts values (4,'parimal',9000);
insert into accounts values (5,'pragnesh',1000);
insert into accounts values (6,'kiran',8000);
insert into accounts values (7,'ansh',6000);
insert into accounts values (8,'priyan',4000);
select * from accounts;
rollback;
commit;
begin;
update accounts set balance = balance - 1000 where acc_id = 1;
update accounts set balance = balance + 1000 where acc_id = 2;
commit;
select * from accounts;
 

