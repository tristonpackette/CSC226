def timer(start):
    while start > 0:
        print(f"Time left until finish baking: {start}")
        start -= 1
    print("Cookies are ready! ")
timer(10)