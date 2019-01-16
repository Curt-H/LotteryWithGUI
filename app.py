import sys

from PyQt5.QtGui import QIcon, QIntValidator
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel,
                             QGridLayout, QLineEdit)


class Selection(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(400, 300, 800, 600)  # set window position, then size
        self.setWindowTitle('抽奖')
        self.setWindowIcon(QIcon('web.png'))

        grid = QGridLayout()
        grid.setSpacing(5)
        self.setLayout(grid)

        id_label = QLabel('工号', self)
        id_content_label = QLabel('x', self)
        name_label = QLabel('姓名', self)
        name_content_label = QLabel('x', self)
        depart_label = QLabel('部门', self)
        depart_content_label = QLabel('x', self)
        num_label = QLabel('中奖人数', self)

        num_edit = QLineEdit()

        start_button = QPushButton('启动', self)
        start_button.clicked.connect(self.button_clicked())

        grid.addWidget(id_label, 1, 1)
        grid.addWidget(id_content_label, 1, 2)
        grid.addWidget(name_label, 2, 1)
        grid.addWidget(name_content_label, 2, 2)
        grid.addWidget(depart_label, 3, 1)
        grid.addWidget(depart_content_label, 3, 2)
        grid.addWidget(num_label, 4, 1)
        grid.addWidget(num_edit, 4, 2)
        grid.addWidget(start_button, 5, 1, 1, 2)

        self.show()

    def button_clicked(self):
        sender = self.sender()
        print('clicked')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Selection()
    sys.exit(app.exec_())
