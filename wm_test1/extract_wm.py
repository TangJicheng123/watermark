from PIL import Image

def place_image_on_black_bg(small_img_path, bg_width, bg_height, output_path):
    # 创建一个黑色背景的图片
    black_bg = Image.new("RGB", (bg_width, bg_height), "black")

    # 打开小图片
    small_img = Image.open(small_img_path)

    # 将小图片放在黑色背景的左上角
    black_bg.paste(small_img, (0, 0))

    # 保存到输出路径
    black_bg.save(output_path)

your_image_path = "origin2_bg_wm_return.jpg"
your_image_path = "modify.jpg"
your_image_path = "modify1.jpg"
your_image_path = "modify2.jpg"
place_image_on_black_bg(your_image_path, 1920, 1080, "modify_bg.jpg")

from blind_watermark import WaterMark

bwm1 = WaterMark(password_img=1, password_wm=1)
wm_extract = bwm1.extract('modify_bg.jpg', wm_shape=95, mode='str')
print(wm_extract)