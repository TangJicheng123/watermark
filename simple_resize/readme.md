# 测试放大缩小对频域水印的影响

原始图片->加入水印->缩小为1/2->放大到原始尺寸->检测水印


使用LANCZOS缩小放大后，依然能读取水印。


但是，必须还原到原始尺寸，否则无法读取水印。