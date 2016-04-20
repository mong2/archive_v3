import cloudpassage
import archive
import json

class ServerCollector(object):

	def __init__(self, session):
		self.session = session
		return None

	def __iter__(self, server_group_list):
		for group_id in server_group_list:
			for server in self.get_servers_from_group(group_id):
				yield server

	def get_servers_from_group(self, s_group_list):
		session = self.session
		s_list = []
		for s_group in s_group_list:
			sg_session = cloudpassage.ServerGroup(session)
			servers_list = sg_session.list_members(s_group)
			for server in servers_list:
				s_list.append(server)
		return s_list 

	# def get_scan(self, server_url):
	# 	session = self.session
	# 	api = cloudpassage.HttpHelper(session)

	# 	scan = api.get(server_url)
	# 	scan_queue.append(scan)
	# 	return None

# serv_coll = collector.ServerCollector(session)
# for s in serv_coll(group_list)



