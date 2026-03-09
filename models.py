#models.py

from abc import ABC, abstractmethod
from typing import List, Optional

class Order:
    def __init__(self, order_id: int, weight: float, distance: float, priority: int):
        self.order_id = order_id
        self.weight = weight
        self.distance = distance
        self.priority = priority
        self._status = "Unassigned"
        self.assigned_vehicle: Optional[str] = None

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        self._status = value

    def to_dict(self) -> dict:
        return {
            "order_id": self.order_id,
            "weight": self.weight,
            "distance": self.distance,
            "priority": self.priority,
            "status": self._status,
            "assigned_vehicle": self.assigned_vehicle
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Order":
        order = cls(data["order_id"], data["weight"], data["distance"], data["priority"])
        order.status = data["status"]
        order.assigned_vehicle = data.get("assigned_vehicle")
        return order

class Vehicle(ABC):
    def __init__(self, vehicle_id: str, capacity: float):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_load = 0.0

    @abstractmethod
    def estimate_time(self, distance: float) -> float:
        pass

    @abstractmethod
    def can_carry(self, order: Order) -> bool:
        pass

    @abstractmethod
    def get_info(self) -> str:
        pass

class Truck(Vehicle):
    def estimate_time(self, distance: float) -> float:
        return distance / 50.0

    def can_carry(self, order: Order) -> bool:
        return (self.current_load + order.weight) <= self.capacity

    def get_info(self) -> str:
        return f"Truck [ID:{self.vehicle_id}] (Cap: {self.capacity}kg, Load: {self.current_load}kg)"

class Drone(Vehicle):
    def __init__(self, vehicle_id: str, capacity: float, max_range: float = 30.0):
        super().__init__(vehicle_id, capacity)
        self.max_range = max_range

    def estimate_time(self, distance: float) -> float:
        return distance / 100.0

    def can_carry(self, order: Order) -> bool:
        return order.weight <= self.capacity and order.distance <= self.max_range

    def get_info(self) -> str:
        return f"Drone[ID:{self.vehicle_id}] (Cap: {self.capacity}kg, Range: {self.max_range}km)"

class RegionNode:
    def __init__(self, name: str, pending_orders_count: int = 0):
        self.name = name
        self.pending_orders_count = pending_orders_count
        self.sub_regions: List['RegionNode'] =[]

    def add_sub_region(self, region: 'RegionNode'):
        self.sub_regions.append(region)
