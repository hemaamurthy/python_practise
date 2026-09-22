def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}")

greet("Hi", "Hema", "Anju", "Badam")
  