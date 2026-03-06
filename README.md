这是一个为您定制的完整、专业的 README.md 文件。您可以直接将它复制并保存为项目根目录下的 README.md。

该文档详细说明了项目的功能、结构、包含的计算机科学核心概念以及如何运行，非常适合用于个人项目展示或课程设计作业。

🚚 智能物流调度系统 (Smart Logistics System)

这是一个基于 Python 及其内置 Tkinter 库构建的桌面应用程序，模拟了基于卡车和无人机（Truck-Drone）的智能物流订单调度。

本项目不仅实现了带有图形用户界面（GUI）的订单管理，还深度融合了多项核心计算机科学（CS）概念与数据结构，包括面向对象编程（OOP）、多态、快速排序、二分查找以及递归算法。

✨ 功能特性

📦 订单管理 (Order Management)

在图形界面中直观地新增（Add）和删除（Delete）订单记录。

订单属性包含：订单ID、重量（kg）、距离（km）以及优先级（Priority）。

🧠 智能派单排序 (Smart Dispatch / Quick Sort)

点击“Smart Sort”按钮，系统会使用**快速排序（Quick Sort）**算法对订单进行重新排列。

排序规则：高优先级的订单优先；优先级相同时，距离短的订单优先。

🔍 极速订单检索 (Binary Search)

输入订单ID，系统使用**二分查找（Binary Search）**算法在毫秒级内定位订单详情，大幅提升检索效率。

🚁 车辆多态模拟 (Vehicle Polymorphism)

系统包含“卡车（Truck）”和“无人机（Drone）”两种载具模型。

利用面向对象的多态性（Polymorphism），根据不同载具的时速动态估算配送时间。

🌳 递归物流网统计 (Recursive Backlog Count)

基于树形数据结构（Tree）构建物流区域网络（总分拨中心 -> 区域枢纽 -> 服务站）。

使用**递归算法（Recursion）**一键统计整张物流网络的总积压订单量。

📁 项目目录结构
code
Text
download
content_copy
expand_less
.
├── main.py         # 程序主入口：包含基于 Tkinter 绘制的 GUI 界面及所有交互逻辑
├── algorithms.py   # 算法核心库：包含快速排序、二分查找、递归树遍历算法
└── models.py       # 数据模型层：包含各类实体类 (Order, Vehicle, RegionNode等)
核心文件简介

models.py:

Order 类：封装了订单的属性和状态（体现封装特性）。

Vehicle 及子类 Truck / Drone：父类定义接口，子类重写 estimate_time 方法（体现继承与多态特性）。

RegionNode 类：树节点模型，用于表示不同层级的物流区域。

algorithms.py:

quick_sort_orders(orders)：基于自定义比较逻辑的快速排序实现。

binary_search_order(sorted_orders, target_id)：时间复杂度为 O(log n) 的二分查找实现。

calculate_total_orders_recursive(region_node)：树的前序遍历递归求和。

main.py:

继承与实例化 Tkinter 组件构建界面框架。

连接UI事件与底层算法，提供实时的系统运行日志（System Run Log）。

🚀 快速开始
环境依赖

本项目仅需 Python 3.x 环境，无需安装任何额外的第三方依赖。图形界面使用的是 Python 内置的标准库 tkinter。

运行方式

将 main.py、algorithms.py 和 models.py 下载到同一个文件夹中。

打开终端（Terminal）或命令提示符（CMD），进入该目录。

执行以下命令启动系统：

code
Bash
download
content_copy
expand_less
python main.py

(注：Mac或Linux用户可能需要使用 python3 main.py 命令启动)

🎮 界面操作指南

Order Management (左上角):

填入对应信息 (ID / Weight / Distance / Priority) 后点击 "Add New Order" 即可添加新订单。

在右侧表格中点击选中一行，然后点击 "Delete Selected Order" 即可将其删除。

Algorithm Dispatch (左侧中部):

"Smart Sort": 点击后，右侧订单列表将按照智能优先级逻辑重新排序。

"Restore Default List": 恢复初始或未排序的订单视图。

"Binary Search": 在文本框中输入需要查询的数字ID，点击按钮后将弹出结果。

OOP & Adv. Features (左下角):

"Vehicle Polymorphism Eval": 点击后，下方的日志区会打印出卡车与无人机对于相同距离（60km）的不同预估耗时。

"Recursive Backlog Count": 点击后，日志区将使用递归算法自动算出区域数据中的待处理订单总量。

👨‍💻 技术要点回顾 (CS Concepts)

Encapsulation（封装）: 使用 __status 定义私有属性，通过 getter/setter 访问（models.py）。

Inheritance & Polymorphism（继承与多态）: Truck 和 Drone 继承自 Vehicle，并以不同的方式实现了方法覆盖。

Divide and Conquer（分治法）: 运用在 quick_sort_orders 中，使得海量订单排序更加高效。

Recursion（递归）: 运用在树形解构的汇总遍历中，代码简洁且易于拓展。

Created with ❤️ via Smart Logistics Python Project
