tasks = []  # list to store tasks

while True:
    print("\n--- TO-DO LIST MENU ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        if not tasks:
            print("No tasks yet!")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove!")
        else:
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
            try:
                num = int(input("Enter task number to remove: "))
                removed = tasks.pop(num-1)
                print(f"Task '{removed}' removed!")
            except (ValueError, IndexError):
                print("Invalid choice!")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, try again.")
