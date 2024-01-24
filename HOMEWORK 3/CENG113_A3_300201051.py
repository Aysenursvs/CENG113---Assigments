####  300201051  ####
import os
def create_file(query):                                                         #create file function
    query_list = query.split()
    check_file = os.listdir()
    #print(check_file)
    if query_list[2]+".txt" in check_file:                                       #check if file exists or not 
        new_file1 = open("{}.txt".format(query_list[2]), "w")
        new_file1.write("id," + query_list[4] + "\n")
        print("There was already such a file. It is removed and then created again.")
    else:
        if "id" in query:                                                        #check the query that if id is in query or not
            print("You cannot create a file with attribute'id'.")
        else:
            new_file2 = open("{}.txt".format(query_list[2]), "w")                #create a new file with write mode
            new_file2.write("id," + query_list[4] + "\n")                        #write line attributes in the first line 
            print("Corresponding file was successfully created.")

def delete_file(query):                                                         #delete file function
    query += ".txt"                                                             #make suitable the file name for queries
    query_list = query.split()
    check_file = os.listdir()
    if query_list[2]  not in check_file:                                        #check the file exists or not in the same path
        print("There is no such file.")
    else:
        deleted_file = query_list[2]                                            #delete the file with remove function
        os.remove(deleted_file)
        print("Corresponding file was successfully deleted.")

def display_file():                                                             #display file funtion
    check_file = os.listdir()                                                   #make a list that includes files that are in the same path
    nth = 1                                                                     #number of queue
    print("Number of files:", len(check_file))
    for i in range(len(check_file)):
        file_read = open(check_file[i], "r")
        print(str(nth) + ")", check_file[i].rstrip(".txt") + ":", file_read.readline())     #read just first line of files and print
        nth += 1

def add_line(query):                                                            #add line funtion
    query += ".txt"                                                             #make suitable the file name for query
    query_list = query.split()
    check_file = os.listdir()
    if query_list[3]  not in check_file:                                        #check the file exists or not
        print("There is no such file.")
    else:
        new_query_list = query_list[1].split(",")
        file_read = open(query_list[3], "r")
        if len(list(file_read.readline().split(","))) == len(new_query_list) + 1:

            id = 1
            for i in file_read:                                                 #assign a id number for every line that was added
                if i != query_list[1]:
                    id += 1
            file_read = open(query_list[3], "a")                                #add the lines with append mode to the file
            file_read.write(str(id) + "," + query_list[1] + "\n")

            print("New line was successfully added to {} with id {}".format(query_list[3].rstrip(".txt"), id))
        else:
            print("Numbers of attributes do not match.") 

