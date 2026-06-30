# 招聘市场数据看板 — 部署指南

## 一、环境准备

```bash
# 1. 安装依赖
pip install streamlit plotly pandas numpy pillow

# 2. 确认已有数据文件
ls cleaned_recruitment_data.csv
```

## 二、快速版


```bash
# 先生成图片
python step3_visualize.py

# 启动看板
streamlit run app_quick.py
```

浏览器自动打开 `http://localhost:8501`

## 三、进阶版（交互式 Plotly 图表）

> 适合：需要悬停查看、侧边栏筛选、指标卡片

```bash
streamlit run app_interactive.py
```

功能亮点：
    侧边栏多维度筛选（城市/技能/学历/薪资范围）
    顶部 5 个 KPI 指标卡片
    所有图表可悬停查看详细数据
    热力图单元格显示薪资+样本量    
## 四、局域网共享

```bash
# 让同一网络的其他人也能访问
streamlit run app_interactive.py --server.address 0.0.0.0 --server.port 8501
```

其他人通过 `http://你的IP:8501` 访问

## 五、公网部署（免费方案）

### 方案 A：Streamlit Community Cloud
1. 将代码推送到 GitHub 仓库
2. 访问 https://share.streamlit.io
3. 选择仓库 → 选择 `app_interactive.py` → 部署
4. 获得 `https://your-app.streamlit.app` 公开链接

### 方案 B：Docker 部署
```dockerfile
# Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8501
CMD ["streamlit", "run", "app_interactive.py", "--server.address=0.0.0.0"]
```

```bash
# requirements.txt
streamlit
plotly
pandas
numpy
pillow
```

```bash
docker build -t recruitment-dashboard .
docker run -p 8501:8501 recruitment-dashboard
```

### 方案 C：云服务器（阿里云/腾讯云）
```bash
# SSH 登录服务器后
git clone <你的仓库>
cd <项目目录>
pip install streamlit plotly pandas numpy

# 用 nohup 后台运行
nohup streamlit run app_interactive.py --server.port 8501 --server.address 0.0.0.0 &

# 开放安全组 8501 端口
```

## 六、文件结构

```
项目目录/
├── cleaned_recruitment_data.csv   # 清洗后的数据
├── step3_visualize.py             # 原始可视化脚本（生成 PNG）
├── app_quick.py                   # 快速版看板（展示 PNG）
├── app_interactive.py             # 进阶版看板（交互式）
├── panel_a_*.png ~ panel_h_*.png  # 生成的图表
└── requirements.txt               # 依赖清单
```
