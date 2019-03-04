def eval_upos(gold_filename, pred_filename):
    gold_pos = []
    pred_pos = []
    gold_tag = []
    pred_tag = []   
    pred = open(pred_filename, "r", encoding = "utf-8")
    gold = open(gold_filename, "r", encoding = "utf-8")
    pred_line = pred.readline()
    gold_line = gold.readline()
    while gold_line != "":
        gold_clean = gold_line.strip()
        gold_pos.append(gold_line.split("\t"))
        gold_line = gold.readline()
    for i in range(len(gold_pos)):
        if len(gold_pos[i]) > 4:
            gold_tag.append(gold_pos[i][4])
    print(gold_tag)

    while pred_line != "":
        pred_clean = pred_line.strip()
        pred_pos.append(pred_line.split("\t"))
        pred_line = pred.readline()
    for i in range(len(pred_pos)):
        if len(pred_pos[i]) > 4:
            pred_tag.append(pred_pos[i][4])
    print(pred_tag)

acc = eval_upos ("en_gold.conllu", "en_pred.conllu")
print("English accuracy:", (acc , 4))


