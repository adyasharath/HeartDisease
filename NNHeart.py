from keras.models import Sequential
from keras.layers import Dense
from pandas import read_csv
import matplotlib.pyplot as plt


trainPath = '~/HeartDisease/heart.csv'
trainData = read_csv(trainPath)

testPath = "~/HeartDisease/heart.csv"
testData = read_csv(testPath)

arrayTrain = trainData.values
arrayTest = testData.values

X_train = arrayTrain[:,0:13] 
Y_train = arrayTrain[:,13]

X_test = arrayTest[:, 0:13]
Y_test = arrayTest[:, 13]

model = Sequential()
model.add(Dense(12, input_dim=13, init='uniform', activation='relu'))
model.add(Dense(12, init='uniform', activation='sigmoid', use_bias=True))
model.add(Dense(10, init='uniform', activation='sigmoid', use_bias=True))
model.add(Dense(8, init='uniform', activation='sigmoid', use_bias=True))
model.add(Dense(8, init='uniform', activation='sigmoid', use_bias=True))
model.add(Dense(1, init='uniform', activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, Y_train, nb_epoch = 1500, validation_data = (X_test, Y_test))

scores = model.evaluate(X_test, Y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


MyList = history.history['accuracy']
MyFile=open('Accuracy.txt','a')

for element in MyList:
    MyFile.write(str(element))
    MyFile.write('\n')
MyFile.close()


MyList = history.history['loss']
MyFile=open('MSE.txt','a')

for element in MyList:
    MyFile.write(str(element))
    MyFile.write('\n')
MyFile.close()



plt.plot(history.history['accuracy'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Iteration')
plt.legend(['Train'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.title('Mean square error')
plt.ylabel('Mean square error')
plt.xlabel('Iteration')
plt.legend(['Train'], loc='upper right')
plt.show()