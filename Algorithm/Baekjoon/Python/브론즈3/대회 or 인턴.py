from math import ceil
n,male,k = map(int, input().split())

female = n // 2
minimum = min(female, male)

left_female = n - minimum * 2
left_male = male - minimum
k -= left_female + left_male
k = max(0, k)
k = ceil(k / 3)

print(minimum - k)