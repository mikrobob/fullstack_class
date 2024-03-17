workers = ["Света", "Маша", "Олег", "Паша"]

even_days = workers[::2]
odd_days = workers[1::2]

print("В чётные дни работает: ", *even_days,"\n"
      "\n"
      "В нечётные дни: ", *odd_days)