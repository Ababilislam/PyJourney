#
# # def read_file_into_buffer(file_path):
# #     with open(file_path,'r') as file:
# #         file_content = file.read()
# #     return file_content
#
#
# # runner
# # file = 'tex.txt'
# # file_contents = read_file_into_buffer(file)
# # # can read full file
# # print(file_contents)
# # # or can read a specific lenght to a file by string slicing its more effective
# # print(file_contents[:15])
#
#
# ######## reading binary file
#
# def read_binary_file_into_buffer(file):
#     with open(file,'rb') as files:
#         file_contents = files.read()
#     return file_contents
#
# file_path = 'img.png'
#
# file_content = read_binary_file_into_buffer(file_path)
#

######## IO string buffer
import io

def read_string_into_buffer(file_name):
    buffer = io.StringIO(file_name)
    file_contains = buffer.read()
    print(type(buffer))
    return file_contains

data_string = "This is a string containing data that we want to read into a buffer."

file_contain = read_string_into_buffer(data_string)
print(file_contain)
print(type(file_contain))