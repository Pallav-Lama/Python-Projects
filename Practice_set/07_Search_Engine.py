def matchingWords(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return(score)

# Sentences = ["An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.",
# ''' Stories that have morals and messages behind them are always powerful. In fact, it’s crazy just how powerful a 200 word story can be.

# Our last article of short stories became so popular, that we decided to create another list, in which every story has a simple moral behind it.

 

# The 10 Best Short Moral Stories
# Some of these stories are very short and basic. In fact some are so basic they’re most likely featured in children’s books somewhere. However, the strength of the message remains the same.

# Here’s some more of the best short moral stories:

 

# 1. An Old Man Lived in the Village
# Short Moral Stories - An Old Man

# An old man lived in the village. He was one of the most unfortunate people in the world. The whole village was tired of him; he was always gloomy, he constantly complained and was always in a bad mood.

#    The TOP 5 Success Lessons from Eminem
# Play Video
# The longer he lived, the more bile he was becoming and the more poisonous were his words. People avoided him, because his misfortune became contagious. It was even unnatural and insulting to be happy next to him.

# He created the feeling of unhappiness in others.

# But one day, when he turned eighty years old, an incredible thing happened. Instantly everyone started hearing the rumour:''',
# '''People have been coming to the wise man, complaining about the same problems every time. One day he told them a joke and everyone roared in laughter.

# After a couple of minutes, he told them the same joke and only a few of them smiled. ''', '''A salt seller used to carry the salt bag on his donkey to the market every day.

# On the way they had to cross a stream. One day the donkey suddenly tumbled down the stream and the salt bag also fell into the water. The salt dissolved in the water and hence the bag became very light to carry. The donkey was happy.

# Then the donkey started to play the same trick every day.

# The salt seller came to understand the trick and decided to teach a lesson to it. The next day he loaded a cotton bag on the donkey.

# Again it played the same trick hoping that the cotton bag would be still become lighter.''']

sentences = ["Python is Good", "This is good", "Python is not a python snake", 
"Python is not a python snake but it is a program interpreter named python"]

query = input("Enter a search string query: ")
scores = [matchingWords(query, sentence) for sentence in sentences]
sortedSentScores = [sentScore for sentScore in sorted(zip(scores, sentences), reverse= True)]
# print(sortedSentScores)

print(f"{len(sortedSentScores)} results found! \n")
for score, item in sortedSentScores:
    print(f" \"{item}\": with a score of {score}")