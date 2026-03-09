# main.py

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from models import Order, Truck, Drone, RegionNode
from algorithms import quick_sort_orders, binary_search_order, calculate_total_orders_recursive, greedy_dispatch

DATA_FILE = "orders_data.json"

class DeliverySystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Logistics Enterprise System")
        self.root.geometry("1000x650")

        style = ttk.Style()
        if "clam" in style.theme_names():
            style.theme_use("clam")

        self.init_data()
        self.build_ui()
        self.refresh_table(self.orders)
        self.log_message("System initialized successfully. Ready for smart dispatch.")

    def init_data(self):
        self.vehicles = [Truck("T-01", 2000), Drone("D-99", 5, max_range=30)]
        self.orders = []

        self.load_data()
        if not self.orders:
            self.orders = [
                Order(1005, 2.5, 15, 3),
                Order(1001, 10.0, 50, 1),
                Order(1008, 1.2, 5, 5),
                Order(1003, 5.0, 20, 3),
                Order(1002, 8.0, 120, 2)
            ]

        self.hq = RegionNode("HQ Sort Center", 0)
        north = RegionNode("North Hub", 50)
        south = RegionNode("South Hub", 30)
        north.add_sub_region(RegionNode("North Station 1", 120))
        north.add_sub_region(RegionNode("North Station 2", 80))
        self.hq.add_sub_region(north)
        self.hq.add_sub_region(south)

    def load_data(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    data = json.load(f)
                    self.orders = [Order.from_dict(o) for o in data]
                self.log_message(f"Loaded {len(self.orders)} orders from local storage.")
            except Exception as e:
                self.log_message(f"Error loading data: {e}")

    def save_data(self):
        try:
            with open(DATA_FILE, "w") as f:
                json.dump([o.to_dict() for o in self.orders], f, indent=4)
            self.log_message("Data persisted to local storage successfully.")
        except Exception as e:
            self.log_message(f"Error saving data: {e}")

    def build_ui(self):
        toolbar = ttk.Frame(self.root, padding=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)
        ttk.Button(toolbar, text="Save Data", command=self.save_data).pack(side=tk.LEFT, padx=5)
        ttk.Button(toolbar, text="Reset Status", command=self.do_reset_status).pack(side=tk.LEFT, padx=5)

        main_pane = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        main_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        left_notebook = ttk.Notebook(main_pane)
        main_pane.add(left_notebook, weight=1)

        tab_ops = ttk.Frame(left_notebook, padding=10)
        left_notebook.add(tab_ops, text="Order Management")

        ttk.Label(tab_ops, text="Order ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.entry_id = ttk.Entry(tab_ops, width=15)
        self.entry_id.grid(row=0, column=1, pady=5)

        ttk.Label(tab_ops, text="Weight (kg):").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.entry_w = ttk.Entry(tab_ops, width=15)
        self.entry_w.grid(row=1, column=1, pady=5)

        ttk.Label(tab_ops, text="Distance (km):").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.entry_d = ttk.Entry(tab_ops, width=15)
        self.entry_d.grid(row=2, column=1, pady=5)

        ttk.Label(tab_ops, text="Priority (1-5):").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.entry_p = ttk.Entry(tab_ops, width=15)
        self.entry_p.grid(row=3, column=1, pady=5)

        ttk.Button(tab_ops, text="Add Order", command=self.do_add_order).grid(row=4, column=0, columnspan=2,
                                                                              sticky=tk.EW, pady=10)
        ttk.Button(tab_ops, text="Delete Selected", command=self.do_delete_order).grid(row=5, column=0, columnspan=2,
                                                                                       sticky=tk.EW, pady=5)

        tab_algo = ttk.Frame(left_notebook, padding=10)
        left_notebook.add(tab_algo, text="Smart Dispatch")

        ttk.Button(tab_algo, text="1. Smart Sort (Quick Sort)", command=self.do_sort).pack(fill=tk.X, pady=5)
        ttk.Button(tab_algo, text="2. Auto Dispatch (Greedy Algo)", command=self.do_auto_dispatch,
                   style="Accent.TButton").pack(fill=tk.X, pady=5)

        search_frame = ttk.LabelFrame(tab_algo, text="Fast Lookup", padding=5)
        search_frame.pack(fill=tk.X, pady=15)
        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(fill=tk.X, pady=5)
        self.search_entry.insert(0, "Enter Order ID")
        ttk.Button(search_frame, text="Binary Search", command=self.do_search).pack(fill=tk.X)

        tab_analytics = ttk.Frame(left_notebook, padding=10)
        left_notebook.add(tab_analytics, text="System Analytics")
        ttk.Button(tab_analytics, text="OOP Vehicle Eval", command=self.do_polymorphism_test).pack(fill=tk.X, pady=5)
        ttk.Button(tab_analytics, text="Network Backlog (Recursion)", command=self.do_recursive_test).pack(fill=tk.X,
                                                                                                           pady=5)

        right_frame = ttk.Frame(main_pane)
        main_pane.add(right_frame, weight=3)

        columns = ("ID", "Weight(kg)", "Distance(km)", "Priority", "Status", "Vehicle")
        self.tree = ttk.Treeview(right_frame, columns=columns, show="headings", height=15)

        col_widths = [80, 80, 90, 80, 150, 100]
        for col, width in zip(columns, col_widths):
            self.tree.heading(col, text=col)
            self.tree.column(col, width=width, anchor=tk.CENTER)

        self.tree.tag_configure('unassigned', background='#f9f9f9', foreground='black')
        self.tree.tag_configure('drone', background='#d4edda', foreground='#155724')  # 浅绿色
        self.tree.tag_configure('truck', background='#cce5ff', foreground='#004085')  # 浅蓝色
        self.tree.tag_configure('failed', background='#f8d7da', foreground='#721c24')  # 浅红色

        self.tree.pack(fill=tk.BOTH, expand=True, pady=(0, 5))

        log_frame = ttk.LabelFrame(right_frame, text="System Log Console")
        log_frame.pack(fill=tk.X, side=tk.BOTTOM)
        self.log_text = tk.Text(log_frame, height=8, font=("Consolas", 9), bg="#1e1e1e", fg="#00ff00", wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)

    def log_message(self, message):
        self.log_text.insert(tk.END, f"> {message}\n")
        self.log_text.see(tk.END)

    def refresh_table(self, order_list):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for o in order_list:
            vehicle_info = o.assigned_vehicle if o.assigned_vehicle else "-"

            tag = 'unassigned'
            if "Drone" in o.status:
                tag = 'drone'
            elif "Truck" in o.status:
                tag = 'truck'
            elif "Failed" in o.status:
                tag = 'failed'

            self.tree.insert("", tk.END, values=(
                o.order_id, o.weight, o.distance, o.priority, o.status, vehicle_info
            ), tags=(tag,))

    def do_reset_status(self):
        for o in self.orders:
            o.status = "Unassigned"
            o.assigned_vehicle = None
        self.refresh_table(self.orders)
        self.log_message("All order statuses have been reset.")

    def do_add_order(self):
        try:
            o_id = int(self.entry_id.get())
            weight = float(self.entry_w.get())
            distance = float(self.entry_d.get())
            priority = int(self.entry_p.get())

            if any(o.order_id == o_id for o in self.orders):
                messagebox.showerror("Error", f"Order ID {o_id} already exists!")
                return

            new_order = Order(o_id, weight, distance, priority)
            self.orders.append(new_order)
            self.refresh_table(self.orders)
            self.log_message(f"Added new order: ID={o_id}, Priority={priority}")

            for entry in [self.entry_id, self.entry_w, self.entry_d, self.entry_p]:
                entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")

    def do_delete_order(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Hint", "Select an order to delete.")
            return

        target_id = self.tree.item(selected[0])['values'][0]
        self.orders = [o for o in self.orders if o.order_id != target_id]
        self.refresh_table(self.orders)
        self.log_message(f"Deleted order: ID={target_id}")

    def do_sort(self):
        self.log_message("Executing Quick Sort (Priority Desc, Distance Asc)...")
        self.orders = quick_sort_orders(self.orders)
        self.refresh_table(self.orders)
        self.log_message("Sort completed.")

    def do_auto_dispatch(self):
        self.log_message("Initiating Greedy Dispatch Algorithm...")
        greedy_dispatch(self.orders, self.vehicles)
        self.refresh_table(self.orders)

        self.log_message("--- Dispatch Summary ---")
        for v in self.vehicles:
            if isinstance(v, Truck):
                self.log_message(f"{v.vehicle_id} (Truck): Loaded {v.current_load}kg / {v.capacity}kg")
            elif isinstance(v, Drone):
                self.log_message(f"{v.vehicle_id} (Drone): Dispatched out.")

    def do_search(self):
        target = self.search_entry.get()
        try:
            target_id = int(target)
            orders_sorted_by_id = sorted(self.orders, key=lambda x: x.order_id)
            result = binary_search_order(orders_sorted_by_id, target_id)
            if result:
                msg = f"Found Order {result.order_id}:\nDist: {result.distance}km\nStatus: {result.status}"
                messagebox.showinfo("Search Success", msg)
                self.log_message(f"Binary Search: Found order {target_id}")
            else:
                messagebox.showwarning("Search Failed", f"Order {target_id} not found.")
        except ValueError:
            messagebox.showerror("Input Error", "Enter valid numeric Order ID!")

    def do_polymorphism_test(self):
        test_distance = 60
        self.log_message(f"\n[OOP Polymorphism] Delivery time for {test_distance}km:")
        for v in self.vehicles:
            time_cost = v.estimate_time(test_distance)
            self.log_message(f"{v.get_info()} -> ETA: {time_cost:.2f} hrs")

    def do_recursive_test(self):
        total = calculate_total_orders_recursive(self.hq)
        self.log_message(f"\n[Recursion] Tree calculation completed. Total network backlog: {total} orders")


if __name__ == "__main__":
    root = tk.Tk()
    app = DeliverySystemGUI(root)
    root.mainloop()
