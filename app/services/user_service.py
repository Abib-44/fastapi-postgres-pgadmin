import uuid
from hashlib import sha256
from sqlalchemy.orm import Session
from app.models.user import User

def create_fake_user(db: Session) -> User:
    suffix = uuid.uuid4().hex[:8]

    user = User(
        username=f"test_user_{suffix}",
        email=f"test_{suffix}@example.com",
        password_hash=sha256(b"password").hexdigest(),
        first_name="Test",
        last_name="User",
        role="user",
        is_active=True,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
