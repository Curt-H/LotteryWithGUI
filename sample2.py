import random
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QDesktopWidget,
                             QLabel, QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.init_ui()
        self.num = list(range(10))

    def init_ui(self):
        self.resize(800, 600)
        self.center()
        self.setWindowTitle('抽奖程序')
        self.setWindowIcon(QIcon('web.png'))
        infor_hboxes = self.info_layout()

        self.start_button = QPushButton('开始', self)
        self.stop_button = QPushButton('清零', self)
        self.start_button.setFont(QFont("微软雅黑", 20))
        self.stop_button.setFont(QFont("微软雅黑", 20))

        self.start_button.clicked.connect(self.on_click)
        self.stop_button.clicked.connect(self.set_zero)

        hbox_operate = QHBoxLayout()
        hbox_operate.addWidget(self.start_button)
        hbox_operate.addWidget(self.stop_button)

        vbox_operate = QVBoxLayout()
        for b in infor_hboxes:
            print(b)
            vbox_operate.addLayout(b)
        vbox_operate.addLayout(hbox_operate)
        vbox_operate.addLayout(hbox_operate)

        self.label_result = QLabel('', self)
        self.label_count = QLabel(f'已选出{self.counter}位', self)
        self.label_style(self.label_result)
        self.label_style(self.label_count)

        vbox_result = QVBoxLayout()
        vbox_result.addWidget(self.label_result)
        vbox_result.addStretch(1)
        vbox_result.addWidget(self.label_count)

        vbox_main = QHBoxLayout()
        vbox_main.addLayout(vbox_operate)
        vbox_main.addLayout(vbox_result)

        self.setLayout(vbox_main)

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def info_layout(self):
        self.label_title_id = QLabel('工号', self)
        self.label_title_name = QLabel('姓名', self)
        self.label_title_depart = QLabel('部门', self)
        self.label_id = QLabel('工号', self)
        self.label_name = QLabel('姓名', self)
        self.label_depart = QLabel('部门', self)

        self.labels = [
            (self.label_title_id, self.label_id),
            (self.label_title_name, self.label_name),
            (self.label_title_depart, self.label_depart)
        ]

        hboxes = []
        for label in self.labels:
            for l in label:
                self.label_style(l)
            hbox = QHBoxLayout()
            # hbox.addStretch(1)
            hbox.addWidget(label[0])
            hbox.addWidget(label[1])
            hboxes.append(hbox)

        return hboxes

    @staticmethod
    def label_style(label):
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("微软雅黑", 20, QFont.Bold))

    def on_click(self):
        if self.start_button.text() == '开始':
            self.start_button.setText('抽取')
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.setname)
            self.timer.start(100)
        elif self.start_button.text() == '抽取':
            self.counter += 1
            text = self.label_result.text()
            text = '\n'.join([text, self.label_id.text()])
            self.label_result.setText(text)
            for i, j in enumerate(self.num):
                if str(j) == self.label_id.text():
                    self.num.pop(i)
            self.label_count.setText(f'已选出{self.counter}位')

    def set_zero(self):
        self.counter = 0
        self.start_button.setText('开始')
        self.label_count.setText(f'已选出{self.counter}位')

    def setname(self):
        num = self.num[random.randint(0, len(self.num) - 1)]
        self.label_id.setText(f'{num}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Game()
    sys.exit(app.exec_())
