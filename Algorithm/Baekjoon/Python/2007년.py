M, D = map(int, input().split())

days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]

dayGap = sum(month[:M]) + D

print(days[(dayGap - 1) % 7])