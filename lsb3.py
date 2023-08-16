from PIL import Image

def embed_watermark(original_img_path, watermark_img_path, output_path):
    # 加载图片
    original = Image.open(original_img_path)
    watermark = Image.open(watermark_img_path).convert('L')

    if original.size != watermark.size:
        raise ValueError("The original and watermark images must have the same size.")

    original_pixels = original.load()
    watermark_pixels = watermark.load()

    for i in range(original.width):
        for j in range(original.height):
            wm_value = 0 if watermark_pixels[i, j] == 0 else 7  # 7 for white (255), 0 for black (0)
            original_pixel = list(original_pixels[i, j])

            for k in range(3):  # RGB
                original_pixel[k] = (original_pixel[k] & 0xF8) | wm_value  # Preserve top 5 bits and set the bottom 3 bits

            original_pixels[i, j] = tuple(original_pixel)

    original.save(output_path)

def extract_watermark(watermarked_img_path, output_path):
    img = Image.open(watermarked_img_path)
    pixels = img.load()

    watermark = Image.new('L', (img.width, img.height), 255)
    watermark_pixels = watermark.load()

    for i in range(img.width):
        for j in range(img.height):
            wm_value = pixels[i, j][0] & 7  # Extract the three LSB

            if wm_value > 4:  # Majority decision based on the value range 0-7.
                watermark_pixels[i, j] = 255
            else:
                watermark_pixels[i, j] = 0

    watermark.save(output_path)

# 示例
embed_watermark("artifex1.png", "binary_with_text.png", "encoded.png")
extract_watermark("encoded.png", "decoded_watermark.png")
