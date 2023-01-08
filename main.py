# with open("sometext.txt", "w") as f:
#   # Write some text to the file
#   f.write("fjdfhd3747djc@,djf3djvbananappledh3sj")

# list of words to search for
words = ['name',"apple", "orange", "apricot", "banana","ori","0110","00","10","0"]

interpreter=0
counts = {}
for word in words:
  counts[word] = 0

with open("sometext.txt", encoding="utf8",mode="r") as file:

  character = file.read(1)
  while True:
    for word in words:
      if character == word[0]:
        file.seek(file.tell() -1)
        if file.read(len(word)) == word[:]:
          counts[word] += 1
        file.seek(file.tell() - len(word)+1)
    character = file.read(1)
    interpreter+=1
    if (file.tell()<interpreter): break

# print the results
for word in words:
  print(f"{word}: {counts[word]}")
