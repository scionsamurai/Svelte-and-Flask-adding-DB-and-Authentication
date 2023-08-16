import psycopg2
from hide import variables

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    dbname=variables.your_database_name,
    user=variables.your_username,
    password=variables.your_password,
    host=variables.your_host,
    port=variables.your_port
)

cursor = conn.cursor()

# Drop the User table if it exists
cursor.execute('DROP TABLE IF EXISTS "User";')

# Create the User table
cursor.execute('CREATE TABLE "User" (username TEXT, password TEXT, email TEXT);')

# Insert a sample user into the User table
cursor.execute("INSERT INTO \"User\" VALUES ('admin', 'test123', 'example@email');")

# Commit the changes
conn.commit()

# Fetch and print the rows where username is 'admin'
cursor.execute('SELECT * FROM "User" WHERE username = %s;', ('admin',))
rows = cursor.fetchall()
print("Rows:", rows)

# Close the cursor and connection
cursor.close()
conn.close()
