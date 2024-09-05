import sqlite3

def create_table(
    database:str,
    table_name:str,
    columns_desc:str
) -> None:
    """
    Creates a table in the specified SQLite database.

    Parameters:
    -----------
    database : str
        The name of the SQLite database (without the .db extension).
    table_name : str
        The name of the table to be created.
    columns_desc : str
        A string describing the columns and their types (e.g., 'id INTEGER PRIMARY KEY, name TEXT').

    Returns:
    --------
    None
        This function does not return any value. It creates the table if it doesn't exist.
    """

    database = f'{database}.db'

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute(
        f"""CREATE TABLE IF NOT EXISTS {table_name} ({columns_desc})""")

    conn.close()