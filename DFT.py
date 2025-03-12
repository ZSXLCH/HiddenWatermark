import cv2
import numpy as np
def embed_watermark(ori_image_path, watermark_path, alpha=0.01):
    # 读取原始图像和彩色水印图像
    image = cv2.imread(ori_image_path)
    watermark = cv2.imread(watermark_path, cv2.IMREAD_GRAYSCALE)
    # 将水印图像转为二值图像
    _, watermark = cv2.threshold(watermark, 127, 255, cv2.THRESH_BINARY)
    # 将图像转换到YCbCr色彩空间
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
    u_channel = ycbcr_image[:, :, 1]  # 提取U通道
    # 将水印图像缩放到和U通道一样的大小
    watermark = cv2.resize(watermark, (u_channel.shape[1], u_channel.shape[0]))
    # 对U通道进行傅里叶变换
    f_image = np.fft.fft2(u_channel)
    f_image_shifted = np.fft.fftshift(f_image)
    f_watermark = np.fft.fft2(watermark)
    # 嵌入水印
    f_image_shifted += alpha * f_watermark
    # 将嵌入水印后的频域表示转换回空间域
    f_ishift = np.fft.ifftshift(f_image_shifted)
    img_back = np.fft.ifft2(f_ishift)
    img_back = np.abs(img_back)

    # 将嵌入水印后的图像重新转换回BGR
    ycbcr_image[:, :, 1] = img_back  # 将修改后的U通道放回
    img_watermarked = cv2.cvtColor(ycbcr_image, cv2.COLOR_YCrCb2BGR)
    
    # 保存嵌入水印后的图片
    #cv2.imwrite('watermarked_image_u_channel.png', img_watermarked)

    return img_watermarked

def extract_watermark(ori_image_path, img_path, alpha=0.01):
    # 读取原始图像和嵌入水印后的图像
    original_image = cv2.imread(ori_image_path)
    watermarked_image = cv2.imread(img_path)
    
    # 将图像转换到YCbCr色彩空间
    original_ycbcr = cv2.cvtColor(original_image, cv2.COLOR_BGR2YCrCb)
    watermarked_ycbcr = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2YCrCb)
    
    original_u_channel = original_ycbcr[:, :, 1]  # 提取U通道
    watermarked_u_channel = watermarked_ycbcr[:, :, 1]  # 提取嵌入水印后的U通道
    
    # 对U通道进行傅里叶变换
    f_original = np.fft.fft2(original_u_channel)
    f_watermarked = np.fft.fft2(watermarked_u_channel)
    
    # 移动频谱中心
    f_original_shifted = np.fft.fftshift(f_original)
    f_watermarked_shifted = np.fft.fftshift(f_watermarked)
    
    # 提取水印的频域差值
    f_extracted = (f_watermarked_shifted - f_original_shifted) / alpha
    # 逆傅里叶变换恢复水印
    watermark_extracted = np.fft.ifft2(np.fft.ifftshift(f_extracted))
    watermark_extracted = np.abs(watermark_extracted)
    # 显示提取出的水印
    #plt.figure(figsize=(8, 6))
    #plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('原图')
    #plt.subplot(122), plt.imshow(watermark_extracted, cmap='gray'), plt.title('提取出的水印')
    #plt.show()
    # 保存提取出的水印图像
    #cv2.imwrite('extracted_watermark.png', watermark_extracted)

    return watermark_extracted
#攻击测试时候用
def extract_watermark_attack(ori_image_path, watermarked_image, alpha=0.01):
    # 读取原始图像和嵌入水印后的图像
    original_image = cv2.imread(ori_image_path)
    # 将图像转换到YCbCr色彩空间
    original_ycbcr = cv2.cvtColor(original_image, cv2.COLOR_BGR2YCrCb)
    watermarked_ycbcr = cv2.cvtColor(watermarked_image, cv2.COLOR_BGR2YCrCb)
    
    original_u_channel = original_ycbcr[:, :, 1]  # 提取U通道
    watermarked_u_channel = watermarked_ycbcr[:, :, 1]  # 提取嵌入水印后的U通道
    
    # 对U通道进行傅里叶变换
    f_original = np.fft.fft2(original_u_channel)
    f_watermarked = np.fft.fft2(watermarked_u_channel)
    
    # 移动频谱中心
    f_original_shifted = np.fft.fftshift(f_original)
    f_watermarked_shifted = np.fft.fftshift(f_watermarked)
    
    # 提取水印的频域差值
    f_extracted = (f_watermarked_shifted - f_original_shifted) / alpha
    # 逆傅里叶变换恢复水印
    watermark_extracted = np.fft.ifft2(np.fft.ifftshift(f_extracted))
    watermark_extracted = np.abs(watermark_extracted)
    # 显示提取出的水印
    #plt.figure(figsize=(8, 6))
    #plt.subplot(121), plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)), plt.title('原图')
    #plt.subplot(122), plt.imshow(watermark_extracted, cmap='gray'), plt.title('提取出的水印')
    #plt.show()
    # 保存提取出的水印图像
    #cv2.imwrite('extracted_watermark.png', watermark_extracted)

    return watermark_extracted
if __name__ == "__main__":
    img_watermarked = embed_watermark('2.png', 'w.png', alpha=0.1)
    extracted_watermark = extract_watermark('2.png', 'watermarked_image_u_channel.png', alpha=0.1)
