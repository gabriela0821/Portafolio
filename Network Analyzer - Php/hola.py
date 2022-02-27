import simplejson 
import json
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="proyecto1"
)
mycursor = mydb.cursor()


#
#rol="INSERT INTO rol (rol) VALUES (%s,%s)"
#usuario="INSERT INTO usuario (correo, contrasena, respuesta_seg, rol_id_rol) VALUES (%s,%s,%s,%s)"
#droles=("Pendiente")
#dusuario=("marcela","camilo","gabriela",1)
#captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)

#mycursor.execute(usuario,dusuario)
#mydb.commit()
def dhcp():    
    mycursor = mydb.cursor()
    captura="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=2  
    cap=("DHCP",id_usuario)
    mycursor.execute(captura,cap)
    mydb.commit()
    captura_id=mycursor.lastrowid
    f = open("MAXIMILIANOPEPE.json", encoding="utf8")
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







def dns ():
    mycursor = mydb.cursor()
    capturadns="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=2  
    capdns=("DNS",id_usuario)
    mycursor.execute(capturadns,capdns)
    mydb.commit()
    
    captura_iddns=mycursor.lastrowid
    f = open("MAXIMILIANOPEPE.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        auxcap= captura_iddns
        info= i["_source"]["layers"]
        lista1= []
        if "dns" in info.keys() and "udp" in info.keys():
            nombre_serv="DNS"
            dns = info["dns"]["Queries"]
            dns1=info["dns"]
            udp= info["udp"]
            puerto= udp["udp.srcport"]
            valor = list(dns.values())   
            nombreq = valor[0].get('dns.qry.name')
            dns2 = info["dns"]
            if "Answers" in dns2:
                dnsp= dns2["Answers"]
                valor= list(dnsp.values())
                ipdns = valor[0].get('dns.a')
                lista1.append(ipdns) 
                lista1.append(nombre_serv)  
                lista1.append(puerto) 
                lista1.append(nombreq)  
                dns1 = "INSERT INTO dns (captura_idcaptura,ip_dns,nombre_servicio,puerto,query_name) VALUES (%s,%s,%s,%s,%s)"
                datosdns = (auxcap,lista1[0],lista1[1], lista1[2], lista1[3])
                mycursor.execute(dns1,datosdns)
                mydb.commit()
            

    

def http():
    caph="INSERT INTO captura (tipo_serv, usuario_idusuario) VALUES (%s,%s)"
    id_usuario=2
    caphttp=("HTTP",id_usuario)
    mycursor.execute(caph,caphttp)
    mydb.commit()
    
    capturaa_id=mycursor.lastrowid
    f = open("MAXIMILIANOPEPE.json", encoding="utf8")
    content = f.read()
    jsondecoded = json.loads(content)
    for i in jsondecoded:
        info= i["_source"]["layers"]
        if "http" in info.keys() and "tcp" in info.keys():
            nombre_serv="HTTP"
            http = info["http"]
            udp=info["tcp"]
            puerto=udp["tcp.port"]
            http1 = "INSERT INTO http (captura_idcaptura,nombre_servicio,puerto) VALUES (%s,%s,%s)"
            http2= (capturaa_id,nombre_serv,puerto)
            mycursor.execute(http1,http2)
            mydb.commit()

http()
    