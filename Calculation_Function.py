def calculate_average(percentage):
    return int(sum(percentage) / len(percentage)) 
# # The function takes a list of scores as input and returns the average of those scores.
# The function uses the built-in sum() function to calculate the total of the scores and divides it by the number of scores using len().


def assign_efficiency(average):
        if average >= 100:
            return "High"
        elif average >= 95:
            return "Operational"
        elif average >= 85:
            return "Busy"
        else:
            return "Inefficient"
# The function takes an average score as input and returns a string representing the efficiency rating based on the average score.
# The function uses a series of if-elif statements to determine the efficiency rating based on the average score.           

def team_efficiency(employees):
    total_efficiency = 0
    for employee in employees:
        total_efficiency += employee[4]  # The average score is at index 4
    return int(total_efficiency / len(employees) if employees else 0) 
# The function takes a list of employees as input and returns the average efficiency rating for the team.
# The function uses a for loop to iterate through the list of employees and calculates the total efficiency by summing the average scores.  
