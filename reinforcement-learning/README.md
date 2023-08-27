# 强化学习

## 资料

- [强化学习圣经 | Reinforcement Learning：An introduction 第二版](http://incompleteideas.net/book/RLbook2020.pdf)
- [gymnasium](https://gymnasium.farama.org/)
- [微信读书 | 深度强化学习算法与实践:基于PyTorch的实现](https://weread.qq.com/web/reader/1db32480813ab6d74g012a53?)

---

## 环境搭建

### 创建`conda`环境

```sh
conda create -n rl python=3.10.6
conda activate rl
```

> 注意：在mac上使用`python3`替换以下命令中的`python`


### 安装`PyTorch`

#### Windows:

```bash
# 使用 GPU 训练需要手动安装完整版 PyTorch
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# 运行程序脚本测试 PyTorch 是否能成功调用 GPU
python .\utils\check_gpu_status.py
```

#### macOS (Apple Silicon):

```bash
# 使用 GPU 训练需要手动安装 Apple Silicon 版 PyTorch
conda install pytorch::pytorch=2.0.1 torchvision torchaudio -c pytorch

# 运行程序脚本测试 PyTorch 是否能成功调用 GPU
python utils/check_gpu_status_mps.py
```

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