from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPaintEvent, QPainter, QColor, QPen
from PySide6.QtWidgets import QVBoxLayout, QWidget

from TitleBar import TitleBar


class CustomerAreaWidget(QWidget):
    """客户区"""

    def __init__(self, parent):
        super().__init__(parent=parent)


class MainArea(QWidget):
    """主区域，包含客户区和标题栏"""

    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        self.title_bar = TitleBar(self)
        self.customer_area = CustomerAreaWidget(self)

        self.verticalLayout.addWidget(self.title_bar)
        self.verticalLayout.addWidget(self.customer_area)

        self.isMax: bool = False
        self.title_bar.MoveWindow.connect(self.setMoving)
        self.title_bar.Maximized.connect(self.setMaximized)

    @Slot()
    def setMoving(self):
        self.isMax = False

    @Slot()
    def setMaximized(self):
        self.isMax = True

    def TitleBar(self):
        return self.title_bar

    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        # pen = QPen(QColor(184, 184, 184))
        # pen.setWidth(2)
        # painter.setPen(pen)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(240, 240, 240))
        if not (self.isMax and self.window().isMaximized()):
            painter.drawRoundedRect(self.rect(), 10, 10)
        elif self.isMax or self.window().isMaximized():
            painter.drawRect(self.rect())
