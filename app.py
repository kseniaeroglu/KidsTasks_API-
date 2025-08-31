from flask import Flask, jsonify, request
from db_utils import get_all_tasks_db, add_task_db, complete_task_db, get_star_summery_db

app = Flask(__name__)


@app.route("/all_tasks", methods=["GET"])
def get_all_tasks_api():
    return jsonify(get_all_tasks_db())

@app.route("/add_task", methods=["POST"])
def add_task_api():
    data = request.get_json()
    child_name = data.get("child_name").strip()
    task_description = data.get("task_description")
    return jsonify(add_task_db(child_name, task_description))

@app.route("/complete_task/<int:task_id>", methods=["PUT"])
def complete_task_api(task_id):
    try:
        return jsonify(complete_task_db(task_id))
    except ValueError as ve:
        return jsonify(str(ve)), 400
    except Exception:
        return jsonify("Server error"), 500

@app.route("/stars_summary", methods=["GET"])
def stars_summary_api():
    return jsonify(get_star_summery_db())

if __name__ == "__main__":
    app.run(debug=True)
