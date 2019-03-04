def eval_upos(gold_filename, pred_filename):
    gold_pos = []
    pred_pos = []
    gold_tag = []
    pred_tag = []   
    pred = open("en_pred.conllu", "r", encoding = "utf-8")
    gold = open("en_gold.conllu", "r", encoding = "utf-8")
    pred_line = pred.readline()
    gold_line = gold.readline()
    while gold_line != "":
        gold_clean = gold_line.strip()
        gold_pos.append(gold_line.split("\t"))
        gold_line = gold.readline()
    for i in range(len(gold_pos)):
        if len(gold_pos[i]) > 3:
            gold_tag.append(gold_pos[i][3])
    print(gold_tag)
    while pred_line != "":
        pred_clean = pred_line.strip()
        pred_pos.append(pred_line.split("\t"))
        pred_line = pred.readline()
    for i in range(len(pred_pos)):
        if len(pred_pos[i]) > 3:
            pred_tag.append(pred_pos[i][3])
    print(pred_tag)


    acc = len([gold_tag[i] for i in range(0,len(gold_tag)) if gold_tag[i] == pred_tag[i]]) / len(gold_tag)
    return acc




    
    
    
