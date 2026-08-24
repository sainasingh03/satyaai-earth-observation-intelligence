import os

from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "SATYAAI"
    APP_VERSION = "1.0.0"

    NVIDIA_API_KEY = os.getenv("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"
)

    NVIDIA_BASE_URL = os.getenv(
        "NVIDIA_BASE_URL",
        "https://integrate.api.nvidia.com/v1",
    )

    NVIDIA_MODEL = os.getenv(
        "NVIDIA_MODEL",
        "nvidia/nemotron-3.5-lightning-30b-a3b",
    )


settings = Settings()