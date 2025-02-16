import os
from typing import Optional
import dotenv

dotenv.load_dotenv()

class Config:
    _instance: Optional["Config"] = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not hasattr(self, "initialized"):
            self.initialized = True  # Prevent re-initialization

            self.RESET_PASS_JWT_SECRET: str = self.get_env_var("RESET_PASS_JWT_SECRET")
            self.VERIFY_MAIL_JWT_SECRET: str = self.get_env_var(
                "VERIFY_MAIL_JWT_SECRET"
            )
            self.LOGIN_JWT_SECRET: str = self.get_env_var(
                "LOGIN_JWT_SECRET"
            )
            self.RESET_PASS_JWT_LIFE: int = self.get_int_env_var("RESET_PASS_JWT_LIFE")
            self.VERIFY_MAIL_JWT_LIFE: int = self.get_int_env_var(
                "VERIFY_MAIL_JWT_LIFE"
            )
            self.LOGIN_JWT_LIFE: int = self.get_int_env_var(
                "LOGIN_JWT_LIFE"
            )
            self.RESET_PASS_JWT_AUDIENCE: str = self.get_env_var(
                "RESET_PASS_JWT_AUDIENCE"
            )
            self.VERIFY_MAIL_JWT_AUDIENCE: str = self.get_env_var(
                "VERIFY_MAIL_JWT_AUDIENCE"
            )
            self.LOGIN_JWT_AUDIENCE: str = self.get_env_var(
                "LOGIN_JWT_AUDIENCE"
            )

            self.DB_URL: str = self.get_env_var("DB_URL")

            self.GOOGLE_CLIENT_ID: str = self.get_env_var("GOOGLE_CLIENT_ID")

            self.MAIL_USERNAME: str = self.get_env_var("MAIL_USERNAME")
            self.MAIL_SECRET: str = self.get_env_var("MAIL_SECRET")
            self.MAIL_PORT: int = self.get_int_env_var("MAIL_PORT")
            self.MAIL_SERVER: str = self.get_env_var("MAIL_SERVER")
            
            self.BASE_URL: str = os.getenv("BASE_URL", "")

            self.validate()

    def get_env_var(self, key: str) -> str:
        """get environment variable and raise error if not found."""
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is missing.")
        return value

    def get_int_env_var(self, key: str) -> int:
        """get and convert environment variable to int."""
        value = os.getenv(key)
        if value is None:
            raise ValueError(f"Environment variable '{key}' is missing.")
        try:
            return int(value)
        except ValueError:
            raise ValueError(f"Environment variable '{key}' must be an integer.")

    def get_float_env_var(self, key: str, default: float = 0.0) -> float:
        """get and convert environment variable to float."""
        value = os.getenv(key)
        if value is None:
            return default
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Environment variable '{key}' must be a float.")

    def validate(self):
        """Perform any additional validations if necessary."""

        pass
