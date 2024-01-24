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

def print_menu(task, subtask_count = 0):                        #print the content of the dictionary
    for i in task:
        print(str(subtask_count * 2 * "-") + str(i["id"]) + ".", i["description"] , "(" + i["assigned_to"] + ")") 
        if "subtasks" in i:
            print_menu(i["subtasks"], subtask_count +1)

def id_number_func(task,id_count):                              #update the id numbers with the id_number_func
    for i in task:                                              #id_count --> list
        i["id"] = len(id_count) + 1                             #assign the new id number according to lenghth of the id_count list
        id_count.append(i["id"])
        if "subtasks" in i:
            id_number_func(i["subtasks"],id_count)              #call the function for subtasks 

def add_task_recursive(task, add, new_dict):                    #add a new task
    if add == 0:                                                #check the user input if it is 0, add new task
        task.append(new_dict)
    else:
        for i in task:
            if i["id"] == add:                                  #if user wants to a task into a task that is already exists,                                             
                if "subtasks" in i:                             # check the id number and add the task into subtask of that id number
                    i["subtasks"].append(new_dict)
                else:
                    i.pop("time_estimate")                      #remove the time estimate key because it is not necessary
                    i["subtasks"] = list()
                    i["subtasks"] = [new_dict]
            else:
                if "subtasks" in i:                             #call the function for subtasks
                    add_task_recursive(i["subtasks"], add, new_dict)        

def assign_task(tasks, task_number, new_name):                  #assign a new name to the task
    for i in tasks:
        if i["id"] == task_number:                              #assign a new name according to id number that user enter
            i["assigned_to"] = new_name
        else:
            if "subtasks" in i:                                 #call the function but this time with subtasks
                assign_task(i["subtasks"], task_number, new_name)

def complete_task_recursive(task, id_number, description):      #change the status of task
    for i in task:
        if i["id"] == id_number:
            description.append(i["description"])                #append the description name to the description list (in the below if == 3 part) for printing description name that completed
            if "subtasks" in i:
                complete_task_recursive(i["subtasks"], id_number +1, description)
            else:
                i["completed"] = True                           #a new key with True value
                id_number += 1                                  #add one to id number to continue 
        else:
            if "subtasks" in i:
                complete_task_recursive(i["subtasks"], id_number, description)

def generate_report(task,subtask_count = 0):
    general_total_time = 0
    remaining_time = 0
    for i in task:
        time_uncompleted, total_time = calculate_time_recursive(i)          #assign the outputs of function then use inside of the print(end of the print part)
        general_total_time += total_time                                    #calculate total time and remaining time for printing
        remaining_time += time_uncompleted
        if time_uncompleted == 0:                                           #check the time of uncomleted tasks and assign a new value status for printing 
            status = "Completed"                                            
        else:
            status = "Pending"
        print(str(subtask_count * 2 * "-") + str(i["id"]) + ".", i["description"] , "(" + i["assigned_to"] + ")", "--", "Estimated Time to Finish: ", "{} out of {} hours,".format(time_uncompleted, total_time), status) 
        if "subtasks" in i:                                                 #call the function for subtasks
            generate_report(i["subtasks"], subtask_count +1)
    return general_total_time, remaining_time                               # return for printing

def calculate_time_recursive(task):
    if "subtasks" not in task:
        if "completed" in task:
            return 0, task["time_estimate"]                     #return values of times to use insideof the generate function acording to completed status
        else:
            return task["time_estimate"], task["time_estimate"]
    total_time = 0
    time_uncompleted = 0
    for subtask in task["subtasks"]:
        time1, time2 = calculate_time_recursive(subtask)        
        total_time += time2                                     #calculate the times and return them
        time_uncompleted += time1
    return time_uncompleted, total_time

def main():
    tasks = init_tasks()

    while True:
        print("Operations:")                                    #print all operations
        print("     1. Add a new task")
        print("     2. Assign task to a team member")
        print("     3. Complete a task")
        print("     4. Generate report")
        print("     5. Exit")
        operation = int(input("Please select an operation:"))

        if operation == 1:                                      #add a new task operation
            print("0. New Task")
            print_menu(tasks, subtask_count=0)
            add = int(input("To add a new task, enter 0. To add a subtask, select the task ID: "))
            description = input("Please enter the task description: ")
            name = input("Please enter the task responsible: ")
            time = int(input("Please enter the estimated tXme for the task: "))
            new_dict = {}
            new_dict["id"] = 0                                  #make a new dictionary from inputs 
            new_dict["description"] = description
            new_dict["assigned_to"] = name
            new_dict["time_estimate"] = time
            add_task_recursive(tasks, add, new_dict)            #call the function for adding a new task
            id_count = []                                       #id count list to give an id number for each task
            id_number_func(tasks,id_count)
            print("New task is added.")
            input("Please press enter to continue.")

        elif operation == 2:                                    #Assign task to a team member operation
            print_menu(tasks, subtask_count=0)
            task_number = int(input("Please select a task: "))
            new_name = input("Please enter the new team members name: ")
            assign_task(tasks, task_number, new_name)           #call the function to assign task to a team member
            print("Task New task assigned to {}.".format(new_name))
            input("Please press enter to continue.")

        elif operation == 3:                                    #complete task operation
            print_menu(tasks, subtask_count=0)
            id_number = int(input("Enter task ID: "))
            description = []                                    #description list to hold status of task that was completed
            complete_task_recursive(tasks, id_number, description)
            print("Task '{}' marked as completed.".format(description[0]))      #print the sentence with first element of description list
            input("Please press enter to continue.")
          
        elif operation == 4:                                                #generate report operation
            general_total_time, remaining_time = generate_report(tasks)     #assign new values that are outputs of function to general total time and remaining time
            print()
            print("The total time of the project is: ", general_total_time)       #print them with explanations
            print("The remaining time of the tasks to finish the project is: ", remaining_time)
            input("Please press enter to continue.")

        elif operation == 5:                                    #EXIST
            print("Goodbye! :)")
            break                                               #break the loop for existing from program
        
if __name__ == "__main__":
    main()