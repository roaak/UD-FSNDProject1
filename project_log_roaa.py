#! /usr/bin/env python3

#project 1 Log Analysis by ROAA KORDI

import psycopg2

DBNAME = "news"

def main():
    print('Most popular articles :')
    query1 = '''
     SELECT TITLE, PATH, COUNT(PATH) AS NUM 
     FROM ARTICLES JOIN AUTHORS ON ARTICLES.AUTHOR = AUTHORS.ID JOIN LOG ON LOG.PATH = concat('/article/', ARTICLES.SLUG) 
     GROUP BY TITLE, PATH ORDER BY NUM DESC LIMIT 3 ; 
     '''
        
     #SELECT ID,PATH,COUNT(*) AS NUM FROM LOG GROUP BY ID ORDER BY NUM DESC LIMIT 3;
    QueryArt(query1)

    print('Most popular Authors:')
    query2 = ''' 
    SELECT AUTHORS.NAME, COUNT(*) AS NUM FROM ARTICLES 
    JOIN AUTHORS ON ARTICLES.AUTHOR = AUTHORS.ID 
    JOIN LOG ON LOG.PATH = concat('/article/', ARTICLES.SLUG) 
     GROUP BY AUTHORS.NAME ORDER BY NUM DESC;'''
    #SELECT AUTHORS.NAME, COUNT(ARTICLES.AUTHOR) FROM ARTICLES JOIN AUTHORS ON AUTHORS.ID = ARTICLES.AUTHOR GROUP BY AUTHORS.NAME;
    QueryAuth(query2)


    print('Days with more than 1% errors:')
    query3 = '''
        SELECT DATE(TIME),ROUND(100.0* SUM(SELECT COUNT(LOG.STATUS) WHERE STATUS = '404 NOT FOUND'
        THEN 1 ELSE 0 END)/COUNT(LOG.STATUS),2) AS PER
        FROM LOG 
        GROUP BY DATE(TIME)
        ORDER BY PER DESC;
        '''
    #SELECT TIME,COUNT(*) AS NUM FROM LOG WHERE STATUS = '404 NOT FOUND' GROUP BY TIME,STATUS;
    # SELECT DATE(TIME),COUNT(STATUS) AS NUM FROM LOG WHERE STATUS = '404 NOT FOUND' GROUP BY DATE(TIME) ORDER BY NUM DESC;  
    
    QueryLog(query3)
#return posts

def QueryArt(query):

        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result=c.fetchall()
        for row in result :
                print ("\t"  + row[0] + " - " + str(row[2]) + " Views")      
 #close connection
        db.close()
        print ('---------------------------------------------------------------')
#c.execute("Insert into .....  values ('');")
#db.commit()

def QueryAuth(query):
    
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result=c.fetchall()
        for row in result :      
          print("\t"  + row[0] + " - " + str(row[1]) + " views")
        db.close()
        print ('---------------------------------------------------------------')


def QueryLog(query):
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        result=c.fetchall()
    # prints_pattern.stars_repeater()
        for row in result:
                if float(row[1]) > 1:
                  print('\t' + str(row[0]) + ' -- ' + str(row[1]) + ' % errors')
                pass
        db.close()
print ('---------------------------------------------------------------')
   
if __name__ == '__main__':
   main()