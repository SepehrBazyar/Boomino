from passlib.context import CryptContext
from .configs import settings

pwd_context = CryptContext(schemes=['argon2', 'pbkdf2_sha256'], deprecated="auto")

def get_password_hash(password: str) -> str:
    """
    Hashing the Input Password with Argon2 SHA256 Algorithm
    """

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str = settings.ADMIN_PASSWORD) -> bool:
    """
    Check Validate & Verify Password with Hash Value of Password
    """

    return pwd_context.verify(plain_password, get_password_hash(hashed_password))
