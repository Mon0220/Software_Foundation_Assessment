import Calculation_Function
import csv
# this script reads a CSV file containing employee data, calculates the average of their monthly performance, assigns an efficiency rating based on that average, and writes the results to a new CSV file.
# The script uses the Calculation_Function module to perform the calculations and efficiency assignments.

employees = []

with open("Employees.csv", "r") as file:
    reader = csv.reader(file)

    header = next(reader)

    for row in reader:
       name, january, february, march = row
       average = Calculation_Function.calculate_average([int(january), int(february), int(march)])
       assign_efficience = Calculation_Function.assign_efficiency(average)
       employees.append([name, january, february, march, average, assign_efficience])

# Now calculate total average of all employee averages
total_average = Calculation_Function.calculate_average([employee[4] for employee in employees])

with open("Employees_Efficiency.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "January", "February", "March", "Average", "Efficiency"])  
    writer.writerows(employees)
    writer.writerow(["Total Average Efficiency", "", "", "", total_average])  
# The output file contains the employee names, their performance in January, February, and March, their average performance, and their efficiency rating.
# The script also calculates the overall team efficiency and writes it to the output file.
# The script uses the csv module to read and write CSV files, and the Calculation_Function module to perform the calculations and efficiency assignments.
