from User import User
from typing import Dict


class Application:

    def __init__(self, key, cpu_demand=0, mem_demand=0, net_demand=0, exec_delay=0, sla=0, user: User = None):
        self.key = key
        self.resources = {'cpu': cpu_demand, 'mem': mem_demand, 'net': net_demand}
        self.exec_delay = exec_delay
        self.sla = sla
        self.user = user


class Applications:
    dict = {}

    @classmethod
    def get_num(cls):
        return len(cls.dict)

    @classmethod
    def add_app(cls, app: Application):
        cls.dict[app.key] = app

    @classmethod
    def del_app(cls, key):
        del cls.dict[key]

    @classmethod
    def get_app(cls,key)->Application:
        return cls.dict[key]

if __name__ == '__main__':
    user1 = User(7, 8)
    app1 = Application(1, 2, 3, 4, 5, 6, user1)
    # applications = Applications()

    Applications.add_app(app1)
    print(Applications.dict)
    applications = Applications()
    print(applications.dict)
    del app1
    Applications.del_app(1)
    print(Applications.dict)
