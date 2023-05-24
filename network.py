import subprocess

#Саня чекируй
def enable():
    powershell_commands = [
        "netsh advfirewall firewall set rule group=\"Обнаружение сети\" new enable=Yes",
        "netsh advfirewall firewall set rule group=\"Общий доступ к файлам и принтерам\" new enable=Yes",
    ]

    for command in powershell_commands:
        subprocess.run(["powershell", "-Command", command])
