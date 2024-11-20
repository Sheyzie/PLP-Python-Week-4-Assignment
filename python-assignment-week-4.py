''' File Handling'''
# Create a program that reads a file and writes a modified version to a new file.

file = open('my_text.txt', 'r') # open the my_text.txt file

content = str(file.read()) # pass file contents to content
print('content', content)


newDoc = open('new_text.txt', 'w') # create a new file new_text.txt

newDoc.write(content + '\n My name is Oluwaseyi') 

file.close() # make sure to close the file when done
newDoc.close() # make sure to close the file when done

''' Error Handling '''
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
newFile = input('Enter file as filename.txt : ')

print(f'\ntrying to access {newFile}...')
try:
  print(f'reading into {newFile}...')
  file2 = open(newFile, 'r')
  print(file2.read())
  file2.close() # make sure to close the file when done
except FileNotFoundError: # run the next code if condition is met
  print(f'file : {newFile} not found')
finally:
  print('file read complete')