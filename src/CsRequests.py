import requests, json


class CsRequests(object):
    def __init__(self, username='admin', password='admin', url='http://localhost:9000', domain='Global'):
        """
        Logon to server and store token
        :type username: str
        :type password: str
        :type url: str
        :type domain: str
        """
        self.host_url = url
        self.token = self.logon(password, url, username, domain)

    @staticmethod
    def logon(password, url, username, domain):
        token = None
        data = {'username': username, 'password': password, "domain": domain}
        response = requests.put(url + '/Api/Auth/Login', data=data)
        if response.ok:
            token = json.loads(response.text)
        return token

    def get_reservation_details(self, reservation_id):
        """
        :type reservation_id: str
        :return: reservation details
        """
        data = {'SandboxId': reservation_id}
        headers = {"Authorization": "Bearer " + self.token}
        response = requests.get(self.host_url + '/Sandbox/GetReservationDetailsNextGen', data=data, headers=headers)
        if response.ok:
            reservation_details = json.loads(response.text)
        else:
            raise Exception(response.text)
        return reservation_details
