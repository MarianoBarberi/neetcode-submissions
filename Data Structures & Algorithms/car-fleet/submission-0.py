class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ps = sorted(list(zip(position, speed)), reverse = True)
        times = [((target - ps[0][0]) / ps[0][1])]
        fleets = 0
        print(ps[0][0])
        for car in ps:
            time = ((target - car[0]) / car[1])
            if time > times[-1]:
                times.append(time)
        print(times)
        return len(times)