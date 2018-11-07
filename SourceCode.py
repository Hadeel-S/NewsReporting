#  By Hadil Alsudies
#  !/usr/bin/env python3

import psycopg2


def query1(db):
    # Runs the first query and prints it
    c1 = db.cursor()
    c1.execute("""SELECT A.title AS ArticleName, count(log.logSlug)  AS views
    FROM articles A, (SELECT regexp_replace(log.path, '^.+[/\\\]','')
    AS logSlug FROM log) AS log
    WHERE A.slug = log.logSlug GROUP BY A.title ORDER BY views desc LIMIT 3
    """)
    print(" Top 3 popular articles are: "+"\n")
    while True:
        row = c1.fetchone()
        if row is None:
            break
        print("\""+row[0]+"\" -- "+str(row[1])+" views"+"\t\t")


def query2(db):
    # Runs the second query and prints it
    c2 = db.cursor()
    c2.execute("""SELECT authors.name AS AuthorName,
    count(log.logSlug) AS views FROM articles A, authors,
    (SELECT regexp_replace(log.path, '^.+[/\\\]','') AS logSlug FROM log)
    AS log WHERE A.slug = log.logSlug AND A.author = authors.id
    GROUP BY authors.name ORDER BY views desc
    """)
    print("\n\n"+" The most popular article authors of all time are:  "+"\n")
    while True:
        row = c2.fetchone()
        if row is None:
            break
        print(row[0]+" -- "+str(row[1])+" views"+"\t\t")


def query3(db):
    # Runs the third query and prints it
    c3 = db.cursor()
    c3.execute("""SELECT dates, ErrorStatus
    FROM (SELECT to_char(time,'MON DD,YYYY') AS dates,
    ROUND(SUM(CASE WHEN CAST(substring(status,1,1) AS INTEGER)
    IN (4,5) THEN 1 ELSE 0 END) * 100.0 / COUNT(to_char(time,'MON DD,YYYY')),2)
    AS ErrorStatus FROM log
    GROUP BY DATES) AS DateByError WHERE ErrorStatus >= 1
    """)
    print("\n\n"+" Day did more than 1% of requests lead to errors:   "+"\n")
    while True:
        row = c3.fetchone()
        if row is None:
            break
        print(row[0]+" -- "+str(row[1])+" % errors"+"\t\t")


def myquestions():
    # Runs all 3 queries functions
    db = None
    try:
        db = psycopg2.connect('dbname=news user=postgres password=123')
        query1(db)
        query2(db)
        query3(db)
    except psycopg2.DatabaseError:
        print("<error message>")


def main():
    # Runs a function that prints out the results of 3 questions: Q1, Q2 and Q3
    myquestions()

if __name__ == "__main__":
    main()
