#project 1 Log Analysis by ROAA KORDI

import psycopg2

DBNAME = "news"

def main():
    print('what are the most popular three article of all time?')
    query1 = "SELECT ID,PATH,COUNT(*) AS NUM FROM LOG GROUP BY ID ORDER BY NUM DESC LIMIT 3;"

    Queryf(query1)
    print('what are the most popular Authors of all time?')
    query2 = "SELECT AUTHORS.NAME, COUNT(ARTICLES.AUTHOR) FROM ARTICLES JOIN AUTHORS ON AUTHORS.ID = ARTICLES.AUTHOR GROUP BY AUTHORS.NAME;"
    Queryf(query2)
    print('On which days did more than 1% request lead to errors?')
    query3 = "SELECT TIME,COUNT(*) AS NUM FROM LOG WHERE STATUS = '404 NOT FOUND' GROUP BY TIME,STATUS; "
    Queryf(query3)
#return posts

def Queryf(query):

        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result=c.fetchall()
        print(result ,"-- views")
        return result
 #close connection
        db.close()
#c.execute("Insert into .....  values ('');")
#db.commit()

main()