import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtGui import QPainter, QPen, QColor
import time
from PIL import ImageGrab

class ScreenCapture(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rect Selector")
        self.setWindowOpacity(0.3)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(0, 0,
            QApplication.primaryScreen().size().width(),
            QApplication.primaryScreen().size().height())
        self.start_point = None
        self.end_point = None
        self.rect = None
        self.show()
        
    def capture_area(self, x1, y1, x2, y2):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        time.sleep(0.5)  # 少し待ってからキャプチャ
        img = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        filename = f"capture_{time.strftime('%Y%m%d_%H%M%S')}.png"
        img.save(filename)
        print(f"保存しました: {filename}")

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.start_point = event.pos()
            self.end_point = self.start_point
            self.update()

    def mouseMoveEvent(self, event):
        if self.start_point:
            self.end_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.end_point = event.pos()
            self.rect = QRect(self.start_point, self.end_point).normalized()
            self.update()
            self.close()
            self.capture_area(self.rect.x(), self.rect.y(),
                self.rect.x() + self.rect.width(),
                self.rect.y() + self.rect.height())

    def paintEvent(self, event):
        if self.start_point and self.end_point:
            painter = QPainter(self)
            painter.setPen(Qt.red)
            painter.setBrush(QColor(255, 0, 0, 100))
            painter.drawRect(QRect(self.start_point, self.end_point))

    def get_selected_rect(self):
        return self.rect

if __name__ == "__main__":
    app = QApplication(sys.argv)
    selector = ScreenCapture()
    app.exec_()

    rect = selector.get_selected_rect()
    print(f"選択された矩形: {rect}")
