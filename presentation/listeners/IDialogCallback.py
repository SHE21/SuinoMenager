from abc import ABC, abstractmethod


class IDialogCallback(ABC):
    @abstractmethod
    def on_dialog_closed(self, result):
        """Método chamado quando o diálogo é fechado."""
        pass