import sqlite3

def drop_table(
    database:str,
    table_name:str
) -> None:
    """
    Drops a table from the specified SQLite database.

    Parameters:
    -----------
    database : str
        The name of the SQLite database (without the .db extension) from which to drop the table.
    table_name : str
        The name of the table to be dropped from the database.

    Returns:
    --------
    None
        This function does not return any value. It performs the action of dropping the table.
    """
        
    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(f"""
        DROP TABLE {table_name}         
    """)

    conn.close()