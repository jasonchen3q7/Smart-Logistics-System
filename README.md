<div align="center">

# 🚚 Smart Logistics System (智能物流调度系统)

基于 Python 与 Tkinter 构建的桌面应用程序，模拟基于卡车和无人机（Truck-Drone）的智能物流订单调度。

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![OOP](https://img.shields.io/badge/Concept-OOP-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-QuickSort_%7C_BinarySearch-red.svg)

</div>

## 📖 项目简介

本项目是一个物流调度模拟系统，带有完整的图形用户界面（GUI）。项目实现了订单的增删查改，还融合了多项核心计算机科学（CS）概念与数据结构，包括**面向对象编程（OOP）、多态、快速排序、二分查找以及递归算法**

## ✨ 核心功能与技术亮点

* 📦 **订单管理 (Order Management)**
  * 可在界面中直观地新增（Add）和删除（Delete）订单
  * 包含订单ID、重量（kg）、距离（km）以及优先级（Priority）属性
* 🧠 **智能派单排序 (Quick Sort)**
  * 采用快速排序（Quick Sort）算法重新排列订单
  * 规则：高优先级优先；同优先级下，距离短的优先
* 🔍 **极速订单检索 (Binary Search)**
  * 使用二分查找（Binary Search）算法，在 O(log n) 时间复杂度下毫秒级定位订单详情
* 🚁 **车辆多态模拟 (Vehicle Polymorphism)**
  * 构建“卡车（Truck）”和“无人机（Drone）”载具模型
  * 利用多态（Polymorphism）特性，动态计算不同载具在相同距离下的预估配送时间
* 🌳 **递归物流网统计 (Recursive Backlog Count)**
  * 基于树形结构建立多级物流区域网络（总中心 -> 分中心 -> 站点）
  * 运用递归算法（Recursion）一键统计整张物流网络的总积压订单量

## 📁 目录结构

```text
main.py         # 程序主入口：包含 GUI 界面绘制及所有交互逻辑
algorithms.py   # 算法核心库：包含快速排序、二分查找、树的递归遍历算法
models.py       # 数据模型层：包含实体类 (Order, Vehicle, RegionNode 等)

## 🚀 运行指南
### 🛠️ 1. 获取代码
请确保您的计算机上已安装 Python 3.8 或更高版本
您可以直接在 GitHub 页面点击 Code -> Download ZIP 下载并解压，或者使用 Git 命令行将项目克隆到本地：
git clone https://github.com/您的用户名/Smart-Logistics-System.git
### 🏃‍♂️  2. 启动程序
#第 1 步：进入项目目录
cd Smart-Logistics-System
第 2 步：运行主程序
python main.py


