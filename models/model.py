import json
from qqwry import QQwry


class IP2City:
    def __init__(self):
        self.q = QQwry()
        self.q.load_file(r'data/qqwry.dat', loadindex=True)

        with open(r'data/city_gps.json', encoding='utf-8') as f:
            self.city_gps = json.load(f)
            f.close()

        with open(r'data/fly.json', encoding='utf-8') as f:
            self.line_json = json.load(f)
            f.close()

    def from_ip_to_city(self, ip_str):
        ip = self.q.lookup(ip_str)
        return ip


IP = IP2City()
