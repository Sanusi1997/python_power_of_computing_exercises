my_dict = {'bill':100, 'zach':'hi mom', 'laurie':'bye mom'}
try:
    result = ''
    key_str = input("Enter a key:")
    val = my_dict[key_str]
    result = result + val
except KeyError:
    result = 'hi mom'
except TypeError:
    result = '100'
else:
    result = result+" "+'all done'
finally:
    if result.isdigit():
        result = int(result) + 10
print(result)