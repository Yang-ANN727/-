# 复现计划（replication_plan.md）

目标：复现论文主要表格与图形，确保能够得到相同方向与显著性的结果，并提供可复现的代码与随机种子。

环境
- Python 版本：3.10+（推荐 3.11）
- 主要库见 requirements.txt
- 随机种子：42（在数据生成与抽样处固定）

数据
- 本仓库默认使用合成数据作为示例（位于 data/synthetic_data.csv，可用 src/data_prep.py 生成）。
- 若你有论文原始数据，请将其放在 data/ 下（不要提交私有数据到公开仓库），并更新 notebooks 中的路径。

复现步骤
1. 安装依赖：pip install -r requirements.txt
2. 运行 notebooks/00_data_prep.ipynb：生成或下载并清洗数据
3. 运行 notebooks/01_analysis.ipynb：执行基准回归、稳健性检验并绘图
4. 比较输出表格与论文报告的系数、标准误与 R²

可扩展工作
- 使用论文的真实面板数据并复现不同稳健性检验（聚类、双向固定效应、系统 GMM 等）
- 将结果打包成交互式报告（nbconvert / papermill / binder）

负责人
- 复现者：Yang-ANN727
- 联系方式：在 GitHub 上发 issue 或 PR
