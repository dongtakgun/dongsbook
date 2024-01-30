from random import *

# USER = range(1,21)
# USER = list(USER)

# shuffle(USER)

# winners = sample(USER,4)

# print("당첨자 발표")
# print("치킨 당첨자 {}".format(winners[0]))
# print("커피 당첨자{}".format(winners[1:]))

#20명이 있는데 1등 치킨 234등 커피


A=range(1,21)
A=list(A)

shuffle(A)
B=sample(A,4)
print(B)

print("당첨자 발표")
print("치킨 당첨자"+str(B[0]))
print("커피 당첨자"+str(B[1:]))



