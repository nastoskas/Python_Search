import csv
from sklearn.naive_bayes import GaussianNB

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]

    dataset_v2 = []
    for row in dataset:
        row_v2 = [int(el) for el in row]
        dataset_v2.append(row_v2)
    return dataset_v2

if __name__=='__main__':
    dataSet = read_file("medical_data.csv")
    train_set = dataSet[:int(0.7*len(dataSet))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = dataSet[int(0.7*len(dataSet)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()

    classifier.fit(train_x,train_y)
    accuracy = 0
    predictions = classifier.predict(test_x)

    for gt_class, pred_class in zip(test_y,predictions):
        if gt_class == pred_class:
            accuracy += 1

    accuracy = accuracy / len(test_set)
    print(f'accuracy {accuracy}')

    entry = [int(el) for el in input().split(" ")]

    print(classifier.predict([entry])[0])
