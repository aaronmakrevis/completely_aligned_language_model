from typing import Tuple


class Embeddings:
    @staticmethod
    def embedding(text: str) -> Tuple[int]:
        """
        Encode a string into a sequence of integers.

        :param text: The string to encode.
        :return: The sequence of integers.
        """
        return tuple(ord(c) for c in text)
