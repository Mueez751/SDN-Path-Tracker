# SDN Path Tracing Tool

## Problem Statement
Implement an SDN-based Path Tracing Tool using Mininet and POX controller that identifies and displays the path taken by packets through the network.

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

### Scenario 1: Full Connectivity Test
```
pingall
```
Expected: 0% dropped (12/12 received)
This tests if all 4 hosts can communicate with each other.

### Scenario 2: Path Tracing Between Specific Hosts
```
h1 ping -c 5 h4
```
Expected: PATH logs showing switch and port for each packet.
The controller logs show the exact path each packet takes.

### Scenario 3: Flow Table Inspection
```
h1 ping h4 &
sh ovs-ofctl dump-flows s1
```
Expected: Flow rules installed on switch s1 showing match conditions, actions, idle_timeout=10, hard_timeout=30 and packet counts.

### Scenario 4: Bandwidth Measurement
```
h2 iperf -s &
h1 iperf -c 10.0.0.2 -t 5
```
Expected: High bandwidth throughput between h1 and h2.

## Performance Results
- Bandwidth: 38.5 Gbits/sec (measured using iperf)
- Packet Loss: 0%
- RTT: min/avg/max = 0.035/2.211/8.304 ms

## Expected Output
- Controller logs showing PATH for every packet
- Flow table entries showing match-action rules
- 0% packet loss in all ping tests


  <img width="975" height="538" alt="image" src="https://github.com/user-attachments/assets/4ecfb7f4-f9e2-414e-8c9e-d619400b7f5b" />
  <img width="975" height="469" alt="image" src="https://github.com/user-attachments/assets/106a48ac-9d98-422f-8a28-8a7d47713258" />
  <img width="975" height="208" alt="image" src="https://github.com/user-attachments/assets/4e69c473-c373-419f-8dd6-ad0e2c67c340" />
  <img width="975" height="165" alt="image" src="https://github.com/user-attachments/assets/beab60ce-3d90-403d-9b2a-2670bb40b4c7" />
  <img width="975" height="217" alt="image" src="https://github.com/user-attachments/assets/4769c919-abd2-4463-afff-3619281314db" />




