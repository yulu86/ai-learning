import joblib


def load_model():
    # 加载模型
    return joblib.load('models/music-recommender.joblib')


def predict():
    model = load_model()

    # 预测21岁男性喜欢的音乐类型 和 22岁女性喜欢的音乐类型
    return model.predict([
        [21, 1],
        [22, 0]
    ])


if __name__ == '__main__':
    predictions = predict()
    print(predictions)
