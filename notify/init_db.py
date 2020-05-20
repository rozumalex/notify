async def create_tables(conn):
    await conn.execute('''
            CREATE TABLE accounts(
                id serial PRIMARY KEY,
                email text UNIQUE,
                password bytea, 
                full_name text,
                phone text,
                registration_date date
            )
        ''')