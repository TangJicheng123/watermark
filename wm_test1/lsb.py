from PIL import Image

def apply_lsb_watermark(original_image_path, watermark_image_path, output_path):
    # 打开原始图片和水印图片
    original = Image.open(original_image_path).convert("RGB")
    watermark = Image.open(watermark_image_path).convert("RGB")

    # 确保水印大小与原始图片相同
    if original.size != watermark.size:
        watermark = watermark.resize(original.size)

    # 创建一个空白图片来保存加水印后的图片
    watermarked = Image.new("RGB", original.size)

    # 为每个像素应用LSB算法
    for x in range(original.width):
        for y in range(original.height):
            orig_pixel = original.getpixel((x, y))
            water_pixel = watermark.getpixel((x, y))

            # 提取水印图片的最高2位信息
            water_red = (water_pixel[0] & 0xC0) >> 6
            water_green = (water_pixel[1] & 0xC0) >> 6
            water_blue = (water_pixel[2] & 0xC0) >> 6

            # 清除原始图片像素的低2位并嵌入水印信息
            new_red = (orig_pixel[0] & 0xFC) | water_red
            new_green = (orig_pixel[1] & 0xFC) | water_green
            new_blue = (orig_pixel[2] & 0xFC) | water_blue

            # 保存新的像素值
            watermarked.putpixel((x, y), (new_red, new_green, new_blue))

    # 保存加水印后的图片
    watermarked.save(output_path)

# 使用示例
apply_lsb_watermark("original.jpg", "watermark.jpg", "watermarked.jpg")
