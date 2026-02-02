
select count(*) as total_students from students;
select  avg(marks) as average_marks from students;
select max(marks) as highest_marks,min(marks) as lowest_marks from students;
select department, avg (marks) as average_marks from students group by department;
select department , avg (marks) as average_marks from students group by department having avg(marks) > 70;

