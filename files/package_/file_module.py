def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

# if __name__ == '__main__':
print(read_file('my_package/hello.py'))