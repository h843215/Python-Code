def train_and_tag(train_file, test_words):
    f = open(train_file, 'r')
    dict = {}
    while True:
        line = f.readline()
        if not line:
            break
        elif line!='\n':
            tokens = line.split()
            tokens[1] = tokens[1].lower()
            if tokens[1] not in dict:
                dict[tokens[1]] = {}
            if tokens[3] in dict[tokens[1]]:
                dict[tokens[1]][tokens[3]] +=  1
            else:
                dict[tokens[1]][tokens[3]] = 1
        print(dict)

    
    results = []
    for i in range(len(test_words)):
        test_words[i] = test_words[i].lower()
    for i in range(len(test_words)):
        POS = []
        if test_words[i] not in dict:
            results.append('UNK')
        else:
            max_freq = max(dict[test_words[i]].values())
            print(max_freq)
            for key, value in dict[test_words[i]].items():
                if value == max_freq:
                    POS.append(key)
                    print(key)
            #print(dict[test_words[i]])
            results.append(min(POS))


    return results


#print(train_and_tag ("small_train.conllu",  [ "This", "is", "my", "wish" ]))
