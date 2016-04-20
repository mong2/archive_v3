
class UrlRefinement(object):
	def server_url_refinement(self, server_id):
		scan_types = ["svm", "sca"]
		for scan_type in scan_types:
			url = ""
			url = "/v1/servers/%s/%s" % (server_id, scan_type)
			server_url_queue.append(url)
			return url

	