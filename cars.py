import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset

if __name__ == '__main__':
    dataSet = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataSet])

    #prvite 70% za treniranje
    train_set = dataSet[:int(0.7 * len(dataSet))]
    #x e vlez za modelot, y e izlez - klasa
    train_x = [row[:-1]for row in train_set]
    train_y = [row[-1] for row in train_set] #klasata poslednata kolona
    train_x = encoder.transform(train_x)

    #ostanatite 30%
    test_set = dataSet[int(0.7 * len(dataSet)):]
    test_x = [row[:-1]for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    predicted_class = classifier.predict([test_x[0]])[0]
    true_class = test_y[0]
    for i in range(len(test_set)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]

        if predicted_class == true_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)
    print(f'accuracy: {accuracy}')

    entry = [el for el in input().split(' ')]
    encoded_entry = encoder.transform([entry])
    predicted_class = classifier.predict(encoded_entry)

    print(predicted_class)
