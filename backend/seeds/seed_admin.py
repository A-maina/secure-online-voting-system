from app.extensions import db
from app.models.user import User
from app.models.role import Role
from app.services.auth_service import hash_password


def seed_admin():
    admin = User.query.filter_by(
        email="admin@securevote.com"
    ).first()

    if admin:
        print("ℹ Administrator already exists.")
        return

    admin_role = Role.query.filter_by(
        role_name="Administrator"
    ).first()

    if not admin_role:
        raise Exception(
            "Administrator role not found. Seed roles first."
        )

    admin = User(
        registration_number="ADMIN001",
        first_name="System",
        last_name="Administrator",
        email="admin@securevote.com",
        password_hash=hash_password("Admin@123"),
        role_id=admin_role.role_id,
        is_active=True,
        has_voted=False
    )

    db.session.add(admin)
    db.session.commit()

    print("✔ Administrator account created.")