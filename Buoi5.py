from sklearn.datasets import load_iris
X, y = load_iris(return_X_y=True)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)

#Multinominal Narrow Bayes
from sklearn.naive_bayes import MultinomialNB
Mnb = MultinomialNB()
Mnb.fit(X_train, y_train)
y_pred_Mnb = Mnb.predict(X_test)
from sklearn.metrics import accuracy_score, confusion_matrix
ac_Mnb = accuracy_score(y_test, y_pred_Mnb)
cm_Mnb = confusion_matrix(y_test, y_pred_Mnb)
print("Multinominal Narrow Bayes:\n", "accuracy=", ac_Mnb, "\n confusion matrix: \n", cm_Mnb)

#Gaussian Naive Bayes
from sklearn.naive_bayes import GaussianNB
Gnb = GaussianNB()
Gnb.fit(X_train, y_train)
y_pred_Gnb = Gnb.predict(X_test)
ac_Gnb = accuracy_score(y_test, y_pred_Mnb)
cm_Gnb = confusion_matrix(y_test, y_pred_Mnb)
print("Gaussian Narrow Bayes:\n", "accuracy=", ac_Gnb, "\n confusion matrix: \n", cm_Gnb)

#k-NN
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
y_pred_KNN = neigh.predict(X_test)
ac_KNN = accuracy_score(y_test, y_pred_KNN)
cm_KNN = confusion_matrix(y_test, y_pred_KNN)
print("k-NN:\n", "accuracy=", ac_KNN, "\n confusion matrix: \n", cm_KNN)