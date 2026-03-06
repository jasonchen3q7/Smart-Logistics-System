<div align="center">

# 🚚 Smart Logistics System

A desktop application built with Python and Tkinter that simulates intelligent logistics order scheduling based on trucks and drones.

![Python](https://img.shields.io/badge/Python-3.8-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg)
![OOP](https://img.shields.io/badge/Concept-OOP-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-QuickSort_%7C_BinarySearch-red.svg)

</div>

## 📖 Project Overview

This project is a logistics scheduling simulation system with a complete graphical user interface (GUI). It implements order creation, deletion, retrieval, and modification, and integrates several core computer science (CS) concepts and data structures, including **object-oriented programming (OOP), polymorphism, quicksort, binary search, and recursive algorithms**.

## ✨ Core Functions and Technical Highlights

* 📦 **Order Management**
  * Orders can be added and deleted intuitively within the interface.
  * Includes order ID, weight (kg), distance (km), and priority attributes.
* 🧠 **Order sorting**
  * The orders were rearranged using the Quick Sort algorithm.
  * Rule: Higher priority takes precedence; among those with the same priority, shorter distance takes precedence.
* 🔍 **Instant Order Search**
  * Using the binary search algorithm, order details can be located in milliseconds with a time complexity of O(log n).
* 🚁 **Vehicle Polymorphism**
  * Build models of "Truck" and "Drone" vehicles.
  * By leveraging the properties of polymorphism, the estimated delivery time for different vehicles over the same distance is dynamically calculated.
* 🌳 **Recursive Backlog Count**
  * A multi-level logistics regional network (headquarters -> branch centers -> stations) is established based on a tree structure.
  * Using a recursive algorithm, the total backlog of orders across the entire logistics network can be calculated in one click.

## 📁 Directory Structure

- `main.py` —— **Main Program Entry Point:** Contains the GUI interface rendering and all interactive logic.
- `algorithms.py` —— **Core Algorithm Library:** Includes algorithms for quicksort, binary search, and recursive tree traversal.
- `models.py` —— **Data Model Layer:** Contains entity classes (Order, Vehicle, RegionNode, etc.)

## 🚀 Operating Guide
### 🛠️ 1. Get code
Please ensure that Python 3.8 or later is installed on your computer.
You can download and extract the ZIP directly from the GitHub page by clicking Code -> Download ZIP, or clone the project to your local machine using the Git command line:
git clone https://github.com/jasonchen3q7/Smart-Logistics-System.git

### 🏃‍♂️ 2. Startup program

- **Step 1: Navigate to the project directory**
  `cd Smart-Logistics-System`

- **Step 2: Run the main program**
  `python main.py`

