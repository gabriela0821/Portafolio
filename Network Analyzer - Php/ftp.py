#s()
import simplejson 
import json
def ftp():
    f = open("pepetito.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        info= i["_source"]["layers"]
        lista1= []
        if "ftp" in info.keys() and "tcp" in info.keys():
            tcp= info["tcp"]
            ftp=info["ftp"]
            puerto=tcp["tcp.srcport"]
            nombre_serv="SMTP"
            #print(ftp)
            estesi={"ftp":ftp}
            s1=list(estesi.values())
            s2=s1[0]
            w=str(s2)
            #x=s2.split(",")
            #s3=s2['ftp.response.arg']
            #print(w)
            #for i in range(0,len(ftp)):
              #  k=ftp[2]
               # print(f)
            #a2=list(a.values())
            #print(s2)
            s3=list(s2)
            hey=s3[2]
            yy=str(hey)
            este=yy.replace("\\r\\n","")
            print(este)
            #for i in range(0,len(a2)):
               # print(a2[1])
            #a1=a2[0]
            #qq=a.values()
            #h=qq[0]
            #a=[ftp]

ftp()