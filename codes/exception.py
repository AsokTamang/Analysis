try:
    a=1
    b='s'
    print(a/0)
except TypeError as TE:
    print (f'Exception handled:,{TE}')
except ZeroDivisionError as ZE:
    print(f'Exception handled:,{ZE}')
