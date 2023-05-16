import mysql.connector


# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="193.204.40.146",
  user="gr1",
  password="group1#23",
  database="group1"
)

mycursor = mydb.cursor()

# Function to register a new user
def register_user(username, email, password):
    #Check if the user already exist
    sql = "SELECT * FROM Students WHERE email = (%s)"
    mycursor.execute(sql, (email,))#type: ignore
    result = mycursor.fetchall()
    #Add user if they don't exist
    if result == []:
        sql = "INSERT INTO Students (student_name, email, password) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (username, email, password))
        mydb.commit()

        #Check if the user is added successfully
        sql = "SELECT (%s) FROM Students WHERE email = (%s)"
        mycursor.execute(sql, (email))#type: ignore
        result = mycursor.fetchall()
        result = result[0][0]
        message = "Registration Successfull"
        return message
    else:
        message = "This account already exists"
        return message

def login_user(email, password):
    #Check if the user exists
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Students WHERE email = (%s) AND password = (%s)"
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

# Function to log in a user
session_id = login_user("berkeokur99@gmail.com", "berke99")

# Example usage
b = login_user("berkeokur99@gmail.com", "berke99")
print("session id = ", session_id)



