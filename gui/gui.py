import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic , QtWidgets


class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        # self.combo()

    def init_ui(self):
        self.ui = uic.loadUi("./gui/untitled.ui")
        print(self.ui.__dict__)  # 查看ui文件中有哪些控件

        # layout = self.ui.verticalLayout
        self.label = self.ui.label
        # 提取要操作的控件
        self.cb = self.ui.comboBox  # 用户名输入框
        self.zhixing = self.ui.pushButton  # 登录按钮
        self.guanbi = self.ui.pushButton_2  # 忘记密码按钮
        self.tb = self.ui.textBrowser  # 文本显示区域

        # layout.addWidget(self.label)
        # layout.addWidget(self.combox)

        # self.setLayout(layout)
        # 绑定信号与槽函数
        # self.login_btn.clicked.connect(self.login)
        self.cb.addItem('2000~2020年')
        self.cb.addItem('2020~2021年')
        self.cb.addItem('2021~2022年')

        self.cb.currentIndexChanged.connect(self.indexchange)

    def indexchange(self,i) :
        s = self.cb.currentText()
        return s


# def printf(self,ipip):

#         self.tb.append(ipip)   #在指定的区域显示提示信息
#         self.cursor=self.tb.textCursor()
#         self.tb.moveCursor(self.cursor.End)  #光标移到最后，这样就会自动显示出来
        # QtWidgets.QApplication.processEvents()


    # def login(self):
    #     """登录按钮的槽函数"""
    #     user_name = self.user_name_qwidget.text()
    #     password = self.password_qwidget.text()
    #     if user_name == "admin" and password == "123456":
    #         self.textBrowser.setText("欢迎%s" % user_name)
    #         self.textBrowser.repaint()
    #     else:
    #         self.textBrowser.setText("用户名或密码错误....请重试")
    #         self.textBrowser.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    # 展示窗口
    w.ui.show()

    app.exec()