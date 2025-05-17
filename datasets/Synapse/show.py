import cv2
import numpy as np
import os
import random
from PIL import Image
import matplotlib.pyplot as plt


# 将mask绘制在原图
def draw_image(im, ms, brg, opacity):
    image_mask = im.copy()
    contours, _ = cv2.findContours(ms, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)  # 查找轮廓
    image_mask = cv2.drawContours(image_mask, contours, -1, 2)  # 绘制边界
    image_mask = cv2.fillPoly(image_mask, contours, color=brg)  # 填充
    img_bgr = cv2.addWeighted(im, opacity, image_mask, 1 - opacity, 0)

    return im, ms, img_bgr


def main(imagePath, labelPath, bgr, opacity):
    image = np.array(Image.open(imagePath).convert('RGB'))
    label = np.array(Image.open(labelPath).convert('L'))

    a, b, c = draw_image(image, label, bgr, opacity)

    plt.figure(figsize=(12, 8))
    for index, i in enumerate((a, b, c)):
        plt.subplot(1, 3, index + 1)
        plt.imshow(i)

    plt.savefig('./result.png')
    # plt.show()


if __name__ == '__main__':
    root = './data/train/images'
    images_path = [os.path.join(root, i) for i in os.listdir(root)]

    r = random.randint(0, len(images_path) - 1)
    img_path = images_path[r]  # 随机取出一张图片
    mask_path = img_path.replace('images', 'masks').replace('.jpg', '.png')

    # opacity 越小，掩膜效果越深
    main(imagePath=img_path, labelPath=mask_path, bgr=(0, 0, 255), opacity=0.5)