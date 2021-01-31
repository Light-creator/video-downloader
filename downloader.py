import sys, os, pytube
from PyQt5 import QtCore, QtGui, QtWidgets
from name import Ui_MainWindow

class Downloader:

	def __init__(self, url):
		self.url = url
		self.video = pytube.YouTube(self.url)

	def get_filename(self):
		filename = self.video.title
		print(filename)
		return filename

	def download(self, folder):
		try:
			self.video.streams.first().download(folder)
			return True
		except:
			print(folder)
			return False




class Gui(QtWidgets.QMainWindow):
	
	def __init__(self):
		super().__init__()

		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		self.ui.pushButton.clicked.connect(self.get_folder)
		self.ui.pushButton_2.clicked.connect(self.start)

	def get_folder(self):
		self.folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose the folder')
		print(self.folder)
		os.chdir(self.folder)

	def start(self):
		if len(self.ui.lineEdit.text()) > 10:
			if self.folder != None:
				downloader = Downloader(self.ui.lineEdit.text())
				self.ui.label.setText('Downloading' + downloader.get_filename())
				download = downloader.download(self.folder)
				if download == False:
					self.ui.label.setText('Error')
				else:
					self.ui.label.setText('file:  ' + downloader.get_filename() + '  has been downloaded')
			else:
				self.ui.label.setText('You have not selected a folder')
		else:
			self.ui.label.setText('Invalid url')



if __name__ == "__main__":

	app = QtWidgets.QApplication(sys.argv)
	win = Gui()
	win.show()
	sys.exit(app.exec_())