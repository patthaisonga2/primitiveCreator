try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

import maya.OpenMayaUI as omui 
import os 
import importlib
from . import objectCreatorUtil as obutil
importlib.reload(obutil)

ICON_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__),'icons'))


class PrimitiveCreatorDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.resize(300,300)
		self.setWindowTitle('Primitive Creator')

		self.main_layout = QtWidgets.QVBoxLayout()
		self.setLayout(self.main_layout)

		self.object_listWidget = QtWidgets.QListWidget()
		self.object_listWidget.setIconSize(QtCore.QSize(60,60))
		self.object_listWidget.setSpacing(8)
		self.object_listWidget.setViewMode(QtWidgets.QListView.IconMode)
		self.object_listWidget.setMovement(QtWidgets.QListView.Static)
		self.object_listWidget.setResizeMode(QtWidgets.QListView.Adjust)


		self.main_layout.addWidget(self.object_listWidget)

		self.name_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.name_layout)

		self.name_label = QtWidgets.QLabel('Name:')
		self.name_lineEdit = QtWidgets.QLineEdit()
		self.name_lineEdit.setStyleSheet(
			'''
				QLineEdit {
					border-radius: 5px;
					background-color: white;
					color: navy;
					font-size: 24px;
					font-family: Oswald;
				}
			'''
		)


		self.name_layout.addWidget(self.name_label)
		self.name_layout.addWidget(self.name_lineEdit)

		self.button_layout = QtWidgets.QHBoxLayout()
		self.main_layout.addLayout(self.button_layout)
		self.create_button = QtWidgets.QPushButton('😍 Create')
		self.create_button.setStyleSheet(
			'''
				QPushButton {
					background-color: #6600CC
				}
			'''
		)

		self.cancel_button = QtWidgets.QPushButton('😒 Cancel')
		self.cancel_button.setStyleSheet(
			'''
				QPushButton {
					background-color: #FF3366
				}
			'''
		)

		self.button_layout.addStretch()
		self.button_layout.addWidget(self.create_button)
		self.button_layout.addWidget(self.cancel_button)

		self.initIconWidgets()

	def initIconWidgets(self):
		prims = ['cone','cube','sphere','torus']
		for prim in prims:
			item = QtWidgets.QListWidgetItem(prim)
			item.setIcon(QtGui.QIcon(os.path.join(ICON_PATH,f'{prim}.png')))
			self.object_listWidget.addItem(item)

def run():
	global ui 

	try:
		ui.close()
	except:
		pass
	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = PrimitiveCreatorDialog(parent=ptr)
	ui.show()






