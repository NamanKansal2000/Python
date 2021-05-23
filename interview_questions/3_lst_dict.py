def list_to_dict(keys, values):
    d = dict(zip(keys, values))
    print(d)
    dict_to_tuple(d)


def dict_to_tuple(d):
    for i in d.items():
        print(i)


keys = [1,2,3]
values = ["one", 'two', 'three']
list_to_dict(keys, values)
