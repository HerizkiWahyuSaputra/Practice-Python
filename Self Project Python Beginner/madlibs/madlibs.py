# string concatenation (how to put strings together)
# suppose we want to create a string sthat says "subcribe to _____"
# youtuber = "Herizki Saputra" # some string variable

# # a few ways to do this
# print("subrscribe to " + youtuber) # this is statement from string variable
# print("subsrcribe to {}".format(youtuber)) # function non-parameter
# print(f"subscribe to {youtuber}") # function with pramater

# Step 1 you input for string variable
str = input("string: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
solution = input("solution: ")
what_next = input("what_next: ")
why = input("why: ")

# Step 2 for string
madlib = f"technology is so {str}! with technology more than better life for human \
This 20 century is {verb1}. at start new tech and {verb2} next changing for {solution}\
so very important to {what_next} for keep {why} result to better Technology."

# Step 3 for function to call string statement 
print(madlib)