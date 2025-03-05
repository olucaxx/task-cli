from data import load_tasks, save_tasks
from models import Task

tasks = load_tasks()

def add_task(description: str) -> int:
    Task.current_id = tasks['current_task_id']
    tasks['tasks'].append(vars(Task(description)))
    tasks['current_task_id'] = Task.current_id
    save_tasks(tasks)
    return f"Task added successfully (ID: {Task.current_id - 1})"

    
def update_task_description(new_description: str, task_id: int) -> str:
    try:
        for task in tasks['tasks']:
            if task['id'] == task_id:
                task_obj = Task.from_dict(task)
                task_obj.update_description(new_description.strip())
                task.update(vars(task_obj))
        save_tasks(tasks)
        return f"Task ({task_id}) was updated!"
    
    except ValueError:
        return f"'{new_description}' is not a valid name."


def update_task_status(new_status: int, task_id: int) -> str:
    try:
        for task in tasks['tasks']:
            if task['id'] == task_id:
                task_obj = Task.from_dict(task)
                task_obj.update_status(new_status)
                task.update(vars(task_obj))
        save_tasks(tasks)
        return f"Task ({task_id}) was updated!"
    
    except ValueError:
        return f"{new_status} is not a valid status."


def delete_task(task_id: int) -> str:
    for task in tasks['tasks']:
        if task['id'] == task_id:
            del task
            save_tasks(tasks)
            return f"Task ({task_id}) was deleted!"
        
    return f"Couldn't find a task with id ({task_id})."


def list_all_tasks() -> list[str]:
    result = []
    for task in tasks['tasks']:
        result.append(str(Task.from_dict(task)))
    return result


def list_tasks_by_status(status: int) -> list[str]:
    result = []
    for task in tasks['tasks']:
        if task['status'] == status:
            task_obj = Task.from_dict(task)
            result.append(str(task_obj))
    return result


def reset_tasks() -> str:
    save_tasks({"current_task_id":1, "tasks":[]})
    return "All tasks were deleted and id was reseted to (1)."
    
