import cv2
import numpy as np
from PIL import Image
import json
class DCT_Embed(object):
    def __init__(self, background, watermark, block_size,alpha,k1,k2):
        b_h, b_w = background.shape[:2]
        w_h, w_w = watermark.shape[:2]
        assert w_h <= b_h / block_size and w_w <= b_w / block_size, \
            "\r\n请确保您的的水印图像尺寸 不大于 背景图像尺寸的1/{:}\r\nbackground尺寸{:}\r\nwatermark尺寸{:}".format(
                block_size, background.shape, watermark.shape
            )
        self.watermark_size=watermark.shape #!!!攻击测试用到
        # 保存参数
        self.block_size = block_size
        # 水印强度控制
        self.alpha = alpha
        self.k1 =k1
        self.k2 =k2
        #self.k1 = np.random.randn(block_size)
        #self.k2 = np.random.randn(block_size)

    def dct_blkproc(self, background):
        """
        对background进行分块，然后进行dct变换，得到dct变换后的矩阵

        :param image: 输入图像
        :param split_w: 分割的每个patch的w
        :param split_h: 分割的每个patch的h
        :return: 经dct变换的分块矩阵、原始的分块矩阵
        """
        background_dct_blocks_h = background.shape[0] // self.block_size  # 高度
        background_dct_blocks_w = background.shape[1] // self.block_size  # 宽度
        background_dct_blocks = np.zeros(shape=(
            (background_dct_blocks_h, background_dct_blocks_w, self.block_size, self.block_size)
        ))  # 前2个维度用来遍历所有block，后2个维度用来存储每个block的DCT变换的值

     
        h_data = np.vsplit(background, background_dct_blocks_h)  # 垂直方向分成background_dct_blocks_h个块
        for h in range(background_dct_blocks_h):
            block_data = np.hsplit(h_data[h], background_dct_blocks_w)  # 水平方向分成background_dct_blocks_w个块
            for w in range(background_dct_blocks_w):
                a_block = block_data[w]
                background_dct_blocks[h, w, ...] = cv2.dct(a_block.astype(np.float64))  # dct变换
        return background_dct_blocks

    def dct_embed(self, dct_data, watermark):
        """
        将水印嵌入到载体的dct系数中
        :param dct_data: 背景图像（载体）的DCT系数
        :param watermark: 归一化二值图像0-1 (uint8类型)
        :return: 空域图像
        """
        temp = watermark.flatten()
        assert temp.max() == 1 and temp.min() == 0, "为方便处理，请保证输入的watermark是被二值归一化的"

        result = dct_data.copy()
        for h in range(watermark.shape[0]):
            for w in range(watermark.shape[1]):
                k = self.k1 if watermark[h, w] == 1 else self.k2
                # 查询块(h,w)并遍历对应块的中频系数（主对角线），进行修改
                for i in range(self.block_size):
                    result[h, w, i, self.block_size - 1] = dct_data[h, w, i, self.block_size - 1] + self.alpha * k[i]
        return result

    def idct_embed(self, dct_data):
        """
        进行对dct矩阵进行idct变换，完成从频域到空域的变换
        :param dct_data: 频域数据
        :return: 空域数据
        """
        row = None
        result = None
        h, w = dct_data.shape[0], dct_data.shape[1]
        for i in range(h):
            for j in range(w):
                
                block = cv2.idct(dct_data[i, j, ...])
                row = block if j == 0 else np.hstack((row, block))
            result = row if i == 0 else np.vstack((result, row))
        return result.astype(np.uint8)

    def dct_extract(self, synthesis, watermark_size):
        """
        从嵌入水印的图像中提取水印
        :param synthesis: 嵌入水印的空域图像
        :param watermark_size: 水印大小
        :return: 提取的空域水印
        """
        w_h, w_w = watermark_size
        recover_watermark = np.zeros(shape=watermark_size)
        synthesis_dct_blocks = self.dct_blkproc(background=synthesis)
        p = np.zeros(self.block_size)
        for h in range(w_h):
            for w in range(w_w):
                for k in range(self.block_size):
                    p[k] = synthesis_dct_blocks[h, w, k, self.block_size - 1]
                if corr2(p, self.k1) > corr2(p, self.k2):
                    recover_watermark[h, w] = 1
                else:
                    recover_watermark[h, w] = 0
        return recover_watermark



