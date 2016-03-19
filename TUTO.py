# *A little Python Tutorial*
# A comment starts with #
# This tutorial is mostly about the syntax of the loops
for i in {"blub", "blab", "blib"}:
    print(i)
# for-loops in Python are called with a list and not
# with an incremented variable.
# The loop walks through the list right to the in and i gets the value of the
# variable in the list. After the list is a ':' and the  commands
# which are in the loop must be intended.
for i in range(1,11):
    print(i)
# If you want to make a for-loop with a counter variable,
# you must use "range(start,stop)".
# IMPORTANT: i will never get the value of the stop argument!
while i < 20:
    i += 1
    print(i)
# The syntax of while is easier: while [condition]:
# If you thought "Why not using i++?", here's the answer:
# In Python are not incrementing or decrementing operators,
# but +=, -=, *=, /=, ^= and %= exists.
if input("Number please: ") == 20:
    print("The number equals 20.")
else:
    print("The number doesn't equal 20")
# I think this syntax is pretty easy.
#if [condition]:
#   commands
#else:
#   commands
