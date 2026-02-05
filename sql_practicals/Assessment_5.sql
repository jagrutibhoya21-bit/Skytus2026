create table users (user_id serial primary key,name varchar(50),email varchar(100) unique,password varchar(100) not null);
create table orders(order_id serial primary key,user_id int,order_date date,amount int,constraint fk_user foreign key (user_id) references users(user_id));
create index idx_users_email on users(email);
create view user_order_summary as select u.user_id,u.name,u.email,count(o.order_id) as total_orders,sum (o.amount) as total_amount from users u left join orders o on u.user_id = o.user_id group by u.user_id,u.name,u.email;
select * from user_order_summary;
insert into user_order_summary (order_id , user_name , product_name, quantity, price , order_date) values (1,'ravi','mobile', 1 ,1500,'2026-02-01'),(2,'neha','laptop',1,55000,'2026-02-02'),(3,'amit','headphones',2,2000,'2026-02-03');
select * from user_order_summary;