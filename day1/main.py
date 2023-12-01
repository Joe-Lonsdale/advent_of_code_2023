filename = "input.txt"

file = open(filename, "r")

total = 0
i = 0
for line in file:
    i+=1
    nums = [1,2,3,4,5,6,7,8,9]
    nums = [str(num) for num in nums]
    num_words = ['one','two','three','four','five','six','seven','eight','nine']
    head = 0
    tail = len(line)-1
    first,last = None,None
    while not first or not last:
        for word in num_words:
            if word in line[:head+1]:
                first = num_words.index(word)+1
        if(line[head] in nums):
            first = line[head]
        if(not first):
            head+=1


        for word in num_words:
                if word in line[tail:]:
                    last = num_words.index(word)+1
        if(line[tail] in nums):
            last = line[tail]
        if(not last):
            tail-=1
    print(first)
    print(last)
    print(line)
    total += int(first) * 10 + int(last)


print(total)