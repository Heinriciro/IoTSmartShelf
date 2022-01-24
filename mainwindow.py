import sys, os
import Init_design
import Bluetooth_ui
import Writecard
import bluetooth
import socket
import time
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QMainWindow, QWidget, QMessageBox, QListView
import pymysql
import inspect

BLUE = 0  # 表示蓝牙列表相关的标志
GOODS = 1  # 表示货物列表相关的标志
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.settimeout(10)


class UiMain(QMainWindow):  # 定义主窗口类，继承自QMainWindow
    def __init__(self):
        super().__init__()
        self.main_ui = Init_design.Ui_MainWindow()  # 将Designer中设计的窗口类实例化后赋予成员
        self.main_ui.setupUi(self)  # 调用窗口类的setupUi方法以添加窗口内的组件


class UiBlueTooth(QWidget):  # 定义蓝牙子窗口类，继承自QWidget，因为其是一个Form
    def __init__(self):
        super().__init__()
        self.blue_ui = Bluetooth_ui.Ui_Form()  # 将Designer中设计的子窗口类实例化后赋予赋予成员
        self.blue_ui.setupUi(self)  # 调用子窗口类的setupUi方法以添加窗口内的组件


class UiWriteCard(QWidget):
    def __init__(self):
        super().__init__()
        self.write_ui = Writecard.Ui_Form()  # 将Designer中设计的子窗口类实例化后赋予赋予成员
        self.write_ui.setupUi(self)  # 调用子窗口类的setupUi方法以添加窗口内的组件


def search_devices():
    '''
    按键SEARCH_BT_DEVICE 被按下时运行
    搜寻附近蓝牙设备并显示其名称以及地址
    :return:
    '''
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("found %d devices" % len(nearby_devices))
    list2table(nearby_devices, BLUE)

    # item_addr = []                                      # 注释部分为另一种较为繁琐的数据输入方法
    # item_name = []

    # item_name.append(QStandardItem(name))
    # item_addr.append(QStandardItem(addr))
    # for row in range(len(item_name)):
    #     slm.setItem(row, 0, item_name[row])
    #     slm.setItem(row, 1, item_addr[row])
    # layout = QVBoxLayout()                                          # 垂直布局
    # listview = QListView()                                          # 实例化列表视图
    # slm.set(qlist)                                                  # 设置模型列表视图，加载数据列表


def conn_device():
    '''
    按键CONNECT被按下时运行
    获取列表中被选中的蓝牙设备的地址，并进行连接
    :return:
    '''
    bd_addr = get_selected_id()
    print("waiting for implement of the connection to the addr:{}".format(bd_addr))
    # 初步测试连接
    port = 1
    try:
    # if not sock.connected:
        sock.connect((bd_addr, port))
        sock.send("hello,Arduino!")
        QMessageBox.information(BlueTooth, "CONNECT SUCCESS", "You Have Already Connected to a device!",
                                QMessageBox.Ok)
        BlueTooth.close()
    # else:
    #     QMessageBox.information(BlueTooth, "CONNECTED",
    #                             "You Have Already Connected to a device!",
    #                             QMessageBox.Ok)
    except:
        raise_error()
        pass


def disconn_device():
    # try:
    sock.close()
    # sock.rfcomm_close()
    QMessageBox.information(BlueTooth, "DISCONNECTED",
                            "Have Disconnected Successfully",
                            QMessageBox.Ok)
    # except:
    #     raise_error()
    #     pass


def search_id():
    '''
    主界面搜索框旁的按键按下时运行
    在本地数据库中查询目标ID的存在情况，并询问是否要求Arduino进行查询
    :return:
    '''
    try:
        searchid = searchTxt.text()
        if searchid == "":
            print("You must input the ID first!!")
            return
        if not searchid.isalnum():
            print("The input data must be an ID, which only includes digits and letters")
            return
        db = conn_db()
        sql = "SELECT T.RN FROM (SELECT *, ROW_NUMBER() OVER(ORDER BY ID) RN FROM GOODSINFO) T WHERE T.ID='{}'".format(searchid)
        cursor = db.cursor()
        cursor.execute(sql)
        searchtuple = cursor.fetchone()
        rowcount = cursor.rowcount
    except:
        raise_error()
        pass
    else:
        if rowcount == 0:
            print("cant find the item in the local database!")
        else:
            index = searchtuple[0]
            index -= 1
            show_items()
            infoTable.selectRow(index)
            reply = QMessageBox.information(MainWindow, "Find {} records".format(rowcount),
                                            "Do you need the smart-shelf to check it again?",
                                            QMessageBox.Yes | QMessageBox.No)
            if reply != 65536:
                find_shelf(searchid)


