import shelve
from sklearn.naive_bayes import MultinomialNB

samplename = raw_input('Enter the sample_trans file: ')
predictname = raw_input('Enter the predict file: ')

a = shelve.open(predictname)
b = shelve.open(samplename)
sample = b['res']['sample']
labels = b['res']['label']

clf = MultinomialNB()
clf.fit(sample,labels)

expobj = a['res']
l = len(expobj)

for i in range(l):
    #if clf.predict(expobj[i].reshape(1,-1)) == ['chat']:
    print(clf.predict(expobj[i].reshape(1,-1)))
#print expobj