import os

name_os = None
IP_os = None

# Получаем IP-адреса через команду ipconfig
command = "ipconfig"
output = os.popen(command).read()

# Ищем строки, содержащие 'IPv4 Address'
ipv4_lines = [line for line in output.split('\n') if 'IPv4' in line]

# Извлекаем сами адреса
ips = []
for line in ipv4_lines:
    parts = line.split(':')
    if len(parts) > 1:
        ips.append(parts[-1].strip())

name_os = os.getenv('LOGONSERVER')
IP_os = ', '.join(ips)
print(name_os)
print(IP_os)
