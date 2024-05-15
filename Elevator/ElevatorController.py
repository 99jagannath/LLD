import heapq
from collections import deque
from Direction import Direction


class ElevatorController:

    def __init__(self, eleVatorCar) -> None:
        self.elevatorCar = eleVatorCar
        self.minHeap = []
        self.maxHeap = []
        self.pendingTask = deque()

    def submitInternalRequest(self, floor):
        if floor > self.elevatorCar.floor:
            heapq.heapify(self.minHeap, floor)
        else:
            heapq.heapify(self.maxHeap, -1*floor)
        
        self.controlElevator()


    def submitExternalRequest(self, floor, direction):
        if direction == Direction.UP:
            if self.elevatorCar.direction == Direction.UP:
                if floor > self.elevatorCar.floor:
                    heapq.heappush(self.minHeap, floor)
                else:
                    self.pendingTask.append((Direction.UP, floor))
            else:
                heapq.heappush(self.maxHeap, -1*floor)
        else:
            if self.elevatorCar.direction == Direction.DOWN:
                if floor < self.elevatorCar.floor:
                    heapq.heappush(self.maxHeap, -1*floor)
                else:
                    self.pendingTask.appendright(floor)
            else:
                heapq.heappush(self.minHeap, floor)
        self.controlElevator()

    def controlElevator(self):
        while len(self.minHeap) != 0 or len(self.maxHeap) != 0 or len(self.pendingTask) != 0:
            if self.elevatorCar.direction == Direction.UP:
                while len(self.minHeap) > 0:
                    destFloor = heapq.heappop(self.minHeap)
                    self.elevatorCar.move(destFloor)
                self.elevatorCar.direction = Direction.DOWN
                while len(self.pendingTask) > 0:
                    floor = self.pendingTask.popleft()
                    heapq.heappush(self.minHeap, floor)

            else:
                while len(self.maxHeap) > 0:
                    destFloor = -1 * heapq.heappop(self.maxHeap)
                    self.elevatorCar.move(destFloor)
                self.elevatorCar.direction = Direction.UP
                while len(self.pendingTask) > 0:
                    floor = self.pendingTask.popleft()
                    heapq.heappush(self.maxHeap, -1 * floor)