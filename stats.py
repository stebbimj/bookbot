def get_num_words(text):
    return str(len(text.split()))

def get_book_text(filepath):
    with open("/home/stebbimj/workspace/github.com/boot.dev/bookbot/" + filepath) as f:
        file_contents = f.read()
    return file_contents
    #print(file_contents)

def check_freq(x):
    from collections import OrderedDict
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    
    SortedFreq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    for item in SortedFreq:
        if item[0].isalnum() == True and item[0].isdigit() == False:
            print(item[0] + ": " + str(item[1]))

    #print(freq.values()).sort()
