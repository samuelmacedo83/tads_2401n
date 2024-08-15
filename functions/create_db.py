import sqlite3

def create_db(  
    database_name:str      
) -> sqlite3.Connection:
    """
    Creates a SQLite database with the specified name and returns 
    a connection to it.

    Args:
        database_name (str): The name of the database to create. The function 
            will append '.db' to this name to create the SQLite database file.

    Returns:
        sqlite3.Connection: A connection object to the newly created 
            SQLite database.
    """

    return sqlite3.connect(f'{database_name}.db')
