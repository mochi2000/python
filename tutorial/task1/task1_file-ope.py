import os

path = './task1/data'
tmp = os.listdir(path)
files = []
for filename in tmp:
  p = path + '/' + filename
  if os.path.isfile(p):
      files.append(filename)
print(files[:10])