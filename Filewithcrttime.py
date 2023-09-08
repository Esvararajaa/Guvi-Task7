import datetime

# Fetch the current time
current_timestamp = datetime.datetime.now().strftime("%Y-%d-%m %H-%M-%S")
file_content = datetime.datetime.now().strftime("%Y-%d-%m %H:%M:%S")


def filename_timestamp(crt_time, str1):
    # Create a file with prescribed file name
    new_file = open(crt_time + '.txt', 'w+')
    str1 = repr(str1)
    # Write a required content in the created file
    new_file.write("File time, while created: " + str1)
    # Close the opened file
    new_file.close()


# Call the function
filename_timestamp(current_timestamp, file_content)
