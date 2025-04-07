from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Dict, Any

# 出力データの型変数
T = TypeVar('T')

class InputData(ABC, Generic[T]):
    """入力データの基本インターフェース"""
    pass

class OutputData(ABC):
    """出力データの基本インターフェース"""
    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """辞書形式に変換するメソッド"""
        pass 