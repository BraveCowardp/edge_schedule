from user import user
class application:

    def __init__(self,key,cpu_demand=0,mem_demand=0,net_demand=0,exec_delay=0,sla=0,user:user=None):
        self.key=key
        self.cpu_demand=cpu_demand
        self.mem_demand=mem_demand
        self.net_demand=net_demand
        self.exec_delay=exec_delay
        self.sla=sla
        self.user=user


class applications:

    def __init__(self):
        self.set={}

    def get_num(self):
        return len(self.set)

    def add_app(self,app:application):
        self.set[app.key]=app

    def del_app(self,key):
        del self.set[key]

if __name__=='__main__':
    user1=user(7,8)
    app1=application(1,2,3,4,5,6,user1)
    applications=applications()

    applications.add_app(app1)
    print(applications.set)

    applications.del_app(1)
    print(applications.set)
