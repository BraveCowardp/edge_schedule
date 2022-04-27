from application import application
class node:

    def __init__(self,x,y,cpu,mem,net):
        self.x=x
        self.y=y
        self.cpu=cpu
        self.mem=mem
        self.net=net
        self.cpu_usage=0
        self.mem_usage=0
        self.net_usage=0
        self.cpu_usage_rate=0
        self.mem_usage_rate=0
        self.net_usage_rate=0

    def deploy(self,app:application):
        self.cpu_usage+=app.cpu_demand
        self.mem_usage+=app.mem_demand
        self.net_usage+=app.net_demand