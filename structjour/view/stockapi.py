# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\stockapi.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(390, 654)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\../images/ZSLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(41, 25, 311, 573))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.ibRealCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.ibRealCb.setObjectName("ibRealCb")
        self.verticalLayout_7.addWidget(self.ibRealCb)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_7.addWidget(self.label_14)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_7.addWidget(self.label_13)
        self.horizontalLayout_6.addLayout(self.verticalLayout_7)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ibRealPort = QtWidgets.QLineEdit(self.layoutWidget)
        self.ibRealPort.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ibRealPort.setObjectName("ibRealPort")
        self.horizontalLayout.addWidget(self.ibRealPort)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ibRealId = QtWidgets.QLineEdit(self.layoutWidget)
        self.ibRealId.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ibRealId.setObjectName("ibRealId")
        self.horizontalLayout_2.addWidget(self.ibRealId)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.ibPaperCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.ibPaperCb.setObjectName("ibPaperCb")
        self.horizontalLayout_5.addWidget(self.ibPaperCb)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ibPaperPort = QtWidgets.QLineEdit(self.layoutWidget)
        self.ibPaperPort.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ibPaperPort.setObjectName("ibPaperPort")
        self.horizontalLayout_3.addWidget(self.ibPaperPort)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.ibPaperId = QtWidgets.QLineEdit(self.layoutWidget)
        self.ibPaperId.setMaximumSize(QtCore.QSize(75, 16777215))
        self.ibPaperId.setObjectName("ibPaperId")
        self.horizontalLayout_4.addWidget(self.ibPaperId)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_9.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.bcCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.bcCb.setObjectName("bcCb")
        self.verticalLayout_3.addWidget(self.bcCb)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bcKey = QtWidgets.QLineEdit(self.layoutWidget)
        self.bcKey.setObjectName("bcKey")
        self.horizontalLayout_7.addWidget(self.bcKey)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.avCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.avCb.setObjectName("avCb")
        self.verticalLayout_4.addWidget(self.avCb)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.avKey = QtWidgets.QLineEdit(self.layoutWidget)
        self.avKey.setObjectName("avKey")
        self.horizontalLayout_8.addWidget(self.avKey)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.wtdCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.wtdCb.setObjectName("wtdCb")
        self.verticalLayout_8.addWidget(self.wtdCb)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.wtdKey = QtWidgets.QLineEdit(self.layoutWidget)
        self.wtdKey.setObjectName("wtdKey")
        self.horizontalLayout_9.addWidget(self.wtdKey)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_9.addWidget(self.label_11)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_5.addWidget(self.label_9)
        self.fhCb = QtWidgets.QCheckBox(self.layoutWidget)
        self.fhCb.setEnabled(True)
        self.fhCb.setObjectName("fhCb")
        self.verticalLayout_5.addWidget(self.fhCb)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.fhKey = QtWidgets.QLineEdit(self.layoutWidget)
        self.fhKey.setObjectName("fhKey")
        self.horizontalLayout_10.addWidget(self.fhKey)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.verticalLayout_5.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_6.addWidget(self.label_10)
        self.APIPref = QtWidgets.QLineEdit(self.layoutWidget)
        self.APIPref.setObjectName("APIPref")
        self.verticalLayout_6.addWidget(self.APIPref)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.okBtn = QtWidgets.QPushButton(self.layoutWidget)
        self.okBtn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.okBtn.setObjectName("okBtn")
        self.verticalLayout_9.addWidget(self.okBtn)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Stock API"))
        self.ibRealCb.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">In order to use automatic chart generation, structjour uses three possible data sources. </span></p><p><span style=\" font-size:9pt;\">If you have an IB account, you can enable IB. To use the IB data, you must download and install TWSAPI and the IB Gateway. Data is realtime and after hours and historical data is available excluding IBs regular maintenance hours.</span></p><p><span style=\" font-size:9pt;\">TWSAPI can be downloaded from </span><a href=\"https://interactivebrokers.github.io/\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://interactivebrokers.github.io/ </span></a></p><p><span style=\" font-size:9pt;\">IB Gateway can be downloaded </span><a href=\"https://www.interactivebrokers.com/en/index.php?f=16457\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://www.interactivebrokers.com/en/index.php?f=16457</span></a></p><p><span style=\" font-size:9pt;\">To use IB API. fill in the PORT and CLIENTID fields here. These are set in the IB Gateway application (Or in Trader Workstation if you prefer)</span></p></body></html>"))
        self.ibRealCb.setText(_translate("Dialog", "Interactive Brokers"))
        self.label_14.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://interactivebrokers.github.io/\"><span style=\" text-decoration: underline; color:#0000ff;\">IB TWSAPI (right click)</span></a></p></body></html>"))
        self.label_13.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.interactivebrokers.com/en/index.php?f=16457\"><span style=\" text-decoration: underline; color:#0000ff;\">IB Gatewayi (right click)</span></a></p></body></html>"))
        self.label.setText(_translate("Dialog", "Port"))
        self.label_2.setText(_translate("Dialog", "Client ID"))
        self.ibPaperCb.setText(_translate("Dialog", "IB Paper account  "))
        self.label_3.setText(_translate("Dialog", "Port"))
        self.label_4.setText(_translate("Dialog", "Client Id"))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.barchart.com/ondemand/free-market-data-api\"><span style=\" text-decoration: underline; color:#0000ff;\">Barchar free api (right click)</span></a></p></body></html>"))
        self.bcCb.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">To use Barchart get a free key from </span><a href=\"https://www.barchart.com/ondemand/free-market-data-api\"><span style=\" font-size:9pt; font-weight:600; text-decoration: underline; color:#0000ff;\">https://www.barchart.com/ondemand/free-market-data-api</span></a><span style=\" font-size:9pt;\"> Write the api key in box. The licencse will allow 150 getHistory queries per day. The previous 30 days of data are available.</span></p><p><span style=\" font-size:9pt;\">Barchart data for the current day is available by 16:45.</span></p><p><span style=\" font-size:9pt;\">Additionally yesterdays data after 12PM is unavailable during market hours. It also becames available by 16:45</span></p></body></html>"))
        self.bcCb.setText(_translate("Dialog", "Barchart"))
        self.label_6.setText(_translate("Dialog", "API Key"))
        self.label_7.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.alphavantage.co/support/#api-key\"><span style=\" text-decoration: underline; color:#0000ff;\">Alph vantage free api (right click)</span></a></p></body></html>"))
        self.avCb.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">To use Alphavantage APIs get a free API key from </span><a href=\"https://www.alphavantage.co/support/#api-key\"><span style=\" font-size:9pt; text-decoration: underline; color:#0000ff;\">https://www.alphavantage.co/support/#api-key </span></a><span style=\" font-size:9pt;\">   The data is realtime Historical data is available for the last 7 days. Data limts are 500 calls per day and 5 per minute.</span></p></body></html>"))
        self.avCb.setText(_translate("Dialog", "Alphavantage"))
        self.label_8.setText(_translate("Dialog", "API Key"))
        self.label_12.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://www.worldtradingdata.com/register\"><span style=\" text-decoration: underline; color:#0000ff;\">World Trade Data free api (right click)</span></a></p></body></html>"))
        self.wtdCb.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">To use World Trading Data APIs get a free API key from  </span><a href=\"https://www.worldtradingdata.com/register\"><span style=\" text-decoration: underline; color:#0000ff;\">https://www.worldtradingdata.com/register</span></a><span style=\" font-size:9pt;\"> The data is realtime Historical data is available for the last 7 days. But the data limits are only 25 trades per call.</span></p></body></html>"))
        self.wtdCb.setText(_translate("Dialog", "WorldTradeData"))
        self.label_11.setText(_translate("Dialog", "API Key"))
        self.label_9.setText(_translate("Dialog", "<html><head/><body><p><a href=\"https://finnhub.io/\"><span style=\" text-decoration: underline; color:#0000ff;\">Finnhub API (right click)</span></a></p></body></html>"))
        self.fhCb.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">To use Finnhub APIs get a free API key from </span><a href=\"https://finnhub.io/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://finnhub.io </span></a><span style=\" font-size:9pt;\">The data is realtime Historical data  Data limts are 60 calls per minute and no practical limits per day.</span></p></body></html>"))
        self.fhCb.setText(_translate("Dialog", "Finnhub"))
        self.label_15.setText(_translate("Dialog", "API Key"))
        self.label_10.setText(_translate("Dialog", "Order the tokens ib, bc, av, wtd and fh for preference"))
        self.APIPref.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt;\">Place the tokkens in order of preference. Structjour will choose from your preference and the availability of the api</span></p><p><br/></p><p><span style=\" font-size:9pt;\">For Example</span></p><p><br/></p><p><span style=\" font-size:9pt; font-weight:600;\">ib, bc, av, iex</span><span style=\" font-size:9pt;\"/></p><p><span style=\" font-size:9pt;\">If you set the above order and click for a chart update for todays chart at 3:00 PM, </span></p><p><span style=\" font-size:9pt;\">Structjour will use ib if you have opened IBGateway application.</span></p><p><span style=\" font-size:9pt;\">bc cannot be used for todays data till after 4:30</span></p><p><span style=\" font-size:9pt;\">Finally av will be chosen with its real time data.</span></p><p><span style=\" font-size:9pt;\">(iex works OK 1/2 the time)</span></p></body></html>"))
        self.APIPref.setText(_translate("Dialog", "ib, bc, av, wtd"))
        self.okBtn.setText(_translate("Dialog", "OK"))
