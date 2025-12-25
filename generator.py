import time

class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, element):
        self.queue.append(element)
    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def __iter__(self):
        return iter(self.queue)
    def __str__(self):
        return str(self.queue)

lane = {
    "AL1": Queue(), "AL2": Queue(), "AL3": Queue(),
    "BL1": Queue(), "BL2": Queue(), "BL3": Queue(),
    "CL1": Queue(), "CL2": Queue(), "CL3": Queue(),
    "DL1": Queue(), "DL2": Queue(), "DL3": Queue(),
}
LaneA_light = "RED"
LaneB_light = "RED"
LaneC_light = "RED"
LaneD_light = "RED"
def light_changer():
    global LaneA_light, LaneB_light, LaneD_light, LaneC_light
    flag = True
    while True :
        if flag :
            LaneA_light= "GREEN"
            LaneB_light = "RED"
            LaneD_light = "RED"
            LaneC_light = "GREEN"
            print("A:",LaneA_light,"B:",LaneB_light,"D:",LaneD_light,"C:",LaneC_light,"\n")

            flag = False
            time.sleep(9)
        else :
            LaneA_light = "RED"
            LaneB_light = "GREEN"
            LaneD_light = "GREEN"
            LaneC_light = "RED"
            print("A:",LaneA_light,"B:",LaneB_light,"D:",LaneD_light,"C:",LaneC_light,"\n")
            flag = True
            time.sleep(9)

def generator():
    i =0
    while True :
       
        lane["AL3"].enqueue(f"car_AL3_{i}")
        lane["BL3"].enqueue(f"car_BL3_{i}")
        lane["CL3"].enqueue(f"car_CL3_{i}")
        lane["DL3"].enqueue(f"car_DL3_{i}")
        print(f"Generated cars {i} in AL3, BL3, CL3, DL3\n")

        time.sleep(10)

 

        lane["AL2"].enqueue(f"car_AL2_{i}")
        lane["BL2"].enqueue(f"car_BL2_{i}")
        lane["CL2"].enqueue(f"car_CL2_{i}")
        lane["DL2"].enqueue(f"car_DL2_{i}")
        print(f"Generated cars {i} in AL2, BL2, CL2, DL2\n")
        i += 1

        time.sleep(5)
def traversal():
    global LaneA_light,LaneB_light,LaneD_light,LaneC_light

    while True:
        if LaneA_light == "GREEN":
            if not lane["AL2"].is_empty():
                car = lane["AL2"].dequeue()
                lane["BL1"].enqueue(car)
                return "AL2 car moved to BL1"
            elif not lane["AL3"].is_empty():
                car = lane["AL3"].dequeue()
                lane["CL1"].enqueue(car)  # AL3 exits via CL1
                return "AL3 car moved to CL1"

        if LaneB_light == "GREEN":
            if not lane["BL2"].is_empty():
                car = lane["BL2"].dequeue()
                lane["AL1"].enqueue(car)
                return "BL2 car moved to AL1"
            elif not lane["BL3"].is_empty():
                car = lane["BL3"].dequeue()
                lane["DL1"].enqueue(car)  # BL3 exits via DL1
                return "BL3 car moved to DL1"

        if LaneD_light == "GREEN":
            if not lane["DL2"].is_empty():
                car = lane["DL2"].dequeue()
                lane["CL1"].enqueue(car)
                return "DL2 car moved to CL1"
            elif not lane["DL3"].is_empty():
                car = lane["DL3"].dequeue()
                lane["AL1"].enqueue(car)  # DL3 exits via AL1
                return "DL3 car moved to AL1"

        if LaneC_light == "GREEN":
            if not lane["CL2"].is_empty():
                car = lane["CL2"].dequeue()
                lane["DL1"].enqueue(car)
                return "CL2 car moved to DL1"
            elif not lane["CL3"].is_empty():
                car = lane["CL3"].dequeue()
                lane["BL1"].enqueue(car)  # CL3 exits via BL1
                return "CL3 car moved to BL1"
