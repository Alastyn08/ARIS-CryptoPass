from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QGridLayout, QScrollArea, QScrollBar, QPushButton, QHBoxLayout, \
    QLineEdit

from src.widgets.password.website_password_widget import WebsitePasswordWidget


class PasswordScreenWidget(QVBoxLayout):
    def __init__(self, *args, window, passwordList, cryptFile):
        super().__init__(*args)
        self.window = window
        self.passwordList = passwordList
        self.cryptFile = cryptFile
        self.createWidget()

    def createWidget(self):
        screenBox = QGroupBox()
        vbox = QVBoxLayout()
        screenBox.setStyleSheet("QGroupBox{border:none}")


        searchBox = QGroupBox()
        searchBox.setStyleSheet("QGroupBox{border:none}")

        hboxSearch = QHBoxLayout()

        lineEditSearch = QLineEdit()

        boutonSearch = QPushButton()
        boutonSearch.setText("Search")
        hboxSearch.addWidget(lineEditSearch)
        hboxSearch.addWidget(boutonSearch)
        searchBox.setLayout(hboxSearch)

        vbox.addWidget(searchBox)
        scrollArea = QScrollArea()
        groupBoxPassword = QGroupBox()
        groupBoxPassword.setStyleSheet("QGroupBox{border:none}")

        vboxPassword = QVBoxLayout()
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window, website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))
        vboxPassword.addWidget(WebsitePasswordWidget(window=self.window,
                                                   website_password="Site=www.google.com/User=Nicolas/Password=StrongPasswordWaou"))

        scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scrollArea.setWidgetResizable(True)
        scrollArea.setFixedHeight(370)
        groupBoxPassword.setLayout(vboxPassword)
        scrollArea.setWidget(groupBoxPassword)
        vbox.addWidget(scrollArea)

        buttonCreateNewPassword = QPushButton(self.window)
        buttonCreateNewPassword.setText("Create new password")
        buttonCreateNewPassword.setFixedHeight(25)
        buttonCreateNewPassword.setFixedWidth(150)
        vbox.addWidget(scrollArea)
        vbox.addWidget(buttonCreateNewPassword, alignment=Qt.AlignCenter)
        screenBox.setLayout(vbox)

        self.addWidget(screenBox)