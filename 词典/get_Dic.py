filename = "现代汉语词典.txt"
dic = "大辞典.txt"
fp = open(dic,'w')
with open(filename) as t:
    for line in t:
        try:
            voca = line.split('】')[0].split('【')[1]
            if len(voca) >= 5 or len(voca) <= 1:
                continue
            else:
                fp.write(voca + '\n')
        except:
            continue
