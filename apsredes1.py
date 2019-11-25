import json

def lerArquivo():
    try:
        arquivo_json = open('teste.json', 'r')
        dados_json = json.load(arquivo_json)
        ipAddr = dados_json['ipAddr']
        netMask = dados_json['netMask']
        vetSplit =  split(ipAddr, netMask)
        vetCast = cast(vetSplit[0], vetSplit[1])
        return vetCast[0], vetCast[1]
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
        ipBinario.append(binario)
    return ipBinario

def converteDecimal(Ip):
    ipDecimal = []
    for i in range(4):
        n = Ip[i]
        decimal = 0
        n = n[::-1]
        tam = len(n)
        for i in range(tam):
            if n[i] == "1":
                decimal = decimal + 2**i
        ipDecimal.append(decimal)
    return ipDecimal


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
        if(ipAddr[i] > 255):
            aux = 1
            return 1
            break
        elif(netMask[i] > 255):
            aux = 1
            return 2
            break
    
    netMaskBinario = preencherVetor(netMask)
    flag = 0
    for i in range(4):
        for j in range(8):
            if(netMaskBinario[i][j] == "0"):
                flag = 1
            elif(netMaskBinario[i][j] == "1" and flag == 1):
                print("Mascara invalida")
                break   


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
    print("Quantidade de hosts na rede:", hosts)

def ipRede(ipAddr, netMask):
    ipRede = []
    for i in range(4):
        aux = ipAddr[i] & netMask[i]
        ipRede.append(aux)
    return ipRede

def ipBroadcast(ipAddr, netMask):
    ipRedeVetor = ipRede(ipAddr, netMask)
    print("Ip da rede:", ipRedeVetor)
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
    broadcast = converteDecimal(ipBroadcastBinarioCopia)      
    print("Ip de Broadcast: ", broadcast)
    return broadcast




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
    ler = lerArquivo()
    valida = validar(ler[0], ler[1])
    qtde = netID_hostID(ler[1])
    classe = classeIp(ler[0])
    rede = ipRede(ler[0], ler[1])
    broadcast = ipBroadcast(rede, ler[1])
    reserv = reservado(ler[0])

