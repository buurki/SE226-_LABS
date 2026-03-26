tasks = {}
n = int(input("Enter number of tasks: "))
for i in range(n):
    task_name = input("Enter task name: ")
    dep_count = int(input(f"How many dependencies for {task_name}? "))

    dependencies = []
    for j in range(dep_count):
        dep = input(f"Enter dependency {j + 1}: ")
        dependencies.append(dep)

    tasks[task_name] = dependencies

print("TASK STRUCTURE:")
for task in tasks:
    print(f"{task} -> {tasks[task]}")

print("INITIAL TASKS (no dependencies):")
no_dep = [task for task in tasks if len(tasks[task]) == 0]

if no_dep:
    for t in no_dep:
        print(t)
else:
    print("None")

completed = set()
execution_order = []

while len(completed) < len(tasks):
    progress = False

    for task in tasks:
        if task not in completed:
            if all(dep in completed for dep in tasks[task]):
                completed.add(task)
                execution_order.append(task)
                progress = True

    if not progress:
        print("EXECUTION ORDER:")
        print("No task can be started.")
        print("ERROR: Circular dependency detected!")

        print("These tasks could not be completed:")
        for task in tasks:
            if task not in completed:
                print(task)
        break

if len(completed) == len(tasks):
    print("EXECUTION ORDER:")
    for i, task in enumerate(execution_order):
        print(f"Step {i + 1}: {task}")

    print("ALL TASKS COMPLETED SUCCESSFULLY")
