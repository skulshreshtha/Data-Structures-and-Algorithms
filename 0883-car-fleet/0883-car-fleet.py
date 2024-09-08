class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = [[p, s] for p, s in zip(position, speed)]
        
        for p, s in sorted(cars, reverse=True):
            fleet.append((target - p) / s)
            if len(fleet) >= 2 and fleet[-1] <= fleet[-2]:
                fleet.pop()
        
        return len(fleet)