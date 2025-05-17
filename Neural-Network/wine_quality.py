from sklearn.neural_network import MLPClassifier

def read_dataset():
    data = []
    with open('winequality.csv') as f:
        _ = f.readline()
        while True:
            line = f.readline().strip()
            if line == '':
                break
            parts = line.split(';')
            data.append(list(map(float, parts[:-1])) + parts[-1:])
    return data

def divide_sets(dataset):
    bad_classes = [x for x in dataset if x[-1] == 'bad']
    good_classes = [x for x in dataset if x[-1] == 'good']

    train_set = bad_classes[:int(len(bad_classes) * 0.7)] + good_classes[:int(len(good_classes) * 0.7)]
    validation_set = bad_classes[int(len(bad_classes) * 0.7) : int(len(bad_classes) * 0.8)] + good_classes[int(len(good_classes) * 0.7) : int(len(good_classes) * 0.8)]
    test_set = bad_classes[int(len(bad_classes) * 0.8):] + good_classes[int(len(good_classes) * 0.8):]

    return train_set,validation_set,test_set

if __name__=='__main__':
    dataset = read_dataset()
    train_set, validation_set, test_set = divide_sets(dataset)

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    validation_x = [row[:-1] for row in validation_set]
    validation_y = [row[-1] for row in validation_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = MLPClassifier(5, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(100, activation='relu', learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier.fit(train_x,train_y)
    classifier2.fit(train_x,train_y)
    classifier3.fit(train_x,train_y)

    final_classifier = None
    max_accuracy = 0
    for i, clf in enumerate([classifier,classifier2,classifier3]):
        validation_pred = clf.predict(validation_x)
        val_accuracy = 0
        for true, pred in zip(validation_y,validation_pred):
            if true == pred:
                val_accuracy += 1

        val_accuracy = val_accuracy / len(validation_y)
        print(f'Klasifikatorot {i} ima tochnost so validvcisko mnozestvo od {val_accuracy}')

        if val_accuracy > max_accuracy:
            max_accuracy = val_accuracy
            final_classifier = clf

    accuracy = 0
    predictions = final_classifier.predict(test_x)
    for true, pred in zip(test_y, predictions):
        if true == pred:
            accuracy += 1

    accuracy = accuracy / len(test_y)
    print(f'Tocnosta so testirackoto mnozestvo e: {accuracy}')
