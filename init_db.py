
#connection = sqlite3.connect('userDB.db')

#with open('userSchema.sql') as f:
#    connection.executescript(f.read())

#with open('userReadSchema.sql') as f:
#    connection.executescript(f.read())

#with open('bookSchema.sql') as f:
#    connection.executescript(f.read())
    
#with open('wanttoReasSchema.sql') as f:
#    connection.executescript(f.read())
    
#have this be the user bookshelf instead od 'met'
#with open('metSchema.sql') as f:
#    connection.executescript(f.read())

#connection.close()
import sqlite3

# Connect to SQLite database (creates database.db if it doesn't exist)
conn = sqlite3.connect("database.db")
cur = conn.cursor()

# Create the users table
cur.executescript("""
    DROP TABLE IF EXISTS users;

    CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        firstName TEXT NOT NULL,
        lastName TEXT NOT NULL,
        email TEXT NOT NULL,
        userName TEXT NOT NULL UNIQUE,
        userPW TEXT NOT NULL,
        userWeight FLOAT DEFAULT 0,
        currentBook TEXT,
        userBio TEXT,
        userPhoto BLOB,
        userActive BOOLEAN DEFAULT 1
    );
""")

# Commit and close
conn.commit()
conn.close()

print("Database initialized successfully!")