def find_shelf(id):
    '''
    被调用于search_id()中
    向Arduino发送目标ID并执行查询命令id，最终询问是否要求Arduino执行闪烁命令以指示位置
    :param id: 目标id，需要是4个16进制数组成的字符串
    :return:
    '''
    # print("waiting to be implemented")
    try:
        status = cmd_handshake("SEARCH")
        time.sleep(1)
        if status is True:
            response = send_data_and_get_response(id)
            if response != "FOUND":
                QMessageBox.warning(MainWindow, "Not Found!", "There's no such an item on the shelf!!", QMessageBox.Ok)
                return
            reply = QMessageBox.information(MainWindow, "Found It!", "Do you want to turn on the reference?",
                                            QMessageBox.Yes | QMessageBox.No)
            if reply != 65536:
                shine_buzz()
    except:
        raise_error()
        pass


def shine_buzz():
    '''
    向Arduino发送闪烁命令以指示位置
    :return:
    '''
    try:
        status = cmd_handshake("SHINENBUZZ")
        if status is True:
            time.sleep(1)
            response = recv2string()
            if response == "SUCCESS":
                QMessageBox.information(MainWindow, "REFERENCE STARTED", "Find it by utilizing the Sound and The Light!",
                                        QMessageBox.Ok)
            else:
                QMessageBox.warning(MainWindow, "REFERENCE FAILED", "Cant Start a Reference", QMessageBox.Ok)
        else:
            QMessageBox.warning(MainWindow, "REFERENCE FAILED", "Cant Start a Reference", QMessageBox.Ok)

    except:
        raise_error()
        pass


def show_items():
    '''
    按键LIST被按下时执行
    显示本地数据库中的数据
    :return:
    '''
    try:
        db = conn_db()
        sql = "SELECT * FROM GOODSINFO;"
        cursor = db.cursor()
        cursor.execute(sql)
        datatuple = cursor.fetchall()
        list2table(datatuple, GOODS)
        # print(datatuple)
        db.close()
    except:
        raise_error()
        pass


def conn_db():
    '''
    连接本地数据库
    :return:
    '''
    try:
        db = pymysql.connect("localhost", "root", "forever1997!", "IOTSShelf")
        return db
    except:
        raise_error()
        pass


def record_item():
    '''
    RECORD按键按下时运行
    从Arduino中读取UID，DESCRIPTION,WEIGHT数据并存入本地数据库
    :return:
    '''
    # try:
    status = cmd_handshake("SIGNUP")
    if status is True:
        time.sleep(1)
        response = recv2string()
        if response != "OK":
            print("Read Card-uid process error:!")
            QMessageBox.warning(MainWindow, "COMMUNICATION FAILED", "Read Card-uid process error:!", QMessageBox.Ok)
            return
        uidstr = cmd2get_data_and_reply("CONTINUE", 1)
        if uidstr == "EXCEPT":
            QMessageBox.warning(MainWindow, "I/OERROR FAILED", "Communication has failed", QMessageBox.Ok)
            sock.send("FAILED")
            print("conmmuniction error:!")
            return
        time.sleep(1)

        response = recv2string()
        if response != "OK":
            QMessageBox.warning(MainWindow, "COMMUNICATION FAILED", "Read Card-name process error:!", QMessageBox.Ok)
            print("Read Card-name process error:!")
            return
        namestr = cmd2get_data_and_reply("CONTINUE")
        if namestr == "EXCEPT":
            QMessageBox.warning(MainWindow, "I/OERROR FAILED", "Communication has failed", QMessageBox.Ok)
            sock.send("FAILED")
            print("conmmuniction error:!")
            return
        time.sleep(1)

        response = recv2string()
        if response != "OK":
            QMessageBox.warning(MainWindow, "COMMUNICATION FAILED", "Read Card-weight process error:!", QMessageBox.Ok)
            print("Read Card-weight process error:!")
            return
        weightstr = cmd2get_data_and_reply("CONTINUE")
        if weightstr == "EXCEPT":
            QMessageBox.warning(MainWindow, "I/OERROR FAILED", "Communication has failed", QMessageBox.Ok)
            sock.send("FAILED")
            print("conmmuniction error:!")
            return
        time.sleep(1)
        response = recv2string()
        if response != "SUCCESS":
            QMessageBox.warning(MainWindow, "COMMUNICATION FAILED", "Receiving process error:!", QMessageBox.Ok)
            print("Receiving process error:!")
            return
        db = conn_db()
        sql = "SELECT * FROM GOODSINFO;"
        cursor = db.cursor()
        cursor.execute(sql)
        exist_uid = cursor.fetchall()
        flag = False
        for tup in exist_uid:
            if uidstr == tup[1]:
                flag = True
        if flag is True:
            sql = "UPDATE GOODSINFO SET DESCRIPTION = '{}', WEIGHT = '{}' WHERE ID = '{}';".format(namestr,
                                                                                                       weightstr,
                                                                                                       uidstr)
        else:
            sql = "INSERT INTO GOODSINFO(ID,DESCRIPTION,WEIGHT) VALUES('{}','{}','{}');".format(uidstr, namestr, weightstr)
        cursor.execute(sql)
        db.commit()
        db.close()

    else:
        QMessageBox.warning(MainWindow, "CMD SEND FAILED", "COMMAND WASNT SENT OUT", QMessageBox.Ok)
        print("Command Failed!")
        return
    # except IOError:
    #     raise_error()
    #     pass


