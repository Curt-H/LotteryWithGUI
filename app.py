import csv
import random
import sys
import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QTimer
from model import Player
from utils import log


class Game(QWidget):
    def __init__(self):
        super().__init__()
        self.counter = 0

        self.load_data()
        self.init_ui()

    def init_ui(self):
        self.resize(900, 600)
        self.center()
        self.setWindowTitle('抽奖程序')
        self.setWindowIcon(QIcon('web.png'))

        self.init_widgets()
        self.init_grid()
        self.init_style()

        self.bind_events()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_widgets(self):
        self.start_button = QPushButton('开始', self)
        self.font_syle(self.start_button)

        self.stop_button = QPushButton('清零', self)
        self.font_syle(self.stop_button)

        self.save_button = QPushButton('保存', self)
        self.font_syle(self.save_button)

        self.reload_button = QPushButton('重载数据', self)
        self.font_syle(self.reload_button)

        self.label_count = QLabel(f'已选出{self.counter}位', self)
        self.label_style(self.label_count)

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
        for label in self.labels:
            for l in label:
                self.label_style(l)

        self.mtext_result = QTextEdit(self)
        self.font_syle(self.mtext_result, font_size=16)
        self.mtext_result.setReadOnly(True)

    def init_grid(self):
        grid = QGridLayout()
        self.setLayout(grid)

        for x in range(len(self.labels)):
            for y in range(len(self.labels[x])):
                grid.addWidget(self.labels[x][y], x, y, 1, y + 1)

        grid.addWidget(self.start_button, 3, 0, 1, 1)
        grid.addWidget(self.stop_button, 3, 1, 1, 1)
        grid.addWidget(self.save_button, 3, 2, 1, 1)
        grid.addWidget(self.reload_button, 3, 6, 1, 1)

        grid.addWidget(self.mtext_result, 0, 3, 3, 4)
        grid.addWidget(self.label_count, 3, 3, 1, 3)

    def init_style(self):
        self.setStyleSheet('''
                    QWidget{
                        background-color:rgb(61, 79, 93);
                        border-radius:10px;
                        }
                    QPushButton{
                        color:white;
                        background-color:rgb(61, 79, 93);
                        border:1px solid white;
                        }
                    QPushButton:hover{
                        background-color:#08c;
                        }
                    QPushButton{
                        }
                    QPushButton{
                        border-radius:10px
                        }
                    QPushButton{
                        padding:2px 4px
                        }
                    QTextEdit{
                        border: 1px solid;
                        border-radius:10px;
                        background-color:white;
                        }
                    QLabel{
                        color:white;
                        }
                    ''')

    def bind_events(self):
        self.start_button.clicked.connect(self.on_click)
        self.stop_button.clicked.connect(self.reset)
        self.save_button.clicked.connect(self.save_result)
        self.reload_button.clicked.connect(self.reload)

    def load_data(self):
        with open('namelist.csv', 'r', encoding='utf-8-sig') as f:
            lines = csv.reader(f)
            self.namelist = []
            for line in lines:
                # log(line)
                # log(len(line))
                if not (len(line) > 3 and line[-1] != ''):
                    self.namelist.append(Player(line[0], line[1], line[2]))
            # print(self.namelist)

    def on_click(self):
        if self.start_button.text() == '开始':
            self.start_button.setText('抽取')
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.setname)
            self.timer.start(10)
            return 0

        if len(self.namelist) == 0:
            return 0

        if self.start_button.text() == '抽取' and len(self.namelist) > 0:
            self.counter += 1

            text = self.mtext_result.toPlainText()
            infor_labels = [self.label_id.text(), self.label_name.text(), self.label_depart.text()]
            text = '\t'.join(infor_labels) + '\n' + text
            winner = infor_labels[0]
            log(text, winner)
            self.mtext_result.setPlainText(text)

            self.label_count.setText(f'已选出{self.counter}位')
            for p in self.namelist:
                if p.id == winner:
                    self.namelist.pop(self.namelist.index(p))

    def save_result(self):
        fn = str(time.time()) + '.csv'
        with open(fn, 'w', encoding='utf-8-sig') as f:
            result = self.mtext_result.toPlainText()
            result = result.replace('\t', ',')
            f.write(result)
        log('Successfully import')

    def reset(self):
        self.set_zero()
        self.timer.stop()

    def set_zero(self):
        self.counter = 0
        self.start_button.setText('开始')
        self.label_count.setText(f'已选出{self.counter}位')
        self.mtext_result.setText('')

        self.label_id.setText('')
        self.label_name.setText('')
        self.label_depart.setText('')

    def setname(self):
        if len(self.namelist) == 0:
            self.label_id.setText(f'结束')
            self.label_name.setText(f'结束')
            self.label_depart.setText(f'结束')

            self.timer.stop()
            return 0
        p = self.namelist[random.randint(0, len(self.namelist) - 1)]
        self.label_id.setText(f'{p.id}')
        self.label_name.setText(f'{p.name}')
        self.label_depart.setText(f'{p.depart}')

    def reload(self):
        msg = QMessageBox.question(self, "警告", "重载数据后, 抽奖必须重新开始, 确认重载?", QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)  # 这里是固定格式，yes/no不能动
        if msg == QMessageBox.Yes:
            self.load_data()
            self.set_zero()

    @staticmethod
    def label_style(label):
        label.setAlignment(Qt.AlignCenter)
        label.setFont(QFont("微软雅黑", 20, QFont.Bold))

    @staticmethod
    def font_syle(widget, font_size=20, font='微软雅黑', bold=True):
        w = widget
        if bold:
            w.setFont((QFont(font, font_size, QFont.Bold)))
        else:
            w.setFont((QFont(font, font_size)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Game()
    sys.exit(app.exec_())
