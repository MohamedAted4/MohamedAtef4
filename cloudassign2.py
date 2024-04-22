from collections import Counter
import nltk
from nltk.corpus import stopwords

with open("random_paragraphs.txt", "r") as file:
    article = file.read()


stop_words = set(stopwords.words('english')) 

def remove_stop_words(sentence): 
    words = sentence.split() 
    
    filtered_words = [word for word in words if word not in stop_words] 
    
    return ' '.join(filtered_words)

filterarticle=remove_stop_words(article)

def frequency(sentence):
    words = sentence.split()
    word_frequency = Counter(words)
    sorted_word_frequency = word_frequency.most_common()
    
    print("Word frequency count (sorted in descending order):")
    for word, frequency in sorted_word_frequency:
        print(f"{word}: {frequency}")

countOfWordsofarticle= len(article.split())
count_stop_words_original = sum(1 for word in article.split() if word.lower() in stop_words)
countOfWordsoffiltered=len(filterarticle.split())

print("Count of Words in original article :",f"{countOfWordsofarticle:,}")
print("Count of Stop Words in original article:", f"{count_stop_words_original:,}")
print("Count of Words in filtered article :",f"{countOfWordsoffiltered:,}")

frequency(filterarticle)

print(filterarticle)
