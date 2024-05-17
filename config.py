import pydantic_settings
from dotenv import load_dotenv


class Config(pydantic_settings.BaseSettings):
    SELENOID_URL: str = 'selenoid.autotests.cloud'
    SELENOID_LOGIN: str
    SELENOID_PASSWORD: str

    BASE_URL: str
    USER_NAME: str
    USER_PASSWORD: str

    WINDOW_WIDTH: int = 1896
    WINDOW_HEIGHT: int = 1096


load_dotenv()
config = Config()
