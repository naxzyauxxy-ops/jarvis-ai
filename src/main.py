import sys
import os
import threading
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QColor

# Local module imports
from memory import MemoryMonitor
from bridge import TelegramBridge
from orchestrator import Orchestrator

class JarvisUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.start_systems()

    def init_ui(self):
        """Initializes the 'Always-on-Top' Glass-Card UI."""
        self.setWindowTitle("Universal JARVIS")
        self.setFixedSize(300, 450)
        
        # Window Flags: Frameless, Always on Top
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # Central Widget & Layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()
        
        # Arc Reactor Visualization (Placeholder Label)
        self.status_label = QLabel("JARVIS: STANDBY")
        self.status_label.setStyleSheet("color: #00d4ff; font-family: 'Segoe UI'; font-size: 18px; font-weight: bold;")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.layout.addWidget(self.status_label)
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

        # Apply CSS for Glass-Card Effect
        self.setStyleSheet("""
            QWidget {
                background-color: rgba(20, 20, 25, 200);
                border: 1px solid rgba(0, 212, 255, 100);
                border-radius: 15px;
            }
        """)

    def start_systems(self):
        """Launches background automation and monitors."""
        # 1. Start Memory Monitor (8GB Optimization)
        self.monitor = MemoryMonitor(threshold=75)
        self.monitor.start()
        
        # 2. Start Mobile Gateway (Telegram)
        self.bridge = TelegramBridge()
        self.bridge.launch()
        
        # 3. Initialize Orchestrator
        self.orchestrator = Orchestrator()
        
        print("[System] All modules online. Welcome home, Sir.")
        self.status_label.setText("JARVIS: ACTIVE")

    def mousePressEvent(self, event):
        """Enables dragging the frameless window."""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()

    def mouseMoveEvent(self, event):
        """Enables dragging the frameless window."""
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JarvisUI()
    window.show()
    sys.exit(app.exec())
