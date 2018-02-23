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