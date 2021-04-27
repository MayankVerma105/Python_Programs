'''def reverse(str1):
    reverseStr = ' '
    for i in range(len(str1)):
        reverseStr = str[1] + reverseStr
    return reverseStr
'''
def reverse(str1):
    if str1 == ' ':
        return str1
    else:
        return str[1:]` + str1[0]
print(reverse("Hello"))
