"""create new user

Revision ID: 90e511ce8ac4
Revises: e778cb1d223e
Create Date: 2022-08-29 11:37:00.716192

"""
from alembic import op
from datetime import datetime
import uuid


# revision identifiers, used by Alembic.
revision = '90e511ce8ac4'
down_revision = 'e778cb1d223e'
branch_labels = None
depends_on = None


def upgrade():
    user_name_id = str(uuid.uuid4())
    op.execute(f"INSERT INTO string_ids (id) VALUES ('{user_name_id}')")
    op.execute(f"""
    INSERT INTO string_content (id, language, content, edited_at) 
    VALUES ('{user_name_id}', 'en', 'Sarah Rajab', '{datetime.now().isoformat()}')
    """)
    op.execute(f"""
    INSERT INTO users (id, name, role, email, hashed_password, edited_at) 
    VALUES ('{str(uuid.uuid4())}', '{user_name_id}', 'super_admin', 'sarah@shyp.studio', '$2b$12$KNBeouCsJHk8ykSdLcbFpuXJ6lzWAlF7RvhXDoZXbEINxbdvK.0bG', '{datetime.now().isoformat()}')
    """)


def downgrade():
    op.execute("DELETE FROM users WHERE email = 'sarah@shyp.studio';")

