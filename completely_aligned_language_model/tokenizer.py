from typing import Tuple


class Tokenizer:
    @staticmethod
    def tokenize(text: str) -> Tuple[str]:
        """
        Encode a string into a sequence of tokens.
        
        :param text: The string to encode.
        :return: The sequence of tokens.
        """
        return tuple(text.split(' '))
    
    @staticmethod
    def detokenize(tokens: Tuple[str]) -> str:
        """
        Decode a sequence of tokens into a string.
        
        :param tokens: The sequence of tokens to decode.
        :return: The decoded string.
        """
        return ' '.join(tokens)
