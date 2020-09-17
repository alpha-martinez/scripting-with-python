# # open a file
# alpha_file = open('alpha-text', 'r')


# numbers = [1, 2, 3]
# for i in range(len(numbers)):
#     num = numbers[i]
#     alpha_file.write("{}\n".format(num))

# alpha_file.close()



# # close a file
# print(alpha_file.read())
# alpha_file.close()

# open a file
rome_file = open('rome.txt', 'a')

numbers = [1,2,3]
for i in range(len(numbers)):
    num = numbers[i]
    rome_file.write("{}\n".format(num))

# write to the file
# rome_file.write('\nHello\n')
# close a file
rome_file.close()

# read a file
# print(rome_file.read())

# If file is not found, one will be created
adam_file = open('adam.txt', 'w')
adam_file.write('Adam')
# adam_file.write('Adam')
adam_file.close()


# Look up how to read lines from a file in python
new_file = open('new_file.txt')
file_items = new_file.readlines()

for i in range(len(file_items)):
    each_item = file_items[i]
    print('Before: {}'.format(each_item))
    print(each_item[0:-1])
    file_items[i] = each_item[0:-1]
    print(file_items)

# print(file_items)

new_file.close()
