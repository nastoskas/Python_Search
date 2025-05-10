import csv
from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier

def read_file(file_name):
    with open(file_name) as doc:
        csv_reader = csv.reader(doc, delimiter=',')
        dataset = list(csv_reader)[1:]
    return dataset

if __name__=='__main__':
    dataset = read_file('car.csv')

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7*len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7*len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier.fit(train_x,train_y)
    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    accuracy = 0
    pred = classifier.predict(test_x)
    for predicted, true in zip(pred, test_y):
        if predicted == true:
            accuracy+=1

    accuracy = accuracy / len(test_set)

    print(f'accuracy: {accuracy}')

    features_importance = list(classifier.feature_importances_)
    print(f'Feature importance: {features_importance}')

    most_important_feature = features_importance.index(max(features_importance))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = features_importance.index(min(features_importance))
    print(f'Least important feature: {least_important_feature}')

    train_x2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        train_x2.append(row)

    test_x2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != most_important_feature]
        test_x2.append(row)

    train_x3 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        train_x3.append(row)

    test_x3 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != least_important_feature]
        test_x3.append(row)

    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x2, train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x3, train_y)

    print(f'Depth (without most important feature): {classifier2.get_depth()}')
    print(f'Number of leaves (without most important feature): {classifier2.get_n_leaves()}')

    print(f'Depth (without least important feature): {classifier3.get_depth()}')
    print(f'Number of leaves (without least important feature): {classifier3.get_n_leaves()}')

    accuracy2 = 0

    pred = classifier2.predict(test_x2)
    for predicted, true in zip(pred, test_y):
        if predicted == true:
            accuracy2 += 1

    accuracy2 = accuracy2 / len(test_set)

    print(f'accuracy (without most important feature): {accuracy2}')

    accuracy3 = 0

    pred = classifier3.predict(test_x3)
    for predicted, true in zip(pred, test_y):
        if predicted == true:
            accuracy3 += 1

    accuracy3 = accuracy3 / len(test_set)

    print(f'accuracy (without least important feature): {accuracy3}')

