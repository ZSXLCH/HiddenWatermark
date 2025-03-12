from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox
import cv2
import DCT
import DFT
import json
import os
class EmbedWatermarkWindow(object):
    def __init__(self):
        # 初始化原图和水印图文件路径
        self.Original_image_file_name = ""
        self.Watermark_image_file_name = ""
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(879,780)#699, 646
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_2.sizePolicy().hasHeightForWidth())
        self.graphicsView_2.setSizePolicy(sizePolicy)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_3.addWidget(self.graphicsView_2)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_6.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.widget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView_3.sizePolicy().hasHeightForWidth())
        self.graphicsView_3.setSizePolicy(sizePolicy)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_7.addWidget(self.graphicsView_3)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.frame_7 = QtWidgets.QFrame(self.frame_4)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.radioButton = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout_8.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_7)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout_8.addWidget(self.radioButton_2)
        self.horizontalLayout_2.addWidget(self.frame_7)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.label_2)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphicsView.sizePolicy().hasHeightForWidth())
        self.graphicsView.setSizePolicy(sizePolicy)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_5.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "嵌入水印"))
        self.pushButton.setText(_translate("Form", "载入原图"))
        self.pushButton_2.setText(_translate("Form", "载入水印"))
        self.label.setText(_translate("Form", "嵌入方式"))
        self.radioButton.setText(_translate("Form", "离散余弦变换(DCT)"))
        self.radioButton_2.setText(_translate("Form", "离散傅里叶变换(DFT)"))
        self.pushButton_3.setText(_translate("Form", "嵌入水印"))
        self.label_2.setText(_translate("Form", "嵌入后的图片"))
        self.ConnectSlot() #槽函数连接
     #槽函数连接   
    def ConnectSlot(self):
        self.pushButton.clicked.connect(self.load_Original_image)
        self.pushButton_2.clicked.connect(self.load_Watermark_image)
        self.pushButton_3.clicked.connect(self.embed_watermark)
    def load_Original_image(self):
        # 打开文件对话框选择图片
        file_name, _ = QFileDialog.getOpenFileName(None, "选择原图", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        
        if file_name:
            # 存储原图文件路径
            self.Original_image_file_name = file_name
            # 加载图片并显示在graphicsView_2上
            pixmap = QtGui.QPixmap(file_name)
            
            # 创建 QGraphicsScene，并将图片添加到场景
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            
            # 设置 graphicsView_2 的场景
            self.graphicsView_2.setScene(scene)
            self.graphicsView_2.setRenderHint(QtGui.QPainter.Antialiasing)  # 可选，抗锯齿渲染
            
            # 调整视图，确保图片完全显示在 graphicsView_2 中，并保持原比例
            self.graphicsView_2.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
            self.graphicsView_2.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例
    def load_Watermark_image(self):
        # 打开文件对话框选择图片
        file_name, _ = QFileDialog.getOpenFileName(None, "选择水印", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        
        if file_name:
            # 存储水印文件路径
            self.Watermark_image_file_name = file_name
            # 加载图片并显示在 graphicsView_3 上
            pixmap = QtGui.QPixmap(file_name)
            
            
            # 创建 QGraphicsScene，并将图片添加到场景
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            
            # 设置 graphicsView_3 的场景
            self.graphicsView_3.setScene(scene)
            self.graphicsView_3.setRenderHint(QtGui.QPainter.Antialiasing)  # 可选，抗锯齿渲染
            
            # 调整视图，确保图片完全显示在 graphicsView_3 中，并保持原比例
            self.graphicsView_3.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
            self.graphicsView_3.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例

    def embed_watermark(self):
        # 检查是否选中了嵌入方式的单选框
        if not self.radioButton.isChecked() and not self.radioButton_2.isChecked():
            # 弹出对话框提醒用户选择嵌入方式
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先选择一种嵌入方式！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

        # 检查是否加载了原图和水印图
        if self.graphicsView_2.scene() is None or len(self.graphicsView_2.scene().items()) == 0:
            # 弹出对话框提醒用户加载原图
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先加载原图！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

        if self.graphicsView_3.scene() is None or len(self.graphicsView_3.scene().items()) == 0:
            # 弹出对话框提醒用户加载水印图
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("请先加载水印图！")
            msg.setWindowTitle("警告")
            msg.exec_()
            return

        # 获取保存文件路径
        save_file_name, _ = QFileDialog.getSaveFileName(None, "保存嵌入水印图", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        
        if save_file_name:  # 用户选择了保存路径
            # 获取原图和水印图
            original_pixmap = QtGui.QPixmap(self.Original_image_file_name)
            watermark_pixmap = QtGui.QPixmap(self.Watermark_image_file_name)

            # 根据选中的单选框执行相应操作
            if self.radioButton.isChecked():
                # DCT嵌入水印的代码
                print("选择了DCT嵌入方式")
                # 执行DCT嵌入操作的代码
                self.embed_watermark_dct(save_file_name)
            elif self.radioButton_2.isChecked():
                # DFT嵌入水印的代码
                print("选择了DFT嵌入方式")
                # 执行DFT嵌入操作的代码
                self.embed_watermark_dft(save_file_name)

        else:
            print("用户取消了保存操作")  # 用户点击取消，什么也不做


    def embed_watermark_dct(self, save_file_name):
        # 这里是DCT嵌入水印的实现，嵌入完后保存图像到 save_file_name
        print("DCT嵌入水印功能执行中...")
        # 第一步：更新进度条为 25%
        self.progressBar.setValue(25)
        
        # 调用 DCT 嵌入水印的逻辑
        rgb_synthesis, watermark_info = DCT.embed_watermark(self.Original_image_file_name, self.Watermark_image_file_name)
        
        # 第二步：更新进度条为 50%
        self.progressBar.setValue(50)
        
        # 将 RGB 图像转换为 BGR
        bgr_synthesis = cv2.cvtColor(rgb_synthesis, cv2.COLOR_RGB2BGR)
        
        # 第三步：更新进度条为 75%
        self.progressBar.setValue(75)
        
        # 保存嵌入水印后的图像
        cv2.imwrite(save_file_name, bgr_synthesis)
        print(f"水印已嵌入并保存到: {save_file_name}")
    # 保存 watermark_info 到 JSON 文件，位置和名字和图片相同
        if save_file_name:
            # 获取文件路径和文件名（去除扩展名）
            base_name, _ = os.path.splitext(save_file_name)
            
            # 设置保存的 JSON 文件路径
            json_file_name = base_name + '.json'
            
            # 将 watermark_info 写入 JSON 文件
            with open(json_file_name, 'w', encoding='utf-8') as json_file:
                json.dump(watermark_info, json_file, ensure_ascii=False, indent=4)
            print(f"水印信息已保存到: {json_file_name}")
        # 第四步：更新进度条为 100%
        self.progressBar.setValue(100)

        # 加载保存后的图像并显示在 graphicsView 中
        if save_file_name:
            # 加载水印后的图像文件
            pixmap = QtGui.QPixmap(save_file_name)
            
            # 创建 QGraphicsScene，并将图片添加到场景
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            
            # 设置 graphicsView 的场景
            self.graphicsView.setScene(scene)
            self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)  # 可选，抗锯齿渲染
            
            # 调整视图，确保图片完全显示在 graphicsView 中，并保持原比例
            self.graphicsView.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
            self.graphicsView.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例
            
            # 弹出成功提示框
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"水印已嵌入并保存到: {save_file_name}\n秘钥保存到: {json_file_name}")
            msg.setWindowTitle("成功")
            msg.exec_()


    def embed_watermark_dft(self, save_file_name):
        print("DFT嵌入水印功能执行中...")

        # 第一步：更新进度条为 25%
        self.progressBar.setValue(25)

        # 调用 DFT 嵌入水印的方法
        img_watermarked = DFT.embed_watermark(self.Original_image_file_name, self.Watermark_image_file_name)
        
        # 第二步：更新进度条为 50%
        self.progressBar.setValue(50)

        # 保存嵌入水印后的图像
        cv2.imwrite(save_file_name, img_watermarked)
        print(f"水印已嵌入并保存到: {save_file_name}")
        
        # 第三步：更新进度条为 75%
        self.progressBar.setValue(75)

        # 加载保存后的图像并显示在 graphicsView 中
        if save_file_name:
            # 加载水印后的图像文件
            pixmap = QtGui.QPixmap(save_file_name)
            # 第四步：更新进度条为 100%
            self.progressBar.setValue(100)
            # 创建 QGraphicsScene，并将图片添加到场景
            scene = QGraphicsScene()
            scene.addPixmap(pixmap)
            
            # 设置 graphicsView 的场景
            self.graphicsView.setScene(scene)
            self.graphicsView.setRenderHint(QtGui.QPainter.Antialiasing)  # 可选，抗锯齿渲染
            
            # 调整视图，确保图片完全显示在 graphicsView 中，并保持原比例
            self.graphicsView.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)  # 平滑处理图片
            self.graphicsView.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例



            # 弹出成功提示框
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText(f"水印已嵌入并保存到: {save_file_name}")
            msg.setWindowTitle("成功")
            msg.exec_()
