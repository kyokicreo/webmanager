from app.database import SessionLocal
from app import models, auth_utils


def create_superuser():
    username = input("Username: ")
    password = input("Password: ")

    db = SessionLocal()

    existing = db.query(models.User).filter(models.User.username == username).first()
    if existing:
        print(f"Пользователь {username} уже существует. Делаю его админом...")
        existing.is_admin = True
        db.commit()
        print("Готово, права администратора выданы.")
        db.close()
        return

    hashed_password = auth_utils.hash_password(password)
    new_user = models.User(username=username, password_hash=hashed_password, is_admin=True)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print(f"Суперпользователь {username} создан успешно, id={new_user.id}")
    db.close()


if __name__ == "__main__":
    create_superuser()