import time
from collections import deque


lanes = {
    "AL1": deque(), "AL2": deque(), "AL3": deque(),  
    "BL1": deque(), "BL2": deque(), "BL3": deque(),
    "CL1": deque(), "CL2": deque(), "CL3": deque(),
    "DL1": deque(), "DL2": deque(), "DL3": deque(),
}


lights = {
    "A": "RED",
    "B": "RED",
    "C": "RED",
    "D": "RED"
}


def traffic_lights():
    while True:
        lights["A"] = lights["C"] = "GREEN"
        lights["B"] = lights["D"] = "RED"
        print("\nLights: A & C GREEN")
        time.sleep(8)

        lights["A"] = lights["C"] = "RED"
        lights["B"] = lights["D"] = "GREEN"
        print("\nLights: B & D GREEN")
        time.sleep(8)


def generate_cars():
    i = 1
    while True:
        lanes["AL3"].append(f"A3_{i}")
        lanes["BL3"].append(f"B3_{i}")
        lanes["CL3"].append(f"C3_{i}")
        lanes["DL3"].append(f"D3_{i}")
        print(f"Generated priority cars {i}")
        time.sleep(5)

        lanes["AL2"].append(f"A2_{i}")
        lanes["BL2"].append(f"B2_{i}")
        lanes["CL2"].append(f"C2_{i}")
        lanes["DL2"].append(f"D2_{i}")
        print(f"Generated normal cars {i}")
        i += 1
        time.sleep(5)
