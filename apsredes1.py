import json

def lerArquivo():
    try:
        arquivo_json = open('teste.json', 'r')
        dados_json = json.load(arquivo_json)
        ipAddr = dados_json['ipAddr']
        netMask = dados_json['netMask']
        return ipAddr, netMask
    except Exception as erro:
        print("Ocorreu um erro ao carregar o arquivo")
        print("Erro: {}". format(erro))

def split(ipAddr, netMask):
    vetorIpAddr = ipAddr.split(".")
    vetorNetMask = netMask.split(".")
    return vetorIpAddr, vetorNetMask
    
def cast(ipAddr, netMask):   
    vetorIpAddr = []
    for i in ipAddr:
        vetorIpAddr.append(int(i))
    vetorNetMask = []
    for i in netMask:
        vetorNetMask.append(int(i))
    return vetorIpAddr, vetorNetMask


def converteBinario(Ip):
    ipBinario = []
    for i in range(4):
        n = Ip[i]
        binario = ""
        while(True):
            binario = binario + str(n%2)
            n = n//2
            if n == 0:
                break
        binario = binario[::-1]
        #binario = int(binario)
        ipBinario.append(binario)
    return ipBinario

def preencherVetor(Ip):
    contador = []
    ipBinario = converteBinario(Ip)
    for i in range(4):
        contador.append((len(ipBinario[i])))
    
    for i in range(4):
        if(contador[i] < 8):
            aux = 8 - contador[i]
            for j in range(aux):
                ipBinario[i] = str("0") + ipBinario[i]

    return ipBinario

def validar(ipAddr, netMask):
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


    for i in range(4):
        for j in range(8):
            if(netMaskBinario[i][j] == 0):
                flag = 1
            elif(netMaskBinario[i][j] == 1 and flag == 1):
                print("mascara invalida")   


def netID_hostID(netMask):
    netMaskVetor = preencherVetor(netMask)
    contador0 = 0
    contador1 = 0
    for i in range(4):
        for j in range(8):
            if(netMaskVetor[i][j] == '1'):
                contador1 = contador1 + 1
            else:
                contador0 = contador0 + 1
    print("Quantidade de bits da rede:", contador1)
    print("Quantidade de bits da host:", contador0)
    hosts = int(contador0)
    hosts = ((2 ** hosts)-2)
    print("Quantidade de hosts na rede", hosts)

def ipRede(ipAddr, netMask):
    ipRede = []
    for i in range(4):
        aux = ipAddr[i] & netMask[i]
        ipRede.append(aux)
    print("Ip da rede:", ipRede)
    return ipRede

def ipBroadcast(ipAddr, netMask):
    ipRedeVetor = ipRede(ipAddr, netMask)
    ipRedeBinario = preencherVetor(ipRedeVetor)
    ipBroadcastBinario = preencherVetor(netMask)
    contador0 = 0
    aux = 0
    for i in range(3, -1, -1):
        for j in range(7, -1, -1):
            if(ipBroadcastBinario[i][j] == '0'):
                contador0 = contador0 + 1
            else:
                aux = 1
                break
        if(aux == 1):
            break
    
    contador2 = contador0
    ipBroadcastBinarioCopia = ipRedeBinario
    contador1 = 0
    flag = 0
    
    for i in range(3, -1, -1):
        for j in range(7, -1, -1):
            if(contador0 <= 8):
                contador1 = 8
                contador1 = contador1 - contador2
                ipBroadcastBinarioCopia[i] = ipRedeBinario[i][:contador1] + '1'
            elif(contador0 >= 9 and contador0 <= 16):
                if(contador1 == 8):
                    contador1 = contador0 - 8
                    contador1 = abs(contador1 - 8)
                ipBroadcastBinarioCopia[i] = ipRedeBinario[i][:contador1] + '1'
            elif(contador0 >= 17 and contador0 <= 24):
                if(contador1 == 8):
                    contador1 = 0
                    flag = flag + 1
                if(contador1 == 0 and flag == 2):
                    contador1 = 24 - contador0
                ipBroadcastBinarioCopia[i] = ipRedeBinario[i][:contador1] + '1'
            elif(contador0 >= 25 and contador0 <= 32):
                if(contador1 == 8):
                    contador1 = 0
                    flag = flag + 1
                if(contador1 == 0 and flag == 3):
                    contador1 = 32 - contador0
                ipBroadcastBinarioCopia[i] = ipRedeBinario[i][:contador1] + '1'
            contador2 = contador2 - 1
            contador1 = contador1 + 1

            if(contador2 == 0):
                aux = 0
                break
        if(aux == 0):
            break

    print(ipBroadcastBinarioCopia)



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
    #alo = verificar(teste3[0], teste3[1])
    asd = ipBroadcast(teste3[0], teste3[1])
    #teste4 = netID_hostID(teste3[1])
    #oi = ipRede(teste3[0], teste3[1])
    #teste4 = verificar(teste3[0], teste3[1])
    #if(teste4 == 1):
    #    print("IP Inválido")
    #elif(teste4 == 2):
    #    print("Mascara Inválida")        
    #else:    
    #    teste7 = reservado(teste4[0])
    #    teste5 = classeIp(teste4[0])
    #    teste6 = ipRede(teste4[0], teste4[1])
