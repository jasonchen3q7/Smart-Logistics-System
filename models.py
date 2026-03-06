# models.py
class Order:
    def __init__(self, order_id, weight, distance, priority):
        self.order_id = order_id
        self.weight = weight
        self.distance = distance
        self.priority = priority
        self.__status = "Unassigned"

    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        self.__status = new_status


class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity

    def estimate_time(self, distance):
        pass

    def get_info(self):
        pass


class Truck(Vehicle):
    def estimate_time(self, distance):
        return distance / 50.0

    def get_info(self):
        return f"Truck [ID:{self.vehicle_id}] (Capacity: {self.capacity}kg)"


class Drone(Vehicle):
    def estimate_time(self, distance):
        return distance / 100.0

    def get_info(self):
        return f"Drone [ID:{self.vehicle_id}] (Capacity: {self.capacity}kg)"

class RegionNode:
    def __init__(self, name, pending_orders_count=0):
        self.name = name
        self.pending_orders_count = pending_orders_count
        self.sub_regions = []

    def add_sub_region(self, region):
        self.sub_regions.append(region)