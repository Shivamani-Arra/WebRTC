import serial.tools.list_ports

def list_serial_ports():
    """List available serial ports."""
    try:
        ports = serial.tools.list_ports.comports()
        if not ports:
            print("No serial ports found.")
            return

        for port, desc, hwid in sorted(ports):
            print(f"Port: {port}, Description: {desc}, Hardware ID: {hwid}")

    except Exception as e:
        print(f"Error listing serial ports: {e}")

# Call the function to list available ports
list_serial_ports()
