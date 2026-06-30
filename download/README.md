# 招聘市场数据分析与可视化看板

本项目旨在通过自动化数据采集、清洗、分析与可视化，构建一个多维度的招聘市场数据看板。该看板能够深入洞察不同城市、学历、工作经验和技能方向对薪资及招聘需求的影响，为高等教育与培训体系的改革提供数据支撑和决策依据。

## 核心功能

1.  **自动化数据采集**：利用 Selenium 模拟浏览器行为，从主流招聘网站（如 51job）采集招聘岗位数据，支持多城市、多关键词并行采集，并具备失败重试与仿真数据降级机制。
2.  **数据清洗与标准化**：对原始招聘数据进行深度清洗，包括薪酬正则化（统一为 k/月）、学历与经验字段标准化、城市信息提取，并基于 IQR 准则过滤异常离群值，确保数据质量。
3.  **多维统计分析**：对清洗后的数据进行描述性统计、交叉分析（如学历 × 工作经验下的平均薪酬矩阵）和相关性分析，揭示招聘市场关键特征。
4.  **交互式可视化看板**：基于 Streamlit 和 Plotly 构建交互式数据看板，提供丰富的图表（箱线图、柱状图、折线图、热力图等），支持多维度筛选（城市、技能、学历、薪资范围），并实时更新 KPI 指标卡。
5.  **静态图表生成**：提供脚本一键生成 8 张高质量 PNG 格式的静态图表，方便快速查看和报告输出。

## 项目结构

```
project/
├── code/
│   ├── app_interactive.py         # 进阶版交互式数据看板（Plotly + Streamlit）
│   ├── app_quick.py               # 快速版看板（展示静态 PNG 图表）
│   ├── crawl.py                   # 早期版本的数据采集脚本（与 step1_crawl.py 功能类似）
│   ├── run_all.py                 # 一键运行整个数据处理流程的入口脚本
│   ├── step1_crawl.py             # 第一阶段：多城市招聘数据采集 Agent (Selenium)
│   ├── step2_clean_analyze.py     # 第二阶段：数据清洗、标准化与统计分析引擎
│   └── step3_visualize.py         # 第三阶段：生成多维静态可视化图表 (Matplotlib/Seaborn)
├── images/
│   ├── panel_a_*.png              # 静态图表输出：学历薪资箱线图
│   ├── panel_b_*.png              # 静态图表输出：城市招聘需求柱状图
│   ├── panel_c_*.png              # 静态图表输出：经验薪资趋势折线图
│   ├── panel_d_*.png              # 静态图表输出：城市平均薪资柱状图
│   ├── panel_e_*.png              # 静态图表输出：技能薪资溢价水平条形图
│   ├── panel_f_*.png              # 静态图表输出：技术方向需求量柱状图
│   ├── panel_g_*.png              # 静态图表输出：经验壁垒与应届生困境双轴图
│   └── panel_h_*.png              # 静态图表输出：学历经验联合薪资热力图
├── output/
│   ├── cleaned_recruitment_data.csv # 清洗并标准化后的招聘数据
│   └── raw_recruitment_data.csv   # 原始采集的招聘数据
└── DEPLOY_README.md               # 部署指南（本 README 的原始版本，已整合）
```

## 快速开始

### 1. 环境准备

确保您的系统已安装 Python 3.8+。推荐使用 `venv` 创建虚拟环境。

```bash
# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows

# 安装项目依赖
pip install streamlit plotly pandas numpy pillow selenium webdriver-manager
```

**注意**：`step1_crawl.py` 使用 Selenium 进行数据采集，需要安装 Chrome 浏览器，并确保 `chromedriver` 与您的 Chrome 版本匹配。`webdriver-manager` 库会自动管理 `chromedriver` 的下载和配置，但如果遇到问题，可能需要手动指定 `CHROME_BINARY_PATH` 和 `chromedriver_path`。

### 2. 数据采集与处理

运行 `run_all.py` 脚本将依次执行数据采集、清洗分析和静态图表生成。

```bash
python code/run_all.py
```

