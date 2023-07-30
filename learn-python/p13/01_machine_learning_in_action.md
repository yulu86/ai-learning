# Machine learning in action

## Steps

1. Import the Data
2. Clean the Data
3. Split the Data into Training/Test Sets
4. Create a Model
5. Train the Model
6. Make Predictions
7. Evaluate and Improve

## Libraries

- Numpy
- Pandas
- MatPlotLib
- Scikit-Learn

## 创建`conda`环境

```bash
conda create -n ml python=3.10.6
conda activate ml
```

## Jupyter Notebook

### 安装和启动 `jupyter notebook`

```bash
# 安装 jupyter notebook
python -m pip install --upgrade --force-reinstall --no-cache-dir --no-warn-script-location jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple

# 启动 jupyter notebook 服务
jupyter notebook
```

### 访问 `jupyter notebook`
- 访问 [http://localhost:8888/tree](http://localhost:8888/tree)

### 下载数据集
- 访问 [kaggle.com | Video Game Sales](https://www.kaggle.com/datasets/gregorut/videogamesales)

### 在 `jupyter notebook` 中加载数据集

```python
import pandas as pd
df = pd.read_csv('vgsales.csv')
df
```

![](./images/jupyter-notebook_load_csv.png)