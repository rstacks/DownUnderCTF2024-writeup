# Unknown, this is a test array
PERM_inverse = [8, 9, 3, 11, 10, 14, 1, 4, 12, 5, 13, 6, 7, 0, 15, 2]

def reverse_perm(scrambled_message):
  scramble_map = {}
  for i in range(16):
    scramble_map[PERM_inverse[i]] = scrambled_message[i]

  unscrambled_message = ""
  for i in range(16):
    unscrambled_message += scramble_map[i]

  return unscrambled_message

print(reverse_perm("ccaccdabdbdbbada"))
print(reverse_perm("bcaadbdcdbcdacab"))
print(reverse_perm("owuwspdgrtejiiud"))

