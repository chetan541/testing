from translate import Translator
from abc import ABC, abstractmethod
from typing import List

class ITransferModule(ABC):
    @abstractmethod
    def transfer(self, source_tokens: List[str]) -> List[str]:
        """
        Transfer function that maps source tokens to target tokens.

        Parameters:
        - source_tokens (List[str]): List of tokens from the source language.

        Returns:
        - List[str]: List of tokens in the target language.
        """
        pass

class WordMappingTransferModule(ITransferModule):
    def __init__(self, source_lang='en', target_lang='fr'):
        self.source_lang = source_lang
        self.target_lang = target_lang
        self.translator = Translator(to_lang=self.target_lang)

    def transfer(self, source_tokens):
        """
        A transfer function using the translate library for word-to-word mapping.

        Parameters:
        - source_tokens (List[str]): List of tokens from the source language.

        Returns:
        - List[str]: List of tokens in the target language using word mapping.
        """
        # Mapping each token using the translate library
        target_tokens = [self.translator.translate(token) for token in source_tokens]
        return target_tokens

# Example Usage:
transfer_module = WordMappingTransferModule()

source_text = "Hello world, good morning"
source_tokens = source_text.split()

# Using the Transfer Module
target_tokens = transfer_module.transfer(source_tokens)

# Printing the result
print("Source Tokens:", source_tokens)
print("Target Tokens:", target_tokens)
