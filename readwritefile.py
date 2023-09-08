# required file name
filename = input('Create your custom file name: ')
# content to put in file
filecontent = input('Give your own content: ')


# define function with two input
def create_file(name, content):
    # create a file with required file name
    new_file = open(name+'.txt', 'w')
    # add the content to the created file
    new_file.write(content)
    new_file.close()


def read_file(name):
    # open the file and allow read
    new_file = open(name+'.txt', 'r+')
    # print the content of the file
    print(new_file.read())
    new_file.close()


# call the function with the required parameters
create_file(filename, filecontent)
read_file(filename)
