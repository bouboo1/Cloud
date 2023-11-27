# python实现汉诺塔-自动化测试脚本部分报告

## 代码

```yml
name: Python CI

on: [push]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.x

    - name: Install dependencies
      run: python -m pip install --upgrade pip
           pip install -r requirements.txt

    - name: Run tests
      run: pytest test_hanoi.py --capture=no
```

## 内容

actions/checkout@v2：用于检出代码仓库

actions/setup-python@v2：用于设置Python环境

python -m pip install --upgrade pip：升级pip工具

pip install -r requirements.txt：安装项目所需的依赖项
- 请确保在代码仓库的根目录下有一个名为`requirements.txt`的文件，里面包含所有必要的Python包及其版本信息。

  `pytest test.py --capture=no`：运行测试脚本

- 请注意，你需要确保在仓库中有一个名为`test.py`的测试文件，其中包含需要运行的测试代码。

通过将上述配置文件保存为`.github/workflows/python.yml`（或其他合适的文件名），并将其推送到您的GitHub代码仓库中，GitHub Actions将会在每次推送代码时自动执行这个流程。

当你推送代码后，GitHub将自动运行配置文件中定义的步骤，在虚拟环境中设置Python环境，安装依赖项，然后运行测试脚本。
