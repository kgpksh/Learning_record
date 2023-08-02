import sys

def diffMinutes() :
    start, end = sys.stdin.readline().rstrip().split()

    startHour, startMinute = map(int, start.split(':'))
    endHour, endMinute = map(int, end.split(':'))

    return endHour * 60 + endMinute - startHour * 60 - startMinute


answer = 0
for _ in range(5) :
    answer += diffMinutes()

print(answer)