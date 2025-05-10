import csv

from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OrdinalEncoder

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

    classifier = RandomForestClassifier(n_estimators=150, criterion='entropy', random_state=0)
    classifier.fit(train_x,train_y)

    accuracy = 0
    pred = classifier.predict(test_x)
    for predicted, true in zip(pred, test_y):
        if predicted == true:
            accuracy += 1

    accuracy = accuracy / len(test_set)

    print(f'accuracy: {accuracy}')

    feature_importance = list(classifier.feature_importances_)
    print(f'Feature importances: {feature_importance}')

    most_important_feature = feature_importance.index(max(feature_importance))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = feature_importance.index(min(feature_importance))
    print(f'Least important feature: {least_important_feature}')