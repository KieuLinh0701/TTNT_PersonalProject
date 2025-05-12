import sys
import os
os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "0"
sys.setrecursionlimit(2000)
import time
from PyQt6 import QtWidgets, uic

from CheckSolvable import isSolvable

# import các thuật toán
from algorithms.BFS import bfs
from algorithms.DFS import dfs
from algorithms.UCS import ucs
from algorithms.IDS import ids
from algorithms.GreadySearch import greedy
from algorithms.AStar import aStar
from algorithms.IDA import idaStar
from algorithms.SimpleHillClimbing import simpleHillClimbing
from algorithms.SteepestAscentHillClimbing import steepestAscentHillClimbing
from algorithms.StochasticHillClimbing import stochasticHillClimbing
from algorithms.SimulatedAnnealing import simulatedAnnealing
from algorithms.BeamSearch import beamSearch
from algorithms.GeneticAlgorithm import geneticAlgorithm
from algorithms.AndOrSearch import AndOrSearch
from algorithms.SearchWithPartialObservation import searchWithPartialObservation
from algorithms.GenerateAndTest import generateAndTest
from algorithms.BackTracking import backtracking
from algorithms.BacktrackingWithForwardChecking import backtrackingWithForwardChecking
from algorithms.QLearning import qLearning

class PuzzleApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("puzzle.ui", self)
        # Đặt kích thước cố định từ thiết kế
        self.setFixedSize(self.width(), self.height())

        #self.startState = [[2, 6, 5], [0, 8, 7], [4, 3, 1]]
        #self.goalState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        
        #self.goalState = [[1, 2, 3], [4, 5, 6], [7, 0, 8]]

        #self.startState = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

        # Trạng thái test and or seach
        self.startState = [
            [1, 2, 3],
            [4, 0, 5],
            [7, 8, 6]
        ]
        self.goalState = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]
        ] 
        
        self.currentAlgorithm = None  # Thuật toán hiện tại (ban đầu là None)

        # Gán các nhãn
        self.grid_labels = [
            [self.findChild(QtWidgets.QLabel, f"lblSP_{i}_{j}") for j in range(3)]
            for i in range(3)
        ]
        self.origin_labels = [
            [self.findChild(QtWidgets.QLabel, f"lblOS_{i}_{j}") for j in range(3)]
            for i in range(3)
        ]
        self.target_labels = [
            [self.findChild(QtWidgets.QLabel, f"lblTS_{i}_{j}") for j in range(3)]
            for i in range(3)
        ]

        self.lblTime = self.findChild(QtWidgets.QLabel, "lblTime")
        self.lblSteps = self.findChild(QtWidgets.QLabel, "lblSteps")

        # Cập nhật trạng thái ban đầu
        self.updateLabels(self.origin_labels, self.startState)
        self.updateLabels(self.target_labels, self.goalState)
        self.updateLabels(self.grid_labels, self.startState)

        # Tạo danh sách nút và gán hành động
        self.buttons = {
            self.btnBFS: bfs,
            self.btnUCS: ucs,
            self.btnDFS: dfs,
            self.btnIDS: ids,
            self.btnGreedy: greedy,
            self.btnAStar: aStar,
            self.btnIDAStar: idaStar,
            self.btnSimpleHillClimbing: simpleHillClimbing,
            self.btnSteepestAscentHillClimbing: steepestAscentHillClimbing,
            self.btnStochasticHillClimbing: stochasticHillClimbing,
            self.btnSimulatedAnnealing:simulatedAnnealing,
            self.btnBeam:beamSearch,
            self.btnGenetic:geneticAlgorithm, 
            self.btnAndOr:AndOrSearch,
            self.btnComponent:searchWithPartialObservation,
            self.btnGenerateTest:generateAndTest,
            self.btnBackTracking:backtracking,
            self.btnBacktrackingWithForwardChecking: backtrackingWithForwardChecking,
            self.btnQLearning: qLearning
        }

        for btn, algo in self.buttons.items():
            btn.clicked.connect(lambda checked, a=algo, b=btn: self.runAlgorithm(a, b))

        # Kết nối nút btnProcess
        self.btnProcess.clicked.connect(self.showSteps)
        self.btnReset.clicked.connect(self.resetTimeStep)

    def updateLabels(self, labels, state, rows=None):
        if rows is None:
            rows = range(len(state))  # Mặc định cập nhật tất cả các hàng

        for index, i in enumerate(rows):  # Sử dụng `index` để lấy đúng dữ liệu từ `state`
            if i >= len(state):  # Đảm bảo chỉ số hàng hợp lệ
                continue
            
            for j in range(len(state[i])):  # Lặp qua từng phần tử trong hàng
                if j >= len(labels[i]):  # Đảm bảo chỉ số cột hợp lệ
                    continue
                
                val = state[index][j]  # Sử dụng `index` thay vì `i` để lấy đúng dữ liệu từ `state`
                if labels[i][j]:  # Nếu QLabel tồn tại
                    labels[i][j].setText("" if val == 0 else str(val))

    def resetTimeStep(self):
        # Reset giao diện về trạng thái ban đầu.\
        self.updateLabels(self.grid_labels, self.startState)

        # Reset giá trị thời gian và số bước
        self.lblTime.setText("0.00 s")  # Reset thời gian về giá trị mặc định
        self.lblSteps.setText("0")     # Reset bước về giá trị mặc định

    def reset(self, selectedButton):

        self.resetTimeStep()

        # Reset màu của tất cả các nút, trừ nút được chọn
        for btn in self.buttons.keys():
            if btn != selectedButton:
                btn.setStyleSheet("""
    QPushButton {
        background-color: #068251; /* Màu nền */
        color: white;             /* Màu chữ */
        border-radius: 12px;      /* Bo góc */
        padding: 5px;             /* Khoảng cách bên trong */
    }

    QPushButton:hover {
        background-color: #e5e6e7; /* Màu khi hover */
        color: black;
    }

    QPushButton:pressed {
        background-color: #575757; /* Màu khi bấm */
        color: black;
    }

    QPushButton:checked {
        background-color: #575757; /* Màu khi đã chọn */
        color: black;            /* Màu chữ khi chọn */
    }
""")
        QtWidgets.QApplication.processEvents()
    
    def showSteps(self):
        # Hiển thị các bước di chuyển
        if not hasattr(self, 'solutionSteps') or len(self.solutionSteps) <= 1:
            QtWidgets.QMessageBox.warning(self, "Warning", "No solution steps available!")
            return

        if self.currentAlgorithm == geneticAlgorithm:
            QtWidgets.QMessageBox.information(
                self,
                "Thông báo",
                "Thuật toán di truyền đã tìm ra lời giải, nhưng không có bước di chuyển cụ thể!"
            )
            return

        directions = []
        number_changes = []
        for i in range(len(self.solutionSteps) - 1):
            prev_state = self.solutionSteps[i]
            curr_state = self.solutionSteps[i + 1]

            # Tìm vị trí ô trống trong trạng thái trước và hiện tại
            zero_pos_prev = [(x, y) for x in range(3) for y in range(3) if prev_state[x][y] == 0][0]
            zero_pos_curr = [(x, y) for x in range(3) for y in range(3) if curr_state[x][y] == 0][0]

            # Xác định hướng di chuyển
            direction = None
            if zero_pos_curr[0] < zero_pos_prev[0]:  # Di chuyển lên
                direction = "Down"
            elif zero_pos_curr[0] > zero_pos_prev[0]:  # Di chuyển xuống
                direction = "Up"
            elif zero_pos_curr[1] < zero_pos_prev[1]:  # Di chuyển trái
                direction = "Right"
            elif zero_pos_curr[1] > zero_pos_prev[1]:  # Di chuyển phải
                direction = "Left"

            # Ghi lại số và hướng di chuyển
            if direction:
                # Lấy số tại vị trí di chuyển trong trạng thái trước
                moved_number = prev_state[zero_pos_curr[0]][zero_pos_curr[1]]
                directions.append(direction)
                number_changes.append(f"{moved_number} moves {direction}")

        if not number_changes:
            QtWidgets.QMessageBox.warning(self, "Warning", "No valid steps detected!")
            return

        # Tạo widget hiển thị các bước di chuyển
        steps_message = "\n".join(number_changes)
        message_widget = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(message_widget)

        # Tạo QLabel hiển thị thông điệp
        message_label = QtWidgets.QLabel(steps_message)
        message_label.setWordWrap(True)  # Tự động xuống dòng nếu quá dài
        layout.addWidget(message_label)

        # Tạo QScrollArea để cuộn nội dung nếu quá dài
        scroll_area = QtWidgets.QScrollArea()
        scroll_area.setWidget(message_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedSize(300, 400)  # Giới hạn chiều cao và chiều rộng

        # Tạo một QDialog để chứa QScrollArea
        dialog = QtWidgets.QDialog(self)
        dialog.setWindowTitle("Solution Steps")
        dialog_layout = QtWidgets.QVBoxLayout(dialog)
        dialog_layout.addWidget(scroll_area)

        # Nút OK để đóng hộp thoại
        ok_button = QtWidgets.QPushButton("OK")
        ok_button.clicked.connect(dialog.accept)
        dialog_layout.addWidget(ok_button)

        dialog.exec()

    def showMessage(self, title, message):
        QtWidgets.QMessageBox.information(self, title, message)

    def runAlgorithm(self, algorithm, button):
        # Chạy thuật toán giải quyết puzzle
        self.reset(button)  # Reset giao diện về trạng thái ban đầu
        self.currentAlgorithm = algorithm  # Lưu thuật toán hiện tại

        # Đổi màu nút đang được chọn
        button.setStyleSheet("""
        QPushButton {
            background-color: #e5e6e7; /* Màu nền */
            color: black;             /* Màu chữ */
            border-radius: 12px;      /* Bo góc */
            padding: 5px;             /* Khoảng cách bên trong */
        }

        QPushButton:hover {
            background-color: #e5e6e7; /* Màu khi hover */
            color: black;
        }

        QPushButton:pressed {
            background-color: #575757; /* Màu khi bấm */
            color: black;
        }

        QPushButton:checked {
            background-color: #575757; /* Màu khi đã chọn */
            color: black;            /* Màu chữ khi chọn */
        }
    """)

        if isSolvable(self.startState):
            solution = algorithm(self.startState, self.goalState)

            if solution:
                self.solutionSteps = [self.startState] + list(solution)  # Lưu tất cả trạng thái

                start_time = time.time()  # Bắt đầu tính thời gian

                for step in self.solutionSteps:
                    self.updateLabels(self.grid_labels, step)
                    QtWidgets.QApplication.processEvents()
                    time.sleep(0.3)

                end_time = time.time()  # Kết thúc tính thời gian
                
                self.lblTime.setText(f"{end_time - start_time:.2f} s")  # Hiển thị thời gian
                self.lblSteps.setText(str(len(solution)))  # Số bước là số lần di chuyển
            else:
                self.lblTime.setText("N/A")
                self.lblSteps.setText("0")
                self.showMessage("Notification", "Không tìm thấy lời giải")
        else:
            self.lblTime.setText("N/A")
            self.lblSteps.setText("N/A")
            self.showMessage("Notification", "Trạng thái không thể giải được.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = PuzzleApp()
    window.show()
    sys.exit(app.exec())