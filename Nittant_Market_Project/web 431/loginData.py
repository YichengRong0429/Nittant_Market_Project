import csv
import sqlite3 as sql
link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Users(email char(30) primary key NOT NULL, password char(35) NOT NULL);')
infor=csv.reader(open("Users.csv"))
insert='INSERT INTO Users (email,password) values (?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Buyers(emailBuyer char(30) primary key NOT NULL, first_name char(20), last_name char(20), gender char(9), age integer, home_address_id text, billing_address_id text);')
infor=csv.reader(open("Buyers.csv"))
insert='INSERT INTO Buyers (emailBuyer, first_name, last_name, gender, age, home_address_id, billing_address_id) values (?,?,?,?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Sellers(emailSeller char(30) primary key NOT NULL, routing_number char(20), account_number char(20), balance integer);')
infor=csv.reader(open("Sellers.csv"))
insert='INSERT INTO Sellers (emailSeller, routing_number, account_number, balance) values (?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Address(address_ID text primary key NOT NULL, zipcode char(20), street_num text, street_name text);')
infor=csv.reader(open("Address.csv"))
insert='INSERT INTO Address (address_ID, zipcode, street_num, street_name) values (?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Zipcode_Info(zipcode text primary key NOT NULL, city char(20), state_id text, population text, density text, county_name text, timezone text);')
infor=csv.reader(open("Zipcode_Info.csv"))
insert='INSERT INTO Zipcode_Info (zipcode, city, state_id, population, density, county_name, timezone) values (?,?,?,?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Credit_Cards(credit_card_num text primary key NOT NULL, card_code text, expire_month text, expire_year text, card_type text, Owner_email text);')
infor=csv.reader(open("Credit_Cards.csv"))
insert='INSERT INTO Credit_Cards (credit_card_num, card_code, expire_month, expire_year, card_type, Owner_email) values (?,?,?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Categories(parent_category text,category_name text primary key NOT NULL);')
infor=csv.reader(open("Categories.csv"))
insert='INSERT INTO Categories (parent_category, category_name) values (?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Product_Listing(Seller_Email, Listing_ID integer NOT NULL,Category char(20), Title text, Product_Name text, Product_Description text, Price text, Quantity text);')
infor=csv.reader(open("Product_Listing.csv"))
insert='INSERT INTO Product_Listing (Seller_Email, Listing_ID, Category, Title, Product_Name, Product_Description, Price,Quantity) values (?,?,?,?,?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('create table Local_Vendors(Email text primary key NOT NULL, Business_Name text,Business_Address_ID text, Customer_Service_Number text);')
infor=csv.reader(open("Local_Vendors.csv"))
insert='INSERT INTO Local_Vendors (Email, Business_Name, Business_Address_ID, Customer_Service_Number) values (?,?,?,?)'
point.executemany(insert,infor)
link.commit()
link.close()

link=sql.connect("account.db")
point=link.cursor()
point.execute('alter table Product_Listing add column chekP integer default 1;')
point.execute("select * from Product_Listing")
data = point.fetchall()
for rown in  data:
    print(rown)
link.commit()
link.close()