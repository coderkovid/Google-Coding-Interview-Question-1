def add_one(given_array):
	carry = 1
	result = [i*0 for i in range(1, len(given_array)+1)]
	for i in range(len(given_array)-1, -1, -1):
		total = given_array[i] + carry
		if total == 10:
			carry = 1
		else:
			carry = 0
		result[i] = total % 10

	if carry == 1:
		result = [i*0 for i in range(1, len(given_array)+2)]
		result[0] = 1
	return result

print(add_one([9,9,9,9]))
print(add_one([1,2,3,4]))
print(add_one([1,2,9]))