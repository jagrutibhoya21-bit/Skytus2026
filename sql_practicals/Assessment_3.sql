create table departments(dept_id int primary key,dept_name varchar(50));
create table employees (emp_id int primary key ,emp_name varchar(50),dept_id int,salary int, foreign key (dept_id) references departments(dept_id));
insert into departments values (101,'HR'),(102,'IT'),(103,'finance');
insert into employees values(1,'riya',101,50000),(2,'jiya',102,40000),(3,'kunjal',103,45000),(4,'lalita',null,20000);
select * from departments;
select * from employees;
select e.emp_name,d.dept_name from employees e join departments d on e.dept_id = d.dept_id;
select emp_name,salary from employees where salary > 50000;
select d.dept_name, sum(e.salary) as total_salary from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name;
select d.dept_name, count(e.emp_id) as total_emploees from employees e join departments d on e.dept_id = d.dept_id group by d.dept_name having count(e.emp_id)>2;
select e.emp_name from employees e left join departments d on e.dept_id = d.dept_id where d.dept_id is null;