执行完成后，`output/` 目录下会生成 `raw_recruitment_data.csv` 和 `cleaned_recruitment_data.csv`，`images/` 目录下会生成 8 张静态图表。

### 3. 启动数据看板

本项目提供两种数据看板模式：

#### 3.1 快速版看板（展示静态图表）

此版本直接加载 `images/` 目录下的 PNG 图片进行展示，启动速度快，但图表不具备交互性。

```bash
streamlit run code/app_quick.py
```

#### 3.2 进阶版看板（交互式 Plotly 图表）

此版本加载 `output/cleaned_recruitment_data.csv`，并使用 Plotly 动态生成交互式图表。支持侧边栏筛选、KPI 指标卡、图表悬停详情等功能。

```bash
streamlit run code/app_interactive.py
```

运行成功后，浏览器会自动打开 `http://localhost:8501` 查看看板。

## 部署

### 1. 局域网共享

如果您希望同一局域网内的其他设备也能访问您的看板，可以在启动时指定 `server.address` 为 `0.0.0.0`：

```bash
streamlit run code/app_interactive.py --server.address 0.0.0.0 --server.port 8501
```

其他设备通过 `http://您的IP地址:8501` 访问。

### 2. 公网部署（免费方案）

#### 2.1 Streamlit Community Cloud

1.  将您的项目代码推送到 GitHub 仓库。
2.  访问 [Streamlit Community Cloud](https://share.streamlit.io)。
3.  选择您的 GitHub 仓库，并指定 `code/app_interactive.py` 作为主应用文件进行部署。
4.  部署成功后，您将获得一个公开的 `https://your-app.streamlit.app` 链接。

#### 2.2 Docker 部署

创建一个 `Dockerfile` 和 `requirements.txt` 文件：

**`requirements.txt`**
```
streamlit
plotly
pandas
numpy
pillow
selenium
webdriver-manager
```

**`Dockerfile`**
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "code/app_interactive.py", "--server.address=0.0.0.0"]
```

构建并运行 Docker 镜像：

```bash
docker build -t recruitment-dashboard .
docker run -p 8501:8501 recruitment-dashboard
```

#### 2.3 云服务器部署（阿里云/腾讯云等）

1.  通过 SSH 登录到您的云服务器。
2.  克隆您的项目代码：`git clone <您的仓库地址>`。
3.  进入项目目录：`cd <项目目录>`。
4.  安装依赖：`pip install streamlit plotly pandas numpy pillow selenium webdriver-manager`。
5.  使用 `nohup` 在后台运行看板：
    ```bash
nohup streamlit run code/app_interactive.py --server.port 8501 --server.address 0.0.0.0 > streamlit.log 2>&1 &
    ```
6.  确保在云服务器的安全组中开放 `8501` 端口。

## 可视化图表示例

本项目生成以下主要可视化图表，用于支撑招聘市场分析：

1.  **Panel A: 学历门槛 - 薪资分布箱线图**：展示不同学历要求下的薪资分布情况，揭示学历对薪资的影响。
2.  **Panel B: 核心城市招聘需求量柱状图**：对比各城市招聘岗位的数量，反映不同城市的就业机会。
3.  **Panel C: 工作经验 × 平均月薪趋势折线图**：分析工作经验积累与平均月薪的增长关系。
4.  **Panel D: 各城市平均薪资对比柱状图**：直观展示各城市平均月薪水平，并与全国均值进行对比。
5.  **Panel E: 前沿技能薪资溢价对比图**：量化不同技能方向相对于市场平均水平的薪资溢价，突出高价值技能。
6.  **Panel F: 技术方向需求量排行**：统计不同技术方向的招聘岗位数量，反映市场对各类技术人才的需求。
7.  **Panel G: 经验壁垒与应届生困境双轴图**：结合岗位占比和平均月薪，分析不同工作经验要求下的就业难度和薪资水平。
8.  **Panel H: 学历 - 工作经验联合薪资热力图**：通过热力图形式，展示不同学历和工作经验组合下的平均薪资，发现高薪组合。

## 贡献

欢迎对本项目提出建议或贡献代码。请通过 GitHub Pull Request 或 Issue 进行交流。

## 许可证

本项目采用 MIT 许可证。
