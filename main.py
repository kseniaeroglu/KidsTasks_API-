import requests

def get_all_tasks_main():
    endpoint = "http://127.0.0.1:5000/all_tasks"
    return requests.get(endpoint).json()

def add_task_main():
    endpoint = "http://127.0.0.1:5000/add_task"
    child_name = (input("Enter child name: (default: Ivan) ") or "Ivan").strip()
    task_description = input("Enter task description:  (default: Do 15 min spelling) ") or "Do 15 min spelling "
    new_task = {
        "child_name": child_name,
        "task_description": task_description
    }
    return requests.post(endpoint, json=new_task).json()

def complete_task_main(task_id):
    endpoint = f"http://127.0.0.1:5000/complete_task/{task_id}"
    response = requests.put(endpoint)
    if response.status_code != 200:
        raise Exception(f"Task {task_id} not found or already completed")
    return response.json()

def get_star_summary_main():
    endpoint = "http://127.0.0.1:5000/stars_summary"
    return requests.get(endpoint).json()

def run():
    print("\n👋 Welcome to KidTasks - Chore & Star Tracker!")
    print("----------------------------------------------")

    print("\n📝 Adding a new task...")
    print(add_task_main())

    print("\n📋 All tasks so far:")
    tasks = get_all_tasks_main()
    for task in tasks:
        print(task)

    if tasks:
        while True:
            try:
                task_id = int(input("\n🔢 Enter the task ID you want to mark as completed: "))
                print(complete_task_main(task_id))
                break
            except ValueError:
                print("\n Please enter a valid number")
            except Exception as err:
                print("❗️", err)
                print("Please try with a different task ID")


    print("\n🔄 Updated task list:")
    for task in get_all_tasks_main():
        print(task)

    print("\n⭐ Stars Summary:")
    for child in get_star_summary_main():
        print(f"{child[0]}: {child[1]} star(s)")

    print("\n🎉 Thank you for using KidTasks!")

if __name__ == '__main__':
    run()
