from zad2_dataset import dataset
from sklearn.naive_bayes import GaussianNB

if __name__ == '__main__':
    dataSet = dataset
    n = len(dataSet)
    quarter = n // 4

    # Поделба на 4 еднакви дела
    subset1 = dataSet[:quarter]
    subset2 = dataSet[quarter:2*quarter]
    subset3 = dataSet[2*quarter:3*quarter]
    test_set = dataSet[3*quarter:]

    def prepare_data(subset):
        x = [[float(val) for val in row[:-1]] for row in subset]
        y = [row[-1] for row in subset]
        return x, y

    x1, y1 = prepare_data(subset1)
    x2, y2 = prepare_data(subset2)
    x3, y3 = prepare_data(subset3)
    test_x, test_y = prepare_data(test_set)

    # Тренирање на 3 класификатори
    clf1 = GaussianNB().fit(x1, y1)
    clf2 = GaussianNB().fit(x2, y2)
    clf3 = GaussianNB().fit(x3, y3)

    # Пресметка на точноста
    correct = 0
    for features, true_label in zip(test_x, test_y):
        preds = [
            clf1.predict([features])[0],
            clf2.predict([features])[0],
            clf3.predict([features])[0]
        ]
        if preds.count(true_label) >= 2:
            correct += 1

    accuracy = correct / len(test_set)
    print(accuracy)

    # Предвидување од стандарден влез
    entry = [float(el) for el in input().split()]
    preds = [
        clf1.predict([entry])[0],
        clf2.predict([entry])[0],
        clf3.predict([entry])[0]
    ]

    if preds[0] == preds[1] == preds[2]:
        print(preds[0])
    else:
        print("klasata ne moze da bide odredena")
