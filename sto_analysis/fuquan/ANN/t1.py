import numpy as np
X = np.array([ [0,0,1],[0,1,1],[1,0,1],[1,1,1] ])
y = np.array([[0,1,1,0]]).T
syn0 = 2*np.random.random((3,4)) - 1
#print syn0
syn1 = 2*np.random.random((4,1)) - 1
#print syn1
for j in xrange(6000):
    l1 = 1/(1+np.exp(-(np.dot(X,syn0))))
    #print l1
    l2 = 1/(1+np.exp(-(np.dot(l1,syn1))))
    #print l2
    l2_delta = (y - l2)*(l2*(1-l2))
    l1_delta = l2_delta.dot(syn1.T) * (l1 * (1-l1))
    syn1 += l1.T.dot(l2_delta)
    syn0 += X.T.dot(l1_delta)


print np.dot(X,syn0)
print l2
print syn1
print l2
