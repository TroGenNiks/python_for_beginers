import wikipedia
dic = {
    "nature":"the phenomena of the physical world collectively."
    # here u can add multiple words with meanings
    }
print("enter the word")
a= input()
print(dic[a])
print(wikipedia.summary(a))