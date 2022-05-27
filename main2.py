# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(test):
    test = open("story.txt","r")
    text = test.read()
    return text
   
   


def count_words(text):
    text =read_file_content("./story.txt")
    a=text.lower()
    dct_cnt={}
    count=0
    list_s=a.split()
    for word in list_s:
        if word in dct_cnt:
            count= dct_cnt[word]
            count +=1
            dct_cnt.update({word: count})
        else:
            count=1
            dct_cnt.update({word:count})
    return dct_cnt
   

print(count_words("./story.txt"))
