N = int(input())
for i in range(1, N+1):
    print(" "*(N-i)+"*"*(2*i-1), end="")
    print()
for j in range(1, N):
    print(" "*j+"*"*(2*N-2*j-1), end="")
    print()