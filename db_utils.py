import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx

def get_all_tasks_db():
    # Getting all the tasks from DB
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = "SELECT * FROM Tasks"
        cur.execute(query)
        result = cur.fetchall()

        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()

def add_task_db(child_name, task_description):
    # Adding a new task for a child
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = "INSERT INTO Tasks (child_name, task_description) VALUES (%s, %s)"
        cur.execute(query, (child_name, task_description))
        db_connection.commit()

        cur.close()
        return "✅Task added successfully"

    except Exception:
        raise DbConnectionError("⚠️Failed to add task into DB")

    finally:
        if db_connection:
            db_connection.close()

def complete_task_db(task_id):
    # Mark a task as completed and reward a star
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = "UPDATE Tasks SET is_completed = TRUE, stars_earned = 1 WHERE task_id = %s AND is_completed = FALSE"
        cur.execute(query, (task_id,))
        db_connection.commit()

        if cur.rowcount == 0:
            raise ValueError(f"Task {task_id} not found or already completed")

        cur.close()
        return "Task completed and you got a star 🌟"


    except Exception:
        raise DbConnectionError("Failed to update task in DB")

    finally:
        if db_connection:
            db_connection.close()

def get_star_summery_db():
    # Getting a list of kids with total stars earned
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """
            SELECT child_name, SUM(stars_earned) AS total_stars
            FROM Tasks
            WHERE stars_earned > 0
            GROUP BY child_name
        """
        cur.execute(query)
        result = cur.fetchall()

        cur.close()
        return result

    except Exception:
        raise DbConnectionError("Failed to read star summary from DB")

    finally:
        if db_connection:
            db_connection.close()


if __name__ == "__main__":
    print(get_all_tasks_db())
