def todo_list():
    tasks = []
    while True:
        task = input("Enter a new task (or 'done' to finish): ")
        if task.lower() == 'done':
            break
        tasks.append(task)
    
    print("\nYour To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

todo_list()
