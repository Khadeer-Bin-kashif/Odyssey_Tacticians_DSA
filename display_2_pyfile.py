from PyQt5 import QtCore, QtGui, QtWidgets 
from DSA_proj import extract_from_graph, number_of_cities, starting_city, dist_matrix_creator, held_karp_route, index_to_city_convertor, greedy_cycle_generator, graphic, create_subgraph
from display_3 import Ui_Dialog_3

class Ui_Dialog_2(object):
    graph = {
    'Karachi':[('Lahore', 1211), ('Faisalabad', 1115), ('Gwadar', 622), ('Multan', 884), ('Hyederabad', 163), ('Quetta', 590), ('Islamabad', 1412), ('Peshawar', 1554), ('Gujranwala', 1268), ('Rawalpindi', 1396), ('Sialkot', 1312), ('Sukkur', 470), ('Bahawalpur', 676), ('Gujrat', 1090), ('Chaman', 806), ('Nawabshah', 267), ('Larkana', 455), ('Sargodha', 1221), ('Abbottabad', 1501), ('Sahiwal', 1054)],
    'Lahore':[('Karachi', 1211), ('Faisalabad', 192), ('Gwadar', 1839), ('Multan', 348), ('Hyederabad', 1079), ('Quetta', 984), ('Islamabad', 389), ('Peshawar', 531), ('Gujranwala', 73), ('Rawalpindi', 398), ('Sialkot', 132), ('Sukkur', 768), ('Bahawalpur', 426), ('Gujrat', 168), ('Chaman', 1042), ('Nawabshah', 944), ('Larkana', 847), ('Sargodha', 198), ('Abbottabad', 479), ('Sahiwal', 170)],
    'Faisalabad':[('Karachi', 1115), ('Lahore', 192), ('Gwadar', 1735), ('Multan', 244), ('Hyederabad', 975), ('Quetta', 879), ('Islamabad', 320), ('Peshawar', 462), ('Gujranwala', 186), ('Rawalpindi', 304), ('Sialkot', 260), ('Sukkur', 664), ('Bahawalpur', 322), ('Gujrat', 231), ('Chaman', 937), ('Nawabshah', 839), ('Larkana', 742), ('Sargodha', 129), ('Abbottabad', 410), ('Sahiwal', 102)],
    'Gwadar':[('Karachi', 622), ('Lahore', 1839), ('Faisalabad', 1735), ('Multan', 1501), ('Hyederabad', 780), ('Quetta', 919), ('Islamabad', 2028), ('Peshawar', 2171), ('Gujranwala', 1884), ('Rawalpindi', 2012), ('Sialkot', 1929), ('Sukkur', 1091), ('Bahawalpur', 1452), ('Gujrat', 1905), ('Chaman', 1040), ('Nawabshah', 883), ('Larkana', 1059), ('Sargodha', 1838), ('Abbottabad', 2118), ('Sahiwal', 1671)],
    'Multan':[('Karachi', 884), ('Lahore', 348), ('Gwadar', 1501), ('Faisalabad', 244), ('Hyederabad', 744), ('Quetta', 633), ('Islamabad', 539), ('Peshawar', 681), ('Gujranwala', 395), ('Rawalpindi', 522), ('Sialkot', 439), ('Sukkur', 433), ('Bahawalpur', 100), ('Gujrat', 440), ('Chaman', 690), ('Nawabshah', 609), ('Larkana', 512), ('Sargodha', 348), ('Abbottabad', 628), ('Sahiwal', 181)],
    'Hyederabad':[('Karachi', 163), ('Lahore', 1079), ('Gwadar', 780), ('Multan', 744), ('Faisalabad', 975), ('Quetta', 707), ('Islamabad', 1246), ('Peshawar', 1388), ('Gujranwala', 1102), ('Rawalpindi', 1230), ('Sialkot', 1146), ('Sukkur', 333), ('Bahawalpur', 670), ('Gujrat', 1122), ('Chaman', 832), ('Nawabshah', 112), ('Larkana', 315), ('Sargodha', 1055), ('Abbottabad', 1336), ('Sahiwal', 888)],
    'Quetta':[('Karachi', 590), ('Lahore', 984), ('Gwadar', 919), ('Multan', 633), ('Hyederabad', 707), ('Faisalabad', 879), ('Islamabad', 893), ('Peshawar', 840), ('Gujranwala', 1030), ('Rawalpindi', 910), ('Sialkot', 1074), ('Sukkur', 386), ('Bahawalpur', 767), ('Gujrat', 1064), ('Chaman', 125), ('Nawabshah', 581), ('Larkana', 395), ('Sargodha', 766), ('Abbottabad', 971), ('Sahiwal', 816)],
    'Islamabad':[('Karachi', 1412), ('Lahore', 389), ('Gwadar', 2028), ('Multan', 539), ('Hyederabad', 1246), ('Quetta', 893), ('Faisalabad', 320), ('Peshawar', 186), ('Gujranwala', 219), ('Rawalpindi', 22), ('Sialkot', 229), ('Sukkur', 956), ('Bahawalpur', 614), ('Gujrat',176), ('Chaman', 949), ('Nawabshah', 1132), ('Larkana', 1035), ('Sargodha', 231), ('Abbottabad', 103), ('Sahiwal', 415)],
    'Peshawar':[('Karachi', 1554), ('Lahore', 531), ('Gwadar', 2171), ('Multan', 681), ('Hyederabad', 1388), ('Quetta', 840), ('Islamabad', 186), ('Faisalabad', 462), ('Gujranwala', 402), ('Rawalpindi', 187), ('Sialkot', 411), ('Sukkur', 1102), ('Bahawalpur', 760), ('Gujrat', 359), ('Chaman', 898), ('Nawabshah', 1278), ('Larkana', 1181), ('Sargodha', 377), ('Abbottabad', 199), ('Sahiwal', 561)],
    'Gujranwala':[('Karachi', 1268), ('Lahore', 73), ('Gwadar', 1884), ('Multan', 395), ('Hyederabad', 1102), ('Quetta', 1030), ('Islamabad', 219), ('Peshawar', 402), ('Faisalabad', 186), ('Rawalpindi', 212), ('Sialkot', 51), ('Sukkur', 815), ('Bahawalpur', 473), ('Gujrat', 48), ('Chaman', 1088), ('Nawabshah', 991), ('Larkana', 893), ('Sargodha', 190), ('Abbottabad', 341), ('Sahiwal', 262)],
    'Rawalpindi':[('Karachi', 1396), ('Lahore', 398), ('Gwadar', 2012), ('Multan', 522), ('Hyederabad', 1230), ('Quetta',910 ), ('Islamabad', 22), ('Peshawar', 187), ('Gujranwala', 212), ('Faisalabad', 304), ('Sialkot', 221), ('Sukkur', 944), ('Bahawalpur', 602), ('Gujrat', 168), ('Chaman', 950), ('Nawabshah', 1120), ('Larkana', 1023), ('Sargodha', 220), ('Abbottabad', 106), ('Sahiwal',403)],
    'Sialkot':[('Karachi', 1312), ('Lahore', 132), ('Gwadar', 1929), ('Multan', 439), ('Hyederabad', 1146), ('Quetta', 1074), ('Islamabad', 229), ('Peshawar', 411), ('Gujranwala', 51), ('Rawalpindi', 221), ('Faisalabad', 260), ('Sukkur', 858), ('Bahawalpur', 516), ('Gujrat', 58), ('Chaman', 1131), ('Nawabshah', 1034), ('Larkana', 937), ('Sargodha', 264), ('Abbottabad', 351), ('Sahiwal', 305)],
    'Sukkur':[('Karachi', 470), ('Lahore', 768), ('Gwadar', 1091), ('Multan', 433), ('Hyederabad', 333), ('Quetta', 386), ('Islamabad', 956), ('Peshawar', 1102), ('Gujranwala', 815), ('Rawalpindi', 944), ('Sialkot', 858), ('Faisalabad', 664), ('Bahawalpur', 382), ('Gujrat', 835), ('Chaman', 511), ('Nawabshah', 197), ('Larkana', 82), ('Sargodha', 768), ('Abbottabad', 1048), ('Sahiwal', 601)],
    'Bahawalpur':[('Karachi', 676), ('Lahore', 426), ('Gwadar', 1452), ('Multan', 100), ('Hyederabad', 670), ('Quetta', 767), ('Islamabad', 614), ('Peshawar', 760), ('Gujranwala', 473), ('Rawalpindi', 602), ('Sialkot', 516), ('Sukkur', 382), ('Faisalabad', 322), ('Gujrat', 519), ('Chaman', 776), ('Nawabshah', 556), ('Larkana', 459), ('Sargodha', 427), ('Abbottabad', 707), ('Sahiwal', 244)],
    'Gujrat':[('Karachi', 1090), ('Lahore', 168), ('Gwadar', 1905), ('Multan', 440), ('Hyederabad', 1122), ('Quetta', 1064), ('Islamabad', 176), ('Peshawar', 359), ('Gujranwala', 48), ('Rawalpindi', 168), ('Sialkot', 58), ('Sukkur', 835), ('Bahawalpur', 519), ('Faisalabad', 231), ('Chaman', 1116), ('Nawabshah', 1010), ('Larkana', 913), ('Sargodha', 160), ('Abbottabad', 300), ('Sahiwal', 307)],
    'Chaman':[('Karachi', 806), ('Lahore', 1042), ('Gwadar', 1040), ('Multan', 690), ('Hyederabad', 832), ('Quetta', 125), ('Islamabad', 949), ('Peshawar', 898), ('Gujranwala', 1088), ('Rawalpindi', 950), ('Sialkot', 1131), ('Sukkur', 511), ('Bahawalpur', 776), ('Gujrat', 1116), ('Faisalabad',937), ('Nawabshah', 706), ('Larkana', 520), ('Sargodha', 824), ('Abbottabad', 1029), ('Sahiwal', 875)],
    'Nawabshah':[('Karachi', 267), ('Lahore', 944), ('Gwadar', 883), ('Multan', 609), ('Hyederabad', 112), ('Quetta', 581), ('Islamabad', 1132), ('Peshawar', 1278), ('Gujranwala', 991), ('Rawalpindi', 1120), ('Sialkot', 1034), ('Sukkur', 197), ('Bahawalpur', 556), ('Gujrat', 1010), ('Chaman', 706), ('Faisalabad', 839), ('Larkana', 206), ('Sargodha', 944), ('Abbottabad', 1225), ('Sahiwal', 777)],
    'Larkana':[('Karachi', 455), ('Lahore', 847), ('Gwadar', 1059), ('Multan', 512), ('Hyederabad', 315), ('Quetta', 395), ('Islamabad', 1035), ('Peshawar', 1181), ('Gujranwala', 893), ('Rawalpindi', 1023), ('Sialkot', 937), ('Sukkur', 82), ('Bahawalpur', 459), ('Gujrat', 913), ('Chaman', 520), ('Nawabshah', 206), ('Faisalabad', 742), ('Sargodha', 846), ('Abbottabad', 1127), ('Sahiwal', 680)],
    'Sargodha':[('Karachi', 1221), ('Lahore', 198), ('Gwadar', 1838), ('Multan', 348), ('Hyederabad', 1055), ('Quetta', 766), ('Islamabad', 231), ('Peshawar', 377), ('Gujranwala', 190), ('Rawalpindi', 220), ('Sialkot', 264), ('Sukkur', 768), ('Bahawalpur', 427), ('Gujrat', 160), ('Chaman', 824), ('Nawabshah', 944), ('Larkana', 846), ('Faisalabad', 129), ('Abbottabad', 331), ('Sahiwal', 229)],
    'Abbottabad':[('Karachi', 1501), ('Lahore', 479), ('Gwadar', 2118), ('Multan', 628), ('Hyederabad', 1336), ('Quetta', 971), ('Islamabad', 103), ('Peshawar', 199), ('Gujranwala', 341), ('Rawalpindi', 106), ('Sialkot', 351), ('Sukkur', 1048), ('Bahawalpur', 707), ('Gujrat',300 ), ('Chaman', 1029), ('Nawabshah', 1225), ('Larkana', 1127), ('Sargodha', 331), ('Faisalabad', 410), ('Sahiwal', 509)],
    'Sahiwal':[('Karachi', 1054), ('Lahore', 170), ('Gwadar', 1671), ('Multan', 181), ('Hyederabad', 888), ('Quetta', 816), ('Islamabad', 415), ('Peshawar', 561), ('Gujranwala', 262), ('Rawalpindi', 403), ('Sialkot', 305), ('Sukkur', 601), ('Bahawalpur', 244), ('Gujrat', 307), ('Chaman', 875), ('Nawabshah', 777), ('Larkana', 680), ('Sargodha', 229), ('Abbottabad', 509), ('Faisalabad', 102)]
        }
    def extract_from_graph(self, gliph):
        temp = {}
        for i in gliph:
            if i not in self.graph:  # Access the instance variable graph
                print(f'sorry {i} is not in our list of cities.')
            for j in self.graph:
                if j == i:
                    temp[i] = self.graph[i]  # Access the instance variable graph
        # print(temp)

    def open_window1(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog_3()
        self.ui.setupUi(self.window)
        self.window.show()
        # Dialog.hide()

    def setupUi(self, Dialog, Dialog1):
        Dialog.setObjectName("Odyssey Tactician")
        Dialog.resize(1098, 828)

        self.selected_cities_list = QtWidgets.QListWidget(Dialog)  # Add this line
        self.selected_cities_list.setGeometry(QtCore.QRect(50, 150, 191, 231))  # Add this line
        self.selected_cities_list.setObjectName("selected_cities_list")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 1101, 831))
        self.label.setStyleSheet("background-image: url(:/newPrefix/Screenshot (1).png);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/newPrefix/Screenshot (1).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.startingcity = QtWidgets.QListWidget(Dialog)
        self.startingcity.setGeometry(QtCore.QRect(450, 150, 191, 231))
        self.startingcity.setMouseTracking(False)
        self.startingcity.setObjectName("startingcity")
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.startingcity.addItem(item)
        self.othercities = QtWidgets.QListWidget(Dialog)
        self.othercities.setGeometry(QtCore.QRect(450, 520, 191, 231))
        self.othercities.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.othercities.setObjectName("othercities")
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.othercities.addItem(item)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(270, 60, 571, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 420, 581, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog, clicked= lambda: self.open_window1())
        self.pushButton.setGeometry(QtCore.QRect(900, 740, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.pushButton.clicked.connect(self.next_button_clicked)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Odyssey Tactician"))
        __sortingEnabled = self.startingcity.isSortingEnabled()
        self.startingcity.setSortingEnabled(False)
        item = self.startingcity.item(0)
        item.setText(_translate("Dialog", "Karachi"))
        item = self.startingcity.item(1)
        item.setText(_translate("Dialog", "Lahore"))
        item = self.startingcity.item(2)
        item.setText(_translate("Dialog", "Faisalabad"))
        item = self.startingcity.item(3)
        item.setText(_translate("Dialog", "Gwadar"))
        item = self.startingcity.item(4)
        item.setText(_translate("Dialog", "Multan"))
        item = self.startingcity.item(5)
        item.setText(_translate("Dialog", "Hyederabad"))
        item = self.startingcity.item(6)
        item.setText(_translate("Dialog", "Quetta"))
        item = self.startingcity.item(7)
        item.setText(_translate("Dialog", "Islamabad"))
        item = self.startingcity.item(8)
        item.setText(_translate("Dialog", "Peshawar"))
        item = self.startingcity.item(9)
        item.setText(_translate("Dialog", "Gujranwala"))
        item = self.startingcity.item(10)
        item.setText(_translate("Dialog", "Rawalpindi"))
        item = self.startingcity.item(11)
        item.setText(_translate("Dialog", "Sialkot"))
        item = self.startingcity.item(12)
        item.setText(_translate("Dialog", "Sukkur"))
        item = self.startingcity.item(13)
        item.setText(_translate("Dialog", "Bahawalpur"))
        item = self.startingcity.item(14)
        item.setText(_translate("Dialog", "Gujrat"))
        item = self.startingcity.item(15)
        item.setText(_translate("Dialog", "Chaman"))
        item = self.startingcity.item(16)
        item.setText(_translate("Dialog", "Nawabshah"))
        item = self.startingcity.item(17)
        item.setText(_translate("Dialog", "Larkana"))
        item = self.startingcity.item(18)
        item.setText(_translate("Dialog", "Sargodha"))
        item = self.startingcity.item(19)
        item.setText(_translate("Dialog", "Abbottabad"))
        item = self.startingcity.item(20)
        item.setText(_translate("Dialog", "Sahiwal"))
        self.startingcity.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.othercities.isSortingEnabled()
        self.othercities.setSortingEnabled(False)
        item = self.othercities.item(0)
        item.setText(_translate("Dialog", "Karachi"))
        item = self.othercities.item(1)
        item.setText(_translate("Dialog", "Lahore"))
        item = self.othercities.item(2)
        item.setText(_translate("Dialog", "Faisalabad"))
        item = self.othercities.item(3)
        item.setText(_translate("Dialog", "Gwadar"))
        item = self.othercities.item(4)
        item.setText(_translate("Dialog", "Multan"))
        item = self.othercities.item(5)
        item.setText(_translate("Dialog", "Hyederabad"))
        item = self.othercities.item(6)
        item.setText(_translate("Dialog", "Quetta"))
        item = self.othercities.item(7)
        item.setText(_translate("Dialog", "Islamabad"))
        item = self.othercities.item(8)
        item.setText(_translate("Dialog", "Peshawar"))
        item = self.othercities.item(9)
        item.setText(_translate("Dialog", "Gujranwala"))
        item = self.othercities.item(10)
        item.setText(_translate("Dialog", "Rawalpindi"))
        item = self.othercities.item(11)
        item.setText(_translate("Dialog", "Sialkot"))
        item = self.othercities.item(12)
        item.setText(_translate("Dialog", "Sukkur"))
        item = self.othercities.item(13)
        item.setText(_translate("Dialog", "Bahawalpur"))
        item = self.othercities.item(14)
        item.setText(_translate("Dialog", "Gujrat"))
        item = self.othercities.item(15)
        item.setText(_translate("Dialog", "Chaman"))
        item = self.othercities.item(16)
        item.setText(_translate("Dialog", "Nawabshah"))
        item = self.othercities.item(17)
        item.setText(_translate("Dialog", "Larkana"))
        item = self.othercities.item(18)
        item.setText(_translate("Dialog", "Sargodha"))
        item = self.othercities.item(19)
        item.setText(_translate("Dialog", "Abbottabad"))
        item = self.othercities.item(20)
        item.setText(_translate("Dialog", "Sahiwal"))
        self.othercities.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Dialog", "Select the starting point for your journey "))
        self.label_3.setText(_translate("Dialog", "Select the other cities you want to travel through"))
        self.pushButton.setText(_translate("Dialog", "Next"))
    
    def get_selected_items(self, list_widget):
        selected_items = []
        for item in list_widget.selectedItems():
            selected_items.append(item.text())
        return selected_items
        # print(selected_items)

    def next_button_clicked(self):
        selected_starting_cities = self.get_selected_items(self.startingcity)
        selected_other_cities = self.get_selected_items(self.othercities)
        all_selected_cities = selected_starting_cities + selected_other_cities
        
        # Clear the list before adding new items
        self.selected_cities_list.clear()

        # Add selected cities to the list
        for city in all_selected_cities:
            item = QtWidgets.QListWidgetItem(city)
            self.selected_cities_list.addItem(item)
        # return all_selected_cities

        #all the functions for the held karp are called here.
        graph_without_starting_city = extract_from_graph(self.graph, all_selected_cities)
        n = number_of_cities(graph_without_starting_city)
        start_city = starting_city(all_selected_cities)
        k = dist_matrix_creator(graph_without_starting_city, n, start_city)
        dist_mat, index_dic = k
        m = held_karp_route(dist_mat)
        for_held = index_to_city_convertor(m,index_dic)
        i = greedy_cycle_generator(dist_mat)
        for_greedy = index_to_city_convertor(i, index_dic)
        dialog_3 = Ui_Dialog_3()
        dialog_3.setupUi(self.window)
        l = Ui_Dialog_3.display(self, for_held, for_greedy)
        s= create_subgraph(for_held, self.graph)
        graphic(s)


import map_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog_2()
    ui.setupUi(Dialog, Dialog)
    Dialog.show()
    sys.exit(app.exec_())
