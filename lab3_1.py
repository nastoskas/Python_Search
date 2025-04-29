from zad1_dataset import dataset
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder

if __name__ == '__main__':
    dataSet = dataset

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataSet])

    split_index = int(0.25 * len(dataSet))
    eval_set = dataSet[:split_index]
    train_set = dataSet[split_index:]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    eval_x = [row[:-1] for row in eval_set]
    eval_y = [row[-1] for row in eval_set]
    eval_x = encoder.transform(eval_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y)

    # Tochnost 1
    predictions = classifier.predict(eval_x)
    correct = sum(1 for true, pred in zip(eval_y, predictions) if true == pred)
    accuracy1 = correct / len(eval_y)
    print("Tochnost 1:", accuracy1)

    # Читање индекси од стандарден влез
    try:
        indices = list(map(int, input().split()))
    except ValueError:
        print("Vnesete validni celi broevi.")
        exit(1)

    correct2 = 0
    total2 = len(indices)

    for i in indices:
        if i < 0 or i >= len(eval_set):
            print(f"Nevaliden indeks: {i}")
            continue

        sample = eval_set[i]
        x = encoder.transform([sample[:-1]])
        y_true = sample[-1]

        y_pred = classifier.predict(x)[0]
        proba = classifier.predict_proba(x)

        if y_pred == y_true:
            correct2 += 1

        print(y_pred)
        print(proba)

    accuracy2 = correct2 / total2
    print("Tochnost 2:", accuracy2)
