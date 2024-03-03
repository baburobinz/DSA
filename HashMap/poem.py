poem = open('poem.txt','r')

num_of_words = {}


for line in poem:

    word_list = line.split(' ')

    for word in word_list:

        word=word.replace('\n','').replace(',','').replace(':','').replace(';','').replace('.','').replace('â€”','')

       

        if word in num_of_words:
            num_of_words[word]+=1

        else:

            num_of_words[word]=1


print(num_of_words)

