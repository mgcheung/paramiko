__author__ = 'mgcheung'
import paramiko

class MyTestClass():
    def __init__(self,print_method):
        self.print_method = print_method
        self.t = None

    def remote_banner_hook(self,banner):
        self.print_method( 'Remote version: '+banner)

    def negotiation_hook(self,info):
        self.print_method(info)

    def session_id_hook(self,input1,input2):
        self.print_method('Data going into session id: '+ input1.encode('hex'))
        self.print_method('Session id: '+ input2.encode('hex'))

    def sign_hook(self,data,r,s):
        self.print_method('Data being signed: '+data.encode('hex')+'\n'+'r = '+r.encode('hex')+'\n'+'s = '+s.encode('hex'))

    def transportHook(self,transport):
        self.t = transport
        self.print_method('Local version: ' + self.t.get_local_version())
        AlgoList = self.t.get_algorithms()
        for category in AlgoList:
            self.print_method(str(category))
        self.t.set_remote_banner_hook(self.remote_banner_hook)
        self.t.set_negotiation_hook(self.negotiation_hook)
        self.t.set_session_id_hook(self.session_id_hook)


