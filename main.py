import csv

# Читаем кошельки из wallets.txt
with open('wallets.txt', 'r') as f:
    wallets = [line.strip().lower() for line in f]  # Приводим адреса к нижнему регистру

# Создаем словарь для хранения результатов
results = {}

# Читаем CSV файл и проверяем наличие кошельков
with open('phase1xp.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        user_address = row['userAddress'].lower()  # Приводим адреса к нижнему регистру
        if user_address in wallets:
            results[user_address] = row['xpTotal']

# Записываем результаты в result.csv
with open('result.csv', 'w', newline='') as csvfile:
    fieldnames = ['userAddress', 'xpTotal']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for wallet, xp in results.items():
        writer.writerow({'userAddress': wallet, 'xpTotal': xp})

print("Обработка завершена. Файл result.csv создан.")
