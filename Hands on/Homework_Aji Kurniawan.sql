/*create table digitalskola.trx_transactions(
trx_id int primary key,
cust_id int,
prd_id int,
qty int,
price int);

create table digitalskola.ref_customers(
cust_id int primary key,
cust_nm varchar(10)
);

create table digitalskola.ref_products(
prd_id int primary key,
prd_nm varchar(10));

insert into digitalskola.ref_customers (cust_id,cust_nm) values (1,'Marzuq'),(2,'Markus');
insert into digitalskola.trx_transactions(trx_id,cust_id,prd_id,qty,price)
values 
(1,1,1,10,30000),
(2,1,2,20,20000),
(3,1,3,5,10000),
(4,2,1,5,15000),
(5,2,2,5,1000);

insert into digitalskola.ref_products(prd_id,prd_nm)
values
(1,'ABC'),
(2,'XYZ'),
(3,'QWE');*/

/*soal no 1*/
select digitalskola.ref_customers.cust_nm, sum(digitalskola.trx_transactions.qty) as qty
from digitalskola.trx_transactions
inner join digitalskola.ref_customers on digitalskola.ref_customers.cust_id =digitalskola.trx_transactions.cust_id
group by digitalskola.ref_customers.cust_nm;

/*soal no 2*/
select digitalskola.ref_products.prd_nm,sum(digitalskola.trx_transactions.price) as price
from digitalskola.trx_transactions
inner join digitalskola.ref_products on digitalskola.ref_products.prd_id =digitalskola.trx_transactions.prd_id
group by digitalskola.ref_products.prd_nm
having digitalskola.ref_products.prd_nm='ABC';

