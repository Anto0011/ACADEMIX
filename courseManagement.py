import mysql.connector

ht="193.204.40.146"
user="gr1"
pwd="group1#23"
db="group1"

mydb = mysql.connector.connect(
    host = ht,
    user = user,
    password = pwd,
    database = db
)

mycursor = mydb.cursor()

def keys(course_name):
    #Get the primary key of the course
    sql = "SELECT course_id FROM Courses WHERE course_name = (%s)"
    mycursor.execute(sql, (course_name,))
    result = mycursor.fetchall()
    if result == []:
        return False
    else:
        id = result[0][0]
        return id


#Add a new subject
def add_course(name, student_id):
    try:
        sql = "INSERT INTO group1.Courses (course_name) VALUES (%s);"
        mycursor.execute(sql, (name,))
        mydb.commit()
        print(f"{name} added to courses successfully")
    except:
        print("Something went wrong. The universe is a strange place")


#Add a new topic under a subject
def add_topic(course_name, topic_name, student_id):
    #Get the primary key of the course
    id = keys(course_name)

    #Check if the topic already exists
    sql = "SELECT topic_name FROM Topics WHERE course_id = (%s) AND topic_name = (%s) AND Students_student_id = (%s)"
    mycursor.execute(sql, (id, topic_name, student_id))#type: ignore
    result = mycursor.fetchall()

    #Add the topic if it doesn't exist
    if result == []:
        #INSERT the topic into the database with corresponding subject primary key
        sql = "INSERT INTO group1.Topics (course_id, topic_name) VALUES (%s, %s)"
        mycursor.execute(sql, (id, topic_name)) # type: ignore
        mydb.commit()

        #Check if the topic is added successfully
        sql = "SELECT (%s) FROM Topics WHERE course_id = (%s)"
        mycursor.execute(sql, (topic_name, id))#type: ignore
        result = mycursor.fetchall()
        result = result[0][0]
        print(result, "has been successfully added to Topics")
    else:
        print("This topic already exists")


#Remove a subject and related topics
def remove_course(course_name):
    #Get the primary key of the course
    if keys(course_name) != False:
        id = keys(course_name)
        #Delete the subject
        sql = "DELETE FROM Courses WHERE course_name = (%s)"
        mycursor.execute(sql, (course_name,))
        mydb.commit()
        #Delete the related topics
        sql = "DELETE FROM Topics WHERE course_id = (%s)"
        mycursor.execute(sql, (id,))#type: ignore
        mydb.commit()
        print(f"Subject {course_name} and related topics have been removed")
    else:
        print(f"Subject {course_name} doesn't exist")


#Remove a topic under a subject
def remove_topic(course_name, topic_name):
    #Get the primary key of the course
    id = keys(course_name)

    #Check if the topic already exists
    sql = "SELECT topic_name FROM Topics WHERE course_id = (%s) AND topic_name = (%s)"
    mycursor.execute(sql, (id, topic_name))#type: ignore
    result = mycursor.fetchall()

    #Remove the topic if it exists
    if result == []:
       print("This topic doesn't exist")
    else:
        #DELETE the topic from the database with corresponding subject primary key
        sql = "DELETE FROM Topics WHERE topic_name = (%s) AND course_id = (%s)"
        mycursor.execute(sql, (topic_name, id)) # type: ignore
        mydb.commit()

        #Check if the topic is removed successfully
        sql = "SELECT topic_name FROM Topics WHERE topic_name = (%s) AND course_id = (%s)"
        mycursor.execute(sql, (topic_name, id))#type: ignore
        result = mycursor.fetchall()
        print(result)
        #If the topic doesn't exist the operation is successfull
        if result == []:
            print(topic_name, "has been successfully removed from Topics")
        else:
            pass


#Remove all topics under a subject
def remove_all_topics(course_name):
    #Get the primary key of the course
    if keys(course_name) != False:
        id = keys(course_name)
        #Remove all topics from a subject
        sql = "DELETE FROM Topics WHERE course_id = (%s);"
        mycursor.execute(sql, (id,))#type: ignore
        mydb.commit()
        print(f"All topics have been removed from {course_name}")
    else:
        print(f"The subject {course_name} doesn't exist")


