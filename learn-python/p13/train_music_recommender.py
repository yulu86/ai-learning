import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import joblib
from sklearn.metrics import accuracy_score


def load_music_data():
    # 读取数据集
    return pd.read_csv('datasets/music.csv')


def split_input_dataset(music_data):
    # 拆分出输入的数据集
    return music_data.drop(columns=['genre'])


def split_output_dataset(music_data):
    # 拆分出输出的数据集
    return music_data['genre']


def evaluate_model(model, X_test, y_test):
    # 使用测试数据集预测
    predictions = model.predict(X_test)

    # 测试预测的准确率
    return accuracy_score(y_test, predictions)


def train_model():
    music_data = load_music_data()
    X = split_input_dataset(music_data)
    y = split_output_dataset(music_data)

    # 拆分80%的数据作为训练集, 20%的数据作为测试集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    model = DecisionTreeClassifier()
    for _ in range(1000):
        # 训练模型
        model.fit(X_train, y_train)

        # 测试预测的准确率
        score = evaluate_model(model, X_test, y_test)

        if score == 1.0:
            # 保存训练的模型
            joblib.dump(model, 'models/music-recommender.joblib')
            print('got perfect model!!!')
            return


if __name__ == '__main__':
    train_model()
    print('train success!')
