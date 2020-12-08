"""
FETCH REWARDS EXERCISE
Job position - Data Engineer

Title - Finding similarity between two texts
Applicant/Author - Devavrat Bapat
Email id - bapat.dev@gmail.com

"""


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


def preprocess(text):
    print('Inside preprocess')

    text = lowerCaseWords(text)
    text = wordStemming(text)
    text = removeSymbols(text)
    text = removeStopWords(text)
    text = splitText(text)
    text = removeStopWordsPostSplit(text)
    return text


""" 
Code for finding similarity
Steps involved -

2.1 convert text into lower case words
2.2 word stemming (not implemented)
2.3 remove punctuation symbols (except apostrphe)
2.4 remove stopwords
2.5 convert text into a list of words
2.6 remove stop words post lemmatisation

"""

# Step 2.1

# Turn everything small caps

def lowerCaseWords(text):
    print('Inside lowerCase words')
    text = text.lower()
    return text


# Step 2.2

# Convert words into their root words

def wordStemming(text):
    print('Inside word stemming')
    return text


# Step 2.3

# Remove punctuation symbols from text

def removeSymbols(text):
    print('Inside remove symbols')
    punctuationSymbols = ['.', ',', '?', '!', ';', ':', '-', '{', '}', '[', ']', '(', ')', '"', '*', '/', '&', '^', '%','$', '#', '@', '+']
    for symbol in punctuationSymbols:
        text = text.replace('' + symbol, '')
    return text


# Step 2.4

# Remove stop words from the text

def removeStopWords(text):
    print('Inside remove stop words')
    stopWords = ["a", "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren't",
                 "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can't", "cannot",
                 "could", "couldn't", "did","didn't", "do", "does", "doesn't", "doing", "don't", "down", "during", "each", "few", "for", "from",
                 "further", "had", "hadn't","has", "hasn't", "have", "haven't", "having", "he", "he'd", "he'll", "he's", "her", "here", "here's",
                 "hers", "herself", "him","himself", "his", "how", "how's", "i", "i'd", "i'll", "i'm", "i've", "if", "in", "into", "is", "isn't",
                 "it","it's", "its", "itself", "let's", "me", "more", "most", "mustn't", "my", "myself", "no", "nor", "not",
                 "of", "off","on", "once", "only", "or", "other", "ought", "our", "ours	", "ourselves", "out", "over", "own",
                 "same", "shan't", "she","she'd", "she'll", "she's", "should", "shouldn't", "so", "some", "such", "than", "that", "that's",
                 "the", "their", "theirs", "them","themselves", "then", "there", "there's", "these", "they", "they'd", "they'll", "they're", "they've",
                 "this", "those", "through", "to", "too","under", "until", "up", "very", "was", "wasn't", "we", "we'd", "we'll", "we're", "we've", "were",
                 "weren't", "what", "what's","when", "when's", "where", "where's", "which", "while", "who", "who's", "whom", "why", "why's", "with",
                 "won't", "would", "wouldn't","you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves"]

    for stopWord in stopWords:
        text = text.replace(' ' + stopWord + ' ', ' ')

    return text


# Step 2.5

# Turn text into multiple strings of individual words | Tokenization
def splitText(text):
    print('Inside split text')
    print(text)
    text = text.split()

    return text

# Step 2.6

# This step is being repeated to remove any stop words occuring due to punctuation symbols or at
#  the start or end of a sentence.

