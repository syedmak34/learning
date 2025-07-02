def get_lines(filename):
    with open (filename, 'r') as file:
     for line in file:
        yield line 

test= get_lines('text.txt')
print(next(test))
print(next(test))
print(next(test))
print(next(test))
print(next(test))