def mean2(x):
    y = np.sum(x) / np.size(x);
    return y
def corr2(a, b):
    """
    相关性判断
    """
    a = a - mean2(a)
    b = b - mean2(b)
    r = (a * b).sum() / np.sqrt((a * a).sum() * (b * b).sum())
    return r
def to_json(background_shape, watermark_shape, block_size, alpha, k1, k2, filename="watermark_info.json"):
    # 创建一个字典存储信息
    watermark_info = {
        "background_size": background_shape,
        "watermark_size": watermark_shape,
        "block_size": block_size,
        "alpha": alpha,      # 存储alpha参数
        "k1": k1.tolist(),   # 将k1转换为列表
        "k2": k2.tolist()    # 将k2转换为列表
    }
    return watermark_info 


def get_optimal_block_size(background, watermark):
    # 计算背景的行列数与水印的行列数分别相除向下取整的值
    block_size_h = background.shape[0] // watermark.shape[0]
    block_size_w = background.shape[1] // watermark.shape[1]
    # 取这两个值的最小值作为初始的block_size
    block_size = min(block_size_h, block_size_w)
    
    # 遍历block_size，确保能整除并且是偶数
    while block_size > 1:
        if background.shape[0] % block_size == 0 and background.shape[1] % block_size == 0:
            if block_size % 2 == 0:  # 确保block_size为偶数
                break
        block_size -= 1
        
    # 如果block_size为1且不能进一步减少，则说明原图和水印尺寸不匹配
    if block_size == 1:
        print(f"原图尺寸 {background.shape} 和水印图尺寸 {watermark.shape} 不匹配，无法找到合适的块大小。")
    
    return block_size

# 水印嵌入函数
def embed_watermark(background_image_path, watermark_image_path, alpha=10):
    # 读取水印和背景图像
    watermark = cv2.imread(watermark_image_path, cv2.IMREAD_GRAYSCALE)
    watermark = np.where(watermark < np.mean(watermark), 0, 1)  # 二值化水印
    background = cv2.imread(background_image_path)
    background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)  # 转为RGB格式

    # 计算合适的blocksize
    blocksize = get_optimal_block_size(background, watermark)
    k1 = np.random.randn(blocksize)
    k2 = np.random.randn(blocksize)
    print(f"计算得到的合适的blocksize为: {blocksize}")
    background_backup = background.copy()
    yuv_background = cv2.cvtColor(background, cv2.COLOR_RGB2YUV)
    Y, U, V = yuv_background[..., 0], yuv_background[..., 1], yuv_background[..., 2]
    bk = U
    # 初始化DCT算法
    dct_emb = DCT_Embed(bk, watermark,blocksize,alpha,k1,k2)

    # 分块与DCT变换
    background_dct_blocks = dct_emb.dct_blkproc(background=bk)

    # 嵌入水印图像
    embed_watermak_blocks = dct_emb.dct_embed(dct_data=background_dct_blocks, watermark=watermark)

    # 将图像转换为空域形式
    synthesis = dct_emb.idct_embed(dct_data=embed_watermak_blocks)
    yuv_background[..., 1] = synthesis
    rgb_synthesis = cv2.cvtColor(yuv_background, cv2.COLOR_YUV2RGB)

    # 保存相关信息
    watermark_size = watermark.shape
    watermark_info=to_json(background.shape, watermark.shape, blocksize, alpha, dct_emb.k1, dct_emb.k2)
    return rgb_synthesis,watermark_info
def load_dct_emb_from_json(json_file):
    """
    从JSON文件中加载DCT_Embed的参数，并创建DCT_Embed实例

    :param json_file: 存储DCT_Embed参数的JSON文件路径
    :return: 创建的DCT_Embed实例
    """
    # 从JSON文件加载信息
    with open(json_file, 'r') as file:
        data = json.load(file)

    # 从JSON文件中提取相关参数
    background_shape = tuple(data["background_size"])
    watermark_shape = tuple(data["watermark_size"])
    block_size = data["block_size"]
    alpha = data["alpha"]
    k1 = np.array(data["k1"])
    k2 = np.array(data["k2"])

    # 创建DCT_Embed实例
    dct_emb = DCT_Embed(
        background=np.zeros(background_shape),  # 这里需要用背景图像来创建实例
        watermark=np.zeros(watermark_shape),    # 这里需要用水印图像来创建实例
        block_size=block_size,
        alpha=alpha,
        k1=k1,
        k2=k2
    )

    return dct_emb


