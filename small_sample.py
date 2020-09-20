## sample test
import torch
dataset = torch.load("/home/bqw/nlp_data/cnndm/cnndm_bert_ext/cnndm.train.0.bert.pt")
expr_data = []
count=0
for ex in dataset:
    if count>= 3:
        break
    expr_data.append(ex)
    count+=1


torch.save(expr_data, "/home/bqw/paper/test/decodesum/src/expr/expr.pt")
