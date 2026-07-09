from app.extensions import db
from app.models.role import Role


def seed_roles():
    roles = [
        {
            "role_name": "Administrator",
            "description": "System administrator with full access."
        },
        {
            "role_name": "Voter",
            "description": "Registered voter."
        },
        {
            "role_name": "Observer",
            "description": "Election observer."
        }
    ]

    for role in roles:
        existing_role = Role.query.filter_by(
            role_name=role["role_name"]
        ).first()

        if not existing_role:
            db.session.add(Role(**role))
            print(f"✔ Created role: {role['role_name']}")
        else:
            print(f"ℹ Role already exists: {role['role_name']}")

    db.session.commit()