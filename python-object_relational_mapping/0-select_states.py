#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa.

The script takes 3 arguments: MySQL username, mysql password and database name.
it connects to a MySQL server running on localhost at port 3306.
Results are sorted in ascending order by states.id
"""
import MySQLdb
import sys
 
def list_states():
    """ connects to the database and prints all sates.
    thi function retrives all records from the 'states' table of the specified database and prints them to the standard output.
    Args:
    username (str): The MySQL username provided as the first argument.
    password (str): The MySQL password provided as the second argument.
    db_name (str): The database name provided as the third argument.

    Returns:
    None
    """
    #Accessing command line arguments
    user = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    try:
        #Establishes connections to the MySQL server
        conn = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=user,
                passwd=passwd
                db=db
                )
        #Create a cursor object to excute Sql queries
        cursor = conn.cursor()

        #Excute the SQL command to fetch all states ordered by id
        cursor.excute("SELECT * FROM states ORDER BY id ASC")

        #Fetch all the rows from the excuted query
        query_rows = cursor.fetchall()

        #Display the results
        for row in query_rows:
            print(row)

        #close the cursor and the connection
        cursor.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

        if _name_ == "_main_" :
        """
        Prevents the script from being excuted when imported.
        Only runs when called directly.
        """
     if len(sys.argv) == 4:
         list_states()
