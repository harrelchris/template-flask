import bcrypt


def hash_password(password: bytes | str) -> bytes:
    if isinstance(password, str):
        password = bytes(password, encoding="utf-8")
    return bcrypt.hashpw(password, bcrypt.gensalt(rounds=15))


def validate_password(password: bytes | str, hashed: bytes) -> bool:
    if isinstance(password, str):
        password = bytes(password, encoding="utf-8")
    return bcrypt.checkpw(password, hashed)
