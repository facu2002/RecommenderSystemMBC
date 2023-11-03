

documents_filename = f"./data/documents/documents-01.txt"

with open(documents_filename, 'r') as f:
  current_line = f.readline()
  while current_line != '':
    print(current_line)
    current_line = f.readline()
  