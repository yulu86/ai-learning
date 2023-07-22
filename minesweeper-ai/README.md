# 扫雷游戏AI

本项目包含经典游戏《扫雷》的本体和可以自动进行游戏的人工智能代理。

## 运行指南

### 环境配置

```bash
# 创建conda环境
conda create -n MineSweeper python=3.10
conda activate MineSweeper
```

> 参考: [Pytorch | Get Started](https://pytorch.org/get-started/locally/)

#### - Windows

```bash

```

#### - Mac

```bash
conda install pytorch::pytorch torchvision torchaudio -c pytorch
```

### 测试GPU

```bash
python3 utils/check_gpu_status_mps.py
```

### 安装依赖

```bash
python3 -m pip install -r requirements.txt
```

### 运行

#### 运行游戏

```bash
cd main
python3 game.py
```
