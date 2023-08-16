from blind_watermark import WaterMark
from PIL import Image

def add_wm(origin_path, output_path, input_text="@tangjicheng"):
    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img(origin_path)
    wm = input_text
    bwm1.read_wm(wm, mode='str')
    bwm1.embed(output_path)
    len_wm = len(bwm1.wm_bit)
    print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))

def read_wm(wm_path, wm_bit=95):
    bwm1 = WaterMark(password_img=1, password_wm=1)
    wm_extract = bwm1.extract(wm_path, wm_shape=wm_bit, mode='str')
    print(wm_extract)

def crop_image(input_path, output_path, width, height):
    with Image.open(input_path) as img:
        # 裁剪坐标为左上角的(x,y)坐标和右下角的(x,y)坐标
        cropped_img = img.crop((0, 0, width, height))
        cropped_img.save(output_path)

def resize_image(input_path, output_path, rate = 0.5):
    with Image.open(input_path) as img:
        # 获取原始图像的尺寸
        width, height = img.size
        # 计算新的尺寸
        new_width = int(width * rate)
        new_height = int(height * rate)
        # 使用ANTIALIAS方法进行缩放，这是一个高质量的缩放方法
        resized_img = img.resize((new_width, new_height), Image.LANCZOS)
        resized_img.save(output_path)

def resize_and_restore(input_path, output_path):
    with Image.open(input_path) as img:
        # 获取原始图像的尺寸
        width, height = img.size

        # 缩小到1/2
        new_width = int(width * 0.5)
        new_height = int(height * 0.5)
        img = img.resize((new_width, new_height), Image.LANCZOS)

        # 再放大到2倍，即恢复原状
        img = img.resize((width, height), Image.LANCZOS)
        img.save(output_path)

def place_on_top(background_path, small_image_path, output_path):
    with Image.open(background_path) as bg_img:
        with Image.open(small_image_path) as small_img:
            # 确保小图像是128x128的大小
            if small_img.size != (128, 128):
                raise ValueError("The small image is not 128x128 in size!")

            # 将小图像粘贴到背景图像的左上角
            bg_img.paste(small_img, (0, 0))
            bg_img.save(output_path)

origin_img = "./artifex1.png"
crop_img_128 = "./artifex1_crop.png"
crop_image(origin_img, crop_img_128, 128, 128)

corp_img_128_wm = "./artifex1_crop_wm.png"
add_wm(crop_img_128, corp_img_128_wm)

print("1st read wm:")
read_wm("./artifex1_crop_wm.png")


origin_img_replace_wm = "./artifex1_replace_wm.png"

place_on_top(origin_img, corp_img_128_wm, origin_img_replace_wm)


origin_img_replace_wm_resize = "./artifex1_replace_wm_resize.png"
resize_image(origin_img_replace_wm, origin_img_replace_wm_resize, rate=0.5)


origin_img_replace_wm_resize_crop_64 = "./artifex1_replace_wm_resize_crop_64.png"
crop_image(origin_img_replace_wm_resize, origin_img_replace_wm_resize_crop_64, 64, 64)


origin_img_replace_wm_resize_crop_64_to_128 = "./artifex1_replace_wm_resize_crop_64_to_128.png"
resize_image(origin_img_replace_wm_resize_crop_64, origin_img_replace_wm_resize_crop_64_to_128, rate=2)

print("2rd read wm:")
read_wm(origin_img_replace_wm_resize_crop_64_to_128)
