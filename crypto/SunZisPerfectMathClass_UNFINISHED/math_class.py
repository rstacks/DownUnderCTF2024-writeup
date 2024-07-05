# If soldiers stand 3 in a row, 2 should remain
def passes3(num_soldiers):
  return num_soldiers % 3 == 2

# If soldiers stand 5 in a row, 4 should remain
def passes5(num_soldiers):
  return num_soldiers % 5 == 4

# If soldiers stand 7 in a row, 5 should remain
def passes7(num_soldiers):
  return num_soldiers % 7 == 5

for i in range(1000, 1100):
  if passes3(i) and passes5(i) and passes7(i):
    print(f"There are {i} soldiers remaining")
