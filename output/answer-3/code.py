import csv
with open('main.csv','rt')as f:
  data = csv.reader(f)
  att = next(data)
  l=[]
  rowno=0
  for row in data:
      newl=[row[31],row[30],row[0]]
      l.append(newl)
head=[att[31],att[30],att[0]]
l.sort(reverse=True)
n=len(att)
print(l)
filename='solution3.csv'
with open(filename, 'w') as file:
    for head in head[::-1]:
        file.write(str(head) + ', ')
    file.write('\n')
    for row in l:
        for x in row[::-1]:
            file.write(str(x) + ', ')
        file.write('\n')