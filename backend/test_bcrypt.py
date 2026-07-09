from app import create_app
from app.services.auth_service import hash_password, verify_password

app = create_app()

with app.app_context():
    password = "Password123!"

    hashed = hash_password(password)

    print("Original :", password)
    print("Hash     :", hashed)
    print("Matches? :", verify_password(password, hashed))