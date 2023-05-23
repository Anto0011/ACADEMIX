import mysql.connector
import hashlib
import settings

#Create a login manager
class LoginManager:
    def __init__(self):
        self.login_states = {}  # Dictionary to store login states

    #Login user
    def login(self, user_id):
        self.login_states[user_id] = True

    #Logout user
    def logout(self, user_id):
        self.login_states[user_id] = False

    #Check if user is logged in
    def is_logged_in(self, user_id):
        return self.login_states.get(user_id, False)

# Create an instance of LoginManager
login_manager = LoginManager() 

# Connect to the MySQL database
mydb = mysql.connector.connect(
    host = settings.ht,
    user = settings.user,
    password = settings.pwd,
    database = settings.db
)

#Sha256 encryption
def sha256_encrypt(text):
    # Create a SHA-256 hash object
    sha256_hash = hashlib.sha256()

    # Convert the input text to bytes
    text_bytes = text.encode('utf-8')

    # Update the hash object with the input bytes
    sha256_hash.update(text_bytes)

    # Get the encrypted hash in hexadecimal format
    encrypted_hash = sha256_hash.hexdigest()

    # Return the encrypted hash
    return encrypted_hash

#Define register function
def register_user(username, email, password):

    # Create a cursor object
    mycursor = mydb.cursor()

    try:
        # Check if the user already exists
        sql = "SELECT * FROM Students WHERE email = %s"
        mycursor.execute(sql, (email,))
        result = mycursor.fetchall()

        # Add user if they don't exist
        if not result:
            sql = "INSERT INTO Students (student_name, email, password) VALUES (%s, %s, %s)"
            password = sha256_encrypt(password)
            mycursor.execute(sql, (username, email, password))
            mydb.commit()
            return "Registration is successful"

        # Don't add user and return response
        else:
            message = "This account already exists"
            return message
    except Exception as e:
        return ("An error occurred:", str(e))
    finally:
        # Close the cursor
        mycursor.close() #type: ignore

#Define login function
def login_user(email, password):
    # Create a cursor object
    mycursor = mydb.cursor()

    try:
        # Check if the user exists
        sql = "SELECT * FROM Students WHERE email = (%s) AND password = (%s)"
        password = sha256_encrypt(password)
        mycursor.execute(sql, (email, password,))
        myresult = mycursor.fetchall()

        # If the user exists, return True
        if myresult != []:
            return True
        else:
            return False
    finally:
        # Close the cursor
        mycursor.close()






