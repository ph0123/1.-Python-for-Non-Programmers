#List
a= [1,2,3,3]
print(a)
# add, insert and delete
a.append(5)
print('append 5 to end of list: ',a)
a.insert(3,9) #position and value.
print('insert 9 to position 3: a = ',a)

a.remove(3)
print('remove 3 to position 3: a = ',a)

print('The number of elements in list a: ',len(a))

# for loops
print('Print array with enumerate...')
for i,item in enumerate(a):
    print(f'a[{i}] = {item}')

print('Print with in...')
t= 0 
for i in a:
    print(f'a[{t}] = {i}')
    t+=1


print('Print with index...')

for i in range(len(a)):
    print(f'a[{i}] = {a[i]}')

#dictrionaries
dic = {}
for i in range(len(a)):
    dic[i] = a[i]
print(dic)
#delete fist element of dic
del(dic[0])
print(dic)