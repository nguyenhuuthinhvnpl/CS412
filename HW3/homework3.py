#Stub submission file for CS412 Homework 3.

def get_sequences(file, minsup):
    myFile = open(file, "r")
    lines = myFile.readlines()
    seqs = []
    num_seqs = 0
    my_dict = {}
    all_seqs = []
    my_seqs = []
    num_lines = len(lines)
    # lines_
    # for cnt in range(0,num_lines-1):
    for line in lines:
        line = line.split(', ')[1]
        line = line.split('<')[1]
        line = line.split('>')[0]
        n = len(line)
        p = 0
        temp = []
        for i in range(n):
            for leng in range(i+1,n+1):
                sel_seq = line[i: leng]
                # print(sel_seq)
                if(sel_seq in temp):
                    p = p + 1 
                else: 
                    temp.append(sel_seq)

        for kk in range(0, len(temp)):
            all_seqs.append(temp[kk])
        temp.clear()
    
        
        all_seqs.sort()
    rep = 0
    uniq = 0
    num_seqs = len(all_seqs)
    for x in range(0, num_seqs):
        if(all_seqs[x] in my_seqs):
            rep = rep + 1
        else:
            my_seqs.append(all_seqs[x])
            uniq = uniq + 1
    # print(my_seqs)

    for y in range(0, uniq):
        item = my_seqs[y]
        item_count = all_seqs.count(my_seqs[y])
        
        if(item_count >= minsup):
            my_dict.update({item : item_count})

    return (my_dict)
