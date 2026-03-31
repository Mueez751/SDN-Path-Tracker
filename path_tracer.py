from pox.core  import core
from pox.lib.util import dpid_to_str
import pox.openflow.libopenflow_01 as of

log = core.getLogger()
path_log = {}

class PathTracer(object):
	def __init__(self):
		core.openflow.addListeners(self)
		self.mac_to_port = {}
		log.info("Path Tracer Controller Started!")

	def _handle_ConnectionUp(self,event):
		log.info("Switch Conneted : %s",dpid_to_str(event.dpid))

	def _handle_packetIn(self,event):
		packet = event.parsed
		dpid = event.dpid
		in_port = event.port
		if not packet.parsed:
			return
		self.mac_to_port.setdefault(dpid, {} )
		self.mac_to_port[dpid][packet.src] = in_port
		path_key = str(packet.src) + "->" + str(packet.dst)
		if path_key not in path_log:
			path_log[path_key] = []
		path_log[path_key].append("Switch:" + dpid_to_str(dpid) + "Port"+ str(in_port))
		log.info("PATH: %s via switch %s Port %s", path_key , dpid_to_str(dpid), in_port)
		if packet.dst in self.mac_to_port[dpid]:
			out_port = self.mac_to_port[dpid][packet.dst]
		else :
			out_port = of.OFPP_FLOOD
		msg = of.ofp_flow_mod()
		msg.match = of.ofp_match.from_packet(packet,in_port)
		msg.idle_timeout = 10
		msg.hard_timeout = 30
		msg.action.append(of.ofp_action_output(port=out_port))
		msg.data = event.ofp
		event.connection.send(msg)

def launch():
	core.registerNew(PathTracer)
