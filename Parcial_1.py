import re,json

def extractFromRegularExpresion(regex, data):
    return re.findall(regex, data) if data else None

# Ruta del archivo de logs
log_path = r"C:\Users\camil\OneDrive\Escritorio\Apache.log.txt"

# Expresión regular mejorada para capturar IP, fecha, hora, método, código de estado y mensaje de error (si existe)
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s-\s\[(\d{2}/\b[a-zA-Z]{3}\b/\d{4}):(\d{2}:\d{2}:\d{2})\s\+\d{4}]\s\"(\b[A-Z]{3,7}\b)\s\S+\sHTTP/\d\.\d\"\s(\d{3})\s?(.*)?"

# Leer el archivo de logs
with open(log_path, "r", encoding="utf-8") as file:
    data = file.read()

# Extraer los datos
resultado = extractFromRegularExpresion(regex, data)

# Diccionario para almacenar las IPs únicas con sus datos
ipsAlmacenadas = {}

for ip, fecha, hora, metodo, codigo, mensaje in resultado:
    if ip not in ipsAlmacenadas:
        ipsAlmacenadas[ip] = []  # Inicializar lista si la IP no existe
    
    # Formatear los datos del acceso
    log_entry = {
        "fecha": fecha,
        "hora": hora,
        "metodo": metodo,
        "codigo": codigo,
        "mensaje": mensaje.strip() if mensaje else "Sin mensaje"
    }
    
    # Evitar duplicados
    if log_entry not in ipsAlmacenadas[ip]:
        ipsAlmacenadas[ip].append(log_entry)

# Convertir a JSON con formato legible
print(json.dumps(ipsAlmacenadas, indent=4, ensure_ascii=False))

