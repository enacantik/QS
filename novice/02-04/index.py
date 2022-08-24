# # this is my shopping list
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# print ('I have', len(shoplist), 'items to purchase.')

# print('These items are:', end=' ')
# for item in shoplist:
#     print(item, end=' ')

# print('\nI also have to but rice.')
# shoplist.append('rice')
# print('My shopping list is now', shoplist)

# print('I will sort my list now')
# shoplist.sort()
# print('Sorted shopping list is', shoplist)

# print('The first item I will buy is', shoplist[0])
# olditem = shoplist [0]
# del shoplist[0]
# print('I bought the', olditem)
# print('My shopping list is now', shoplist)

# zoo = ('phyton', 'elephat', 'penguin')
# print('Number of animals in the zoo is', len(zoo))

# new_zoo = 'monkey', 'camel', zoo
# print('Number of cages in the new zoo is', len(new_zoo))
# print('All animals in new zoo are', new_zoo)
# print('Animals brought from old zoo are', new_zoo[2])
# print('Last animal brought from old zoo is', new_zoo[2][2])
# print('Number of animals in the new zoo is', 
#     len(new_zoo)-1+len(new_zoo[2]))

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# name = 'swaroop'

# print('Item 0 is', shoplist[0])
# print('Item 1 is', shoplist[1])
# print('Item 2 is', shoplist[2])
# print('Item 3 is', shoplist[3])
# print('Item -1 is', shoplist[-1])
# print('Item -2 is', shoplist[-2])
# print('Character 0 is', name[0])

# print('Item 1 to 3 is', shoplist[1:3])
# print('Item 2 to end is', shoplist[2:1])
# print('Item 1 to -1 is', shoplist[:])

# print('characters 1 to 3 is', name[1:3])
# print('characters 2 to end is', name[2:1])
# print('characters 1 to -1 is', name[1:-1])
# print('characters strat to end is', name[:])

# shoplist = ['apple', 'mango', 'carrot', 'banana']
# shoplist[::1]
# ['apple', 'mango', 'carrot', 'banana']
# shoplist[::3]
# ['apple', 'banana']
# shoplist[::-1]
# ['banana', 'carrot', 'mango', 'apple']

# bri = set(['brazil', 'rusia', 'india'])
# 'india' in bri
# True
# 'usa' in bri
# False
# bric = bri.copy()
# bric.add('china')
# bric.issuperset(bri)
# True
# bri.remove('rusia')
# bri & bric 
# {'brazil', 'india'}

# print('Simple Assignment')
# shoplist = ['apple', 'mango', 'carrot', 'banana']
# mylist = shoplist

# del shoplist[0]

# print('shoplist is', shoplist)
# print('mylist is', mylist)

# print('Copy by making a full slice')
# mylist = shoplist[:]
# del mylist[0]

# print('shoplist is', shoplist)
# print('mylist is', mylist)

name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string strats with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))
