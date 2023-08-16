from blind_watermark import WaterMark

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

add_wm("./girl.jpeg", "./girl_wm.jpeg")

read_wm("./girl_wm.jpeg")

from PIL import Image

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

input_image_path = "girl_wm.jpeg"
output_image_path = "girl_wm_resize.jpeg"

resize_and_restore(input_image_path, output_image_path)

read_wm(output_image_path)
