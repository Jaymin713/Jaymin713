# list

a = [10,20,30,40,50,50]  # 0 to 5
print(a) 
print(a[0]) # random access
print(a[3])
print(a[7]) # error  index out of bound

a[3]=100
print(a[3])
print(a)

b=['ds','da',3.9,10] # diff diff diff data types
print(b)


c=[10,20,30,5]
print(c[-1]) # -1 = 30 logic
print(c[-2]) # -2 = 20 logic


c.reverse()
c.sort() # order asinding set # output 5,10,20,30
c.clear # list 


c1=[10,20,30,5]

c1.append() # value ko add krna list  last index
c1.insert(2,23) # index shifting 
print(c1)

c1.insert(5,23) # error index out of bound 
c1.insert(0,23)
print[c1[5]]



c1=[10,20,30,5]
print(len(c1)) # diifrence bitween index and len ,,index o se start hota hai or len 1 she start hota hai

