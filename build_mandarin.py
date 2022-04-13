import csv

length_limit = 2000
i = 0

f1 = open('test.text.txt', 'a')
f2 = open('test.label.txt', 'a')

with open('Gossiping-QA-Dataset-2_0.csv', newline='') as csvfile:
    for _, sentence in csv.reader(csvfile, delimiter=',', quotechar='"'):
        if len(sentence) >= 8:
            print(sentence, file=f1)
            print(1, file=f2)
            i += 1
            if i == length_limit:
                break

f2.close()
f1.close()
