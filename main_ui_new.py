# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1013, 777)
        Form.setStyleSheet("#info_frame{\n"
"    background-color: #fff;\n"
"    border:none;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"#info_frame QLable,\n"
"#info_frame QLineEdit,\n"
"#info_frame QComboBox,\n"
"#function_frame QPushButton,\n"
"QHeaderView::section {\n"
"    font-family: Segoe Ul Semibold;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"#info_frame QLineEdite,\n"
"#info_frame QComboBox {\n"
"    padding: 4px 5px;\n"
"    border: 1px solid #838383;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"#info_frame QLineEdite:focus,\n"
"#info_frame QComboBox:focus {\n"
"    border-color: #0055ff;\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"    background: transparent;\n"
"    borde: none;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
"    image: url(:/icons/expand_more.svg);\n"
"}\n"
"\n"
"#result_frame{\n"
"    border-radius: 5px;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"QTableWidget{\n"
"    border-radius: 3px;\n"
"    border: 1px solid #f0f0f0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    text-align: left;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"QTableWidget::Item{\n"
"    border-bottom: 1px solid #d0c6ff;\n"
"    color: #000;\n"
"    padding-left: 3px;\n"
"}\n"
"\n"
"#function_frame QPushButton{\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"    background-color: #84e8f7;\n"
"}\n"
"\n"
"#function_frame #delete_btn{\n"
"    background-color:#ff8183;\n"
"}\n"
"\n"
"#function_frame QPushButton:hover{\n"
"    border-color: #4c96f7;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"#function_frame #delete_btn:hover{\n"
"    border-color: #dc0004;\n"
"}\n"
"\n"
"#gridLayout_2 QPushButton{\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"    background-color: #84e8f7;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.gridLayout_5 = QtWidgets.QGridLayout(Form)
        self.gridLayout_5.setContentsMargins(20, 10, 20, 20)
        self.gridLayout_5.setHorizontalSpacing(6)
        self.gridLayout_5.setVerticalSpacing(15)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.titre_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.titre_label.setFont(font)
        self.titre_label.setAlignment(QtCore.Qt.AlignCenter)
        self.titre_label.setObjectName("titre_label")
        self.horizontalLayout_2.addWidget(self.titre_label)
        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)
        self.info_frame = QtWidgets.QFrame(Form)
        self.info_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.info_frame.setObjectName("info_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.info_frame)
        self.gridLayout_3.setContentsMargins(30, 20, 30, 20)
        self.gridLayout_3.setHorizontalSpacing(20)
        self.gridLayout_3.setVerticalSpacing(10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.info_frame)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.info_frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.info_frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setHorizontalSpacing(10)
        self.gridLayout_2.setVerticalSpacing(15)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(self.info_frame)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.info_frame)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_2.addWidget(self.lineEdit_4, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_2.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.info_frame)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.info_frame)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_2.addWidget(self.lineEdit_5, 1, 1, 1, 1)
        self.image_btn = QtWidgets.QPushButton(self.info_frame)
        self.image_btn.setStyleSheet("QPushButton{\n"
"    font-size: 14px;\n"
"    padding: 5px 10px;\n"
"    border: 2px solid #f0f0f0;\n"
"    border-radius: 5px;\n"
"    background-color: #84e8f7;\n"
"}\n"
"QPushButton:hover{\n"
"    border-color: #4c96f7;\n"
"    font-size: 15px;\n"
"}")
        self.image_btn.setObjectName("image_btn")
        self.gridLayout_2.addWidget(self.image_btn, 3, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.info_frame)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        self.gridLayout_5.addWidget(self.info_frame, 1, 0, 1, 1)
        self.function_frame = QtWidgets.QFrame(Form)
        self.function_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.function_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.function_frame.setObjectName("function_frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.function_frame)
        self.horizontalLayout.setContentsMargins(30, 10, 30, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtWidgets.QPushButton(self.function_frame)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\icons/add.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_btn.setIcon(icon)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QtWidgets.QPushButton(self.function_frame)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\icons/update.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_btn.setIcon(icon1)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.select_btn = QtWidgets.QPushButton(self.function_frame)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\icons/select.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.select_btn.setIcon(icon2)
        self.select_btn.setObjectName("select_btn")
        self.horizontalLayout.addWidget(self.select_btn)
        self.search_btn = QtWidgets.QPushButton(self.function_frame)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(".\\icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon3)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.clear_btn = QtWidgets.QPushButton(self.function_frame)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(".\\icons/clear.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_btn.setIcon(icon4)
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.delete_btn = QtWidgets.QPushButton(self.function_frame)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(".\\icons/delete.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_btn.setIcon(icon5)
        self.delete_btn.setObjectName("delete_btn")
        self.horizontalLayout.addWidget(self.delete_btn)
        self.gridLayout_5.addWidget(self.function_frame, 2, 0, 1, 1)
        self.result_frame = QtWidgets.QFrame(Form)
        self.result_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.result_frame.setObjectName("result_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.result_frame)
        self.gridLayout_4.setContentsMargins(9, 9, 9, 9)
        self.gridLayout_4.setSpacing(6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.tableWidget = QtWidgets.QTableWidget(self.result_frame)
        self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.gridLayout_5.addWidget(self.result_frame, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.titre_label.setText(_translate("Form", "Students Information"))
        self.label_4.setText(_translate("Form", "Last Name"))
        self.label_2.setText(_translate("Form", "Student ID"))
        self.label_3.setText(_translate("Form", "First Name"))
        self.label_7.setText(_translate("Form", "Email Address"))
        self.label_6.setText(_translate("Form", "Groupe"))
        self.label_5.setText(_translate("Form", "Filiere"))
        self.image_btn.setText(_translate("Form", "Image"))
        self.label.setText(_translate("Form", "Image"))
        self.add_btn.setText(_translate("Form", "Add"))
        self.update_btn.setText(_translate("Form", "Update"))
        self.select_btn.setText(_translate("Form", "Select"))
        self.search_btn.setText(_translate("Form", "Search"))
        self.clear_btn.setText(_translate("Form", "Clear"))
        self.delete_btn.setText(_translate("Form", "Delete"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Student ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Frist Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Filiere"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Groupe"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Email Address"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Date et Heure d\'entree"))
