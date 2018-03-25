 # -*- coding:utf-8 -*-

import socket
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#info = 'python'
def get_computer_tuling(info):
    key = '186cccedc79549ecac4dcc8a56fc9fb4'
    api = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info
    response = urllib.urlopen(api).read()
    dic_json = json.loads(response)
#    return '机器人:'.decode('utf-8')+dic_json['text']
    return 'server:'.decode('utf-8')+dic_json['text']


host = socket.gethostbyname(socket.gethostname())
print host
port = 11112
s = socket.socket()
s.bind((host,port))
s.listen(1)

while True:
    clnt,addr = s.accept()
    print 'client address:',addr
    while True:
         data = clnt.recv(1024)
         #print data
         if not data:sys.exit()
         print 'server: ',data
         result = get_computer_tuling(data)
         if len(result) == 0:
             result = "EXD"
         clnt.sendall(result)

clnt.close()
