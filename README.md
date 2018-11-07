# Log Analysis Project
This project uses psycopg2 database by Python to run three reports.

# Getting Started
To start on this project, you'll need database software (provided by a Linux virtual machine) and the data to analyze load it using newsdata.sql file by putting this file into the vagrant directory.

# Prerequisites
To load the data, cd into the vagrant directory and use the command:
psql -d news -f newsdata.sql
Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data.
Connect to your database using 
psql -d news
Explore the tables using the \dt and \d table commands and select statements in your terminal.
The database called news includes three tables:

The authors table includes information about the authors of articles.
The articles table includes the articles themselves.
The log table includes one entry for each time a user has accessed the site.

Examples:
news=# \dt
             List of relations
 Schema |   Name   | Type  |     Owner
--------+----------+-------+---------------
 public | articles | table | Administrator
 public | authors  | table | Administrator
 public | log      | table | Administrator
(3 rows)


news=# \d articles
                                     Table "public.articles"
 Column |           Type           | Collation | Nullable |               Defaul
t
--------+--------------------------+-----------+----------+---------------------
-----------------
 author | integer                  |           | not null |
 title  | text                     |           | not null |
 slug   | text                     |           | not null |
 lead   | text                     |           |          |
 body   | text                     |           |          |
 time   | timestamp with time zone |           |          | now()
 id     | integer                  |           | not null | nextval('articles_id
_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


news=# \d authors
                            Table "public.authors"
 Column |  Type   | Collation | Nullable |               Default
--------+---------+-----------+----------+-------------------------------------
 name   | text    |           | not null |
 bio    | text    |           |          |
 id     | integer |           | not null | nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFE
RENCES authors(id)


news=# \d log
                                     Table "public.log"
 Column |           Type           | Collation | Nullable |             Default

--------+--------------------------+-----------+----------+---------------------
------------
 path   | text                     |           |          |
 ip     | inet                     |           |          |
 method | text                     |           |          |
 status | text                     |           |          |
 time   | timestamp with time zone |           |          | now()
 id     | integer                  |           | not null | nextval('log_id_seq'
::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

# Installing
This project uses Linux-based virtual machine (VM) you can download it and install it from this website
https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
you need to install vagrant you can download it and install it from this website
https://www.vagrantup.com/downloads.html
you need to bring the virtual machine back online (with vagrant up), do so now. Then log into it with vagrant ssh.
Put newsdata.sql file into the vagrant directory.
Download the SourceCode.py file.
To load the data, cd into the vagrant directory and use the command psql -d news -f newsdata.sql.
you could use the following command into your terminal to connect you with the news database and it will ask you about your password
$ psql -d news
Password:
Enter your password then tou are going to be connected with news database.
Explore the tables using the \dt and \d table commands and select statements in your terminal gitbash
Examples:
news=# \dt
             List of relations
 Schema |   Name   | Type  |     Owner
--------+----------+-------+---------------
 public | articles | table | Administrator
 public | authors  | table | Administrator
 public | log      | table | Administrator
(3 rows)


news=# \d articles
                                     Table "public.articles"
 Column |           Type           | Collation | Nullable |               Defaul
t
--------+--------------------------+-----------+----------+---------------------
-----------------
 author | integer                  |           | not null |
 title  | text                     |           | not null |
 slug   | text                     |           | not null |
 lead   | text                     |           |          |
 body   | text                     |           |          |
 time   | timestamp with time zone |           |          | now()
 id     | integer                  |           | not null | nextval('articles_id
_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)


news=# \d authors
                            Table "public.authors"
 Column |  Type   | Collation | Nullable |               Default
--------+---------+-----------+----------+-------------------------------------
 name   | text    |           | not null |
 bio    | text    |           |          |
 id     | integer |           | not null | nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFE
RENCES authors(id)


news=# \d log
                                     Table "public.log"
 Column |           Type           | Collation | Nullable |             Default

--------+--------------------------+-----------+----------+---------------------
------------
 path   | text                     |           |          |
 ip     | inet                     |           |          |
 method | text                     |           |          |
 status | text                     |           |          |
 time   | timestamp with time zone |           |          | now()
 id     | integer                  |           | not null | nextval('log_id_seq'
::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)

# Running the tests and Deployment
To run this project using your Git Bash terminal, you need to type this command to point inot your directory that it has the SourceCode.py file
$ cd '<yourDirectory>'

then, you could run the Python source code by:
$ python SourceCode.py
the output will shown up as the following:
____________________________________________________________________

 Top 3 popular articles are:

"Candidate is jerk, alleges rival" -- 338647 views
"Bears love berries, alleges bear" -- 253801 views
"Bad things gone, say good people" -- 170098 views


 The most popular article authors of all time are:

Ursula La Multa -- 507594 views
Rudolf von Treppenwitz -- 423457 views
Anonymous Contributor -- 170098 views
Markoff Chaney -- 84557 views


 Day did more than 1% of requests lead to errors:

JUL 17,2016 -- 2.25 % errors

____________________________________________________________________

If you would like to ceate an output file for this project, just type this command:
$ python SourceCode.py > output.log
you are going to see the output as the output.log file.

You can do a quick check using the pep8 command-line tool, you need to install it by 
$ pip install pep8
in the terminal type the following to check each error
$ pep8 --show-source --show-pep8 SourceCode.py

# Built With
Git Bash
pgAdmin 4 
virtual machine
vagrant
Sublime Text editor

# Authors
HADIL SALEH ALSUDIES

# Acknowledgments
All the activities we have done during the virtual session by: MS. MASHAEL ELSAEEDI helped me, Thank you MS. MASHAEL.