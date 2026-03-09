# algorithms.py

from typing import List, Optional
from models import Order, Vehicle

def quick_sort_orders(orders: List[Order]) -> List[Order]:
    if len(orders) <= 1:
        return orders

    pivot = orders[len(orders) // 2]
    left, middle, right = [], [], []

    for order in orders:
        if order.priority > pivot.priority or (order.priority == pivot.priority and order.distance < pivot.distance):
            left.append(order)
        elif order.priority == pivot.priority and order.distance == pivot.distance:
            middle.append(order)
        else:
            right.append(order)

    return quick_sort_orders(left) + middle + quick_sort_orders(right)

def binary_search_order(sorted_orders_by_id: List[Order], target_id: int) -> Optional[Order]:
    low, high = 0, len(sorted_orders_by_id) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_id = sorted_orders_by_id[mid].order_id

        if mid_id == target_id:
            return sorted_orders_by_id[mid]
        elif mid_id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def calculate_total_orders_recursive(region_node) -> int:
    total = region_node.pending_orders_count
    for sub_region in region_node.sub_regions:
        total += calculate_total_orders_recursive(sub_region)
    return total

def greedy_dispatch(orders: List[Order], vehicles: List[Vehicle]) -> None:

    sorted_orders = quick_sort_orders(orders)

    for v in vehicles:
        v.current_load = 0.0

    drones = [v for v in vehicles if type(v).__name__ == "Drone"]
    trucks = [v for v in vehicles if type(v).__name__ == "Truck"]

    for order in sorted_orders:
        if order.status != "Unassigned":
            continue

        assigned = False
        for drone in drones:
            if drone.can_carry(order):
                order.status = "Dispatched (Drone)"
                order.assigned_vehicle = drone.vehicle_id
                assigned = True
                break

        if not assigned:
            for truck in trucks:
                if truck.can_carry(order):
                    truck.current_load += order.weight
                    order.status = "Dispatched (Truck)"
                    order.assigned_vehicle = truck.vehicle_id
                    assigned = True
                    break

        if not assigned:
            order.status = "Failed (Overload)"
