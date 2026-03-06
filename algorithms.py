# algorithms.py
def quick_sort_orders(orders):
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

def binary_search_order(sorted_orders_by_id, target_id):
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

def calculate_total_orders_recursive(region_node):
    total = region_node.pending_orders_count
    for sub_region in region_node.sub_regions:
        total += calculate_total_orders_recursive(sub_region)
    return total