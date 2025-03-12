from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QGraphicsScene, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np
import DCT
import DFT
from PyQt5.QtWidgets import QButtonGroup
from PIL import Image
class AttackTesting(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(743*1.3, 609)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.graphicsView = QtWidgets.QGraphicsView(self.frame_4)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_8.addWidget(self.graphicsView)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_8.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.frame_5)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_7.addWidget(self.graphicsView_2)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.frame_14 = QtWidgets.QFrame(self.frame_3)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_14)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.frame_17 = QtWidgets.QFrame(self.frame_14)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_17)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.radioButton_10 = QtWidgets.QRadioButton(self.frame_17)
        self.radioButton_10.setObjectName("radioButton_10")
        self.verticalLayout_10.addWidget(self.radioButton_10)
        self.radioButton_11 = QtWidgets.QRadioButton(self.frame_17)
        self.radioButton_11.setObjectName("radioButton_11")
        self.verticalLayout_10.addWidget(self.radioButton_11)
        self.horizontalLayout_7.addWidget(self.frame_17)
        self.verticalLayout_3.addWidget(self.frame_14)
        self.frame_8 = QtWidgets.QFrame(self.frame_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_8)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_4.addItem(spacerItem1)
        self.frame_13 = QtWidgets.QFrame(self.frame_8)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_2.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_13)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_2.addWidget(self.radioButton_2)
        self.verticalLayout_4.addWidget(self.frame_13)
        self.frame_9 = QtWidgets.QFrame(self.frame_8)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_3.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_9)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_3.addWidget(self.radioButton_4)
        self.verticalLayout_4.addWidget(self.frame_9)
        self.frame_12 = QtWidgets.QFrame(self.frame_8)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_4.addWidget(self.radioButton_5)
        self.radioButton_6 = QtWidgets.QRadioButton(self.frame_12)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_4.addWidget(self.radioButton_6)
        self.verticalLayout_4.addWidget(self.frame_12)
        self.frame_10 = QtWidgets.QFrame(self.frame_8)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton_7 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_5.addWidget(self.radioButton_7)
        self.radioButton_8 = QtWidgets.QRadioButton(self.frame_10)
        self.radioButton_8.setObjectName("radioButton_8")
        self.horizontalLayout_5.addWidget(self.radioButton_8)
        self.verticalLayout_4.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_8)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_9 = QtWidgets.QRadioButton(self.frame_11)
        self.radioButton_9.setObjectName("radioButton_9")
        self.horizontalLayout_6.addWidget(self.radioButton_9)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.verticalLayout_3.addWidget(self.frame_8)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.frame_2)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.graphicsView_3 = QtWidgets.QGraphicsView(self.frame_6)
        self.graphicsView_3.setObjectName("graphicsView_3")
        self.verticalLayout_6.addWidget(self.graphicsView_3)
        self.verticalLayout_2.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_7)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.graphicsView_4 = QtWidgets.QGraphicsView(self.frame_7)
        self.graphicsView_4.setObjectName("graphicsView_4")
        self.verticalLayout_5.addWidget(self.graphicsView_4)
        self.verticalLayout_2.addWidget(self.frame_7)
        self.horizontalLayout.addWidget(self.frame_2)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.group = QButtonGroup()
        self.group.addButton(self.radioButton)
        self.group.addButton(self.radioButton_2)
        self.group.addButton(self.radioButton_3)
        self.group.addButton(self.radioButton_4)
        self.group.addButton(self.radioButton_5)
        self.group.addButton(self.radioButton_6)
        self.group.addButton(self.radioButton_7)
        self.group.addButton(self.radioButton_8)
        self.group.addButton(self.radioButton_9)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "攻击测试"))
        self.pushButton.setText(_translate("Form", "载入原图"))
        self.pushButton_2.setText(_translate("Form", "载入水印"))
        self.pushButton_3.setText(_translate("Form", "攻击并提取水印"))
        self.label_4.setText(_translate("Form", "嵌入方式"))
        self.radioButton_10.setText(_translate("Form", "DCT"))
        self.radioButton_11.setText(_translate("Form", "DFT"))
        self.label.setText(_translate("Form", "攻击方式"))
        self.radioButton.setText(_translate("Form", "不攻击"))
        self.radioButton_2.setText(_translate("Form", "剪切"))
        self.radioButton_3.setText(_translate("Form", "平移"))
        self.radioButton_4.setText(_translate("Form", " 椒盐噪声"))
        self.radioButton_5.setText(_translate("Form", "泊松噪声"))
        self.radioButton_6.setText(_translate("Form", "均值滤波"))
        self.radioButton_7.setText(_translate("Form", "中值滤波"))
        self.radioButton_8.setText(_translate("Form", "高斯滤波"))
        self.radioButton_9.setText(_translate("Form", "双边滤波"))
        self.label_2.setText(_translate("Form", "水印嵌入与攻击处理后的图片"))
        self.label_3.setText(_translate("Form", "提取的水印"))
        self.ConnectSlot()

            
    #槽函数连接   
    def ConnectSlot(self):
        self.pushButton.clicked.connect(self.load_Original_image)
        self.pushButton_2.clicked.connect(self.load_Watermark_image)
        self.pushButton_3.clicked.connect(self.attack_and_extract_watermark)
    def load_Original_image(self):
        # 打开文件对话框选择图片
        file_name, _ = QFileDialog.getOpenFileName(None, "选择原图", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        
        if file_name:
            # 存储原图文件路径
            self.Original_image_file_name = file_name
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
    def load_Watermark_image(self):
        # 打开文件对话框选择图片
        file_name, _ = QFileDialog.getOpenFileName(None, "选择水印", "", "Images (*.png *.jpg *.bmp *.jpeg)")
        
        if file_name:
            # 存储水印文件路径
            self.Watermark_image_file_name = file_name
            # 加载图片并显示在 graphicsView_2 上
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

        

    def attack_and_extract_watermark(self):
        # 检查原图和水印文件是否已加载
        if not hasattr(self, 'Original_image_file_name') or not self.Original_image_file_name:
            QMessageBox.warning(None, "警告", "请先加载原图")
            return
        
        if not hasattr(self, 'Watermark_image_file_name') or not self.Watermark_image_file_name:
            QMessageBox.warning(None, "警告", "请先加载水印")
            return

        # 检查嵌入方式是否选择
        selected_embedding_method = None
        if self.radioButton_10.isChecked():
            selected_embedding_method = 'DCT'
        elif self.radioButton_11.isChecked():
            selected_embedding_method = 'DFT'
        
        if not selected_embedding_method:
            QMessageBox.warning(None, "警告", "请选择嵌入方式（DCT 或 DFT）")
            return
        
        # 检查攻击方式是否选择
        selected_attack_method = None
        if self.radioButton.isChecked():
            selected_attack_method = '不攻击'
        elif self.radioButton_2.isChecked():
            selected_attack_method = '剪切'
        elif self.radioButton_3.isChecked():
            selected_attack_method = '平移'
        elif self.radioButton_4.isChecked():
            selected_attack_method = '椒盐噪声'
        elif self.radioButton_5.isChecked():
            selected_attack_method = '泊松噪声'
        elif self.radioButton_6.isChecked():
            selected_attack_method = '均值滤波'
        elif self.radioButton_7.isChecked():
            selected_attack_method = '中值滤波'
        elif self.radioButton_8.isChecked():
            selected_attack_method = '高斯滤波'
        elif self.radioButton_9.isChecked():
            selected_attack_method = '双边滤波'
        
        if not selected_attack_method:
            QMessageBox.warning(None, "警告", "请选择攻击方式")
            return

        # 这里可以根据选择的嵌入方式进行不同的处理
        if selected_embedding_method == 'DCT':
            # 调用DCT嵌入方式相关的函数
            self.embed_watermark_dct()
        elif selected_embedding_method == 'DFT':
            # 调用DFT嵌入方式相关的函数
            self.embed_watermark_dft()

    def embed_watermark_dct(self):
        rgb_synthesis, dct_emb = DCT.embed_watermark_Attack(self.Original_image_file_name, self.Watermark_image_file_name)
        # 转bgr通道
        bgr_synthesis = cv2.cvtColor(rgb_synthesis, cv2.COLOR_RGB2BGR)
        
        # 获取攻击方式
        selected_attack_method = None
        if self.radioButton.isChecked():
            selected_attack_method = '不攻击'
        elif self.radioButton_2.isChecked():
            selected_attack_method = '剪切'
        elif self.radioButton_3.isChecked():
            selected_attack_method = '平移'
        elif self.radioButton_4.isChecked():
            selected_attack_method = '椒盐噪声'
        elif self.radioButton_5.isChecked():
            selected_attack_method = '泊松噪声'
        elif self.radioButton_6.isChecked():
            selected_attack_method = '均值滤波'
        elif self.radioButton_7.isChecked():
            selected_attack_method = '中值滤波'
        elif self.radioButton_8.isChecked():
            selected_attack_method = '高斯滤波'
        elif self.radioButton_9.isChecked():
            selected_attack_method = '双边滤波'
        
        # 根据 selected_attack_method 选择攻击方式
        if selected_attack_method == '不攻击':
            pass  # 不做任何处理
        elif selected_attack_method == '剪切':
            bgr_synthesis = self.add_crop_attack(bgr_synthesis)
        elif selected_attack_method == '平移':
            dct_emb.block_size
            bgr_synthesis = self.add_translation_attack(bgr_synthesis,dct_emb.block_size*25,dct_emb.block_size*25)
            #bgr_synthesis = self.add_translation_attack(bgr_synthesis,200,200)
        elif selected_attack_method == '椒盐噪声':
            bgr_synthesis = self.add_salt_and_pepper_noise(bgr_synthesis)
        elif selected_attack_method == '泊松噪声':
            bgr_synthesis = self.add_poisson_noise_batch(bgr_synthesis)
        elif selected_attack_method == '均值滤波':
            bgr_synthesis = self.add_average_filter(bgr_synthesis)
        elif selected_attack_method == '中值滤波':
            bgr_synthesis = self.add_median_filter(bgr_synthesis)
        elif selected_attack_method == '高斯滤波':
            bgr_synthesis = self.add_gaussian_filter(bgr_synthesis)
        elif selected_attack_method == '双边滤波':
            bgr_synthesis = self.add_bilateral_filter(bgr_synthesis)
        rgb_synthesis = cv2.cvtColor(bgr_synthesis, cv2.COLOR_BGR2RGB)#转回RGB
        # 提取水印
        extracted_watermark = DCT.extract_watermark_Attack(rgb_synthesis, dct_emb)
        
        # 将水印嵌入与攻击处理后的图像转换为QImage格式

        height, width, channels = rgb_synthesis.shape
        bytes_per_line = channels * width
        qimage = QImage(rgb_synthesis.data, width, height, bytes_per_line, QImage.Format_RGB888)

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
        self.display_extracted_watermark(extracted_watermark)

    def embed_watermark_dft(self):
        bgr_synthesis=DFT.embed_watermark(self.Original_image_file_name,self.Watermark_image_file_name)
        # 获取攻击方式
        selected_attack_method = None
        if self.radioButton.isChecked():
            selected_attack_method = '不攻击'
        elif self.radioButton_2.isChecked():
            selected_attack_method = '剪切'
        elif self.radioButton_3.isChecked():
            selected_attack_method = '平移'
        elif self.radioButton_4.isChecked():
            selected_attack_method = '椒盐噪声'
        elif self.radioButton_5.isChecked():
            selected_attack_method = '泊松噪声'
        elif self.radioButton_6.isChecked():
            selected_attack_method = '均值滤波'
        elif self.radioButton_7.isChecked():
            selected_attack_method = '中值滤波'
        elif self.radioButton_8.isChecked():
            selected_attack_method = '高斯滤波'
        elif self.radioButton_9.isChecked():
            selected_attack_method = '双边滤波'
        
        # 根据 selected_attack_method 选择攻击方式
        if selected_attack_method == '不攻击':
            pass  # 不做任何处理
        elif selected_attack_method == '剪切':
            bgr_synthesis = self.add_crop_attack(bgr_synthesis)
        elif selected_attack_method == '平移':
            bgr_synthesis = self.add_translation_attack(bgr_synthesis,200,200)
        elif selected_attack_method == '椒盐噪声':
            bgr_synthesis = self.add_salt_and_pepper_noise(bgr_synthesis)
        elif selected_attack_method == '泊松噪声':
            bgr_synthesis = self.add_poisson_noise_batch(bgr_synthesis)
        elif selected_attack_method == '均值滤波':
            bgr_synthesis = self.add_average_filter(bgr_synthesis)
        elif selected_attack_method == '中值滤波':
            bgr_synthesis = self.add_median_filter(bgr_synthesis)
        elif selected_attack_method == '高斯滤波':
            bgr_synthesis = self.add_gaussian_filter(bgr_synthesis)
        elif selected_attack_method == '双边滤波':
            bgr_synthesis = self.add_bilateral_filter(bgr_synthesis)
        extracted_watermark=DFT.extract_watermark_attack(self.Original_image_file_name,bgr_synthesis)
        
        rgb_synthesis=cv2.cvtColor(bgr_synthesis, cv2.COLOR_BGR2RGB)
        height, width, channels = rgb_synthesis.shape
        bytes_per_line = channels * width
        qimage = QImage(rgb_synthesis.data, width, height, bytes_per_line, QImage.Format_RGB888)

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
        self.display_extracted_watermark(extracted_watermark)
    
    # 攻击方法
    def add_crop_attack(self, image):#剪切
        # 将OpenCV的BGR格式图像转换为PIL的Image格式
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # 定义剪切区域，格式为 (左, 上, 右, 下)，可以根据需要调整
        box = (50, 50, 500, 500)  # 例如，剪切从(50, 50)到(250, 250)的区域

        # 剪切指定区域
        cropped = pil_image.crop(box)

        # 创建一个与剪切区域大小相同的全黑图像
        black_image = Image.new('RGB', cropped.size, color='black')

        # 将全黑图像粘贴到原图像的剪切位置
        pil_image.paste(black_image, box)

        # 将修改后的PIL图像转换回OpenCV格式
        modified_image = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)
        
        return modified_image
    def add_translation_attack(self, image, dx, dy):#平移
        # 将OpenCV的BGR格式图像转换为PIL的Image格式
        pil_image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        
        # 获取图像的宽度和高度
        width, height = pil_image.size
        
        # 创建一个新的黑色背景图像，大小与原图像相同
        new_image = Image.new('RGB', (width, height), color='black')
        
        # 粘贴平移后的图像到新图像上
        new_image.paste(pil_image, (dx,dy))
        
        # 将修改后的PIL图像转换回OpenCV格式
        modified_image = cv2.cvtColor(np.array(new_image), cv2.COLOR_RGB2BGR)
        
        return modified_image
    def add_salt_and_pepper_noise(self, image):
        row, col, _ = image.shape
        s_vs_p = 0.02
        amount = 0.02
        out = np.copy(image)
        noisy = np.random.choice([0, 1], size=(row, col), p=[1 - s_vs_p, s_vs_p])
        out[noisy == 1] = 255
        return out

 

    def add_poisson_noise_batch(self, image, batch_size=256):
        # 将图像分成块处理
        height, width, channels = image.shape
        noisy_image = np.copy(image)
        
        # 遍历图像的块
        for i in range(0, height, batch_size):
            for j in range(0, width, batch_size):
                batch = noisy_image[i:i+batch_size, j:j+batch_size]
                # 归一化并添加噪声
                batch_float = np.float32(batch)
                normalized_batch = np.clip(batch_float / 255.0, 0, 1)
                noisy_batch = np.random.poisson(normalized_batch * 255)
                # 限制像素值范围
                noisy_batch = np.clip(noisy_batch, 0, 255).astype(np.uint8)
                # 替换原图像中的对应块
                noisy_image[i:i+batch_size, j:j+batch_size] = noisy_batch

        return noisy_image

    def add_average_filter(self, image):
        return cv2.blur(image, (5, 5))  # 5x5均值滤波

    def add_median_filter(self, image):
        return cv2.medianBlur(image, 5)  # 5x5中值滤波

    def add_gaussian_filter(self, image):
        return cv2.GaussianBlur(image, (5, 5), 0)  # 5x5高斯滤波

    def add_bilateral_filter(self, image):
        return cv2.bilateralFilter(image, 9, 75, 75)  # 双边滤波

    def display_extracted_watermark (self,extracted_watermark):
        # 将提取的水印图像转换为QImage格式
        #cv2.cvtColor函数通常期望的是CV_8U,确保图像的深度为CV_8U类型
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
        self.graphicsView_4.setScene(scene)
        # 调整视图，确保图片完全显示在 graphicsView_4 中，并保持原比例
         # DFT提取的水印不全屏显示显示异常,必须全屏显示才正常，原因未知
        self.graphicsView_4.setRenderHint(QtGui.QPainter.SmoothPixmapTransform)   # 平滑处理图片
        self.graphicsView_4.fitInView(scene.itemsBoundingRect(), QtCore.Qt.KeepAspectRatio)  # 保持比例
if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = AttackTesting()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
