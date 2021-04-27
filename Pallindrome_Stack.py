# Python3 implementation of the approach
stack = []
top = -1

# push function
def push(ele: str):
	global top
	top += 1
	stack[top] = ele

# pop function
def pop():
	global top
	ele = stack[top]
	top -= 1
	return ele

# Function that returns 1
# if str is a palindrome
def isPalindrome(string: str) -> bool:
	global stack
	length = len(string)

	# Allocating the memory for the stack
	stack = ['0'] * (length + 1)

	# Finding the mid
	mid = length // 2
	i = 0
	while i < mid:
		push(string[i])
		i += 1

	# Checking if the length of the string
	# is odd, if odd then neglect the
	# middle character
	if length % 2 != 0:
		i += 1

	# While not the end of the string
	while i < length:
		ele = pop()

		# If the characters differ then the
		# given string is not a palindrome
		if ele != string[i]:
			return False
		i += 1
	return True

# Driver Code
if __name__ == "__main__":

	string = "madam"

	if isPalindrome(string):
		print("Yes")
	else:
		print("No")

