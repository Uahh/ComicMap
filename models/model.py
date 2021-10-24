from qqwry import QQwry


class ip():
    def __init__(self):
        self.q = QQwry()
        self.q.load_file('/Users/uahh/Project/ComicMap/static/qqwry.dat')

    def from_ip_to_city(self, ip_str):
        ip = self.q.lookup(ip_str)
        return ip

