filename = 'text_2_var_78'
with open(filename) as file:
    lines = file.readlines()

sum_lines = list()

for line in lines:
    #print(line.strip())
    nums = line.split(".")
    #print (nums)
    sum_line = 0
    for num in nums:
        num.replace("\n", "")
        sum_line += int(num)

    sum_lines.append(sum_line)

with open('text_2_var_78_result.txt', 'w') as result:
    for value in sum_lines:
        result.write(str(value) + "\n")