# 共享数字红利：同行业企业间的数字拘束涓滴效应 — 复现工程

本仓库旨在复现论文《共享数字红利：同行业企业间的数字拘束涓滴效应》的实证分析。该复现工程以 Python 为主，包含数据预处理、示例分析 Notebook、可复用脚本与环境说明。

主要内容

- notebooks/: Jupyter notebooks（数据生成/清洗、实证回归、稳健性检验与图表）
- src/: 可复用的 Python 脚本（数据生成、处理与分析）
- data/: （不包含真实数据）下载脚本与合成示例数据
- results/: 产出表格与图像（受限/大文件请本地运行后自行上传）
- replication_plan.md: 复现步骤与环境说明

注意

- 本仓库不会上传受限或大型原始数据。示例 notebook 使用合成数据或提供下载脚本（若论文使用公开数据，我会提供下载与处理指引）。

如何开始（快速入门）

1. 克隆仓库并进入目录：
   git clone https://github.com/Yang-ANN727/-
   cd -
2. 建议使用虚拟环境：
   python -m venv .venv
   source .venv/bin/activate  # macOS / Linux
   .venv\Scripts\activate     # Windows
3. 安装依赖：
   pip install -r requirements.txt
4. 在 notebooks/ 打开并运行 00_data_prep.ipynb 和 01_analysis.ipynb。

联系方式

如果你想让我改用 R 实现、加入具体的论文数据下载脚本，或把文件提交到不同分支，请回复说明。
