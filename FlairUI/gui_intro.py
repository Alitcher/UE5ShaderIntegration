import sys
import unreal

from PySide2 import QtWidgets, QtUiTools

class SimpleGUI(QtWidgets.QWidget):
    window = None
    def __init__(self, parent=None):
        super(SimpleGUI, self).__init__(parent)

        self.widget = QtUiTools.QUiLoader().load(r"D:\Somying's\Job\ADMISSION\Tartu\MSC\thesis\QtPlayground\UE5ui\UntitledProject\qtuiue5\mainwindow.ui")
        self.widget.setParent(self)

    def on_start(self):
        self.button.setEnabled(False)
        self.thread.start()

    def report_progress(self, n):
        print(f"Progress: {n}")

    def cleanup(self):
        print("Thread finished")
        self.button.setEnabled(True)

# only create an instance of the GUI when it's not already running
app = None
if not QtWidgets.QApplication.instance():
    app = QtWidgets.QApplication(sys.argv)

# start the GUI
main_window = SimpleGUI()
main_window.show()