def removeStopWordsPostSplit(text):

    print('Inside remove stop words')
    stopWords = ["a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at",
                "be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did",
                "didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't",
                "has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him",
                "himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it",
                "it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off",
                "on","once","only","or","other","ought","our","ours	","ourselves","out","over","own","same","shan't","she",
                "she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them",
                "themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too",
                "under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's",
                "when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't",
                "you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]


    for stopWord in stopWords:
        if stopWord in text:
            text.remove(''+stopWord)

    return text


# Generating log
def lg(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

# Calculate document frequency, Term frequency, Inverse document frequency and  common words

def dftf(text1_prep, text2_prep):
    print('Inside dftf')
    All_DF = {}
    text1_TF = {}
    text2_TF = {}
    commonWords = {}
    idf = {}
    tfidf1 = {}
    tfidf2 = {}

    All_DF = {key: 0 for key in text1_prep + text2_prep}
    text1_TF = {key: 0 for key in text1_prep + text2_prep}
    text2_TF = {key: 0 for key in text1_prep + text2_prep}
    commonWords = {key: 0 for key in text1_prep + text2_prep}
    idf = {key: 0 for key in text1_prep + text2_prep}
    tfidf1 = {key: 0 for key in text1_prep + text2_prep}
    tfidf2 = {key: 0 for key in text1_prep + text2_prep}

    for word in text1_prep:
        text1_TF[word] = text1_TF[word] + 1
        All_DF[word] = All_DF[word] + 1
        commonWords[word] = 1

    for word in text2_prep:
        text2_TF[word] = text2_TF[word] + 1
        All_DF[word] = All_DF[word] + 1
        if commonWords[word] == 1:
            commonWords[word] = 2
        else:
            commonWords[word] = 1

    # Total words in each text

    text1_totalWords = sum(text1_TF.values(), 0.0)
    text2_totalWords = sum(text2_TF.values(), 0.0)

    for k, v in text1_TF.items():
        text1_TF[k] = text1_TF[k] / text1_totalWords

    for k, v in text2_TF.items():
        text2_TF[k] = text2_TF[k] / text2_totalWords

    # Find IDF
    for k, v in idf.items():
        idf[k] = lg(1 + 2 / commonWords[k])

    # Find tf.idf

    for k, v in tfidf1.items():
        tfidf1[k] = text1_TF[k] * idf[k]

    for k, v in tfidf2.items():
        tfidf2[k] = text2_TF[k] * idf[k]

    print('Total t1 =', text1_totalWords)
    print('Total t2 =', text2_totalWords)

    return All_DF, text1_TF, text2_TF, text1_totalWords, text2_totalWords, commonWords, idf, tfidf1, tfidf2



def cosineSimilarity(tfidf1, tfidf2):
    total = 0

    for k, v in tfidf1.items():
        total = total + (tfidf1[k] * tfidf2[k])

    print('length 1 = ', len(tfidf1.keys()))
    print('length 2 = ', len(tfidf2.keys()))

    sqr1 = 0
    sqr2 = 0

    tfidf1sqr = {}
    tfidf2sqr = {}

    for k, v in tfidf1.items():
        tfidf1sqr[k] = tfidf1[k] ** 2

    for k, v in tfidf2.items():
        tfidf2sqr[k] = tfidf2[k] ** 2

    norm_a = (sum(tfidf1sqr.values()) ** 0.5)
    norm_b = (sum(tfidf2sqr.values()) ** 0.5)

    print('Divisor1 = ', norm_a)
    print('Divisor2 = ', norm_b)
    score = total / (norm_a * norm_b)
    print('Final score =',score)
    return round(score, 2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def findingSimilarity():
    try:

        # This statement will print the type of method we are receiving
        print('Method =',request.method)

        # We are only going to proceed if the the method is POST. We will invoke the similarity() method and pass the
        # texts to compare.
        if request.method == "POST":
            text1 = request.form["text1"]
            text2 = request.form["text2"]
            return similarity(text1,text2)

    except Exception as e:
        print(e)
        return render_template("index.html")

@app.route("/similarity'")
def similarity(text1='',text2=''):

    print('Text 1 = ',text1)
    print('Text 2 =', text2)


    if (text1 =='') | (text2 == ''):
        return f"<p>Either text is empty. Hence score = <b>{0}</b></p>"

    print('We are here')
    # Below we will pre-process the texts from the user
    text1_prep = preprocess(text1)
    text2_prep = preprocess(text2)

    # We will use the TF.IDF technique to generate the vectors for each text. You can view the results at every stage.
    df, tf1, tf2, total1, total2, cw, idf, tfidf1, tfidf2 = dftf(text1_prep, text2_prep)

    # We will use cosine similarity on the vectors to find the similarity in 0 to 1 scale.
    finalScore = cosineSimilarity(tfidf1, tfidf2)
    return f"<p> Please note that the similarity score is between 0 and 1.<br>0 -> Texts with no common words<br>1 -> " \
           f"Texts that are exactly same<br><br><b>Similarity between these documents =</b> <h1>{finalScore}</h1> "


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

