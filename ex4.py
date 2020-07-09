num = int(input(" Enter the number: "))

res = [i for i in range(1, num+1) if num%i == 0]

print(f" The list of divisor for the given number {num} are: {res}")