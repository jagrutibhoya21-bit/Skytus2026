select e.emp_name from employees e left join departments d on e.dept_id = d.dept_id where d.dept_id is null;
select emp_name, salary from employees where salary >(select avg (salary)from employees);
select d.dept_name, sum(e.salary) as total_salary from employees e inner join departments d on e.dept_id = d.dept_id group by d.dept_name order by total_salary desc limit 1;
select emp_name,salary from employees where salary =(select distinct salary from employees order by salary desc limit 1 offset 1 );
select emp_name from employees where dept_id = (select dept_id from employees where emp_name = 'jiya');
select * from employees;
select * from departments;