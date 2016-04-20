import dateutil.parser
import json


class Enrichment(object):
    def server_scan_refinement(self, server_scan):
        new_findings = []
        findings = server_scan['scan']['findings']
        if not findings:
            return None
        for finding in findings:
            if finding['status'] == 'bad':
                new_findings.append(finding)
        if new_findings:
            server_scan['scan']['findings'] = new_findings
        if server_scan['scan']['module'] == 'sca':
            csm_scan_queue.append(server_scan)
        else:
            for new_finding in new_findings:
                new_finding['age'] = self.get_issue_age(new_finding['package_name'], server_scan['id'])
                sva_scan_queue.append(server_scan)
        return None

    def get_issue_age(self, package_name, agent_id):
        session = self.session
        api = cloudpassage.HttpHelper(session)

        endpoint = "/v2/issues?issue_type=sva&name=%s&agent_id=%s" % (package_name, agent_id)
        issue_data = api.get(endpoint)

        issues = issue_data['issues']
        created_at = dateutil.parser.parse(issue['created_at'])
        last_seen = dateutil.parser.parse(issue['last_seen_at'])
        duration = last_seen - created_at
        return str(duration.days)
