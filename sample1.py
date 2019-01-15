import random
import copy
import sys
from PyQt5.QtWidgets import *


class Prize(QWidget):
    " 年终抽奖 "

    def __init__(self, filename):
        super(Prize, self).__init__()
        self.getMemberMsg(filename)
        self.initUI()

    def getMemberMsg(self, filename):
        '''获取员工信息'''
        # data=open(filename,'r').readlines() # 读取员工信息
        self.members = [range(100)]  # 去掉\n

    def initUI(self):
        '''UI界面'''
        self.setWindowTitle("年终抽奖")
        self.setFixedSize(300, 330)
        self.first_label = QLabel(self)
        self.first_label.setText('一等奖人数：')
        self.first_label.setGeometry(10, 10, 80, 30)
        self.first_num = QSpinBox(self)
        self.first_num.setGeometry(100, 10, 190, 30)
        self.second_label = QLabel(self)
        self.second_label.setText('二等奖人数：')
        self.second_label.setGeometry(10, 50, 80, 30)
        self.second_num = QSpinBox(self)
        self.second_num.setGeometry(100, 50, 190, 30)
        self.third_label = QLabel(self)
        self.third_label.setText('三等奖人数：')
        self.third_label.setGeometry(10, 90, 80, 30)
        self.third_num = QSpinBox(self)
        self.third_num.setGeometry(100, 90, 190, 30)
        self.btn = QPushButton(self)
        self.btn.setText("抽奖")
        self.btn.setGeometry(10, 130, 280, 30)
        self.btn.clicked.connect(self.lottery)
        self.show_msg = QTextEdit(self)
        self.show_msg.setReadOnly(True)
        self.show_msg.setGeometry(10, 170, 280, 150)

    def lottery(self):
        '''抽奖函数'''
        members = copy.deepcopy(self.members)
        first_member = []  # 一等奖
        second_member = []  # 二等奖
        third_member = []  # 三等奖
        for i in range(self.first_num.value()):  # 抽取一等奖
            f_tmp = random.choice(members)  # 随机抽取获奖员工
            members.remove(f_tmp)  # 去掉已获奖的员工
            first_member.append(f_tmp)  # 插入first_member列表
        for i in range(self.second_num.value()):  # 抽取二等奖
            s_tmp = random.choice(members)  # 随机抽取获奖员工
            members.remove(s_tmp)  # 去掉已获奖的员工
            second_member.append(s_tmp)  # 插入second_member列表
        for i in range(self.third_num.value()):  # 抽取三等奖
            t_tmp = random.choice(members)  # 随机抽取获奖员工
            members.remove(t_tmp)  # 去掉已获奖的员工
            third_member.append(t_tmp)  # 插入third_member列表
        msg = '一等奖名单：' + ','.join(first_member) + '\n'
        msg = msg + '二等奖名单：' + ','.join(second_member) + '\n'
        msg = msg + '三等奖名单：' + ','.join(third_member) + '\n'
        self.show_msg.setPlainText(msg)  # 显示获奖人员信息


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Prize('member.txt')
    ex.show()
sys.exit(app.exec_())
