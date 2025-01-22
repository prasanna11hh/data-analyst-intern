import matplotlib.pyplot as plt

# Step 1: Define the dataset
# Each employee is represented as a dictionary
employees = [
    {"EmployeeID": 1, "Age": 29, "Attrition": "Yes", "PerformanceRating": 3},
    {"EmployeeID": 2, "Age": 35, "Attrition": "No", "PerformanceRating": 4},
    {"EmployeeID": 3, "Age": 42, "Attrition": "No", "PerformanceRating": 5},
    {"EmployeeID": 4, "Age": 28, "Attrition": "Yes", "PerformanceRating": 2},
    {"EmployeeID": 5, "Age": 33, "Attrition": "No", "PerformanceRating": 4},
]

# Step 2: Basic Analysis
total_employees = len(employees)
attrition_count = sum(1 for emp in employees if emp["Attrition"] == "Yes")
attrition_rate = (attrition_count / total_employees) * 100
average_performance = sum(emp["PerformanceRating"] for emp in employees) / total_employees

# Output the results
print(f"Total Employees: {total_employees}")
print(f"Attrition Count: {attrition_count}")
print(f"Attrition Rate: {attrition_rate:.2f}%")
print(f"Average Performance Rating: {average_performance:.2f}")

# Step 3: Visualization
# Attrition Pie Chart
attrition_labels = ["Attrition", "No Attrition"]
attrition_sizes = [attrition_count, total_employees - attrition_count]
plt.figure(figsize=(6, 6))
plt.pie(attrition_sizes, labels=attrition_labels, autopct='%1.1f%%', startangle=90, colors=["red", "green"])
plt.title("Attrition Rate")
plt.show()

# Performance Rating Distribution
performance_ratings = [emp["PerformanceRating"] for emp in employees]
ages = [emp["Age"] for emp in employees]

plt.figure(figsize=(8, 5))
plt.bar(ages, performance_ratings, color="blue", alpha=0.7)
plt.xlabel("Age")
plt.ylabel("Performance Rating")
plt.title("Performance Rating by Age")
plt.show()
