import sys
from PyQt5.QtWidgets import (
    QApplication
)

from presentation.SuinoForm import SuinoForm

def main():
    app = QApplication(sys.argv)
    form = SuinoForm()
    form.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
