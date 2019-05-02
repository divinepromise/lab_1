def first(word):
	return word[0]


def last(word):
	return word[-1]


def middle(word):
	return word[1:-1]



def is_palindrome(word):
	if len(word) <= 1:
		return True
	elif first(word) == last(word):
		return True
	elif middle(word) == word[::-1]:
		return True
	else:
		return False

is_palindrome("noon")
