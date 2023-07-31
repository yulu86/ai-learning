## 创建`conda`环境

```bash
conda create -n rl python=3.10.6
conda activate rl
```

> 注意：Mac环境以下命令中 `python` 替换为 `python3`

## 安装依赖

```bash
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

> 更新依赖
> ```bash
> python -m pip install --upgrade --force-reinstall --no-cache-dir --no-warn-script-location -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
> ```

## Jupyter Notebook

### 启动 `jupyter notebook` 服务

```bash
jupyter notebook
```

### 访问 `jupyter notebook`

- 访问 [http://localhost:8888/tree](http://localhost:8888/tree)