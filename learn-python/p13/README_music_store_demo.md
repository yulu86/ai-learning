# Music Store Demo

[`jupyter notebook` 使用](./README.md) | 音乐商店Demo

## 激活`conda`环境

```bash
conda activate ml
```

> 注意：Mac环境以下命令中 `python` 替换为 `python3`

## Jupyter Notebook

### 启动 `jupyter notebook` 服务

```bash
jupyter notebook
```

### 访问 `jupyter notebook`

- 访问 [http://localhost:8888/tree](http://localhost:8888/tree)

### 下载数据集

- 访问 [music csv](http://bit.ly/music-csv)

### 使用 `jupyter notebook` 访问 [music_store](./music_store.ipynb)

## 使用代码训练和预测

```bash
# 训练模型
python train_music_recommender.py

# 预测
python predict_music_recommender.py
```
