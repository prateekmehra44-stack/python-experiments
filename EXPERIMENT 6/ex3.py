N = int(input("Enter N: "))
scores = list(map(int, input("Enter scores: ").split()))

unique_scores = list(set(scores))
unique_scores.sort()

print(unique_scores[-2])