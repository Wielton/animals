from dbcreds import *
import mariadb

def connect_db():
    conn = None
    cursor = None
    try:
        conn = mariadb.connect(host=host,port=port,database=database,user=user,password=password)
        cursor=conn.cursor()
        return(conn, cursor)
    except mariadb.OperationalError as e: # This will allow to print the exception as it happens
        print("Got an operational error")
        if ("Access Denied" in e.msg):
            print("Failed to log in")
        disconnect_db(conn, cursor)
        
    # if (e.msg.find("Access denied") != -1)
    
def disconnect_db(conn,cursor):
    if(cursor !=None ):
        cursor.close()
    if (conn != None):
        conn.rollback()
        conn.close()

def run_query(statement, args=None):
    try:
        (conn, cursor) = connect_db()
        if statement.startswith("SELECT"):
            cursor.execute(statement, args)
            result = cursor.fetchall()
            print("Total of {} animals".format(cursor.rowcount))
            return result
        elif statement.startswith("POST"):
            if ("CONSTRAINT `animals_CHECK_animal_name`" in e.msg):
                print("Error, animal already exists!")
            else:
                conn.commit()
                print("Query successful")
        elif statement.startswith("UPDATE"):
            cursor.execute(statement, args)
            conn.commit()
            print("Animal successfully updated")
        else:
            cursor.execute(statement, args)
            conn.commit()
            print("Animal successfully deleted from database")
    except mariadb.IntegrityError as e:
        print("Integrity error")
        if ("CONSTRAINT `animals_CHECK_animal_name`" in e.msg):
            print("Error, animal already exists!")
        else:
            print(e.msg)
            
    except mariadb.ProgrammingError as e:
        print(e.msg)

    except RuntimeError as e:
        print(e.msg)
        

    except Exception as e:
        print(e.msg)

    finally:
        disconnect_db(conn,cursor)