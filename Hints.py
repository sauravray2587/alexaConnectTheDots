import wikipedia

#print(wikipedia.search("Barak"))
#page = wikipedia.page("Barak Obama")
#print(page.content)
#print(wikipedia.search("barak obama",results = 10,suggestion = True))
next_node = "Into the wild book"
def gethint(next_node):
    pronouns = ["he","she","it","them","they","their"]
    help_verbs = ["is","am","are","was","were","been","have","has","had","do","did","does","would","will","shall","should","can","could","being","am"]
    page = wikipedia.page(next_node)
    content = page.content
    content = content.lower()
    content = list(content)
    key =0 
    for i in range(0,len(content)):
        if key==0:
            if content[i]=='(':
                key =1
            if content[i]=='.':
                key = 2
        if key ==1:
            if content[i]==')':
                key = -1
            if key!=-1:
                content[i] = ''
            else:
                content[i] = '' 
                key = 2
        if key==2:
            break
    content = "".join(content)
    sentences = content.split(".")
    pronoun = None
    for i in range(1,len(sentences)):
        words1 = sentences[i].split(" ")
        for word in words1:
            if word in pronouns:
                pronoun = word
                break
        if(pronoun!=None):
            break
    i = None
    words = sentences[0].split(" ")
    for i in range(0,len(words)):
        if words[i] in help_verbs:
            break
    final_sentence = pronoun
    for i in range(i,len(words)):
        final_sentence = final_sentence + " "+ words[i]
    return final_sentence                                 
print(gethint(next_node))
