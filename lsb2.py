from PIL import Image, ImageDraw, ImageFont

def embed_lsb_watermark(original_image_path, watermark_image_path, output_path):
    """嵌入LSB水印"""
    original = Image.open(original_image_path)
    watermark = Image.open(watermark_image_path).convert("1")  # 确保为二值图像

    if original.size != watermark.size:
        raise ValueError("The original image and watermark image should have the same dimensions.")

    pixels = original.load()
    watermark_pixels = watermark.load()

    for i in range(original.width):
        for j in range(original.height):
            # 获取原始像素值
            r, g, b = pixels[i, j]
            # 根据水印像素来设置LSB
            if watermark_pixels[i, j] == 255:  # 白色
                r |= 1  # Set LSB
                g |= 1
                b |= 1
            else:
                r &= ~1  # Clear LSB
                g &= ~1
                b &= ~1

            pixels[i, j] = (r, g, b)

    original.save(output_path)

def extract_lsb_watermark(original_image_path, output_watermark_path):
    """提取LSB水印"""
    original = Image.open(original_image_path)
    watermark = Image.new("1", original.size)

    pixels = original.load()
    watermark_pixels = watermark.load()

    for i in range(original.width):
        for j in range(original.height):
            r, g, b = pixels[i, j]
            # 检查LSB，根据大部分RGB的LSB来确定水印的颜色
            if r & 1 and g & 1 and b & 1:
                watermark_pixels[i, j] = 255  # 白色
            else:
                watermark_pixels[i, j] = 0  # 黑色

    watermark.save(output_watermark_path)


def create_binary_image_with_text(image_path, output_path, text):
    # 打开原始图片并获取其大小
    with Image.open(image_path) as img:
        width, height = img.size

    # 创建一个白色的二值图片
    binary_img = Image.new("1", (width, height), color=1)

    # 绘制文字
    draw = ImageDraw.Draw(binary_img)
    font = ImageFont.truetype("Chalkduster.ttf", 50)  # 可以根据需要修改字体和大小
    text_width, text_height = draw.textsize(text, font=font)

    # 计算文本在图片中的位置（居中显示）
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), text, font=font, fill=0)  # 使用黑色（0）绘制文本

    # 保存生成的图片
    binary_img.save(output_path)

# 示例
create_binary_image_with_text("artifex1.png", "binary_with_text.png", "Hello, World!")


# 示例
embed_lsb_watermark("artifex1.png", "binary_with_text.png", "watermarked.png")
extract_lsb_watermark("watermarked.png", "extracted_watermark.png")
