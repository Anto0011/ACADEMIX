import mysql.connector
import login_register
from login_register import login_manager
import settings

#Establish connection with database
mydb = mysql.connector.connect(
    host = settings.ht,
    user = settings.user,
    password = settings.pwd,
    database = settings.db
)

# Get the primary key of the course
def guide_key(course_name):
    # Create a cursor
    mycursor = mydb.cursor()

    try:
        # SQL query to select guide_id based on course_name
        sql = "SELECT guide_id FROM Study_guide WHERE course_name = (%s)"
        mycursor.execute(sql, (course_name,))
        result = mycursor.fetchall()

        if result == []:
            return False
        else:
            id = result[0][0]  # type: ignore
            return id

    finally:
        # Close the cursor
        mycursor.close()

def guide_key2(student_id):
    # Create a cursor
    mycursor = mydb.cursor()

    try:
        # SQL query to select guide_id based on course_name
        sql = "SELECT guide_id FROM Study_guide WHERE student_id = (%s)"
        mycursor.execute(sql, (student_id,))
        result = mycursor.fetchall()

        if result == []:
            return False
        else:
            id = result[0][0]  # type: ignore
            return id

    finally:
        # Close the cursor
        mycursor.close()


# Get student primary id using student_name
def get_student_id(name):
    # Create a cursor
    mycursor = mydb.cursor()

    try:
        # Find student id using username
        sql = "SELECT student_id FROM Students WHERE student_name = (%s)"
        mycursor.execute(sql, (name,))
        result = mycursor.fetchall()  # Fetch all the results

        if result != []:
            student_id = result[0][0]  # type: ignore
            return student_id
        else:
            return False

    finally:
        # Close the cursor
        mycursor.close()


def get_existing_topics(username):
    student_id = get_student_id(username)
   
    # Create a cursor object
    mycursor = mydb.cursor()
    try:
        #Fetch existing topics
        sql = "SELECT topic_name FROM Topics WHERE guide_id IN (SELECT guide_id FROM Study_guide WHERE student_id = (%s))"
        mycursor.execute(sql, (student_id,))
        result = mycursor.fetchall()

        #Return the topics if there is any
        if result != []:
            #Extract topics from the results
            topic_names = [topic[0] for topic in result] #type: ignore
            return topic_names
        else:
            return []
    except Exception as e:
        return ("An error occurred:", str(e))
    finally:
        # Close the cursor
        mycursor.close()



#Get existing courses
def get_existing_courses(username):
    student_id = get_student_id(username)
   
    # Create a cursor object
    mycursor = mydb.cursor()
    try:
        #Fetch existing courses
        sql = "SELECT course_name FROM Study_guide WHERE student_id = (%s)"
        mycursor.execute(sql, (student_id,))
        result = mycursor.fetchall()

        #Return the courses if there is any
        if result != []:
            #Extract names from the results
            course_names = [course[0] for course in result] #type: ignore
            return course_names
        else:
            return ("There is no course added yet")
    except Exception as e:
        return ("An error occurred:", str(e))
    finally:
        # Close the cursor
        mycursor.close()



# Add a new course
def add_course(course_name, student_name):
    # Create a cursor object
    mycursor = mydb.cursor()

    # Get student id from username
    student_id = get_student_id(student_name)

    # Check if the same course has already been added by the user
    sql = "SELECT COUNT(*) FROM group1.Study_guide WHERE course_name = (%s) AND student_id = (%s)"
    mycursor.execute(sql, (course_name, student_id))
    result = mycursor.fetchone()

    if result[0] > 0: #type: ignore
        return "This course is already added"
    else:
        sql = "INSERT INTO group1.Study_guide (course_name, student_id) VALUES (%s, %s)"
        mycursor.execute(sql, (course_name, student_id))
        mydb.commit()
        mycursor.close()  # Close the cursor
        return f"{course_name} added to the study guide successfully"

# Add a new topic under a course
def add_topic(course_name, topic_name):
    # Get the primary key of the course
    guide_id = guide_key(course_name)

    # Create a cursor object
    mycursor = mydb.cursor()

    try:
        # Check if the topic already exists
        sql = "SELECT topic_name FROM Topics WHERE guide_id = (%s) AND topic_name = (%s)"
        mycursor.execute(sql, (guide_id, topic_name,))
        result = mycursor.fetchall()

        # Add the topic if it doesn't exist
        if result == []:
            # INSERT the topic into the database with corresponding course foreign key
            sql = "INSERT INTO group1.Topics (guide_id, topic_name) VALUES (%s, %s)"
            mycursor.execute(sql, (guide_id, topic_name))
            mydb.commit()

            # Check if the topic is added successfully
            sql = "SELECT topic_name FROM Topics WHERE topic_name = (%s)"
            mycursor.execute(sql, (topic_name,))
            result = mycursor.fetchall()
            result = result[0][0] #type: ignore
            return result, "has been successfully added to Topics"
        else:
            return "This topic already exists"
    except Exception as e:
        return ("An error occurred:", str(e))
    finally:
        # Close the cursor
        mycursor.close()

# Remove a course and related topics
def remove_course(course_name, name):
    # Get the primary key of the course
    student_id = get_student_id(name)

    # Check if the course exists
    existing_courses = get_existing_courses(name)

    if course_name not in existing_courses:
        return f"Course {course_name} doesn't exist"

    try:
        # Create a cursor
        mycursor = mydb.cursor()

        # Delete the related topics
        sql = "DELETE FROM Topics WHERE guide_id IN (SELECT guide_id FROM Study_guide WHERE student_id = (%s))"
        mycursor.execute(sql, (student_id,))
        mydb.commit()

        # Delete the course
        sql = "DELETE FROM Study_guide WHERE course_name = (%s)"
        mycursor.execute(sql, (course_name,))
        mydb.commit()

        return f"Course {course_name} and related topics have been removed from the study guide"

    except Exception as e:
        return "An error occurred: " + str(e)

    finally:
        # Close the cursor
        mycursor.close() #type: ignore

# Remove a topic under a course
def remove_topic(topic_name, username):
    # Get the primary key of the course
    student_id = get_student_id(username)
    guide_id = guide_key2(student_id)
    print(guide_id)
    try:
        # Check if the topic exists
        existing_topics = get_existing_topics(username)

        if topic_name not in existing_topics:
            return f"Topic {topic_name} doesn't exist"
        else:
            # Create a cursor
            mycursor = mydb.cursor()

            try:
                # DELETE the topic from the database with the corresponding course primary key
                sql = "DELETE FROM Topics WHERE guide_id = (%s) AND topic_name = (%s)"
                mycursor.execute(sql, (guide_id, topic_name))
                mydb.commit()

                return f"Topic {topic_name} has been removed from study guide"

            except Exception as e:
                return "An error occurred: " + str(e)
            finally:
                # Close the cursor
                mycursor.close()

    except Exception as e:
        return "An error occurred: " + str(e)







