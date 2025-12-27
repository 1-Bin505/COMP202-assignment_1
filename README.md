
# Traffic Light Simulation and Queue Management System

## Title

**Name**: Binayak Dhungana

**Class**: CS-I

**Roll number**: 23

**Assignment**: I

**Submitted to**: Rupak Ghimire

**Course**: Data Structures and Algorithms (COMP202)

## Introduction



## Demo Output



## System Architecture
The project is designed with a **Producer-Consumer** architecture using file I/O as the communication buffer.

- `traffic_generator.py` acts as the **Producer** that randomly generates vehicles arrivals based on probability. It then writes vehicle IDs that are timestamped into buffer files in the `lane_data/` directory.

- `visualizer.py` acts as the **Consumer** that reads buffer files in the `lane_data` directory to spawn vehicles in the GUI. It renders the intersection along with the vehicles using the `pygame` module. It also executes the traffic light state machine and physics engine.


## Features
- **Priority Logic**: This system monitors the lane L2 of road A. If the queue length for that lane exceeds 10 vehicles, it triggers a "Priority Mode" that sets and holds the green light for AL2 lane until the queue drops to 5 or fewer vehicles.
- **Left-Hand Traffic (LHT)**: Vehicles follow LHT rules, standard in Nepal.
- **Real-time Visualization**: `visualizer.py` is built with `pygame`, which features visual cues for traffic light along with glowing effects, moving vehicles, and lane markings.
- **Dynamic Traffic Generation**: A separate generator script `traffic_generator.py` simulates varying vehicle loads by writing data to file buffers in real-time.

  
## Installation & Prerequisites

This project requires **Python 3.x** to run as intended. So, ensure you have **Python 3.x** installed.

You can check your installed Python version by typing the command `python --version` in the terminal.

1. **Install Dependencies**

The only external dependecy required is `pygame` for the visualization.
```bash
pip install pygame 
```
If you have multiple Python versions, use:
```bash
pip3 install pygame
```
The recommended method of installation is inside a **Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate    # for Linux/ macOS
venv\Scripts\activate       # for Windows
pip install pygame
```
On **Linux** systems, you can use different package managers to install `pygame`:
```bash
sudo pacman -S python-pygame       # Arch / Omarchy
sudo apt install python3-pygame    # Ubuntu / Debian
sudo dnf install python3-pygame    # Fedora
```

2. **Environment Setup**

Clone the repository:
```bash

```
Ensure the folder looks like this:
```
/dsa-queue-simulator/
     ├── traffic_generator.py    # Generates vehicles
     ├── simulator.py            # Main visualization
     ├── road.png               # Road background 
     ├── car1.png               # Car png image
     ├── car3.png               # Car png image
    |── `README.md`
```

## Execution Instructions

After cloning the repository, open your terminal/ command prompt to go to the project directory.
```bash
cd dsa-queue-simulator
```
To simulate real-time traffic using this project, you must run the **Generator** `traffic_generator.py` and the **Visualizer** `visualizer.py` simultaneously in two separate terminal windows.

First, start the **Generator** by opening a terminal and writing the following command: 
```bash
python src/traffic_generator.py
```
*Output*: You should logs like `[GENERATOR] Added 1 vehicles to AL2`. 

Keep this window **open**.

Next, start the **Visualizer** by opening a **second** terminal window and running the following command:
```bash
python src/visualizer.py
```
*Output*: A **Pygame** window will launch that simulates real-time traffic intersection.

## Logic & Algorithms


## References

The following resources were referenced during the development of this project:
* **Assignment**: COMP202 Assignment I (Traffic Light Simulation and Queue Management)
* **GitHub repo**: https://github.com/1-Bin505/dsa-queue-simulaator
* * **Pygame documentation**: https://www.pygame.org/docs/
* **Python 3.13 documentation**: https://docs.python.org/3.13/
* **100 days of code**: https://www.youtube.com/playlist?list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg

