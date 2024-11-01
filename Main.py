employee_file = open("Employees.txt", "a")

employee_file.write("Toby - Human Resources") #It attaches as is to the latest line, so if there is no empty new line,
                                                # it'll attach right after the last one

employee_file.write("\nKelly - Customer Service")

employee_file = open("Employees_Another.txt", "w")

employee_file.write("Toby - Human Resources")

employee_file = open("Website.html", "w")

employee_file.write("<p>This is HTML</p>")

employee_file.close()