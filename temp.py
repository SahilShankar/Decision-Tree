from sklearn import tree
features = [[0,1,1],[1,0,0],[2,1,1],[0,0,1],[2,1,0],[1,0,1]]
labels = [1,1,0,1,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)
print(clf.predict([[0,0,0]]))