import bluetooth
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel


def search_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))

    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))

    # 垂直布局
    layout = QVBoxLayout()
    # 实例化列表视图
    listview = QListView()

    # 实例化列表模型，添加数据
    slm = QStringListModel()
    qList = nearby_devices[name]

    # 设置模型列表视图，加载数据列表
    slm.setStringList(qList)

    # 设置列表视图的模型
    listview.setModel(slm)

    # 单击触发自定义的槽函数
    # listview.clicked.connect(self.clicked)

    # 设置窗口布局，加载控件
    layout.addWidget(listview)

    return layout

# def conn_arduino():


if __name__ == '__main__':
    search_devices()
