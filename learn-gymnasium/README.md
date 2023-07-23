# Gymnasium学习

本项目包含`OpenAI Gymnasium`学习。

## 运行指南

### 环境配置

```bash
# 创建conda环境
conda create -n LearnGym python=3.10
conda activate LearnGym
```

### 安装 `pytorch`

> 参考: [Pytorch | Get Started](https://pytorch.org/get-started/locally/)

- #### Windows

```bash
conda install pytorch=2.0.0 torchvision pytorch-cuda=11.8 -c pytorch -c nvidia
```

- #### Mac

```bash
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

### 测试GPU

- #### Windows

```bash
python utils/check_gpu_status.py
```

- #### Mac

```bash
python3 utils/check_gpu_status_mps.py
```

### 安装依赖

```bash
python3 -m pip install -r requirements.txt
```