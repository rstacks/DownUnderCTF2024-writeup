import random

def apply_perm(s, PERM):
	assert len(s) == 16
	return ''.join(s[PERM[p]] for p in range(16))

def decodeFirst():

	plaintext = "aaaabbbbccccdddd"
	ciphertext = "ccaccdabdbdbbada"

	PERM = list(range(16))
	random.shuffle(PERM)

	while True:
		found_list = list(range(16))
		candidate = apply_perm(plaintext, PERM)
		if candidate == ciphertext:
			#print("Found it.", PERM)
			return PERM
			break
		
		incomplete_PERM = ["a" for i in range(16)]
		for i in range(16):
			if candidate[i] == ciphertext[i]:
				incomplete_PERM[i] = PERM[i]
				try:
					found_list.remove(PERM[i])
				except ValueError:
					print(f"that was weird, found {PERM[i]} more than once...")

		#print("Didn't work. Here's progress:", incomplete_PERM)
		random.shuffle(found_list)
		#print("Here's the remaining positions:", found_list)
		index = 0
		for i in range(16):
			if incomplete_PERM[i] == "a":
				PERM[i] = found_list[index]
				index += 1
			else:
				PERM[i] = incomplete_PERM[i]
		#print("And here's the next PERM we'll try:", PERM)
		#print()

def decodeSecond():

	plaintext = "abcdabcdabcdabcd"
	ciphertext = "bcaadbdcdbcdacab"

	PERM = list(range(16))
	random.shuffle(PERM)

	while True:
		found_list = list(range(16))
		candidate = apply_perm(plaintext, PERM)
		if candidate == ciphertext:
			#print("Found it.", PERM)
			return PERM
			break
		
		incomplete_PERM = ["a" for i in range(16)]
		for i in range(16):
			if candidate[i] == ciphertext[i]:
				incomplete_PERM[i] = PERM[i]
				try:
					found_list.remove(PERM[i])
				except ValueError:
					print(f"that was weird, found {PERM[i]} more than once...")

		#print("Didn't work. Here's progress:", incomplete_PERM)
		random.shuffle(found_list)
		#print("Here's the remaining positions:", found_list)
		index = 0
		for i in range(16):
			if incomplete_PERM[i] == "a":
				PERM[i] = found_list[index]
				index += 1
			else:
				PERM[i] = incomplete_PERM[i]
		#print("And here's the next PERM we'll try:", PERM)
		#print()

attempts = 0
while True:
	lst1 = decodeFirst()
	lst2 = decodeSecond()
	if lst1 == lst2:
		print("Found it.", lst1)
		break
	else:
		print("Not it:", lst1, lst2)
		print(f"That was attempt {attempts}")
		attempts += 1
