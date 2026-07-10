import requests

BASE_URL = "http://127.0.0.1:8000"


def register(username: str, password: str) -> bool:
    response = requests.post(
        f"{BASE_URL}/auth/register",
        json={"username": username, "password": password},
    )
    if response.status_code == 200:
        return True
    else:
        print(f"Ошибка регистрации: {response.json().get('detail', 'неизвестная ошибка')}")
        return False


def login(username: str, password: str) -> str:
    response = requests.post(
        f"{BASE_URL}/auth/login",
        data={"username": username, "password": password},
    )
    response.raise_for_status()
    return response.json()["access_token"]


def main():
    print("=== File Manager Client ===")
    print("1 - Войти")
    print("2 - Зарегистрироваться")
    choice = input("Выберите действие: ").strip()

    username = input("Логин: ")
    password = input("Пароль: ")

    if choice == "2":
        if not register(username, password):
            return
        print("Регистрация успешна!")

    try:
        token = login(username, password)
        print("Вход выполнен успешно!")
    except requests.exceptions.HTTPError:
        print("Неверный логин или пароль")
        return

    headers = {"Authorization": f"Bearer {token}"}

    print("Введите команду (CREATE <path>, DELETE <path>, LIST [path], HISTORY, EXIT)")

    while True:
        line = input("> ").strip()
        if not line:
            continue

        parts = line.split(maxsplit=1)
        command = parts[0].upper()
        path = parts[1] if len(parts) > 1 else ""

        if command == "EXIT":
            break

        elif command == "LIST":
            response = requests.get(f"{BASE_URL}/files/list", params={"path": path}, headers=headers)
            data = response.json()
            print(data["message"])
            for entry in data.get("data", []):
                print(f"  {entry}")

        elif command == "CREATE":
            response = requests.post(f"{BASE_URL}/files/create", json={"path": path}, headers=headers)
            data = response.json()
            print(data["message"])

        elif command == "DELETE":
            response = requests.post(f"{BASE_URL}/files/delete", json={"path": path}, headers=headers)
            data = response.json()
            print(data["message"])

        elif command == "HISTORY":
            response = requests.get(f"{BASE_URL}/history/", headers=headers)
            data = response.json()
            for entry in data:
                print(f"  {entry['timestamp']} | {entry['username']} | {entry['command']} | "
                      f"{entry['path']} | {'OK' if entry['success'] else 'FAILED'} | {entry['message']}")

        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    main()