import json
from qqwry import QQwry


class IP2City:
    def __init__(self):
        self.q = QQwry()
        self.q.load_file(r'data/qqwry.dat', loadindex=True)

    def from_ip_to_city(self, ip_str):
        ip = self.q.lookup(ip_str)
        return ip


IP = IP2City()
