from netmiko import ConnectHandler

device = input("Insira o endereço IP: ")
username = input("Insira o usuário: ")
password = input("Insira a senha: ")
roteador = {
        'device_type': 'cisco_ios',
        'host': device,
        'username': username,
        'password': password,
    }
extensão = ".txt"
connect = ConnectHandler(**roteador)
output = connect.send_command(input("Insira o comando: "))
print(output)

with open(input("Insira o nome do arquivo: ") + extensão, "w") as arquivo:
    for valor in output:
        arquivo.write(valor)