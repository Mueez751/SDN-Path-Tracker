from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import SingleSwitchTopo
from mininet.log import setLogLevel
from mininet.cli import CLI

def run():
	setLogLevel('info')
	topo = SingleSwitchTopo(4)
	net = Mininet(topo = topo, controller = lambda name: RemoteController(name,ip='127.0.0.1' , port = 6653))
	net.start()
	print("Network Started")
	print("Hosts:", [h.name for h in net.hosts])
	print("Switches:" , [s.name for s in net.switches])
	CLI(net)
	net.stop()

if __name__ == '__main__':
	run()
