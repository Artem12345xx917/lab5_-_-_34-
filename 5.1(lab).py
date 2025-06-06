import requests

username = "Artem12345xx917"
url = f"https://api.github.com/users/{username}"

response = requests.get(url)

if response.status_code != 200:
    print("❌ Не вдалося отримати дані. Код помилки:", response.status_code)
    exit()

user = response.json()

print(f"👤 Логін: {user['login']}")
print(f"📛 Ім’я: {user.get('name', 'Не вказано')}")
print(f"📅 Акаунт створено: {user['created_at']}")
print(f"📦 Публічних репозиторіїв: {user['public_repos']}")
print(f"🌍 Посилання: {user['html_url']}")
print(f"🖼️ Аватар: {user['avatar_url']}")