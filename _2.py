# # 1/a
# list = [3, 5, 45, 97, 32, 22, 10, 19, 39, 43]
# list = [i for i in list if i%2==0]
# print(list)
# #1/b
# list=[2,3.75,0.04,59.354,6,7.777,8,9]
# list=[i for i in list if type(i)!= float]
# print(list)
# 1/c
# list=[i for i in range(3, 1001) if "3" in str(i)]
# print(list)
# #2
# list=[9, 3, 11, 10, 22, 21, 20, 8, 7, 6, 12, 5, 4, 1,]
# list.sort()
# list = [i for i in list[-3:]]
# print(list)
# #3
# first_list = [1, 4, 5, 7, 9, 12, 14, 18, 20, 25, 30, 34, 37, 39, 40, 42, 45, 48, 50, 55]
# second_list = [2, 5, 7, 10, 14, 18, 21, 25, 29, 33, 34, 37, 39, 41, 44, 48, 49, 52, 55, 60]
# # thelist=first_list+second_list
# # print([i for i in set(thelist) if thelist.count(i) > 1])
# list=[i for i in first_list if i in second_list]
# print(list)
# #4
# word=input("enter a word")
# num=int(input("enter a num"))
# list=[]
# for i in range(0, len(word), num):
#     list.append(word[i])
# print(list)
# # l = [word[i] for i in range(0, len(word), num)]
# # print(l)
# ##5
# len = int(input("entr the length of your list"))
# list = []
# for i in range(len):
#     num = int(input("enter a num dor your list"))
#     list.append(num)
# l = [i for i in range(0, len-1) if list[i]<list[i+1]]
# print(sum(l))
# #6
# test_list = [777 ,543 ,777 ,81 ,10 ,777 ,21 ,21 ,543 ,22 ,777 ,10 ,543 ,22 ,10]
# max = 0
# res = test_list[0]
# for i in test_list:
#     freq = test_list.count(i)
#     print(freq)
#     if freq > max:
#         max = freq
#         res = i
# print("Most frequent number is : " + str(res))
# print(test_list.count(res))
##
# max = 0
# dict={}
# for i in test_list:
#     dict[i]=test_list.count(i)
#     if dict[i] >max:
#         max= dict[i]
#         value = {i for i in dict if dict[i] == max}
#         print(value)
# #
# ##7
# from random import *
#
# list=[5,4,8,1]
# list2=[]
# for i in range(len(list)):
#     ran = randrange(0, len(list))
#     while list[ran] in list2:
#         ran = randrange(0, len(list))
#     list2.append(list[ran])
#     print(list2)
# ##8
# first_list = ["father", "kayak", "madam", "Ronaldo", "Noa", "David"]
# second_list = ["xavi", "Xman", "banana", "aoN", "madam", "kayak"]
# re_list = [x[::-1] for x in second_list]
#
# def countList(first_list, re_list):
#     return [item for pair in zip(first_list, re_list + [0])
#             for item in pair]
# print(countList(first_list, re_list))
# join=countList(first_list, re_list)
# for i in join:
#     if join.count(i)>1:
#         join.remove(i)
# print(join)
# #9
# MONEY=50
# shopping_list = ["eggs", "milk", "chocolate", "banana", "salt", "chips"]
# prices = {
# "eggs": 20.2,
# "yogurt": 5,
# "cheese": 20,
# "milk": 6.75,
# "chocolate": 15.5,
# "cornflakes": 25.3,
# "banana": 2,
# "apple": 3.1,
# "salt": 1.8,
# "chips": 13}
# shopping_list = ["eggs", "milk", "chocolate", "banana", "salt", "chips"]
# list=[prices[i] for i in shopping_list]
# off_b=sum(list)
# list2=[]
# for i in list:
#     x= off_b-MONEY
#     if x<=i:
#         list2.append(i)
#         list2.sort()
# value = {i for i in prices if prices[i]==list2[0]}
# print("The product that needs to be removed is",  value)
# print("your change is", off_b-list2[0])
# # 10
# num = 1
# rates = []
# subjects = []
# sub_ = input("enter your subject, 'stop' to exit :")
# while sub_ != "stop":
#     subjects.append(sub_)
#     sub_ = input("enter your subject, 'stop' to exit :")
#     num += 1
# for i in range(num - 1):
#     print("Rate the subject:", subjects[i - 1], "between 1 -", num - 1)
#     rate = int(input())
#     while rate in  rates:
#         print("Rate the subject:", subjects[i - 1], "between 1 -", num - 1)
#     rates.append(rate)
#
#
# dict = dict(zip(rates, subjects))
#
# rates.sort()
#
# amount = int(input("how many subject do you want"))
# rates=rates[0:amount]
# for i in rates:
#     print(dict[i])
#

# ##11
# comedy_movie = []
# thriller_movie = []
# horror_movie = []
# drama_movie = []
# dict = {"comedy": comedy_movie, "thriller": thriller_movie, "horror": horror_movie, "drama": drama_movie}
# exit = 1
#
# while exit == 1:
#     qes1 = input("if you want to add a movie, enter 1. else, enter 5")
#
#     while qes1 == "1":
#         movie_name = input("enter the name of the movie that you would like to add")
#         movie_genre = input("enter the name of the movie genre ")
#         if movie_genre in dict.keys():
#             dict[movie_genre] += [movie_name]
#             qes1 = input("if you want to add a movie, enter 1. else, enter 5")
#         else:
#             print("Error, invalid genre")
#
#     print(dict)
#     qes2 = input("if you want to remove a movie, enter 2.else, enter 5 ")
#
#     while qes2 == "2":
#         movie_name = input("enter the name of the movie that you would like to remove")
#         movie_genre = input("enter the name of the movie genre ")
#         if movie_genre in dict.keys():
#             if movie_genre == "drama":
#                 drama_movie.remove(movie_name)
#             elif movie_genre == "thriller":
#                 thriller_movie.remove(movie_name)
#             elif movie_genre == "horror":
#                 horror_movie.remove(movie_name)
#             elif movie_genre == "comedy":
#                 comedy_movie.remove(movie_name)
#
#             qes2 = input("if you want to remove a movie, enter 2.else, enter 5")
#         else:
#             print("Error, the movie", movie_name, "was not found in the database")
#     print(dict)
#     exit = input("if you want to exit, enter 2, to stay 1")



# Sorting dictionary by values using sorted()
# Example dictionary
my_dict = {'apple': 5, 'banana': 2, 'orange': 8, 'grape': 3}
print(my_dict)


sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))

# Printing the sorted dictionary
print(sorted_dict)

#     print(ran_vote)
#     num_vote.append(ran_vote.count(i))
#     ran_vote.sort()
#     # num_vote = ran_vote.sort()
#     # win = max(num_vote)
#     # print(win)
#     # if ran_vote.count(i) == num_vote[-1]:
#     #     print("the winner is:", i, max(num_vote))
#     print(ran_vote)
# a=[i for i in ran_vote if max(ran_vote)]
# print("the winner is:",  max(num_vote))
#
#     # print(i, num_vote)