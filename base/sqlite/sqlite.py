
import sqlite3
import logging

def main():
    logging.basicConfig(level=logging.DEBUG)
    logging.info("----------------- sqlite work example ------------")

    from sqlite import create, update
    con = sqlite3.connect("testDB.db")

    cursor = con.cursor()

    #create user
    create(cursor)

    print('create user done')

    #update user
    update(cursor)
    print('update user done')







if __name__ == '__main__':
    main()



def create(cur):
   #create table
    try:
        cur.execute("CREATE TABLE USER(ID INT PRIMARY KEY  NOT NULL,  NAME TEXT    NOT NULL,  AGE INT NOT NULL,   ADDRESS CHAR(50),  SALARY REAL)")

    except Exception as err:
        print(err)

    #insert table
    cur.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )")
    cur.execute("INSERT INTO USER (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'John', 50, 'Florida', 5500.50 )")


    res = cur.execute("SELECT * FROM USER")
    result = res.fetchall()

    #print results
    for usr in result:
        print(usr)



def update(cur):
   #update table
    #update user
    try:
        cur.execute("UPDATE USER SET NAME='Tamil', ADDRESS='Chennai' WHERE ID=1")
       
    except Exception as err:
        print(err)

    res = cur.execute("SELECT * FROM USER")
    result = res.fetchall()

    #print results
    for usr in result:
        print(usr)