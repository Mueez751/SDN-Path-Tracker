# SDN Path Tracing Tool

## Problem Statement
Implement an SDN-based Path Tracing Tool using Mininet and POX controller 
that identifies and displays the path taken by packets through the network.

## Tools Used
- Mininet
- POX Controller
- Open vSwitch
- iperf
- Ubuntu 24.04

## Network Topology
- 4 Hosts: h1, h2, h3, h4
- 1 Switch: s1
- Controller: POX (port 6653)

## Setup & Execution Steps

### Step 1: Install Mininet
```
sudo apt install mininet -y
```

### Step 2: Install POX
```
git clone https://github.com/noxrepo/pox
```

### Step 3: Copy controller file
```
cp path_tracer.py ~/pox/pox/forwarding/
```

### Step 4: Start POX Controller (Terminal 1)
```
cd ~/pox
python3 pox.py openflow.of_01 --port=6653 forwarding.path_tracer
```

### Step 5: Start Mininet Topology (Terminal 2)
```
sudo python3 topology.py
```

## Test Scenarios

### Scenario 1: Full connectivity test
```
mininet> pingall
```
Expected: 0% dropped (12/12 received)

### Scenario 2: Path tracing between specific hosts
```
mininet> h1 ping -c 5 h4
```
Expected: PATH logs showing switch and port for each packet

## Performance Results
- Bandwidth: 38.5 Gbits/sec (measured using iperf)
- Packet Loss: 0%
- RTT: min/avg/max = 0.035/2.211/8.304 ms

## Expected Output
- Controller logs showing PATH for every packet
- Flow table entries showing match-action rules
- 0% packet loss in all ping tests