def write_card():
    '''
    按键WRITECARD按下时运行
    输入标签DESDCRIPTION以及WEIGHT信息，将其发送向Arduino并命令其写入RFID标签
    :return:
    '''
    try:
        namestr = descText.text()
        weightstr = weightText .text()
        if len(namestr) > 16 or len(weightstr) > 16:
            QMessageBox.warning(MainWindow, "INPUT-TYPE ERROR!", "Format Input error:Please reinput", QMessageBox.Ok)
            print("Format Input error:Please reinput")
            return
        if len(namestr) <= 0 or len(weightstr) <= 0:
            QMessageBox.warning(MainWindow, "INPUT-TYPE ERROR!", "Input can not be NULL:Please reinput", QMessageBox.Ok)
            print("Pleas input something!")
            return
        status = cmd_handshake("WRITETAG")

        if status is True:
            response = send_data_and_get_response(namestr)
            if response == "EXCEPT":
                QMessageBox.warning(MainWindow, "I/O-ERROR!", "COMMUNICATION has failed",
                                    QMessageBox.Ok)
                sock.send("FAILED")
                print("Failed")
                return
            elif response != "OK":
                print("Name received error")
                sock.send("FAILED")
                return
            response = send_data_and_get_response(weightstr)
            if response == "EXCEPT":
                QMessageBox.warning(MainWindow, "I/O-ERROR!", "COMMUNICATION has failed",
                                    QMessageBox.Ok)
                sock.send("FAILED")
                print("Failed")
                return
            elif response != "OK":
                print("Weight received error")
                sock.send("FAILED")
                return
            response = send_data_and_get_response("CONTINUE")
            if response == "SUCCESS":
                QMessageBox.information(MainWindow, "WRITE-SUCCESS", "WRITE-CMD have been done!", QMessageBox.Ok)
                print("Write success!")
            elif response == "EXCEPT":
                QMessageBox.warning(MainWindow, "I/O-ERROR!", "COMMUNICATION has failed",
                                    QMessageBox.Ok)
                sock.send("FAILED")
                print("Failed")
                return
            else:
                QMessageBox.warning(MainWindow, "WRITE-ERROR!", "WRITE-CMD have failed",
                                    QMessageBox.Ok)
                print("Failed")
    except:
        raise_error()
        pass
    WriteCard.close()


def cmd_handshake(cmd):
    '''
    向Arduino发送命令，并获得回应的握手过程，握手后向Arduino发送继续工作指令
    :param cmd: 命令(String)
    :return:
    '''
    status = False
    try:
        sock.send(cmd)
        time.sleep(1)
        response = sock.recv(255)
        response = str(response, "utf-8")
        if response == "OK":
            sock.send("CONTINUE")
            status = True
            time.sleep(1)
        elif respons == "FAILED":
            return status
        else:
            sock.send("FAILED")
    except socket.timeout:
        print("connection timed out")
        QMessageBox.warning(MainWindow, "TIME-OUT!", "Socket Times out!",
                            QMessageBox.Ok)
        pass
    except socket.error as error:
        print(error)
        QMessageBox.warning(MainWindow, "I/OERROR", "I/OError Occured!!",
                            QMessageBox.Ok)
    return status


def recv2string():
    '''
    将接收到的字节数据转换为字符串
    :return:
    '''
    data = sock.recv(255)
    data = str(data, "utf-8")
    return data


def recv_and_reply():
    '''
    接受命令/数据后回复接收状态
    :return:
    '''
    try:
        data = recv2string()
        sock.send("OK")
        return data
    except socket.timeout as error:
        print("connection timed out error:{}".format(error))
        sock.send("FAILED")
        pass


def send_data_and_get_response(data):
    '''
    发送数据后收取Arduino的接收状态
    :param data:
    :return:
    '''
    response = "EXCEPT"
    try:
        sock.send(data)
        time.sleep(1)
        response = recv2string()
    except:
        raise_error()
        pass
    return response


