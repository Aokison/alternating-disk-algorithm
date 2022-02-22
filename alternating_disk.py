def alternating_disk(n, L):
  swaps = 0
  for i in range(n):
    pair = i
    for j in range(i,n):
      L[pair], L[pair+1] = L[pair+1], L[pair]
      swaps+=1
      pair+=2
  return L, swaps

n = int(input("Enter positive integer: "))
L = []
for x in range(n):
  L.append("Light")
  L.append("Dark")
rearrangedL, swaps = alternating_disk(n,L)
print("Number of swaps:", swaps)
print("Rearranged List:", rearrangedL)