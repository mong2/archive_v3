import cloudpassage
import collector
import refinement
import threading
from collections import deque
from multiprocessing import Pool


class ArchiveScan:
    def __init__(self):
        self.api_key = '89a6825d'
        self.api_secret = '42bb35b20d0c5e5b84ce90ea0b3f5587'
        self.api_host = 'api.cloudpassage.com'
        self.api_port = 443
        global server_url_queue
        global server_info_queue
        global scan_queue
        global csm_scan_queue
        global sva_scan_queue

        server_url_queue = deque([])
        server_info_queue = deque([])
        scan_queue = deque([])
        csm_scan_queue = deque([])
        sva_scan_queue = deque([])

        return None

    def build_session(self):
        session = cloudpassage.HaloSession(self.api_key,
                                           self.api_secret,
                                           api_host=self.api_host,
                                           api_port=self.api_port)
        return(session)

    def server_group_list(self, session):
        s_group_list = []
        sg_session = cloudpassage.ServerGroup(session)
        server_group_list = sg_session.list_all()

        for server_group in server_group_list:
            s_group_list.append(server_group["id"])
        return s_group_list

    def populate_server_queue(self, session, s_group_list):
        serv_coll = collector.ServerCollector(session)
        for s in serv_coll.get_servers_from_group(s_group_list):
            server_info_queue.append(s)
        return None

    def server_url_refinement(self):
        serv_ref = refinement.UrlRefinement()
        self.url_refinement_worker.start()
        print self.url_refinement_worker

    def run(self):
        s = self.build_session()
        server = self.server_group_list(s)
        self.populate_server_queue(s, server)
        pool = Pool()
        url_refinement_worker = pool.map(refinement.UrlRefinement().server_url_refinement, server_info_queue)
        return None

if __name__ == "__main__":
    ArchiveScan().run()
