def init_tasks():
    return [
        {'id': 1, 'description': "Complete Project Proposal", 'assigned_to': "John Doe", "subtasks": [
            {'id': 2, 'description': "Research", 'assigned_to': "Alice Brown", 'time_estimate': 5},
            {'id': 3, 'description': "Outline", 'assigned_to': "Bob Johnson", 'subtasks': [
                {'id': 4, 'description': "Introduction", 'assigned_to': "Jane Smith", 'time_estimate': 3},
                {'id': 5, 'description': "Body", 'assigned_to': "Jane Smith", 'time_estimate': 6},
                {'id': 6, 'description': "Conclusion", 'assigned_to': "David Wilson", 'time_estimate': 2}
                ]}
        ]}]

def print_menu(task, subtask_count = 0):                        #
    #subtask_count = 0
    for i in task:
        print(str(subtask_count * 2 * "-") + str(i["id"]) + ".", i["description"] , "(" + i["assigned_to"] + ")") 
        if "subtasks" in i:
            #print_menu(i["subtasks"]) 
            print_menu(i["subtasks"], subtask_count +1)

def id_number_func(task, id, id_count):
    for i in task:
        i["id"] = len(id_count) + 1
        id_count.append(i["id"])
        if "subtasks" in i:
            id += 1
            id_number_func(i["subtasks"], id, id_count)
        else:
            id += 1
        
    #print(id_count)        

def add_task_recursive(task, add, new_dict):
    if add == 0:
        task = task.append(new_dict)
    else:
        for i in task:
            if i["id"] == add:
                if "subtasks" in i:
                    #print(i["subtasks"])
                    i["subtasks"].append(new_dict)
                else:
                    i.pop("time_estimate")
                    i["subtasks"] = list()
                    #print(new_dict)
                    #print(i["subtasks"])
                    i["subtasks"] = [new_dict]
            else:
                if "subtasks" in i:
                    add_task_recursive(i["subtasks"], add, new_dict)        
    #print(task)

def assign_task(tasks, task_number, new_name):
    #task_number = int(input("Please select a task: "))
    #new_name = input("Please enter the new team members name: ")
    for i in tasks:
        if i["id"] == task_number:
            i["assigned_to"] = new_name
        else:
            if "subtasks" in i:
                assign_task(i["subtasks"], task_number, new_name)
    #print("Task New task assigned to {}".format(new_name))

def complete_task_recursive(task, id_number, description):
    for i in task:
        if i["id"] == id_number:
            description.append(i["description"])
            if "subtasks" in i:
                complete_task_recursive(i["subtasks"], id_number +1, description)
            else:
                i["completed"] = True
                #description.append(i["description"])
                id_number += 1
        else:
            if "subtasks" in i:
                complete_task_recursive(i["subtasks"], id_number, description)
    #print("Task {} marked as completed.".format(description))    
    #print(task)

def generate_report(task, general_total_time, remaining_time, subtask_count = 0):
    for i in task:
        time_uncompleted, total_time = calculate_time_recursive(i)
        general_total_time += total_time
        remaining_time += time_uncompleted
        if time_uncompleted == 0:
            statuas = "Completed"
        else:
            statuas = "Pending"
        print(str(subtask_count * 2 * "-") + str(i["id"]) + ".", i["description"] , "(" + i["assigned_to"] + ")", "--", "Estimated Time to Finish: ", "{} out of {} hours,".format(time_uncompleted, total_time), statuas) 
        if "subtasks" in i:
            #print_menu(i["subtasks"]) 
            generate_report(i["subtasks"], general_total_time, remaining_time, subtask_count +1)
    return general_total_time, remaining_time

def calculate_time_recursive(task):
    if "subtasks" not in task:
        if "completed" in task:
            return 0, task["time_estimate"]
        else:
            return task["time_estimate"], task["time_estimate"]
    total_time = 0
    time_uncompleted = 0
    for subtask in task["subtasks"]:
        time1, time2 = calculate_time_recursive(subtask)
        total_time += time2
        time_uncompleted += time1
    return time_uncompleted, total_time

def main():
    tasks = init_tasks()

    operation = 0
    #print(operation)
    while operation <=  5 :
        print("Operations:")
        print("     1. Add a new task")
        print("     2. Assign task to a team member")
        print("     3. Complete a task")
        print("     4. Generate report")
        print("     5. Exit")
        operation = int(input("Please select an operation:"))
        #print(operation)

        if operation == 1:
            #print("add")
            print("0. New Task")
            #subtask_count = 0
            print_menu(tasks, subtask_count=0)
            add = int(input("To add a new task, enter 0. To add a subtask, select the task ID: "))
            description = input("Please enter the task description: ")
            name = input("Please enter the task responsible: ")
            time = int(input("Please enter the estimated tXme for the task: "))
            new_dict = {}
            new_dict["id"] = 0   
            new_dict["description"] = description
            new_dict["assigned_to"] = name
            new_dict["time_estimate"] = time
            add_task_recursive(tasks, add, new_dict)
            id = 1
            id_count = []
            id_number_func(tasks, id, id_count)
            print("New task is added.")
            operation = input("Please press enter to continue.")
            operation = 0
            #print(tasks)

        elif operation == 2:
            #print("assign")
            print_menu(tasks, subtask_count=0)
            task_number = int(input("Please select a task: "))
            new_name = input("Please enter the new team members name: ")
            assign_task(tasks, task_number, new_name)
            print("Task New task assigned to {}.".format(new_name))
            operation = input("Please press enter to continue.")
            operation = 0

        elif operation == 3:
            print_menu(tasks, subtask_count=0)
            id_number = int(input("Enter task ID: "))
            description = []
            complete_task_recursive(tasks, id_number, description)
            #print(description)
            print("Task '{}' marked as completed.".format(description[0]))
            #print(tasks) #
            operation = input("Please press enter to continue.")
            operation = 0
            
        elif operation == 4:
            general_total_time = 0
            remaining_time = 0
            general_total_time, remaining_time = generate_report(tasks, general_total_time, remaining_time)
            print("The total time of the project is: ", general_total_time)
            print("The remaining time of the tasks to finish the project is: ", remaining_time)
            operation = input("Please press enter to continue.")
            operation = 0

        elif operation == 5:
            print("Goodbye! :)")
            break
        
if __name__ == "__main__":
    main()