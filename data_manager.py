import bcrypt
import sql_connection


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    print(hashed_bytes.decode('utf-8'))
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    return bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)


@sql_connection.connection_handler
def registration(cursor, registration, hash):
    cursor.execute("""
        INSERT INTO users (username, password)
        VALUES (%(registration)s, %(hash)s);
        """,
        {'hash': hash, 'registration': registration})


@sql_connection.connection_handler
def login(cursor, username):
    cursor.execute("""
        SELECT password FROM users
        WHERE  username= %(username)s;
        """,
        {'username':username})
    return cursor.fetchall()


@sql_connection.connection_handler
def user_checking(cursor, username):
    cursor.execute("""
            SELECT username FROM users
            WHERE  username= %(username)s;
            """,
            {'username': username})
    return cursor.fetchall()


@sql_connection.connection_handler
def get_id_by_user_name(cursor, username):
    cursor.execute("""
                    SELECT user_id FROM users
                    WHERE username = %(username)s; 
                   """,
                   {'username': username})
    return cursor.fetchone()
