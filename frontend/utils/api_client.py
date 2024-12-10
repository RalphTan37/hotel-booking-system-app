import requests
from typing import Optional, Dict, Any
from .config import API_BASE_URL, API_TIMEOUT

class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.timeout = API_TIMEOUT
        self.token: Optional[str] = None

    def set_token(self, token: str):
        self.token = token

    def get_headers(self) -> Dict[str, str]:
        headers = {'Content-Type': 'application/json'}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'
        return headers

    def get(self, endpoint: str) -> Dict[str, Any]:
        response = requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers(),
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers(),
            json=data,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict[str, Any]:
        response = requests.put(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers(),
            json=data,
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint: str) -> Dict[str, Any]:
        response = requests.delete(
            f"{self.base_url}{endpoint}",
            headers=self.get_headers(),
            timeout=self.timeout
        )
        response.raise_for_status()
        return response.json()

