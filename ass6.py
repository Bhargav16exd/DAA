import sys

def branch_and_bound(cost_matrix, n):
    def solve(student, current_cost, visited, assignment):
        nonlocal min_cost, best_assignment

        # If all students are assigned, update the minimum cost and assignment
        if student == n:
            if current_cost < min_cost:
                min_cost = current_cost
                best_assignment = assignment[:]
            return

        # Try assigning the student to each club
        for club in range(n):
            if not visited[club] and current_cost + cost_matrix[student][club] < min_cost:
                visited[club] = True
                assignment[student] = club  # Assign this club to the student
                solve(student + 1, current_cost + cost_matrix[student][club], visited, assignment)
                visited[club] = False  # Backtrack

    # Initialize variables
    min_cost = sys.maxsize
    best_assignment = [-1] * n
    visited = [False] * n

    # Start the recursion
    solve(0, 0, visited, [-1] * n)
    return min_cost, best_assignment

# Input from user
n = int(input("Enter the number of students/clubs: "))
print("Enter the cost matrix row by row (space-separated):")
cost_matrix = [list(map(int, input().split())) for _ in range(n)]

# Get the result
min_cost, assignment = branch_and_bound(cost_matrix, n)

# Display the results
print(f"The minimum assignment cost is: {min_cost}")
print("Assignments (Student → Club):")
for student, club in enumerate(assignment):
    print(f"Student {student + 1} → Club {club + 1}")

