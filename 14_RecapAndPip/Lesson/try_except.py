import sys


def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
#
#
# try:
#     linux_interaction()
# except AssertionError as error:
#     print(error)
#     print('The linux_interaction() function was not executed')
#
#
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except:
#     print('Could not open file.log')
#
# try:
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)

# try:
#     linux_interaction()
#     with open('file.log') as file:
#         read_data = file.read()
# except FileNotFoundError as fnf_error:
#     print(fnf_error)
# except AssertionError as error:
#     print(error)
#     print('Linux linux_interaction() function was not executed')


try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