def remove_lines(query):                                                        #remove line funtion
    query_list = query.split()
    query_list[3] = query_list[3] + ".txt"                                      #make suitable the file name for query
    check_file = os.listdir()
    if query_list[3]  not in check_file:                                        #check file exists or not
        print("There is no such file.")
    else:
        remove = open(query_list[3], "r")                                       #open the file with read mode
        removed_line_number = 0
        line_count = 0
        flag = True
        for i in remove:
            i = i.rstrip("\n")
            line_list = i.split(",")
            if line_count == 0:                                                 #compare the attributes that are in the file and in the query                                      
                if query_list[5] not in line_list:
                    print("Your query contains an unknown attribute. ")
                    flag = False                                                #assign the flag that is false when unknown attribute exists in the query
                    break                                                       #so other conditions will not be checked and after the attribute sentence was printed
                line_count += 1                                                 #berak the for loop
               
        if flag:
            #print(query_list[6])                                               #condition is that flag = True
            if query_list[6] == "==":                                           #oparator is ==
                remove = open(query_list[3], "r")
                removed_line_number = 0
                line_count = 0                                                  #assign a line count for undertstanding which line first is 
                line_list1 = []                                                 #assign a empty list for line that will be rewrited
                for i in remove:                                                #a for loop to read and check line by line
                    i = i.rstrip("\n")                                          #append the all lines line by line for loop
                    line_list1.append(i + "\n")
                    line_list2 = i.split(",")

                    if line_count == 0:                                         #when the line count equals 0, program is reading the first line in the file
                        index_number = line_list2.index(query_list[5])          #an index number for attribute that is wanted
                    if line_list2[index_number] == query_list[7] and line_count > 0:    #check the other lines with index number if the line suitable according to query or not
                        line_list1.remove(i +"\n")                              #remove the line from list
                        removed_line_number += 1
                        
                
                    line_count += 1
                
            elif query_list[6] == "!=":                                         #make same steps for operator !=
                remove = open(query_list[3], "r")
                removed_line_number = 0
                line_count = 0
                line_list1 = []
                for i in remove:
                    i = i.rstrip("\n")
                    line_list1.append(i + "\n")
                    line_list2 = i.split(",")

                    if line_count == 0:
                        index_number = line_list2.index(query_list[5])
                    
                    if line_list2[index_number] != query_list[7] and line_count > 0:
                        print(i)
                        line_list1.remove(i + "\n")
                        removed_line_number += 1
                    line_count += 1
               
            if removed_line_number == 0:                                        #if any line does not remove that mean there is an unknown attribute
                print("Your query contains an unknown attribute.")
            else:
                print("{} lines were successfully removed.".format(removed_line_number))
            #print(line_list1)
            line_count2 = 0
            remove = open(query_list[3], "w")                                   #open the file to rewrite elements in the line list in the write mode 

            for i in range(len(line_list1)):
                if line_count2 == 0:
                    remove.write(str(line_list1[i]))                            #write the first line with write mode
                else:
                    remove = open(query_list[3], "a")                           #append the other lines by reading the list 
                    remove.write(str(line_list1[i]))
                line_count2 += 1

def modify_lines(query):                                                        #modify lines function
    query_list = query.split()
    query_list[3] = query_list[3] + ".txt"                                      #make suitable the file name for query
    check_file = os.listdir()
    if query_list[3]  not in check_file:                                        #check file exists or not
        print("There is no such file.")
    elif query_list[1] == "id":                                                 #check that if query is made with id or not
        print("Id values cannot be changed.")
    else:
        try:
            modify_file = open(query_list[3], "r")
            line_count = 0
            modified_count = 0
            modify_list = []                                                    #an empty list for modified lines
            for line in modify_file:
                line = line.rstrip("\n")
                line = line.split(",")
                if line_count == 0:                                             #if line count equls 0, line is first
                    index_number = line.index(query_list[1])                    #an index number for attribute that is wanted
                    modify_list.append(line)
                    #first_line_list = line
                else:
                    if query_list[8] == "==":                                   #operator ==
                        if line[index_number] == query_list[9]:                 #modify the line by using list and append the element that was modified to the list
                            line[index_number] = query_list[5]                  
                            modify_list.append(line)
                            modified_count += 1
                        else:
                            modify_list.append(line)
                    elif query_list[8] == "!=":                                 #same steps for operator !=
                        if line[index_number] != query_list[9]:
                            line[index_number] = query_list[5]
                            modify_list.append(line)
                            modified_count += 1
                        else:
                            modify_list.append(line)
                line_count += 1

            line_count2 = 0
            for i in range(len(modify_list)):
                modify_list[i] = str(modify_list[i])                            #convert to string to write to file correctly
                modify_list[i] = modify_list[i].rstrip("]")                     #delete unwanted punctiation in the list
                modify_list[i] = modify_list[i].lstrip("[")
                modify_list[i] = modify_list[i].split(",")
                line_string = ""                                                #empty string for new versions of lines
                for element in modify_list[i]:
                    element = element.strip()                                   #for every element in the every list, remove unwanted things
                    element = element.rstrip("'")
                    element = element.lstrip("'")
                    line_string += "," + element                                #add the new versions to the string
                line_string = line_string.lstrip(",")
                if line_count2 == 0:                                            #in the first line, write with write mode but append the other ones
                    modify_file = open(query_list[3], "w")
                    modify_file.write(line_string + "\n")
                else:
                    modify_file = open(query_list[3], "a")
                    modify_file.write(line_string + "\n")
                line_count2 += 1
            print("{} lines were successfully modified.".format(modified_count)) 
        except ValueError:                                                      #if there is unknown attribute, program will give value error because of "index" function
            print("Your query contains an unknown attribute.")                  #with try - except, solve this promblem
    
