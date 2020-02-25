def func1 (str1, str2):
    if str1 > str2:
        result_str = str1[1:]
    else:
        result_str = str2[:-1]
    return result_str   

response1_str = input("Enter a string:")
response2_str = input("Enter a second string:")
print(func1(response1_str, response2_str)) 
print(func1(response2_str, response1_str))