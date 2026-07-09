from app import create_app
from app.services.auth_service import hash_password, verify_password

app = create_app()

with app.app_context():
    password = "Password123!"

    hashed = hash_password(password)

    print(f"Original Password : {password}")
    print(f"Password Hash     : {hashed}")
    print(f"Password Valid    : {verify_password(password, hashed)}")