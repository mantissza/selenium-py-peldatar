# 022.md hw's solution aka chr() and ord() functions' usage

start = int(ord('a'))
end = int(ord('z'))
max_length = (end-start+1)+2
list = [' '] * max_length

i = 0
while start <= end:
    if (start < 100):
        start = '0' + str(start)
        list[i] = chr(int(start)) + ' : ' + start
        start = int(start)
    else:
        list[i] = chr(start) + ' : ' + str(start)
    i += 1
    start += 1

#  print(list)

for i in range(7):
    print(list[i] + ' | ' + list[i+7] + ' | ' + list[i+14] + ' | ' + list[i+21])
