import sys

total = 0
correct = 0

with open('test.label.txt') as f1, open(sys.argv[1]) as f2:
    for a, b in zip(f1, f2):
        total += 1
        if a == b:
            correct += 1

print(f'Accuracy: {correct / total * 100:.2f}%')