def fetch_lines(query):                                                         #fetch line function
    query_list = query.split()
    query_list[3] = query_list[3] + ".txt"
    check_file = os.listdir()
    line_in_file = 0
    
    if query_list[3]  not in check_file:                                        #check the file exists or not
        print("There is no such file.")
    else:
        fetch_file = open(query_list[3], "r")
        line_count = 0
        flag = True
        for line in fetch_file:                                                 #check the query includes unknown attribute or not by using for loops and list
            line = line.rstrip("\n")
            line = line.split(",")
            if line_count == 0:
                new = query_list[1].split(",")
                for i in new:
                    if i not in line:
                        flag = False
                        print("Your query contains an un known attribute.")     #if there is unknown attribute break the for loop and assign the flag with False
                        break
            line_count += 1

        if flag:                                                                #if flag is False the code will not check the conditions but if flag is True program will check the conditions
            title_list = query_list[1].split(",")
            fetch_file = open(query_list[3], "r")
            
            for i in title_list:
                print("|" + i + "\t", end="")                                   #print titles 
            print()
            
            for title in title_list:                                            #hold the datas and print with for loops
                line_count2 = 0
                line_condition = 0
                fetch_file = open(query_list[3], "r")
                for line in fetch_file:
                    line = line.rstrip("\n")
                    line = line.split(",")
                    if line_count2 == 0:
                        index_num = line.index(title)
                    else:
                        if query_list[6] == "==":                               #check the operator
                            if line[0] == query_list[7]:                        #check the condition
                                print(title, ":", line[index_num])              #and print the variables
                                line_condition += 1
                        elif query_list[6] == "!=":
                            if line[0] != query_list[7]:                        #same steps for operator !=
                                print(title, ":", line[index_num])
                                line_condition += 1
            
                    line_count2 += 1
                    line_in_file = line_count2 - 1
                
            print("Number of lines in file {}:".format(query_list[3].rstrip(".txt")),line_in_file) 
            print("Number of lines that hold the condition:", line_condition)         
    
def main():
    query = input("What is your query? \n")                                     #input firstly
    
    while query != "x":                                                         #a while loop for asking again and again
        query_list = query.split()
        query_list.append("a")                                                  #append some elements to the query list for not taking index error
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")
        query_list.append("a")

        if query == "create file {} with {}".format(query_list[2], query_list[4]):      #check all queries with if - elif - else statements 
            create_file(query)
        elif query == "delete file {}".format(query_list[2]):
            delete_file(query)
        elif query == "display files":
            display_file()
        elif query == "add {} into {}".format(query_list[1], query_list[3]):
            add_line(query)
        elif query == "remove lines from {} where {} {} {}".format(query_list[3], query_list[5], query_list[6], query_list[7]):
            remove_lines(query)
        elif query == "modify {} in {} as {} where {} {} {}".format(query_list[1], query_list[3], query_list[5], query_list[7], query_list[8], query_list[9]):
            modify_lines(query)
        elif query == "fetch {} from {} where {} {} {}".format(query_list[1], query_list[3], query_list[5], query_list[6], query_list[7]):
            fetch_lines(query)
        else:
            print("Invalid query!")                                                    #in the else statement, "Invalid Query"
        query = input("What is your query? \n")

main()                                                                          #call the main function and run the code

