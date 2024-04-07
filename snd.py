import cv2
import numpy as np

tmp = input("縦軸の最大値を入力")

logo = cv2.imread('system/AnaPyzer_logo.bmp')
input_image = cv2.imread('tmp/tmp.bmp')
threshold_image = cv2.imread('tmp/color.bmp')
color = threshold_image[0, 0]  # Threshold imageの(0,0)ピクセルの色を取得

voltage = tmp
time = 1.0

x_max = input_image.shape[1]
y_max = input_image.shape[0]

y_unit = float(tmp)/y_max
x_unit = time/x_max

pixel_coordinates_y = []
pixel_coordinates_x = []
pixel_coordinates = []

for x in range(x_max):
    for y in range(y_max):
        pixel_color = input_image[y, x]
        # 特定の色が見つかった場合
        if np.array_equal(pixel_color, color):
            # 別の色で塗りつぶす (ここでは白色で塗りつぶす)
            input_image[y, x] = [255, 255, 255]
            # ピクセル座標を保存
            pixel_coordinates_x.append((x))
            pixel_coordinates_y.append((y))#####################
            pixel_coordinates.append((x_unit*x,y_unit*(y_max-y)))
            break

# x_maxが時間軸であるので，1秒間もしくは１周期の画像を読み込めばそのshape[1]がサンプリングレートとなる．
f_s = 1/len(pixel_coordinates_x)
#記録時間
t_fin = 1
#サンプル数
sampleNum = int(len(pixel_coordinates_x)*t_fin)

#サンプリング周期
dt = 1/f_s

pixel_fft = np.fft.fft(pixel_coordinates_y)
fft_power = np.abs(pixel_fft)

freqs = np.fft.fftfreq(len(pixel_coordinates_x), d=dt)

np.savetxt(
    'result/power_spectrum.csv',
    fft_power[:len(freqs)//2],
    delimiter=','
)
cv2.imwrite('modified_tmp.jpg', input_image)
#cv2.imwrite('spectrum.bmp', fft_image)

# ピクセル座標を出力
print("特定の色が見つかったピクセル座標:")
for coord in pixel_coordinates_y:
    print(coord)

np.savetxt(
    "result/pixel_xy.csv",
    pixel_coordinates,
    fmt="%.14e",
    delimiter=",",
    newline="\n",
)

# 画像を表示
logo = cv2.resize(logo, (x_max,y_max))
input_image = cv2.addWeighted(src1=input_image, alpha=1, src2=logo, beta=1, gamma=0)
cv2.imshow('Modified Image', input_image)
#cv2.imshow('FFT', fft_image)

cv2.waitKey(0)

cv2.destroyAllWindows()