with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'r') as f:
     print(f.readlines())  #reading multiple lines


#calculating the total points scored by players in whole tournament
with open("C:/Users/ashok/OneDrive/Desktop/change.txt",'r') as f:
    next(f)  #here we are skipping the very first line cause the very first line consists of the headings
    lines = f.readlines()
    data = {}
    for line in lines:
        line.strip()  #removing empty space from the beginning and the end of the line
        name,id,score = line.split('\t')
        data[name] = data.get(name,0) + int(score)  #here we are assuming the 0 as the default score
    print(data)
