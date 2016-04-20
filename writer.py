import json
import os


class Write(object):

	def __init__(self):
		return None

	def write_file(directory, scan_time, data, server_info):
		time = str(scan_time.year) + '/' + str(scan_time.month) + '/' + str(scan_time.day) + '/'
		filename = directory + "/output/" + time

		if server_info:
			filename += data['id'] + 'server_info.json'
		else:
			filename += data['scan']['server_id'] + '/' 
			filename += data['scan']['module'] + data['scan']['id'] + '.json'
		
		if not os.path.exists(os.path.dirname(filename)):
			os.makedirs(os.path.dirname(filename))
		with open (filename, "w") as f:
			json.dump(data, f)
		return None

