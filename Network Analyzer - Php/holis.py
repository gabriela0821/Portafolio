import simplejson 
import json
import mysql.connector
import sys
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="proyecto1"
)


#print("hola desde python")
nombre=sys.argv[1]

#def usuario(nombre):
    

#print("hola")
mycursor = mydb.cursor()
a="SELECT idusuario as id FROM usuario WHERE nombre_usuario='"+nombre+"'"
#print(a)
a2=str(a)
mycursor.execute(a2)
myresult = mycursor.fetchall()
resp=0
for row in myresult:
    resp=row[0]


#
#rol="INSERT INTO rol (rol) VALUES (%s,%s)"
#usuario="INSERT INTO usuario (correo, contrasena, respuesta_seg, rol_id_rol) VALUES (%s,%s,%s,%s)"
#droles=("Pendiente")
#dusuario=("marcela","camilo","gabriela",1)
#captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)

#mycursor.execute(usuario,dusuario)
#mydb.commit()



def dhcp(nombre):    
    mycursor = mydb.cursor()
    captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=nombre  
    cap=("DHCP",id_usuario)
    mycursor.execute(captura,cap)
    mydb.commit()
    captura_id=mycursor.lastrowid
    f = open("pepetito.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        info= i["_source"]["layers"]
        if "dhcp" in info.keys() and "udp" in info.keys():
            nombre_serv="DHCP"
            dhcp = info["dhcp"]
            udp=info["udp"]
            iplen= dhcp["dhcp.ip.client"],dhcp["dhcp.ip.your"],dhcp["dhcp.ip.server"] 
            lista=[]
            iplen2=udp["udp.dstport"],udp["udp.srcport"]
            lista.append(nombre_serv)
            lista.extend(iplen)
            lista.extend(iplen2)
            dhcp1 = "INSERT INTO dhcp (captura_idcaptura,ip_cliente, ip_pc_fisic, ip_server, nombre_servicio,puerto, puerto_src) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            datos = (captura_id,lista[1],lista[2],lista[3],lista[0],lista[4],lista[5])
            mycursor.execute(dhcp1,datos)
        mydb.commit()



def ftp(nombre):
    mycursor = mydb.cursor()
    captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=nombre  
    cap=("FTP",id_usuario)
    mycursor.execute(captura,cap)
    mydb.commit()
    captura_id=mycursor.lastrowid
    f = open("pepetito.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        info= i["_source"]["layers"]
        lista1= []
        if "ftp" in info.keys() and "tcp" in info.keys() and "ip" in info.keys():
            tcp= info["tcp"]
            ftp=info["ftp"]
            nmbre= "FTP"
            puerto=tcp["tcp.srcport"]
            ip1=info["ip"]
            ip2= ip1["ip.host"]
            #print(ftp)
            estesi={"ftp":ftp}
            s1=list(estesi.values())
            s2=s1[0]
            s3=list(s2)
            hey=s3[2]
            yy=str(hey)
            

            este=yy.replace("\\r\\n","")
            ftp1 = "INSERT INTO ftp (nombre_servicio,puerto,captura_idcaptura, arg, ip) VALUES (%s,%s,%s,%s,%s)"
            ftp2= (nmbre,puerto,captura_id,este, ip2)
            mycursor.execute(ftp1,ftp2)
            mydb.commit()
            

            
def dns (nombre):
    mycursor = mydb.cursor()
    capturadns="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    nombre2="SELECT idusuario FROM usuario WHERE nombre_usuario='nombre';"
    id_usuario=nombre  
    capdns=("DNS",id_usuario)
    mycursor.execute(capturadns,capdns)
    mydb.commit()
    
    captura_iddns=mycursor.lastrowid
    f = open("pepetito.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        auxcap= captura_iddns
        info= i["_source"]["layers"]
        lista1= []
        if "dns" in info.keys() and "udp" in info.keys() and "ip" in info.keys() :
            nombre_serv="DNS"
            dns = info["dns"]["Queries"]
            dns1=info["dns"]
            udp= info["udp"]
            puerto= udp["udp.srcport"]
            valor = list(dns.values())   
            nombreq = valor[0].get('dns.qry.name')
            ip=info["ip"]
            iphost=ip["ip.src_host"]

            dns2 = info["dns"]
            if "Answers" in dns2:
                dnsp= dns2["Answers"]
                valor= list(dnsp.values())
                ipdns = valor[0].get('dns.a')
                lista1.append(ipdns) 
                lista1.append(nombre_serv)  
                lista1.append(puerto) 
                lista1.append(nombreq)  
                dns1 = "INSERT INTO dns (captura_idcaptura,ip_dns,nombre_servicio,puerto,query_name,ip_host) VALUES (%s,%s,%s,%s,%s,%s)"
                datosdns = (auxcap,lista1[0],lista1[1], lista1[2], lista1[3], iphost)
                mycursor.execute(dns1,datosdns)
                mydb.commit()

            

def http(nombre):
    caph="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=nombre
    caphttp=("HTTP",id_usuario)
    mycursor.execute(caph,caphttp)
    mydb.commit()
    
    capturaa_id=mycursor.lastrowid
    f = open("pepetito.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:


        info= i["_source"]["layers"]
        if "http" in info.keys() and "tcp" in info.keys() and "ip" in info.keys():
            nombre_serv="HTTP"
            http = info["http"]
            udp=info["tcp"]
            puerto=udp["tcp.port"]
            ip1= info["ip"]
            ip2=ip1["ip.dst_host"]
            http1 = "INSERT INTO http (captura_idcaptura,nombre_servicio,puerto, ip) VALUES (%s,%s,%s,%s)"
            http2= (capturaa_id,nombre_serv,puerto, ip2)
            mycursor.execute(http1,http2)
            mydb.commit()


def smtp(nombre):
  mycursor = mydb.cursor()
  captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
  id_usuario=nombre
  cap=("SMTP",id_usuario)
  mycursor.execute(captura,cap)
  mydb.commit()
  captura_id=mycursor.lastrowid
  f = open("pepetito.json", encoding="utf8")
  content = f.read()
  jsondecoded = json.loads(content)
  for i in jsondecoded:
    info = i["_source"]["layers"]

    if "smtp" in info.keys() and "ip" in info.keys() and "tcp" in info.keys():
      ip=info["ip"]
      ip_host=ip["ip.host"]
      ip_dst= ip["ip.dst"]
      tcp=info["tcp"]
      smtp=info["smtp"]
      #print(smtp)
      puertoinicio=tcp["tcp.srcport"]
      puertofinal=tcp["tcp.dstport"]
      nombre="SMTP"
    # print(smtp.keys())
      if "smtp.command_line_tree" in smtp.keys():
        line_tree=smtp["smtp.command_line_tree"]
        infosmtpd= line_tree["smtp.req.command"]
        if(infosmtpd=="DATA"):
          fmtp1 = "INSERT INTO smtp (nombre_servicio, captura_idcaptura, data, ip_dst, ip_host,puertoinicio,puertofinal) VALUES (%s,%s,%s,%s,%s,%s,%s)"
          datos = (nombre, captura_id, infosmtpd, ip_dst, ip_host, puertoinicio, puertofinal)
          mycursor.execute(fmtp1,datos)
          mydb.commit()


#print("esto-> " +usuario(nombre)+ " <--")
dhcp(resp)
http(resp)
dns(resp)
ftp(resp)
smtp(resp)






