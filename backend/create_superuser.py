from app.database import SessionLocal
from app import models, auth_utils


def create_superuser():
    username = input("Username: ")
    password = input("Password: ")

    db = SessionLocal()

    existing = db.query(models.User).filter(models.User.username == username).first()
    if existing:
        print("User already exists. Making superadmin...")
        existing.role = "superadmin"
        db.commit()
        print("Done.")
        db.close()
        return

    hashed_password = auth_utils.hash_password(password)
    new_user = models.User(username=username, password_hash=hashed_password, role="superadmin")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    print("Superadmin created successfully, id=" + str(new_user.id))
    db.close()


if __name__ == "__main__":
    create_superuser()
