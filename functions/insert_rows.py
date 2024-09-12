import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,  
    columns_name:str,
    values:str
) -> None:
    """
    Inserts a single row of data into a specified table in an SQLite database.

    Parameters:
    -----------
    database_name : str
        The name of the SQLite database (without the `.db` extension) where the data will be inserted.
    table_name : str
        The name of the table in the database where the row will be inserted.
    columns_name : str
        The names of the columns, separated by commas, where the values will be inserted.
    values : str
        The values to be inserted into the specified columns, provided as a comma-separated string.

    Returns:
    --------
    None
        This function performs an insertion and commits the change to the database but does not return a value.

    Example:
    --------
    insert_one_row('my_database', 'users', 'name, age', "'John Doe', 30")
    """
    database_name = f'{database_name}.db'
    conn = sqlite3.connect(database_name)
    cursor = conn.cursor()

    query = f"""
        INSERT INTO {table_name} ({columns_name})
        VALUES ({values})
    """

    cursor.execute(query)
    conn.commit()
    conn.close()

    return None