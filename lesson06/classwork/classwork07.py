list_of_names = ['john', 'helen', 'nencie', 'jack']

def making_upper(string):
    return string.upper()

result = []
for name in list_of_names:
    result.append(making_upper(name))

print(result)

#2
print([making_upper(name) for name in list_of_names])

#3
print(list(map(making_upper, list_of_names)))

#4
print(list(map(lambda x, y: (x.upper(),y), list_of_names, list_of_names)))

#Filter
def func(extra_value, **kwargs):
    for k, v in kwargs:
        if v == extra_value:
           kwargs.pop(k)
           break
    return kwargs

extra_value = 'token'
kwargs = {'sum':12, 'id':124, 'token':'fhgfhjgkhkjhk'}
d1 = dict(filter(lambda kv: kv[1] != extra_value, kwargs.items()))
d2 = func(extra_value, **kwargs)
print(d1)

