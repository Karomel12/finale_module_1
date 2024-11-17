immutable_var = 12, 'Карамель', True, [23,123,543]
print(immutable_var)
# Мы можем изменять только список, а кортеж остается неизменным!
# immutable_var [2] = 'Banana'
# out = TypeError: 'tuple' object does not support item assignment

# В то же время мы можем изменять список внутри кортежа
immutable_var [3] [2] = '32' # out = (12, 'Карамель', True, [23, 123, '32'])
#                                                                     ^^^^^
print(immutable_var)
print("------------------------------------------------------------")
mutable_list = [32131,143645,'Apple',True]
mutable_list [1] = "coconut"
mutable_list [0] = False
mutable_list [-1] = 9023590
print(mutable_list)