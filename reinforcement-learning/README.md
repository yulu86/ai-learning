# 强化学习

## 资料

- [强化学习圣经 | Reinforcement Learning：An introduction 第二版](http://incompleteideas.net/book/RLbook2020.pdf)
- [gymnasium](https://gymnasium.farama.org/)

---

## 环境搭建

### 创建`conda`环境

```sh
conda create -n rl python=3.10.6
conda activate rl
```

> 注意：在mac上使用`python3`替换以下命令中的`python`

### 安装依赖

```sh
python -m pip install -r requirement.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装`gymnasium`依赖
```sh
python -m pip install gymnasium[all]
```

### 测试

```sh
python ./src/00_gymnasium_demo.py
```


### 启动`jupyter notebook`

```sh
python -m notebook
```

访问[http://localhost:8888/tree](http://localhost:8888/tree)


### 去激活环境

```sh
conda deactivate rl
```