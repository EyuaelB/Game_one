# numlist = [4, 5, 6, 9, 1, 7, 13, 8, 2]
# sm  = float('inf')
# ssm  = float('inf')
# for num in numlist:
#     if num <= sm:
#         sm, ssm = num, sm
#     elif num < ssm:
#         ssm = num
# print(sm)
# print(ssm
# 


# """Counting list elements and changin to Dictionary
# """

# # my_laptop = ['Hp', 'Hp', 'Dell', 'Acer']

# # final_lap_cout= {}
# # for lap in my_laptop:
# #     if lap not in final_lap_cout:
# #         final_lap_cout.update({lap : 1})
# #     else:
# #         final_lap_cout.update({lap:final_lap_cout[lap]+1})
        
# # print(final_lap_cout)



# """List comprehension
# """

# list1 = [i for i in range(1, 10)]
# print(list1)

# """Dictionary comprehension
# """

# dict1 = {i:i*i for i in range(1, 5)}
# print(dict1)

# """Lambda function
# """

# even = lambda n :list(range(0,n,2))

# a = print(even(10))




# ser = (1,2,3)
# print(ser[2])



# dfv = {}

# print(type(dfv))






list1= []
my_inputs = input("entter numbers with comma separation \n")

for ch in my_inputs:
    if ch in ['0','1','2','3','4','5','6','7','8','9']:
        list1.append(int(ch))
        
        
print(list1)
