import serial
import os
import django

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'acessibilidade.settings')
django.setup()

from leituras.models import AcessoRFID

# Porta do Arduino (use a mesma do teste)
SERIAL_PORT = 'COM6'
BAUD_RATE = 9600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    print(f"Conectado à porta {SERIAL_PORT}. Aguardando leituras...")
except Exception as e:
    print(f"Erro ao abrir a porta serial: {e}")
    exit()

while True:
    if ser.in_waiting > 0:
        linha = ser.readline().decode().strip()
        if linha:
            print(f"UID lido: {linha}")
            # Salva no banco de dados SQLite
            novo_acesso = AcessoRFID(uid=linha)
            novo_acesso.save()
            print(f"Salvo no banco com sucesso!")