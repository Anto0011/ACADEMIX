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
def register_user(name, email, password):
    #Check if the user already exist
    sql = "SELECT email FROM Students WHERE email = (%s)"
    mycursor.execute(sql, (email,))#type: ignore
    result = mycursor.fetchall()
    #Add the topic if it doesn't exist
    if result == []:
        sql = "INSERT INTO Students (student_name, email, password) VALUES (%s, %s, %s)"
        mycursor.execute(sql, (name, email, password))
        mydb.commit()

        #Check if the user is added successfully
        sql = "SELECT (%s) FROM Students WHERE email = (%s)"
        mycursor.execute(sql, (email))#type: ignore
        result = mycursor.fetchall()
        result = result[0][0]
        print(result, "has been successfully added to Students")

    else:
        print("record inserted.")

# Function to log in a user
def login_user(email, password):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM Students WHERE email = (%s) AND password = (%s)"
    mycursor.execute(sql, (email, password))
    myresult = mycursor.fetchall()
    if myresult:
        print("Login successful.")
    else:
        print("Invalid email or password.")





