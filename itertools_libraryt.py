import itertools
def convert_bool(v):
    if v == 1:
        return True
    return False
a = [1,2,3,4,5,6]
l =[1,0,1,0,1,0]
l = map(convert_bool,l)
# print(list(itertools.compress(a, l)))


#filter false

filter_this_list = [n for n in range(10)]
# print(list(itertools.filterfalse(lambda x: x%2 == 0, filter_this_list)))
# output ---> [1, 3, 5, 7, 9]


#group by


group_this_list = [('a',2), ('a',10),('b',20), ('c',90), ('c',4),('c',8)]
# for key,i in itertools.groupby(group_this_list, key = lambda x:x[0]):
#     print(key, list(i))
    #output --- >
# a [('a', 2), ('a', 10)]
# b [('b', 20)]
# c [('c', 90), ('c', 4), ('c', 8)]


# print(sorted(group_this_list))
# print(sorted(group_this_list, key = lambda x: x[0]))  key functin takes a function and returns a a valie jis sey humain sort ya group by karwana hai



#isslice
import time
a = [n for n in range(100000)]
i_t = time.time()
# print(list(itertools.islice(a,5)))
# print("Itertools ney yai time liya : ", time.time() - i_t)
# i_t = time.time()
# print(a[:5])
# print("Pyton ney itna time liya : ", time.time() - i_t)


# output -->
# [0, 1, 2, 3, 4]
# Itertools ney yai time liya :  0.00025343894958496094
# [0, 1, 2, 3, 4]
# Pyton ney itna time liya :  0.0010118484497070312

#pairwise

a = [1,2,3,4,5]
# print(list(itertools.pairwise(a)))
# output -- >
# # [(1, 2), (2, 3), (3, 4), (4, 5)]


#starmaping



a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
result = itertools.starmap(lambda x, y: x * y, zip(a, a))
# print(list(result))
# output -->
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]


#tee

take_while = [n for n in range(50)]
# print(list(itertools.takewhile(lambda x: x <= 10, take_while)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


a= [12,3,4,55,6,7,8,9]
o = itertools.tee(a,10)
# for k,i in enumerate(o):
#     print(k,list(i), sep=" :")


#zip_longest


a = [n for n in range(25)]
b = [chr(i) for i in range(67,80)]
# print(list(itertools.zip_longest("X",a,b, fillvalue=None)))


#product
 

a = "Ghazi"
s = 0  # Initialize s to 1
# for i in range(5):  # Iterate 5 times
#     s += len(list(itertools.permutations(a, i+1)))  # Update s by multiplying with the number of combinations
# #     print(s)

# print(s)


s1= "123"
s2 = "abc"
print(list(itertools.product(s2,s1, repeat = 2)) == list(itertools.product(s1+s2, repeat = 2)))
