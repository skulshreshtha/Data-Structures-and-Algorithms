class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet = []
        cars = [(p, s) for p, s in zip(position, speed)]

        for c in sorted(cars, reverse=True):
            time_current = (target - c[0])/c[1]
            if not fleet or time_current > fleet[-1]:
                fleet.append(time_current)
        
        return len(fleet)