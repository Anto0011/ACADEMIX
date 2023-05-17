import mysql.connector
import hashlib

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="193.204.40.146",
  user="gr1",
  password="group1#23",
  database="group1"
)

mycursor = mydb.cursor()

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


# Function to register a new user
def register_user(username, email, password):
    
    #Check if the user already exist
    sql = "SELECT * FROM Students WHERE email = (%s)"
    mycursor.execute(sql, (email,))#type: ignore
    result = mycursor.fetchall()

    #Add user if they don't exist
    if result == []:
        try:
            sql = "INSERT INTO Students (student_name, email, password) VALUES (%s, %s, %s)"
            password = sha256_encrypt(password)
            mycursor.execute(sql, (username, email, password))
            mydb.commit()
            return "Registration is successfull"
        except:
            return "Something went wrong"

    #Don't add user and send message
    else:
        message = "This account already exists"
        return message


#User authentication and login
def login_user(email, password):
    #Check if the user exists
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Students WHERE email = (%s) AND password = (%s)"
    password = sha256_encrypt(password)
    mycursor.execute(sql, (email, password,))
    myresult = mycursor.fetchall()

    #If the user exists return student_id
    if myresult != []:
        sql = "SELECT student_id FROM Students WHERE email = (%s)"
        mycursor.execute(sql, (email,))
        result = mycursor.fetchall()
        result = result[0][0]
        return result
    else:
        return False

# Example usage
b = login_user("berkeokur@gmail.com", "berke99")
print(b)



