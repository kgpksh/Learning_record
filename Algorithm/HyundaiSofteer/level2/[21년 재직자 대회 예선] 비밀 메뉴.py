import sys

sys.stdin.readline().rstrip()

secret = sys.stdin.readline().rstrip()
userInput = sys.stdin.readline().rstrip()

outputs = {True : 'secret', False : 'normal'}

print(outputs[secret in userInput])