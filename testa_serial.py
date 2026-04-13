import serial

# Use a porta que você anotou (COM6)
ser = serial.Serial('COM6', 9600, timeout=1)

print("Aguardando leituras da COM6...")
while True:
    if ser.in_waiting > 0:
        linha = ser.readline().decode().strip()
        print(f"Recebido: {linha}")