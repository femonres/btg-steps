from abc import ABC, abstractmethod


class IAuthenticator(ABC):
    @abstractmethod
    def authenticate(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def get_token(self) -> str:
        pass

    @abstractmethod
    def clear_token(self) -> None:
        pass