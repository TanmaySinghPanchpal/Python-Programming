# Python Program to Display Course Costs.
courses = {
    "B.Sc": "60K",
    "M.Sc": "40K",
    "B.Tech": "80K",
    "M.Tech": "70K"}

for course, cost in courses.items():
    print(f"{course}: {cost}")

