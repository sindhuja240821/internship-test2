import csv
file=open('main.csv')
r=csv.reader(file)
h=[]
h=next(r)
l=[]
for row in r:
    l.append(row)
res=[]
res.append(h)
count=0
m=len(l[0])
n_list=[0]*(m-1)
for i in l:
    if count<=10:
        if count==0:
            n_list[0]=i[0]
        n_list[1]+=int(i[1])
        n_list[2]+=int(i[3])
        n_list[3]+=int(i[4])
        n_list[4]+=int(i[5])
        n_list[5]+=int(i[6])
        n_list[6]+=int(i[7])
        n_list[7]+=int(i[8])
        n_list[8]+=int(i[9])
        n_list[9]+=int(i[10])
        count+=1
        if count==10:
            res.append(n_list)
            count=0
            n_list=[0]*(m-1)
res.append(n_list)
h.remove('Total')
h[0]=''
file_name='output.csv'
with open(file_name,'w') as f:
    for y in h :
        f.write(str(y)+', ')
    f.write('\n')
    for r in res:
        for s in r:
            f.write(str(s)+', ')
        f.write('\n')