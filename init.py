import os
import subprocess


def createFolderAndSetupFirewall():
    folder = input("Введите название папки: ")
    try:
        os.mkdir(f'c:\\{folder}')
    except FileExistsError as e:
        print(f"Папка {folder} уже существует, настраиваю файрвол")

    powershell_command = [f'Add-MpPreference -ExclusionPath C:\\{folder} ',
                          "Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled True ",
                          "Set-NetFirewallProfile -Name Domain, Public, Private -DefaultInboundAction Allow",
                          "Set-NetFirewallProfile -Name Domain, Public, Private -DefaultOutboundAction Allow"]

    for command in powershell_command:
        subprocess.run(["powershell", "-Command", command])

