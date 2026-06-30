"""
一键运行入口：依次执行数据采集 → 清洗分析 → 可视化展示
用法：python run_all.py
"""

import subprocess
import sys
import os

scripts = [
    ("step1_crawl.py",         "第一阶段：数据采集"),
    ("step2_clean_analyze.py", "第二~四阶段：数据清洗与特征分析"),
    ("step3_visualize.py",     "第五阶段：可视化展示"),
]

# 切换到脚本所在目录，确保 CSV 文件路径正确
os.chdir(os.path.dirname(os.path.abspath(__file__)))

for script, label in scripts:
    print(f"\n{'='*60}")
    print(f"  ▶ 开始执行 {label}")
    print(f"{'='*60}")
    result = subprocess.run([sys.executable, script], capture_output=False)
    if result.returncode != 0:
        print(f"[ERROR] {script} 执行失败，流程中止。")
        sys.exit(result.returncode)

print("\n[完成] 全部阶段执行成功！")
print("  · 原始数据：raw_recruitment_data.csv")
print("  · 清洗数据：cleaned_recruitment_data.csv")
print("  · 分析图表：")
print("      - panel_a_education_salary_boxplot.png  （学历×薪资箱线图）")
print("      - panel_b_city_demand_barchart.png      （城市需求柱状图）")
print("      - panel_c_experience_salary_lineplot.png （经验×薪资折线图）")
