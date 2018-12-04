# UD-FSND Project1 

### Project Description

In This project we are dealing with the database  of a newspaper site that contains three main tables: Authors, Articles and log.
we have been asked to build an internal reporting tool to now what's the best articles and authors based on the pages visit that are stated in the log table. To do this task, we (me and other students) have been asked to use python programming language and run the program in the terminal.

For the database part, this project use postegre SQL database in connection in python code file. 


### Dependencies/Pre-requisties 

To start working on the project you will need to have the following folder which include the data you will work on  (newsdata.sql) which we will use mainly for this project.
* you can download the zip folder [here](https://www.dropbox.com/sh/du5qa4euumn5f91/AADTNHXNih8QVjGEoyMwvSjUa?dl=0)

### The python role with Database

The python file (project_log_roaa.py) is the main file in this project. From it we can deal with the database.  It has the connection code to the database and include the DB queries that fetch the information needed to answere these three questions:

1. What are the most popular three article of all time?

2. What are the most popular Authors of all time?

3. On which days did more than 1% requests lead to errors?


so basically the python file process three different queries.


### Setup / installation Guide

you will need to download the following:

1. Git bash ( https://git-scm.com/downloads) for windows, for Mac or Linux systems, you can use the
built-in Terminal.

2. Pyhton 3: (https://www.python.org)

3. Psycopg2 v2.7.5:   (http://initd.org/psycopg/download/) 

4. PostgreSQL v9.5.14:  (https://www.postgresql.org/download/)

5. Vagrant: (https://www.vagrantup.com/downloads.html)

6. Virtual Machine v5.1.38: (https://www.virtualbox.org/wiki/Downloads)
 


### Usage and instructions


to use and test the project to see the outputs follow these instructions:

1. Open the Git bash termninal.

2. type command: cd [your folder name]   

 *Your folder should include the vagrant folder(that includes vagrant VM) inorder to work on vagrant 
Commands*

3. Now go to vagrant folder: cd vagrant

4. Run command: vagrant up

5. Then run: vagrant ssh

6. Go again to vagrant folder: cd /vagrant

7. run the python file(project with the following command: python3 project_log_roaa.py

*Please note that the python file should be in the same folder with vagrant vm folder and newsdata.sql*


### Project output

The output should be as following:


Most popular articles:

        - Candidate is jerk, alleges rival - 338647 Views
        
        - Bears love berries, alleges bear - 253801 Views
        
        - Bad things gone, say good people - 170098 Views



Most popular authors:

       -  Ursula La Multa - 507594 views
       
       -  Rudolf von Treppenwitz - 423457 views
       
       -  Anonymous Contributor - 170098 views
       
       -  Markoff Chaney - 84557 views



Days with more than 1% errors:

        - 2016-07-17 ---> 2.26 %




##### To view the news database

1- First load the data from the sql file:

psql -d news -f newsdata.sql

2- Then connect to the database:

psql -d news

3- To view all DB tables type:

\dt

4- To see table details type:

\d log

*log is a table name in the news database*


### known issues

* To exist the postegreSQL database: ctrl + C
* To exist Vagrant : ctrl + D

### Future plans 

The code could be reused with different SQL database and different quires to fetch information from database.

### Lisence 
This code belong to the author of this github profile. for any inquires please email: roaak2009@gmail.com









