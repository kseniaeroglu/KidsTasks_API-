# KidTasks API - Chore & Star Tracker

KidTasks is a simple Flask-based API designed to help manage daily tasks for kids and reward them with stars for completed chores. It connects to a MySQL database and supports viewing tasks, adding tasks, completing them (which awards stars), and viewing stars summary.

📁 Project Structure
KidsTasks.sql - SQL Database
config.py - Stores database credentials
db_utils.py - Handles DB connections and SQL operations
app.py - Flask API with endpoints
main.py - Client side to interact with the API
🔢 Step by step users guide
Create a Database in MySQLWorkbench using this file
KidsTasks.sql
In terminal install required libraries
pip install mysql-connector-python
pip install flask
pip install requests
In config.py file in PyCharm or VS enter your correct details for USER, PASSWORD, HOST and the name of DATABASE will be "KidTasks"

Run db_utils.py

Run app.py

Run main.py You will be able to:

Add a new task or use defaults
View all tasks
Complete a task by entering its ID. It will check if this ID exists and not completed and that you enter a valid number
See updated task list
View stars summary per child
API endpoints
/all_tasks - Returns all tasks. Using GET method
/add_task - Adds a new task for a child. Using POST method
/complete_task/ - Marks a task as completed. Using PUT method
/stars_summary - Returns total stars per child. Using GET method
