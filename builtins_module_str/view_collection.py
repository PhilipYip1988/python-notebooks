def view(collection):
    print('Index', '\t', 'Type'.ljust(20), '\t', 'Size'.ljust(6), '\t', 'Value'.ljust(30))
    for idx, obj in enumerate(collection):
        if '__len__' in dir(obj):
            size = len(obj)
        else:
            size = 1
        print(idx, '\t', str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)

def view_neg(collection):
    print('Index', '\t', 'Type'.ljust(20), '\t', 'Size'.ljust(6), '\t', 'Value'.ljust(30))
    for idx, obj in enumerate(collection):
        idx = idx - len(collection)
        if '__len__' in dir(obj):
            size = len(obj)
        else:
            size = 1
        print(idx, '\t', str(type(obj)).removeprefix("<class '").removesuffix("'>").ljust(20), '\t', str(size).ljust(6), '\t', str(obj).ljust(30), '\t',)