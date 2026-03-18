import socket
import psutil

def obter_hostname():
    return socket.gethostname()

def obter_fqdn_dominio():
    """Obtém o sufixo do domínio (FQDN) da máquina"""
    try:
        fqdn = socket.getfqdn()
        return fqdn.lower()
    except Exception:
        return ""

def eh_rede_redecorp():
    """Verifica se a máquina está conectada à rede REDECORP"""
    fqdn = obter_fqdn_dominio()
    return "redecorp.br" in fqdn

def obter_ip_redecorp():
    """Obtém o IP corporativo da rede REDECORP"""
    # Primeiro verifica se está na rede REDECORP
    if not eh_rede_redecorp():
        return None
    
    ips_validos = []
    try:
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET:  
                    ip = addr.address
                    
                    # Válido para rede 10.x.x.x (REDECORP) ou 172.21.x.x
                    if ip.startswith("10.") or ip.startswith("172.21."):
                        # Descarta IPs de loopback
                        if not ip.startswith("127."):
                            ips_validos.append(ip)
    except Exception as e:
        print(f"Erro ao obter IPs: {e}")
        return None
    
    return ips_validos[0] if ips_validos else None

def verificar_ip():
    ip = obter_ip_redecorp()
    hostname = obter_hostname()
    if ip:
        return f"Computador: {hostname}\nIP Corporativo: {ip}"
    else:
        return f"Computador: {hostname}\n⚠️ Ligue a VPN para obter IP corporativo"