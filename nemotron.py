from openai import OpenAI

from app.core.config import settings


class NemotronService:

    def __init__(self):

        if not settings.NVIDIA_API_KEY:
            raise RuntimeError(
                "NVIDIA_API_KEY is missing."
            )

        self.client = OpenAI(
            base_url=settings.NVIDIA_BASE_URL,
            api_key=settings.NVIDIA_API_KEY,
        )

        self.model = settings.NVIDIA_MODEL

    def complete(
        self,
        messages: list[dict],
        temperature: float = 0.2,
        max_tokens: int = 3000,
    ) -> str:

        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            top_p=0.95,
            max_tokens=max_tokens,
        )

        return (
            response.choices[0]
            .message.content
            or ""
        )