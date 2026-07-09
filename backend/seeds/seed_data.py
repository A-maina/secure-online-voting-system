from app import create_app

from seeds.seed_roles import seed_roles
from seeds.seed_admin import seed_admin

app = create_app()

with app.app_context():
    print("\n===== DATABASE SEEDING =====\n")

    seed_roles()
    seed_admin()

    print("\n✔ Database seeding completed successfully.")