import glob
import os
import shutil

file_counter = 0
document_list = []
choice = None

while True:
    try:
        choice = int(input('To use the smaller files for testing to avoid preprocessing high cost give me zero else for big files give me one:'))
        print(choice)
    except ValueError:
        # To avoid giving anything different than a number.
        print("Input is invalid please give me a number: ")
        continue
    if not(choice == 0 or choice == 1):
        print('That is not a valid choice please choose again!')
        continue
    else:
        break

current_directory = os.getcwd()

if (choice == 0):
    os.chdir('small')
    file_directory = os.getcwd()
elif (choice == 1):
    os.chdir('big')
    file_directory = os.getcwd()

files = os.listdir(file_directory)

for file, f in zip(glob.glob("*.txt"), files):
    document_list.append(f'"{file}"')
    file_counter = file_counter + 1
    shutil.copy(file_directory + '\\' + f, current_directory)
print(f'We have {file_counter} documents to compare.')
print('You can copy the document list so you can later use it.')
document_list = ' '.join(document_list)
print(document_list)