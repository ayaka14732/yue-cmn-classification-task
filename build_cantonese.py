import yaml

length_limit = 2000
i = 0

f1 = open('test.text.txt', 'w')
f2 = open('test.label.txt', 'w')

with open('cantonese.1.yaml') as f:
    obj = yaml.safe_load(f)
def write_to_file(obj):
    global i
    for sentence_group in obj[3]['conversations']:
        for sentence in sentence_group:
            if len(sentence) >= 8:
                print(sentence, file=f1)
                print(0, file=f2)
                i += 1
                if i == length_limit:
                    return
write_to_file(obj)

with open('henry.txt') as f:
    for line in f:
        sentence = line.rstrip('\n')
        if len(sentence) >= 8:
            print(sentence, file=f1)
            print(0, file=f2)
            i += 1
            if i == length_limit:
                break

f2.close()
f1.close()
