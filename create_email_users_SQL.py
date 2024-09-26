import mysql.connector, hashlib


######## CREATE NEW VIRTUAL MAILBOX USERS AND INSERT THEM INTO A SQL DATABASE

# Create the mail user

username = input('Enter your username: ')
fullname = input('Enter your full name: ')
domains = ['VIRTUAL_DOMAIN_1', 'VIRTUAL_DOMAIN_2']
print(dict(enumerate(domains)))
domain_number = int(input('Choose domain number: '))
domain = domains[domain_number]
password = hashlib.md5(input('Enter your password: ').encode()).hexdigest()
userid = f'{username}@{domain}'

domains_id = {
    'VIRTUAL_DOMAIN_1': (5000, 5000),
    'VIRTUAL_DOMAIN_2': (5001, 5001)
}

uid = domains_id[domain][0]
gid = domains_id[domain][1]
maildir = f'/{domain}/{username}/Maildir/'
data = (username, domain, password, 1, 1, userid, uid, gid, maildir)

### DATABASE OPS

# Define connection parameters
config = {
    'user': 'USERNAME',
    'password': 'PASSWORD',
    'host': 'DB_SERVER',
    'database': 'DATABASE',
    'port': 3306
}

# Create a connection to the MySQL database
conn = mysql.connector.connect(**config)

# Create a cursor to interact with the database
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT DATABASE();")

# Fetch the result of the query
db_name = cursor.fetchone()
print(f"Connected to database: {db_name}")

query = """
    INSERT INTO virtual_users (username, domain, password, auth, active, userid, uid, gid, home)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
"""

cursor.execute(query, data)
conn.commit()

query = "SELECT * FROM virtual_users WHERE username = %s;"

cursor.execute(query, (username,))
results = cursor.fetchall()

print(f"User {username} successfully inserted in table\n", results)

# Close the cursor and connection
cursor.close()
conn.close()
