#! /usr/bin/env python3
# project1 Log Analysis by ROAA KORDI
import psycopg2

DBNAME = "news"


def main():
    print("Most popular articles:")
    query1 = """\
        SELECT TITLE, PATH, COUNT(PATH) AS NUM
        FROM ARTICLES JOIN AUTHORS ON ARTICLES.AUTHOR = AUTHORS.ID
        JOIN LOG ON LOG.PATH = concat('/article/', ARTICLES.SLUG)
        GROUP BY TITLE, PATH ORDER BY NUM DESC LIMIT 3 ;
    """
    QueryArt(query1)

    print("Most popular Authors:")
    query2 = """\
        SELECT AUTHORS.NAME, COUNT(*) AS NUM
        FROM ARTICLES JOIN AUTHORS ON ARTICLES.AUTHOR = AUTHORS.ID
        JOIN LOG ON LOG.PATH = concat('/article/', ARTICLES.SLUG)
        GROUP BY AUTHORS.NAME ORDER BY NUM DESC;
    """
    QueryAuth(query2)
    print("Days with more than 1% errors:")
    query3 = """\
        SELECT DATE(TIME),ROUND(100.0* SUM(CASE LOG.STATUS
        WHEN '404 NOT FOUND' THEN 1 ELSE 0 END)/COUNT(LOG.STATUS),2) AS PER
        FROM LOG GROUP BY DATE(TIME) ORDER BY PER DESC;
    """
    QueryLog(query3)


def QueryArt(query):

    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    for row in result:
        print ("\t" + row[0] + " - " + str(row[2]) + " views")
    db.close()
    print ("------------------------------")


def QueryAuth(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    for row in result:
        print ("\t" + row[0] + " - " + str(row[1]) + " views")
    db.close()
    print ("------------------------------")


def QueryLog(query):
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result = c.fetchall()
        for row in result:
            if float(row[1]) > 1:
                print("\t" + str(row[0]) +
                      " -- " + str(row[1]) + "% errors")
            pass
        db.close()
        print("------------------------------")


if __name__ == '__main__':
    main()

    # References used in this code:
    # for round function
    # https://stackoverflow.com/questions/36531361/calculate-percentage-between-
    # two-columns-in-sql-query-as-another-column
    # To print the result of SQL in neat way
    # http://www.mikusa.com/python-mysql-docs/row_results.html
    # Also https://thepythonguru.com/fetching-results/
