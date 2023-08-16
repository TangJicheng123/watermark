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

# 使用示例
place_image_on_black_bg("origin2.jpeg", 1920, 1080, "origin2_bg.jpg")

from blind_watermark import WaterMark

bwm1 = WaterMark(password_img=1, password_wm=1)
bwm1.read_img('origin2_bg.jpg')
wm = '@tangjicheng'
bwm1.read_wm(wm, mode='str')
bwm1.embed('origin2_bg_wm.png')
len_wm = len(bwm1.wm_bit)
print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
# 95

def crop_top_left_corner(input_img_path, width, height, output_path):
    # 打开原始图片
    original_img = Image.open(input_img_path)

    # 使用crop函数来剪切左上角
    cropped_img = original_img.crop((0, 0, width, height))

    # 保存剪切后的图片
    cropped_img.save(output_path)

# 使用示例
crop_top_left_corner("origin2_bg_wm.png", 256, 384, "origin2_bg_wm_return.jpg")
