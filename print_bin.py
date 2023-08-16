from PIL import Image


def print_binary_image_values(image_path):
    # 加载图片
    with Image.open(image_path) as img:
        # 确保是二值格式
        img = img.convert('1')

        width, height = img.size
        pixels = img.load()

        # 遍历每个像素并打印其值
        for y in range(height):
            for x in range(width):
                # 对于二值图像，像素值为True或False，我们可以将其转换为整数（1或0）
                print(int(pixels[x, y]), end=' ')
            print()  # 换行


# 示例
print_binary_image_values("binary_with_text.jpg")
