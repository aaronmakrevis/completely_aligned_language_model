import random
from pathlib import Path
from typing import List, Sequence, Tuple

from .tokenizer import Tokenizer
from .utils.checkpoints import load_checkpoint


def find_tokens(
        large_sequence: Sequence,
        sequence: Sequence
) -> int:
    """
    Find a sequence of tokens in a larger sequence of tokens.
    
    :param large_sequence: The sequence of tokens to search in.
    :param sequence: The sequence of tokens to search for.
    :return: The index of the sequence of tokens in the larger sequence of tokens.
    """
    for i in range(len(large_sequence) - len(sequence) + 1):
        if large_sequence[i:i + len(sequence)] == sequence:
            return i
    return -1


def shorten_sequence(
        large_sequence: Sequence,
        sequences: Sequence[Sequence]
) -> Tuple:
    """
    Shorten a sequence of tokens.
    
    :param large_sequence: The sequence of tokens to shorten.
    :param sequences: The sequences of tokens to shorten the sequence of tokens to.
    :return: The shortened sequence of tokens.
    """
    indices = [find_tokens(large_sequence, sequence) for sequence in sequences]
    index = min(index for index in indices if index != -1)
    return large_sequence[:index]


class AMCalm:
    def __init__(
            self,
            checkpoint: Path = Path(__file__).parent / "checkpoints" / "checkpoint_1.txt"
    ):
        self.tokenizer = Tokenizer()
        self.weights = self.load(checkpoint)
    
    def load(self, checkpoint: Path) -> Tuple[Tuple[str]]:
        """
        Load the weights from a checkpoint.
        
        :param checkpoint: The checkpoint to load the weights from.
        :return: The weights.
        """
        return tuple(self.tokenizer.tokenize(line) for line in load_checkpoint(checkpoint))
    
    def generate(
            self,
            prompt: str,
            max_tokens: int = 256,
            echo: bool = False,
            temperature: float = 0.6,
            stop_tokens: List[str] = None,
            seed: int = None,
    ) -> str:
        """
        Generate a completion for the given prompt.
        
        :param prompt: The prompt to generate a completion for.
        :param max_tokens: The maximum number of tokens to generate.
        :param echo: Whether to echo the prompt in the completion.
        :param temperature: The temperature to use when generating the completion.
        :param stop_tokens: A list of tokens to stop generation at.
        :param seed: The seed to use for generating the completion.
        :return: The generated completion.
        """
        tokenized_prompt: Tuple[str] = self.tokenizer.tokenize(prompt)
        weights: Tuple[Tuple[str]] = self.weights
        
        random.seed(seed)
        weights = random.sample(weights, len(weights))
        max_weights = max(int(len(weights) * temperature), 1)
        phrases = weights[:max_weights]
        
        completion: Tuple[str] = random.choice(phrases)
        completion = completion[:max_tokens]
        
        if stop_tokens:
            stop_tokens = [self.tokenizer.tokenize(token) for token in stop_tokens]
            completion = shorten_sequence(completion, stop_tokens)
        
        if echo:
            completion: List[str] = list(tokenized_prompt) + list(completion)
        
        return self.tokenizer.detokenize(completion)
