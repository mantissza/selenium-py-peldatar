# 032.md hw's solution aka while loop practice

print("Gimme a number! (<10)")
num = int(input())
sum = 0

while num < 10:
    sum += num
    print("Gimme another number!")
    num = int(input())

print("The final result is %i." % sum)
