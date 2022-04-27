from Application import Application
from Application import Applications
from Utils import Utils

global applications


class Node:

    def __init__(self, x, y, key, cpu, mem, net):
        self.x = x
        self.y = y
        self.key=key
        self.resources = {'cpu': cpu, 'mem': mem, 'net': net}
        self.resources_usage = {'cpu': 0, 'mem': 0, 'net': 0}
        self.resources_usage_rate = {'cpu': 0, 'mem': 0, 'net': 0}
        self.deploy_app_key_set = set()

    def update_resources_usage(self):
        for resource in self.resources_usage:
            self.resources_usage[resource] = 0
            self.resources_usage_rate[resource] = 0

        for app_key in self.deploy_app_key_set:
            for resource in self.resources:
                self.resources_usage[resource] += Applications.get_app(app_key).resources[resource]

        for resource in self.resources:
            self.resources_usage_rate[resource] = self.resources_usage[resource] / self.resources[resource]

    def if_deploy(self, app: Application):
        flag = True

        if not app.exec_delay + Utils.get_trans_delay(app.user.x, app.user.y, self.x, self.y) <= app.sla:
            flag = False
            return flag

        for resource in self.resources:
            if self.resources_usage[resource] + app.resources[resource] > self.resources[resource]:
                flag = False
                return flag

        return flag

    def deploy(self, app: Application):
        self.deploy_app_key_set.add(app.key)

    def release(self, app: Application):
        self.deploy_app_key_set.remove(app.key)


class Nodes:

    dict={}

    @classmethod
    def get_num(cls):
        return len(cls.dict)

    @classmethod
    def get_node(cls,key)->Node:
        return cls.dict[key]

    @classmethod
    def add_node(cls,node:Node):
        cls.dict[node.key]=node

    @classmethod
    def del_node(cls,node:Node):
        del cls.dict[node.key]