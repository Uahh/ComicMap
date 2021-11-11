import json
from qqwry import QQwry


class IP2City:
    def __init__(self):
        self.q = QQwry()
        self.q.load_file(r'data/qqwry.dat', loadindex=True)

        with open(r'data/city_line.json', encoding='utf-8') as json_file:
            self.city_line = json.load(json_file)
            json_file.close()

    def from_ip_to_city(self, ip_str):
        ip = self.q.lookup(ip_str)
        return ip


IP = IP2City()