def extract_watermark(image_path, json_file):
    """
    从嵌入水印的图像中提取水印，自动加载DCT_Embed参数
    :param image_path: 水印图像的路径
    :param json_file: 存储DCT_Embed参数的JSON文件路径
    :return: 提取的水印图像
    """
    # 加载DCT_Embed实例
    dct_emb = load_dct_emb_from_json(json_file)
    # 打开图像并确保其为RGB格式
    image = Image.open(image_path)
    image_rgb = image.convert('RGB')  # 转换为RGB格式（确保图像为RGB）
    # 转换为NumPy数组
    image_array = np.array(image_rgb)
    # 使用OpenCV将图像转换为YUV格式
    image_yuv = cv2.cvtColor(image_array, cv2.COLOR_RGB2YUV)
    # 提取YUV图像的U通道（此处使用U通道进行水印提取）
    synthesis = image_yuv[..., 1]
    # 从JSON文件中读取水印尺寸
    with open(json_file, 'r') as file:
        data = json.load(file)
        watermark_size = tuple(data['watermark_size'])  # 假设JSON中包含watermark_size字段
    # 使用DCT_Embed实例提取水印
    extract_watermark = dct_emb.dct_extract(synthesis=synthesis, watermark_size=watermark_size) * 255
    # 确保水印图像为整数类型并保存
    extract_watermark = extract_watermark.astype(np.uint8)
    #cv2.imwrite('extracted_watermark.png', extract_watermark)
    return extract_watermark


#攻击测试用到
def embed_watermark_Attack(background_image_path, watermark_image_path, alpha=10):
    # 读取水印和背景图像
    watermark = cv2.imread(watermark_image_path, cv2.IMREAD_GRAYSCALE)
    watermark = np.where(watermark < np.mean(watermark), 0, 1)  # 二值化水印
    background = cv2.imread(background_image_path)
    background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)  # 转为RGB格式

    # 计算合适的blocksize
    blocksize = get_optimal_block_size(background, watermark)
    k1 = np.random.randn(blocksize)
    k2 = np.random.randn(blocksize)
    print(f"计算得到的合适的blocksize为: {blocksize}")
    background_backup = background.copy()
    yuv_background = cv2.cvtColor(background, cv2.COLOR_RGB2YUV)
    Y, U, V = yuv_background[..., 0], yuv_background[..., 1], yuv_background[..., 2]
    bk = U
    # 初始化DCT算法
    dct_emb = DCT_Embed(bk, watermark,blocksize,alpha,k1,k2)

    # 分块与DCT变换
    background_dct_blocks = dct_emb.dct_blkproc(background=bk)

    # 嵌入水印图像
    embed_watermak_blocks = dct_emb.dct_embed(dct_data=background_dct_blocks, watermark=watermark)

    # 将图像转换为空域形式
    synthesis = dct_emb.idct_embed(dct_data=embed_watermak_blocks)
    yuv_background[..., 1] = synthesis
    rgb_synthesis = cv2.cvtColor(yuv_background, cv2.COLOR_YUV2RGB)

    # 保存相关信息
    watermark_size = watermark.shape
    watermark_info=to_json(background.shape, watermark.shape, blocksize, alpha, dct_emb.k1, dct_emb.k2)
    return rgb_synthesis,dct_emb
def extract_watermark_Attack(image_rgb, dct_emb):

    image_array = np.array(image_rgb)
    # 使用OpenCV将图像转换为YUV格式
    image_yuv = cv2.cvtColor(image_array, cv2.COLOR_RGB2YUV)
    # 提取YUV图像的U通道（此处使用U通道进行水印提取）
    synthesis = image_yuv[..., 1]

    # 使用DCT_Embed实例提取水印
    extract_watermark = dct_emb.dct_extract(synthesis=synthesis, watermark_size=dct_emb.watermark_size) * 255
    # 确保水印图像为整数类型并保存
    extract_watermark = extract_watermark.astype(np.uint8)
    #cv2.imwrite('extracted_watermark.png', extract_watermark)
    return extract_watermark

if __name__ == '__main__':
    embed_watermark('4.png', 'w.png', alpha=10)
    extract_watermark('synthesis_with_watermark.png','watermark_info.json')
