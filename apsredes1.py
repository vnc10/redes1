import json

def lerArquivo():
    try:
        arquivo_json = open('teste.json', 'r')
        dados_json = json.load(arquivo_json)
        ipAddr = dados_json['ipAddr']
        netMask = dados_json['netMask']
        #print(ipAddr)
        #print(netMask)
        return ipAddr, netMask
    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo")
        print("Erro: {}". format(erro))

def split(ipAddr, netMask):
    vetorIpAddr = ipAddr.split(".")
    #print(vetorIpAddr) 
    vetorNetMask = netMask.split(".")
    #print(vetorNetMask)
    return vetorIpAddr, vetorNetMask
    
def cast(ipAddr, netMask):   
    vetorIpAddr = []
    for i in ipAddr:
        vetorIpAddr.append(int(i))
    #print(vetorIpAddr)
    vetorNetMask = []
    for i in netMask:
        vetorNetMask.append(int(i))
    #print(vetorNetMask)
    return vetorIpAddr, vetorNetMask

def verificar(ipAddr, netMask):
    aux = 0
    for i in range(4):
        if(ipAddr[i] < 0 or ipAddr[i] > 255):
            aux = 1
            return 1
            break
        elif(netMask[i] < 0 or netMask[i] > 255):
            aux = 1
            return 2
            break
    if (aux == 0):
        #print("IP e Mascara Válida")
        #print(ipAddr, netMask)
        return ipAddr, netMask

def ipRede(ipAddr, netMask):
    vet = []
    for i in range(4):
        aux = ipAddr[i] & netMask[i]
        vet.append(aux)
    print("Ip da rede:", vet)

def classeIp(ipAddr):
    if(ipAddr[0] <= 127):
        print("Classe A")
    elif(ipAddr[0] >= 128 and ipAddr[0] <= 191):
        print("Classe B")
    elif(ipAddr[0] >= 192 and ipAddr[0] <= 223):
        print("Classe C")

def reservado(ipAddr):
    if(ipAddr[0] == 127):
        print("Endereço de loopback")
    elif(ipAddr[0] == 10):
        print("Ip reservado")    
    elif(ipAddr[0] == 172 and (ipAddr[1] >= 16 or ipAddr[1] <= 31)):
        print("Ip reservado")
    elif(ipAddr[0] == 192 and ipAddr[1] == 168):
        print("Ip reservado")
    elif(ipAddr[0] == 169 and ipAddr[1] == 254):
        print("Ip reservado")

if __name__ == "__main__":
    teste1 = lerArquivo()
    teste2 = split(teste1[0], teste1[1])
    teste3 = cast(teste2[0], teste2[1])
    teste4 = verificar(teste3[0], teste3[1])
    if(teste4 == 1):
        print("IP Inválido")
    elif(teste4 == 2):
        print("Mascara Inválida")        
    else:    
        teste7 = reservado(teste4[0])
        #teste5 = classeIp(teste4[0])
        #teste6 = ipRede(teste4[0], teste4[1])
