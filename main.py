# main.py
import tkinter as tk
from tkinter import ttk, messagebox
from models import Order, Truck, Drone, RegionNode
from algorithms import quick_sort_orders, binary_search_order, calculate_total_orders_recursive


class DeliverySystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Logistics System (Truck-Drone)")
        self.root.geometry("900x600")  # Slightly elongated window to fit new buttons

        self.init_data()
        self.build_ui()
        self.refresh_table(self.orders)
        self.log_message("System initialization complete. Welcome to the Smart Logistics System!")

    def init_data(self):
        self.orders = [
            Order(1005, 2.5, 15, 3),
            Order(1001, 10.0, 50, 1),
            Order(1008, 1.2, 5, 5),
            Order(1003, 5.0, 20, 3),
            Order(1002, 8.0, 120, 2)
        ]
        self.vehicles = [Truck("T-01", 2000), Drone("D-99", 5)]

        self.hq = RegionNode("HQ Sort Center", 0)
        north = RegionNode("North Hub", 50)
        south = RegionNode("South Hub", 30)
        north.add_sub_region(RegionNode("North Station 1", 120))
        north.add_sub_region(RegionNode("North Station 2", 80))
        self.hq.add_sub_region(north)
        self.hq.add_sub_region(south)

    def build_ui(self):
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 10), padding=5)
        style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
        style.configure("Treeview", font=("Arial", 10), rowheight=25)

        control_frame = ttk.Frame(self.root, width=250)
        control_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)

        add_frame = ttk.LabelFrame(control_frame, text="Order Management", padding=10)
        add_frame.pack(fill=tk.X, pady=5)

        ttk.Label(add_frame, text="ID / Wgt(kg) / Dist(km) / Priority").pack(anchor=tk.W)
        input_frame = ttk.Frame(add_frame)
        input_frame.pack(fill=tk.X, pady=5)

        self.entry_id = ttk.Entry(input_frame, width=6)
        self.entry_id.pack(side=tk.LEFT, padx=1)
        self.entry_w = ttk.Entry(input_frame, width=5)
        self.entry_w.pack(side=tk.LEFT, padx=1)
        self.entry_d = ttk.Entry(input_frame, width=5)
        self.entry_d.pack(side=tk.LEFT, padx=1)
        self.entry_p = ttk.Entry(input_frame, width=5)
        self.entry_p.pack(side=tk.LEFT, padx=1)

        ttk.Button(add_frame, text="Add New Order", command=self.do_add_order).pack(fill=tk.X, pady=2)
        ttk.Button(add_frame, text="Delete Selected Order", command=self.do_delete_order).pack(fill=tk.X, pady=2)

        algo_frame = ttk.LabelFrame(control_frame, text="Algorithm Dispatch", padding=10)
        algo_frame.pack(fill=tk.X, pady=5)

        ttk.Button(algo_frame, text="Restore Default List", command=lambda: self.refresh_table(self.orders)).pack(fill=tk.X, pady=2)
        ttk.Button(algo_frame, text="Smart Sort (Quick Sort)", command=self.do_sort).pack(fill=tk.X, pady=2)

        search_frame = ttk.Frame(algo_frame)
        search_frame.pack(fill=tk.X, pady=5)
        self.search_entry = ttk.Entry(search_frame, width=12)
        self.search_entry.pack(side=tk.LEFT, padx=(0, 5))
        self.search_entry.insert(0, "Enter Order ID")
        ttk.Button(search_frame, text="Binary Search", command=self.do_search).pack(side=tk.LEFT)

        oop_frame = ttk.LabelFrame(control_frame, text="OOP & Adv. Features", padding=10)
        oop_frame.pack(fill=tk.X, pady=5)

        ttk.Button(oop_frame, text="Vehicle Polymorphism Eval", command=self.do_polymorphism_test).pack(fill=tk.X, pady=2)
        ttk.Button(oop_frame, text="Recursive Backlog Count", command=self.do_recursive_test).pack(fill=tk.X, pady=2)

        data_frame = ttk.Frame(self.root)
        data_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

        columns = ("ID", "Weight(kg)", "Distance(km)", "Priority", "Status")
        self.tree = ttk.Treeview(data_frame, columns=columns, show="headings", height=10)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor=tk.CENTER)
        self.tree.pack(fill=tk.X, pady=(0, 10))

        log_label = ttk.Label(data_frame, text="System Run Log:", font=("Arial", 10, "bold"))
        log_label.pack(anchor=tk.W)
        self.log_text = tk.Text(data_frame, height=10, font=("Consolas", 10), bg="#f4f4f4", wrap=tk.WORD)
        self.log_text.pack(fill=tk.BOTH, expand=True)

    def log_message(self, message):
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def refresh_table(self, order_list):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for o in order_list:
            self.tree.insert("", tk.END, values=(o.order_id, o.weight, o.distance, o.priority, o.get_status()))

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
            self.log_message(f"Successfully added new order: ID={o_id}, Priority={priority}")

            self.entry_id.delete(0, tk.END)
            self.entry_w.delete(0, tk.END)
            self.entry_d.delete(0, tk.END)
            self.entry_p.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")

    def do_delete_order(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Hint", "Please select an order from the table to delete.")
            return

        item_data = self.tree.item(selected_item[0])
        target_id = item_data['values'][0]

        for o in self.orders:
            if o.order_id == target_id:
                self.orders.remove(o)
                break

        self.refresh_table(self.orders)
        self.log_message(f"Successfully deleted order: ID={target_id}")

    def do_sort(self):
        self.log_message("\nExecuting Quick Sort (High priority first, short distance first)")
        sorted_orders = quick_sort_orders(self.orders)
        self.refresh_table(sorted_orders)
        self.log_message("List updated to smart dispatch order.")

    def do_search(self):
        target = self.search_entry.get()
        try:
            target_id = int(target)
            orders_sorted_by_id = sorted(self.orders, key=lambda x: x.order_id)
            result = binary_search_order(orders_sorted_by_id, target_id)
            if result:
                messagebox.showinfo("Search Successful",
                                    f"Order Found:\nID: {result.order_id}\nDistance: {result.distance}km\nPriority: {result.priority}")
                self.log_message(f"Binary Search: Successfully located order {target_id}.")
            else:
                messagebox.showwarning("Search Failed", f"Order with ID {target_id} not found.")
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid numeric Order ID!")

    def do_polymorphism_test(self):
        test_distance = 60
        self.log_message(f"\nOOP Polymorphism Test: Delivery time evaluation for {test_distance}km")
        for v in self.vehicles:
            time_cost = v.estimate_time(test_distance)
            self.log_message(f"{v.get_info()} Estimated time: {time_cost:.2f} hours")

    def do_recursive_test(self):
        self.log_message("\nRecursion Test: Network backlog volume count")
        total = calculate_total_orders_recursive(self.hq)
        self.log_message(f"Recursive calculation from root node completed. Total backlog: {total} orders")

if __name__ == "__main__":
    root = tk.Tk()
    app = DeliverySystemGUI(root)
    root.mainloop()
