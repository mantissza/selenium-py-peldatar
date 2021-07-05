# 010.md python hw's solution aka list practice

list_of_nums = []
user_input = None

print("Welcome! Please give me some positive numbers. If you type 0 the loop will shut down.")

while user_input != 0:
    user_input = input("Enter a positive number: ")
    user_input = int(user_input)
    if user_input > 0:
        list_of_nums.append(int(user_input))
        print(str(user_input) + " added to the list.")
    elif user_input < 0:
        print("Please type a positive number next time!")
    else:
        print("You type 0. The loop is complete.")

print("The final list's content: " + str(list_of_nums))

