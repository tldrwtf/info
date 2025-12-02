
# ==========================================
# TASK 7.1: Sorting with Lambda
# ==========================================
products = [
    {'name': 'Apple', 'price': 10},
    {'name': 'Orange', 'price': 5},
    {'name': 'Banana', 'price': 20}
]

# Sort by price descending
sorted_products = sorted(products, key=lambda x: x['price'], reverse=True)
print("Sorted Products:", sorted_products)

# ==========================================
# TASK 7.2: Map (Raise Salary)
# ==========================================
employees = [
    {'name': 'A', 'salary': 50000},
    {'name': 'B', 'salary': 60000}
]

def give_raise(emp):
    new_emp = emp.copy()
    new_emp['salary'] = emp['salary'] * 1.07
    return new_emp

# Using map
raised_employees = list(map(give_raise, employees))
print("Raised Salaries:", raised_employees)

# ==========================================
# TASK 7.3: Filter (Books)
# ==========================================
books = [
    {'title': 'Book A', 'rating': 3.5},
    {'title': 'Book B', 'rating': 4.5},
    {'title': 'Book C', 'rating': 4.0}
]

top_rated = list(filter(lambda b: b['rating'] >= 4.0, books))
print("Top Rated Books:", top_rated)

# ==========================================
# TASK 7.4: List Comprehension
# ==========================================
numbers = [1, 2, 3, 4, 5, 6]
# Keep evens, double them
doubled_evens = [n * 2 for n in numbers if n % 2 == 0]
print("Doubled Evens:", doubled_evens)
