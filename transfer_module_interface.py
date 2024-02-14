# transfer_module/transfer_module_interface.py

from abc import ABC, abstractmethod

class TransferModuleInterface(ABC):
    @abstractmethod
    def transfer(self, analysis_result):
        pass
