**Introduction**

Academix is a project designed to help university students study more efficiently. It offers a set of features aimed at enhancing the study experience. The main features of Academix include:

•	**Study Guide Creation:** Academix allows users to create a personalized study guide by adding courses of interest.

•	**Question Generation:** With the integration of the OpenAI API, Academix generates practice questions based on the selected study guide courses.

•	**Study Guide Management:** Academix provides functionalities for adding and removing courses from the study guide.

**Installation**

To get started with Academix, follow these steps:

**Prerequisites**

•	Python 3.x installed on your system

•	Access to the OpenAI API (API key required)

•	Access to the Discord API (API key required)

**Step 1: Clone the Repository**
1.	Open a terminal or command prompt.
2.	Navigate to the directory where you want to store the project.
3.	Clone the Academix repository by running the following command:
git clone [https://github.com/berkeokur/Academix]

**Step 2: Set Up the Environment**
1.	Install virtualenv package using pip:

_pip install virtualenv_

OR

_pip3 install virtualenv_

2.	Create a virtual environment for Academix by running the following command in the project's root directory:

**•	Windows:**

_Python3 -m venv env_
	
**•	Mac/Linux:**

_venv env_


3.	Activate the virtual environment:

**•	Windows:**

_env\Scripts\activate_

**• macOS/Linux:**

_source env/bin/activate_


4. Create a folder named _logs_ in the projects root directory



**Step 3: Install Dependencies**
1.	Install the required Python packages by running the following command:

_pip install -r requirements.txt_

OR

_pip3 install -r requirements.txt_




**Step 4: Set Up the .env File**
1.	In the project's root directory, create a file named .env.
2.	Open the .env file in a text editor.
3.	Add the following lines to the file:

DISCORD_API_KEY= <your_api_key>

OPENAI_API_KEY= <your_api_key>

GUILD= <your_guild_id>

ht= <your_hostname>

user= <your_username>

pwd= <your_password>

db= <default_schema>

pwd= <your_password>


**Step 5: Start Academix**

1.	In the terminal or command prompt, ensure that you are still in the project's root directory and the virtual environment is active.
2.	Run the following file inside Visual Studio Code to start Academix:
main.py


**Usage**

Academix provides a set of commands and features to help university students study more efficiently. Here's an overview of the main functionalities:

**Autocompletion**

When entering course or topic names, Academix provides autocompletion suggestions to help you select the correct option. The autocompletion feature will automatically suggest available course and topic names as you type.


**Registering and Logging in**

**Register**

The register command allows you to register your account to the database. You can use the command as follows:

•	_/access register <email> <password>_
	
	
**Login**
	
The login command allows you to use the functionalities of our application. You can use the command as follows:
	
•	_/access login <email> <password>_
	
	
**Course management**
	
Creating a Study Guide
The add_course command allows you to add a course to your study guide. You can use the command as follows:
	
•	_/study_guide add_course <course_name>_

	
**Adding Topics**
	
The add_topic command enables you to add a topic to an existing course in your study guide. Use the command as follows:
	
•	_/study_guide add_topic <course_name> <topic_name>_

	
**Removing Courses and Topics**
	
You can remove a course from your study guide using the remove_course command:
	
•	_/study_guide remove_course <course_name>_

	
To remove a topic from a course, use the remove_topic command:
	
•	_/study_guide remove_topic <course_name> <topic_name>_

	
**Generating Questions**
	
The generate_question command generates a question based on the specified course, topic, and difficulty level. Here's how to use the command:
	
•	_/gpt generate_question <course_name>  <topic_name>  <difficulty_level>_

	
**Asking GPT**
	
The ask_gpt command allows you to ask a question to the GPT model. Temperature is the creativity of GPT and it takes a value between 0 and 1(default=0.5). Here's an example of how to use it:
	
•	_/gpt ask_gpt <your_question> <temperature>_
	
	
