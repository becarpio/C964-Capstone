import pandas as pd
import sys
from os import path
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView, QMessageBox
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MaxAbsScaler

if path.exists("MyAnimeList Dataset/anime_list_scrubbed.csv"):
    # This file has the titles intact
    anime_list = pd.read_csv("MyAnimeList Dataset/anime_list_scrubbed.csv")
else:
    print("Anime .csv import failed")
    sys.exit(1)

if path.exists("movie_info_model.pkl"):
    # Import the model created in Jupyter Notebooks
    knn_model = pickle.load(open("movie_info_model.pkl", "rb"))
else:
    print(".pkl import failed")
    sys.exit(2)


class Ui_RecommendationWindow(object):
    def __init__(self):
        self.chosen_title = ""

    def setChosenTitle(self, title):
        self.chosen_title = title

    def getChosenTitle(self):
        return self.chosen_title

    def makeRecommendations(self):
        distance, indices = knn_model.kneighbors(transformed_anime_list[self.chosen_title], n_neighbors=6)

        self.rec_lbl_title1.setText(anime_list["title"].iloc[indices.item(1)])
        self.rec_lbl_title2.setText(anime_list["title"].iloc[indices.item(2)])
        self.rec_lbl_title3.setText(anime_list["title"].iloc[indices.item(3)])
        self.rec_lbl_title4.setText(anime_list["title"].iloc[indices.item(4)])
        self.rec_lbl_title5.setText(anime_list["title"].iloc[indices.item(5)])

    def setupUi(self, RecommendationWindow):
        RecommendationWindow.setObjectName("RecommendationWindow")
        RecommendationWindow.resize(333, 196)
        self.centralwidget = QtWidgets.QWidget(RecommendationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 311, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rec_lbl_header = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.rec_lbl_header.setFont(font)
        self.rec_lbl_header.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.rec_lbl_header.setObjectName("rec_lbl_header")
        self.verticalLayout.addWidget(self.rec_lbl_header)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.rec_lbl_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_lbl_1.setFont(font)
        self.rec_lbl_1.setObjectName("rec_lbl_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.rec_lbl_1)
        self.rec_lbl_title1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rec_lbl_title1.setObjectName("rec_lbl_title1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.rec_lbl_title1)
        self.rec_lbl_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_lbl_2.setFont(font)
        self.rec_lbl_2.setObjectName("rec_lbl_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.rec_lbl_2)
        self.rec_lbl_title2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rec_lbl_title2.setObjectName("rec_lbl_title2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.rec_lbl_title2)
        self.rec_lbl_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_lbl_3.setFont(font)
        self.rec_lbl_3.setObjectName("rec_lbl_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.rec_lbl_3)
        self.rec_lbl_title3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rec_lbl_title3.setObjectName("rec_lbl_title3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rec_lbl_title3)
        self.rec_lbl_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_lbl_4.setFont(font)
        self.rec_lbl_4.setObjectName("rec_lbl_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.rec_lbl_4)
        self.rec_lbl_title4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rec_lbl_title4.setObjectName("rec_lbl_title4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rec_lbl_title4)
        self.rec_lbl_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.rec_lbl_5.setFont(font)
        self.rec_lbl_5.setObjectName("rec_lbl_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.rec_lbl_5)
        self.rec_lbl_title5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rec_lbl_title5.setObjectName("rec_lbl_title5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.rec_lbl_title5)
        self.verticalLayout.addLayout(self.formLayout)
        RecommendationWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(RecommendationWindow)
        self.statusbar.setObjectName("statusbar")
        RecommendationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RecommendationWindow)
        QtCore.QMetaObject.connectSlotsByName(RecommendationWindow)

    def retranslateUi(self, RecommendationWindow):
        _translate = QtCore.QCoreApplication.translate
        RecommendationWindow.setWindowTitle(_translate("RecommendationWindow", "Anime Recommendations"))
        self.rec_lbl_header.setText(_translate("RecommendationWindow", "Top 5 Recommended for You"))
        self.rec_lbl_1.setText(_translate("RecommendationWindow", "1)"))
        self.rec_lbl_title1.setText(_translate("RecommendationWindow", "TextLabel"))
        self.rec_lbl_2.setText(_translate("RecommendationWindow", "2)"))
        self.rec_lbl_title2.setText(_translate("RecommendationWindow", "TextLabel"))
        self.rec_lbl_3.setText(_translate("RecommendationWindow", "3)"))
        self.rec_lbl_title3.setText(_translate("RecommendationWindow", "TextLabel"))
        self.rec_lbl_4.setText(_translate("RecommendationWindow", "4)"))
        self.rec_lbl_title4.setText(_translate("RecommendationWindow", "TextLabel"))
        self.rec_lbl_5.setText(_translate("RecommendationWindow", "5)"))
        self.rec_lbl_title5.setText(_translate("RecommendationWindow", "TextLabel"))


class Ui_MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.rec = QtWidgets.QMainWindow()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.main_txtinput = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.main_btn_filter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_listview_animetitles = QtWidgets.QListView(self.verticalLayoutWidget)
        self.listview_model = QStandardItemModel(self.main_listview_animetitles)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.main_btn_graph3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_graph2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_graph1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_recommend = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.main_btn_exit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)

    # Show correlation between the non-genre and non-studio features
    def correlation_matrix(self):
        sns.set(font_scale=0.75)
        anime_corr_map = sns.heatmap(anime_list[anime_list.columns[0:8]].corr(), cmap="YlGnBu")
        plt.show()

    # Show the a total of shows in each genre
    def genre_bargraph(self):
        # Create a "sub" DataFrame with genre info only
        genre_info = pd.DataFrame(anime_list.iloc[:, anime_list.columns.get_loc("Action"):])
        # From the info frame, create a DF with each column as a row
        # and the total number of entries for each column
        genre_total = pd.DataFrame(data=genre_info.sum(axis=0))
        genre_total.columns = ["Total"]
        # Plot a bar graph showing the number of shows per genre
        # most shows cross into more than one genre
        genre_total.plot(kind="bar")
        plt.show()

    # Show the a total of shows in each rating
    def ratings_graph(self):
        # 0: PG - 13 - Teens 13 or older
        # 1: PG - Children
        # 2: G - All Ages

        # Create a "sub" DataFrame with sum for each rating
        ratings_info = anime_list.iloc[:, anime_list.columns.get_loc("rating")]

        ratings_totals = pd.DataFrame(ratings_info.value_counts())

        ratings_totals.columns = ["Total"]
        ratings_totals.index = ["PG-13", "PG", "G"]
        ratings_totals.plot(kind="bar")
        plt.show()

    def getRecommendation(self):
        # Get selected item index from listview
        index = self.main_listview_animetitles.currentIndex()
        # Convert index into title name
        title_name = self.listview_model.itemFromIndex(index).text()
        # Convert title name into anime_list index
        title_index = anime_list[anime_list["title"] == title_name].index.values

        recommendation_window = Ui_RecommendationWindow()
        recommendation_window.setupUi(self.rec)
        recommendation_window.setChosenTitle(title_index[0])
        recommendation_window.makeRecommendations()
        self.rec.show()

    def initializeListView(self):
        # Delete rows in current listview_model
        self.listview_model.removeRows(0, self.listview_model.rowCount())

        for title in anime_list["title"]:
            item = QStandardItem(title)
            self.listview_model.appendRow(item)
        # Show the model
        self.main_listview_animetitles.setModel(self.listview_model)
        self.main_listview_animetitles.setCurrentIndex(self.listview_model.index(0, 0))

    def updateListView(self):
        # Delete rows in current listview_model
        self.listview_model.removeRows(0, self.listview_model.rowCount())

        # If the text input box is blank
        if self.main_txtinput.text() == "":
            for title in anime_list["title"]:
                item = QStandardItem(title)
                self.listview_model.appendRow(item)
        # Otherwise, if something is in the text input box, filter the information
        else:
            for title in anime_list["title"]:
                if self.main_txtinput.text().lower() in title.lower():
                    item = QStandardItem(title)
                    self.listview_model.appendRow(item)
        if self.listview_model.rowCount() > 0:
            # Show the model
            self.main_listview_animetitles.setModel(self.listview_model)
            self.main_listview_animetitles.setCurrentIndex(self.listview_model.index(0, 0))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("No matches found, please select a different filter term")
            msg.setWindowTitle("Critical Error")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
            self.initializeListView()

    def setupUi(self, MainWindow):
        # Set up initial part of UI
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(526, 450)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 501, 401))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout.setObjectName("horizontalLayout")

        """
            Line Edit Widget: The user should type all or part of the anime 
            they'd like a recommendation from.

            Filter Button: When the user clicks filter, the information from
            the LEW should be pulled and then search the titles for matches.
            Update the list view with any matches

        """
        self.main_txtinput.setObjectName("main_txtinput")
        self.horizontalLayout.addWidget(self.main_txtinput)

        self.main_btn_filter.setObjectName("main_btn_filter")

        # UI Setup
        self.horizontalLayout.addWidget(self.main_btn_filter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        """
            Anime Titles List View:
            - Begin with all of the titles showing, update as needed when filter
              is applied.            
        """

        # Set up the initial list View
        self.main_listview_animetitles.setObjectName("main_listview_animetitles")
        self.main_listview_animetitles.setSelectionMode(QAbstractItemView.SingleSelection)
        # Call initializeListView above to set up the model
        self.initializeListView()
        # Update when filter button is clicked
        self.main_btn_filter.clicked.connect(self.updateListView)

        # More UI setup
        self.verticalLayout_2.addWidget(self.main_listview_animetitles)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        """
            Set up Correlation Graph
        """
        self.main_btn_graph1.setObjectName("main_btn_graph1")
        self.horizontalLayout_3.addWidget(self.main_btn_graph1)
        self.main_btn_graph1.clicked.connect(self.correlation_matrix)

        """
            Set Up Genre Histogram        
        """
        self.main_btn_graph2.setObjectName("main_btn_graph2")
        self.horizontalLayout_3.addWidget(self.main_btn_graph2)
        self.main_btn_graph2.clicked.connect(self.genre_bargraph)

        """
            Set up third Graph
        """
        self.main_btn_graph3.setObjectName("main_btn_graph3")
        self.horizontalLayout_3.addWidget(self.main_btn_graph3)
        self.main_btn_graph3.clicked.connect(self.ratings_graph)

        # Shockingly, more UI setup
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        """
            When the user clicks recommend, the highlighted anime in listview
            should be sent to the model and return 5 title recommendations via
            a message box        
        """
        self.main_btn_recommend.setObjectName("main_btn_recommend")
        self.horizontalLayout_2.addWidget(self.main_btn_recommend)
        self.main_btn_recommend.clicked.connect(self.getRecommendation)

        """
            Exit Button:
            Close application when pressed
        """
        # Set up Exit button for Main Window
        self.main_btn_exit.setObjectName("main_btn_exit")
        self.main_btn_exit.clicked.connect(QApplication.instance().quit)

        # Even more UI setup
        self.horizontalLayout_2.addWidget(self.main_btn_exit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Anime Recommendations"))
        self.main_txtinput.setText(_translate("MainWindow", "Enter Anime Title"))
        self.main_btn_filter.setText(_translate("MainWindow", "Filter"))
        self.main_btn_graph1.setText(_translate("MainWindow", "Correlation Matrix"))
        self.main_btn_graph2.setText(_translate("MainWindow", "Genre Bargraph"))
        self.main_btn_graph3.setText(_translate("MainWindow", "Ratings Graph"))
        self.main_btn_recommend.setText(_translate("MainWindow", "Recommendations"))
        self.main_btn_exit.setText(_translate("MainWindow", "Exit"))


def prepData():
    revised_anime_list = anime_list.drop(["anime_id"], axis=1)
    categorical_features = ["title"]

    one_hot = OneHotEncoder()
    transformer = ColumnTransformer([("one_hot",
                                      one_hot,
                                      categorical_features)],
                                    remainder="passthrough")

    global transformed_anime_list
    transformed_anime_list = transformer.fit_transform(revised_anime_list)

    # Normalize the data

    max_abs_scaler = MaxAbsScaler()
    transformed_anime_list = max_abs_scaler.fit_transform(transformed_anime_list)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    # Set up Main Window
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    prepData()

    MainWindow.show()
    sys.exit(app.exec_())
