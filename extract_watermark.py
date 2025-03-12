from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import cv2
import DCT
import DFT
import json
class Extract_watermark(object):
    def __init__(self):
        super().__init__()
        self.file_loaded = False  # 初始化加载状态
        self.img_with_watermark_file_name = ""  # 初始化为空字符串
        self.key_file_name=""
        self.original_image_file_name=""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(857*1.35, 576/1.1)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.frame_6 = QtWidgets.QFrame(self.frame_5)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_3.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_6)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_3.addWidget(self.radioButton_2)
        self.horizontalLayout_3.addWidget(self.frame_6)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.verticalLayout_5.addWidget(self.frame_5)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_5.addWidget(self.pushButton_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem4)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.frame_31 = QtWidgets.QFrame(self.widget)
        self.frame_31.setObjectName("frame_31")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_31)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.frame_31)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem6)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_4.addWidget(self.graphicsView_3)
        self.progressBar = QtWidgets.QProgressBar(self.frame_31)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_4.addItem(spacerItem7)
        self.horizontalLayout_2.addWidget(self.frame_31)
        self.horizontalLayout.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "提取水印"))
        self.pushButton.setText(_translate("Form", "读取含水印图片"))
        self.label_2.setText(_translate("Form", "嵌入方式"))
        self.radioButton.setText(_translate("Form", "DCT"))
        self.radioButton_2.setText(_translate("Form", "DFT"))
        self.pushButton_2.setText(_translate("Form", "载入密钥"))
        self.pushButton_3.setText(_translate("Form", "提取水印"))
        self.label.setText(_translate("Form", "提取的水印"))
        self.ConnectSlot()
    #槽函数连接   
    def ConnectSlot(self):
        self.pushButton.clicked.connect(self.load_img_with_watermark)
        self.radioButton.toggled.connect(self.update_button_text)  # 监听 DCT 单选框
        self.radioButton_2.toggled.connect(self.update_button_text)  # 监听 DFT 单选框
        self.pushButton_2.clicked.connect(self.load_key_or_image)  # 连接载入按钮的槽函数
        self.pushButton_3.clicked.connect(self.extract_watermark)

    def load_img_with_watermark(self):
            # 打开文件对话框选择图片
            file_name, _ = QFileDialog.getOpenFileName(None, "选择带水印图片", "", "Images (*.png *.jpg *.bmp *.jpeg)")
            
            if file_name:
                # 存储带水印图片文件路径
                self.img_with_watermark_file_name = file_name
                # 加载图片并显示在graphicsView上
                pixmap = QtGui.QPixmap(file_name)
                
                # 创建 QGraphicsScene，并将图片添加到场景
                scene = QGraphicsScene()
                scene.addPixmap(pixmap)
                
                # 设置 graphicsView 的场景
                self.graphicsView.setScene(scene)
                self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)  # 可选，抗锯齿渲染
                # 调整视图，确保图片完全显示在 graphicsView 中，并保持原比例
                self.graphicsView.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
                self.graphicsView.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例
    def update_button_text(self):
        if self.radioButton.isChecked():  # 选择了 DCT
            self.pushButton_2.setText("载入密钥")
        elif self.radioButton_2.isChecked():  # 选择了 DFT
            self.pushButton_2.setText("载入原图")
    def load_key_or_image(self):
        # 根据选择的嵌入方式，执行不同的操作
        if self.radioButton.isChecked():  # 选择了 DCT
            self.load_key()  # 加载密钥
        elif self.radioButton_2.isChecked():  # 选择了 DFT
            self.load_original_image()  # 加载原图
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先选择嵌入方式！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

    def load_key(self):
        # 载入密钥的代码
        file_name, _ = QFileDialog.getOpenFileName(None, "选择密钥", "", "JSON Files (*.json)")
        if file_name:
            try:
                with open(file_name, 'r') as json_file:
                    self.key_data = json.load(json_file)  # 加载 JSON 文件内容
                self.key_file_name = file_name
                
                # 更新按钮文本
                self.pushButton_2.setText("已载入密钥")
                # 设置加载状态为 True
                self.file_loaded = True
            except Exception as e:
                self.pushButton_2.setText("载入密钥失败")
                self.file_loaded = False  # 如果加载失败，状态为 False
        else:
            self.pushButton_2.setText("载入密钥失败")
            self.file_loaded = False  # 如果文件选择取消，状态为 False

    def load_original_image(self):
        # 载入原图的代码
        file_name, _ = QFileDialog.getOpenFileName(None, "选择原图", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        if file_name:
            self.original_image_file_name = file_name
            # 更新按钮文本
            self.pushButton_2.setText("已载入原图")
            # 设置加载状态为 True
            self.file_loaded = True
        else:
            self.pushButton_2.setText("载入原图失败")
            self.file_loaded = False  # 如果加载失败，状态为 False
    def extract_watermark(self):
        # 判断是否载入含水印的图片
        if not self.img_with_watermark_file_name:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先载入含水印的图片！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

        # 判断文件是否载入成功
        if not self.file_loaded:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先选择嵌入方式并载入相关文件")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

        # 根据选择的嵌入方式执行提取水印操作
        if self.radioButton.isChecked():  # 选择了 DCT
            self.extract_watermark_with_dct()  # DCT 提取水印函数
        elif self.radioButton_2.isChecked():  # 选择了 DFT
            self.extract_watermark_with_dft()  # DFT 提取水印函数
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先选择嵌入方式！")
            msg.setWindowTitle("警告")
            msg.exec_()
    def display_extracted_watermark(self, extracted_watermark):
        # 将提取的水印图像转换为QImage格式
        extracted_watermark_rgb = cv2.cvtColor(extracted_watermark, cv2.COLOR_BGR2RGB)
        height, width, channels = extracted_watermark_rgb.shape
        bytes_per_line = channels * width
        qimage = QImage(extracted_watermark_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # 将QImage转换为QPixmap
        pixmap = QPixmap.fromImage(qimage)
        # 创建一个QGraphicsScene，并将图像显示在graphicsView_3中
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView_3.setScene(scene)
        # 调整视图，确保图片完全显示在 graphicsView 中，并保持原比例
        self.graphicsView_3.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
        self.graphicsView_3.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例

    def display_extracted_watermark_dft(self, extracted_watermark):
        # 将提取的水印图像转换为QImage格式
        extracted_watermark = cv2.convertScaleAbs(extracted_watermark)
        extracted_watermark_rgb = cv2.cvtColor(extracted_watermark, cv2.COLOR_BGR2RGB)
        height, width, channels = extracted_watermark_rgb.shape
        bytes_per_line = channels * width
        qimage = QImage(extracted_watermark_rgb.data, width, height, bytes_per_line, QImage.Format_RGB888)

        # 将QImage转换为QPixmap
        pixmap = QPixmap.fromImage(qimage)
        # 创建一个QGraphicsScene，并将图像显示在graphicsView_3中
        scene = QGraphicsScene()
        scene.addPixmap(pixmap)
        self.graphicsView_3.setScene(scene)
        # 调整视图，确保图片完全显示在 graphicsView 中，并保持原比例
         # DFT提取的水印不全屏显示显示异常,必须全屏显示才正常，原因未知
        self.graphicsView_3.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)   # 平滑处理图片
        self.graphicsView_3.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例

    def extract_watermark_with_dct(self):
        # 检查是否已载入秘钥
        if not self.key_file_name:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请载入秘钥！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return  # 如果没有载入秘钥，直接返回

        # 使用 DCT 提取水印的代码逻辑
        print("使用 DCT 提取水印")
        # 弹出保存文件框，选择保存路径和文件名
        save_path, _ = QFileDialog.getSaveFileName(None, "保存提取的水印", "", "PNG Image (*.png);;All Files (*)")
        # 如果用户点击取消按钮，save_path将是空字符串，直接返回
        if not save_path:
            return  # 用户取消选择文件，退出操作
        # 调用 DCT 提取水印的函数
        self.progressBar.setValue(25)
        extract_watermark = DCT.extract_watermark(self.img_with_watermark_file_name, self.key_file_name)
        # 保存提取的水印图像
        self.progressBar.setValue(50)
        cv2.imwrite(save_path, extract_watermark)
        self.progressBar.setValue(100)
        # 显示提取的水印图像到QGraphicsView
        self.display_extracted_watermark(extract_watermark)

    def extract_watermark_with_dft(self):
        if not self.original_image_file_name:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请载入原图！")
            msg.setWindowTitle("警告")
            msg.exec_() 
        # 这里是 DFT 提取水印的代码逻辑
        print("使用 DFT 提取水印")

         # 弹出保存文件框，选择保存路径和文件名
        save_path, _ = QFileDialog.getSaveFileName(None, "保存提取的水印", "", "PNG Image (*.png);;All Files (*)")
        # 如果用户点击取消按钮，save_path将是空字符串，直接返回
        if not save_path:
            return  # 用户取消选择文件，退出操作
        # 调用 DFT 提取水印的函数
        self.progressBar.setValue(25)
        extract_watermark = DFT.extract_watermark(self.original_image_file_name,self.img_with_watermark_file_name)
        # 保存提取的水印图像
        self.progressBar.setValue(50)
        cv2.imwrite(save_path, extract_watermark)
        self.progressBar.setValue(100)
        # 显示提取的水印图像到QGraphicsView
        #extract_watermark = cv2.imread(save_path)
        
        self.display_extracted_watermark_dft(extract_watermark)

if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Extract_watermark()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
