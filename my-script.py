# open a file
alpha_file = open('alpha-text', 'r')


numbers = [1, 2, 3]
for i in range(len(numbers)):
    num = numbers[i]
    alpha_file.write("{}\n".format(num))

alpha_file.close()



# close a file
print(alpha_file.read())
alpha_file.close()