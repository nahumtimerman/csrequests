import requests, json

class CsRequests(object):
    def __init__(self, username='admin', password='admin', url='http://localhost:9000', domain='Global'):
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

    def get_reservation_details(self, reservation_id:str):
        data = { 'reservation_id': reservation_id, 'token': self.token}
        response = requests.get(self.host_url + '/sandbox/GetReservationDetails', data=data)
        if response.ok:
            reservation_details = json.loads(response.text)
        else:
            raise Exception(response.text)
        return reservation_details
