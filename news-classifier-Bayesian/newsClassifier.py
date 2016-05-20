import random #to shuffle the training set
import time #to time learning and and classification
import nltk
from textblob import TextBlob #to tokenize our sentences into words
from nltk.corpus import stopwords #to remove unwanted stop words 
from textblob.classifiers import NaiveBayesClassifier

def get_list_tuples(read_file):
    list_tuples = []
    with open(read_file,"r") as r:
        c=0
        for line in r:
            tabsep = line.strip().split('\t')
            msg = TextBlob(tabsep[1])
            try:
                words=msg.words
            except:
                continue
            for word in words:
                if word not in stopwords.words() and not word.isdigit():
                    list_tuples.append((word.lower(),tabsep[0]))
            c+=1 #limiting factor begins
            if c==6: #limiting factor ends
                return list_tuples

a = time.time()
entire_data = get_list_tuples("NewsCollection.txt")
print "It took "+str(time.time()-a)+" seconds to import data" 
print 'data imported'
random.seed(1)
random.shuffle(entire_data)
train = entire_data[:9]
test = entire_data[7:9]
print 'training data'
a = time.time()
cl = NaiveBayesClassifier(train)
print "It took "+str(time.time()-a)+" seconds to train data"
print 'data trained, now checking accuracy:'
accuracy = cl.accuracy(test)
print "accuracy: "+str(accuracy)
print cl.classify("Women MPs reveal sexist tauntsWomen MPs endure shocking levels of sexist abuse at the hands of their male counterparts, a new study shows.Male MPs pretended to juggle imaginary breasts and jeered melons as women made Commons speeches, researchers from Birkbeck College were told. Labour's Yvette Cooper said she found it hard to persuade Commons officials she was a minister and not a secretary. Some 83 MPs gave their answers in 100 hours of taped interviews for the study Whose Secretary are You, minister.The research team, under Professor Joni Lovenduski, had set out to look at the achievements and experiences of women at Westminster. But what emerged was complaints from MPs of all parties of sexist barracking in the Chamber, sexist insults and patronising assumptions about their abilities. Barbara Follet, one of the so-called Blair Babes elected in 1997, told researchers: I remember some Conservatives - whenever a Labour woman got up to speak they would take their breasts - imaginary breasts - in their hands and wiggle them and say 'melons' as we spoke. Former Liberal Democrat MP Jackie Ballard recalled a stream of remarks from a leading MP on topics such as women's legs or their sexual persuasion. And ex-Tory education secretary Gillian Shepherd remembered how one of her male colleagues called all women Betty.When I said, 'Look you know my name isn't Betty', he said, 'ah but you're all the same, so I call you all Betty'. Harriet Harman told researchers of the sheer hostility prompted by her advancement to the Cabinet: Well, you've only succeeded because you're a woman. Another current member of the Cabinet says she was told: Oh, you've had a very fast rise, who have you been sleeping with? Even after the great influx of women MPs at the 1997 general election, and greater numbers of women in the Cabinet, female MPs often say they feel stuck on the edge of a male world.Liberal Democrat Sarah Teather, the most recent female MP to be elected, told researchers: Lots of people say it's like an old boys club. I've always said to me it feels more like a teenage public school - you know a public school full of teenagers. Prof Joni Lovenduski, who conducted the study with the help of Margaret Moran MP and a team of journalists, said she was shocked at the findings. We expected a bit of this but nothing like this extent. We expected to find a couple of shocking episodes. But she said there was a difference between the experiences of women before the 1997 intake and afterwards. This was mainly because there were more women present in Parliament who were not prepared to put up with the sexist attitudes they came across, Prof Lovenduski said. But she added: ") 
print cl.classify("eat weight lose weight exercise")