def cmd2get_data_and_reply(cmd, flag=0):
    '''
    发送命令以获取数据，并回复接收状态
    :param cmd: 命令（String）
    :param flag: 用于辨别是否要接收UID数据，以检验数据类型是否正确
    :return:
    '''
    response = "EXCEPT"
    try:
        sock.send(cmd)
        time.sleep(1)
        response = recv2string()
        if flag == 1:
            if not response.isalnum():
                response = "EXCEPT"
    except socket.error as error:
        print("I/OError occured!:{}".format(error))
        pass
    else:
        sock.send("OK")
    return response


def get_selected_id():
    '''
    获取TableView中选中行数据的UID
    :return: 选中数据的UID
    '''
    # blueList.selectRow(blueList.currentIndex().row())
    selected_row = blueList.currentIndex().row()
    id_index = blueList.model().index(selected_row, 1)
    selected_id = blueList.model().data(id_index)
    print("the selected id is {}".format(selected_id))
    return selected_id


def list2table(datatuple, flag):
    '''
    使用数据元组datatuple中的数据构建TableView数据模型，并在其中显示
    :param datatuple: 数据元组
    :param flag: 用于判别是蓝牙数据还是标签数据
    :return:
    '''
    slm = QStandardItemModel()  # 实例化列表模型，添加数据
    if flag == BLUE:
        slm.setHorizontalHeaderLabels(['Name', 'BD_address'])
        for addr, name in datatuple:
            print("{}---{}".format(addr, name))
            slm.appendRow([center_item(name), center_item(addr)])
        blueList.setModel(slm)  # 设置列表视图的模型
        blueList.setEditTriggers(QListView.NoEditTriggers)  # 设置不可编辑
        blueList.verticalHeader().hide()                    # 隐藏行号
        blueList.horizontalHeader().setStretchLastSection(True)  # 最后一列决定充满剩下的界面
        blueList.doubleClicked.connect(conn_device)  # 双击触发自定义的槽函数
    elif flag == GOODS:
        slm.setHorizontalHeaderLabels(['No', 'ID', 'description', 'weight'])
        for no, uid, description, weight in datatuple:
            print("{}--{}--{}--{}".format(no, uid, description, weight))

            slm.appendRow([center_item(str(no)), center_item(uid), center_item(description),
                           center_item(str(weight))])
            # print(QStandardItem(str(no)).textAlignment())
        infoTable.setModel(slm)  # 设置列表视图的模型
        infoTable.setEditTriggers(QListView.NoEditTriggers)  # 设置不可编辑
        infoTable.verticalHeader().hide()                    # 隐藏行号
        infoTable.horizontalHeader().setStretchLastSection(True)  # 最后一列决定充满剩下的界面
        # infoTable.doubleClicked.connect(conn_device)  # 双击触发自定义的槽函数


def center_item(datastr):
    '''
    居中表格数据
    :param datastr:
    :return:
    '''
    item = QStandardItem(datastr)
    item.setTextAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
    return item


def is_zh(istr):
    for c in istr:
        if '\u4e00' <= c <= '\u9fa5':
            return True
    return False


def raise_error():
    QMessageBox.warning(MainWindow, "Error Occured!",
                        "Something goes wrong in the function: {}\n Please Try Again!".format(inspect.stack()[1][3]),
                        QMessageBox.Ok)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = UiMain()  # 构造Ui_Main实例
    BlueTooth = UiBlueTooth()
    WriteCard = UiWriteCard()

    infoTable = MainWindow.main_ui.infoTable
    writeBtn = MainWindow.main_ui.writeBtn
    writeBtn.clicked.connect(WriteCard.show)
    blueBtn = MainWindow.main_ui.blueToothBtn
    blueBtn.clicked.connect(BlueTooth.show)
    dbConnBtn = MainWindow.main_ui.databaseConnBtn
    dbConnBtn.clicked.connect(show_items)
    searchTxt = MainWindow.main_ui.searchTxt
    searchBtn = MainWindow.main_ui.searchBtn
    searchBtn.clicked.connect(search_id)

    scanBtn = BlueTooth.blue_ui.scanBtn
    scanBtn.clicked.connect(search_devices)

    blueList = BlueTooth.blue_ui.blueList

    connBtn = BlueTooth.blue_ui.connBtn
    connBtn.clicked.connect(conn_device)

    disconnBtn = BlueTooth.blue_ui.disconnBtn
    disconnBtn.clicked.connect(disconn_device)

    recordBtn = MainWindow.main_ui.signupBtn
    recordBtn.clicked.connect(record_item)

    descText = WriteCard.write_ui.descTxt
    weightText = WriteCard.write_ui.weightTxt
    submitBtn = WriteCard.write_ui.submitBtn
    submitBtn.clicked.connect(write_card)

    MainWindow.show()

    sys.exit(app.exec_())
