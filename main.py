import ctypes

import createAdmin
import init
import network

is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

if not is_admin:
    print("АЛЁ ДАЙ АДМИНА")
    input()
    exit(1)

actions = {
    1: createAdmin.createAdminUser,
    2: init.createFolderAndSetupFirewall,
    3: network.enable
}

print("Выберите действие:")
print("1. Создать пользователя")
print("2. Создать папку")
print("3. Настроить файрвол")


selectedOption = int(input("Выберите действие: "))

try:
    actions[selectedOption]()
except KeyError as e:
    print(f"Действие {e} не найдено")


