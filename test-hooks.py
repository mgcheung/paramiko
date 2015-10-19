__author__ = 'mgcheung'
import paramiko

class MyTestClass():
    def __init__(self):
        self.t = None

    def remote_banner_hook(self,banner):
        print 'Remote version: '+banner

    def negotiation_hook(self,info):
        print info

    def session_id_hook(self,input1,input2):
        print 'Data going into session id: '+ input1.encode('hex')
        print 'Session id: '+ input2.encode('hex')

    def sign_hook(self,data,r,s):
        print 'Data being signed: '+data.encode('hex')
        print 'r = '+r.encode('hex')
        print 's = '+s.encode('hex')

    def transportHook(self,transport):
        self.t = transport
        print 'Local version: ' + self.t.get_local_version()
        AlgoList = self.t.get_algorithms()
        for category in AlgoList:
            print category
        self.t.set_remote_banner_hook(self.remote_banner_hook)
        self.t.set_negotiation_hook(self.negotiation_hook)
        self.t.set_session_id_hook(self.session_id_hook)

mytest = MyTestClass()
pkey = paramiko.dsskey.DSSKey(filename='/home/mgcheung/.ssh/testdsa',sign_hook=mytest.sign_hook)
ssh = paramiko.SSHClient()
ssh.connect('localhost',username='mgcheung',pkey=pkey,transport_hook=mytest.transportHook)

