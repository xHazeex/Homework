

def print_params(a=1, b='Str', c=True):
    print(a, b, c)

print_params()
print()
print_params(a=2, b='str2', c=False)
print()
print_params(b=25,)
print()
print_params(c=[1,2,3])
print()

value_list = [1, 'str', True]
values_dict = {'a' : 'False', 'b' : True, 'c' : 3.14}

print_params(*value_list)
print()
print_params(**values_dict)
print()

value_list_2 = [2, 'str2']
print_params(*value_list_2,42)