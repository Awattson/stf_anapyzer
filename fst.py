import numpy as np
#import matplotlib.pyplot as plt
import cv2
import keyboard as key
import time
"""
zunda = [
    "// .::-=-:...........:-+=.                           .=+-.................-=-:",
    "// .....................:+=                         =+:......................:",
    "// .......................-+.      ..:---===--::. .+-..................::.....",
    "// ...:..::................:+.:-==----:::::::--==++:...........:........:.....",
    "// ::::.:.......:...........:=-::--::::::::::----::::..:...::..::.......:..:..",
    "// ....::......::.:.......:::----:............:-::::---:::::....::::::::...:::",
    "// .....::::::::.:.....::::::-::......................::::-:..................",
    "// :......:::.....:::::::...-:.............................::::...............",
    "// *-::............:-::...:=:....................................::::::::::---",
    "// :++=---::::::.:--:....:*:..................:....................:+*+====++=",
    "//   .=++===--:::--:....:*:.... ..............-...................:.:==....   ",
    "//      .::--*+---:.....==.... .. ............-.......:--:........::..-+.     ",
    "//         .+=--::.....:*:... ................+........:---:........::.:*.    ",
    "//        .*=-::......-++....................-#=.........---.........-:.:*.   ",
    "//       .+=-:....-::+=+=....................+-*:.:=:.....:-..........---=*.  ",
    "//       ==:......:+*-:*-...................:*:-*:+-.......::..........---++  ",
    "//      :+........:**-:+=...................+=:-**:.........-:....... .:---*: ",
    "//     :+........-*-:=+*=..................-*-++-*:.........:+:......  .+=-=+ ",
    "//    :+::......:*:....-+..................*=:...-*..........:+.........:+--#.",
    "//   :+::......:*:......*:................+=......=+..........=:.........-+-+=",
    "//  .*:-.......+=.......-+...............=+...:-::.+=.........:=..........*-=*",
    "//  +:=.......-*...:=+***#-.............=+..=######+*=........:+........-:==-#",
    "// =-+=......:#-..+#*+===*#-........:..=+..+=--==-=*##+:.......+........-+:+-#",
    "// +-#:......++-+*#-.:++*+=*:......::.==...  -###*-.=#+*:.....:+.........*.+-*",
    "// -+#:.....:#-.**:   =#**#**:....:::+-......=##**#= -#-==:...-=........-#:+=*",
    "// :**-.....=#--#. +-+#**###=*=..=*++:....-###*+*###: ++.:+-..+:........*#:=++",
    "// -++=:....+#-== :##*+==+##-.-++=-:......-#*+===++*- =*...+*=+........-**-=*:",
    "// ==-*-:...=#=+- :#--====-*=.............-+---==--*: =+...=##:.......:*-*-=* ",
    "// =-.*=--::-#=-=  *=:::::=#...............*=.....=+  +:...-#=......:-*=-*:+- ",
    "// =- :*=----#=.=. .*-...:*-................+=---++. ::....=+....:--=*=--*:*  ",
    "// -=  :*=::-=+......-===-....................:-:........:==.::----++---+==-  ",
    "// :*    =*=--+-........................................:+=:-----+*=----*:+   ",
    "// :+-     -+*+*:......................................-+--::-=++=-----*=+:   ",
    "// +:*.       *-...............==+++++++-............:++===+*+=-------**==    ",
    "// -==+       -+...............++=======*............:::=#*=--------=+*=+     ",
    "//  -+=+       -+..............++=======*..............-*=-------+++-+==      ",
    "//   :+++.      .+=:...........:*=======*............-+=--------+=:.+*-       ",
    "//     -+*-       .-+-..........-+====++:.........-++=----=--:=+.  ==.        ",
    "//       ..          :*+-:........:-==:.......:-=#+---::-+*-=*-               ",
    "//                     -++===---:::::::--==++==-=*--:::++.++-.                ",
    "//                      .-++--=---===*=---::::::*=:::=*-                      ",
    "//                         .=+*+++=+##=:::::::::#*=+**+                       ",
    "//                               :#-=#-:::::::=*+*#+==#.                      ",
    "//                               :+:-+=:::::-*=-:-*=+*=+.                     ",
    "//                           ...:-*+-:+=::=*=-:::-+ :+=+*-:.                  ",
    ]
"""
path = input("画像名を入力(拡張子も)")
#path = 'noise5.png'
img = cv2.imread(path)
speed = [1, 5, 10, 50, 100]
i = 3

#カラーバリエーション 青->緑->赤->白の順
color = [[0xff,0x00,0x00],
         [0x00,0xff,0x00],
         [0x00,0x00,0xff],
         [0xfe,0xfe,0xfe]
         ]

x_y_00 = [0, 0]
x_y_11 = [img.shape[1], img.shape[0]]
select = 0

colorselect = [127, 127, 127]

offset = 5

while True:
    img_cut = img.copy()
    if key.is_pressed('w'):
        x_y_00[1] -= speed[i]
        x_y_11[1] -= speed[i]
    if key.is_pressed('s'):
        x_y_00[1] += speed[i]
        x_y_11[1] += speed[i]
    if key.is_pressed('a'):
        x_y_00[0] -= speed[i]
        x_y_11[0] -= speed[i]
    if key.is_pressed('d'):
        x_y_00[0] += speed[i]
        x_y_11[0] += speed[i]
    
    if key.is_pressed('f'):
        x_y_11[0] -= speed[i]
        x_y_11[1] -= speed[i]
    if key.is_pressed('g'):
        x_y_11[0] += speed[i]
        x_y_11[1] += speed[i]

    if key.is_pressed('2'):
        if select+1 <= 3:
            select += 1
            time.sleep(0.5)
        else:
            select = 0
            time.sleep(0.5)

    if key.is_pressed('h'):
        x_y_11[0] -= speed[i]
    if key.is_pressed('l'):
        x_y_11[0] += speed[i]
    if key.is_pressed('j'):
        x_y_11[1] -= speed[i]
    if key.is_pressed('k'):
        x_y_11[1] += speed[i]
    
    if key.is_pressed('1'):
        if i+1 <= 4:
            i += 1
            time.sleep(0.5)
        else:
            i = 0
            time.sleep(0.5)
    
    if key.is_pressed('e'):
        target = img[x_y_00[1]:x_y_11[1], x_y_00[0]:x_y_11[0]]
        minBGR = np.array([colorselect[0]-offset, colorselect[1]-offset, colorselect[2]-offset])
        maxBGR = np.array([colorselect[0]+offset, colorselect[1]+offset, colorselect[2]+offset])

        maskBGR = cv2.inRange(target, minBGR, maxBGR)
        target = cv2.bitwise_and(target, target, mask = maskBGR)#result
        cv2.imwrite('tmp/tmp.bmp', target)
        csimage = np.zeros((100, 100, 3))
        csimage += colorselect
        cv2.imwrite('tmp/color.bmp', csimage)



    if key.is_pressed('7') & (colorselect[0] < 255):
        colorselect[0] += 1
        time.sleep(0.05)
    #<-
    if key.is_pressed('8') & (colorselect[1] < 255):
        colorselect[1] += 1
        time.sleep(0.05)
    #->
    if key.is_pressed('9') & (colorselect[2] < 255):
        colorselect[2] += 1
        time.sleep(0.05)
    
    if key.is_pressed('4') & (colorselect[0] > 0):
        colorselect[0] -= 1
        time.sleep(0.05)
    #<-
    if key.is_pressed('5') & (colorselect[1] > 0):
        colorselect[1] -= 1
        time.sleep(0.05)
    #->
    if key.is_pressed('6') & (colorselect[2] > 0):
        colorselect[2] -= 1
        time.sleep(0.05)
    if key.is_pressed('0'):
        colorselect = color[select]
    if key.is_pressed('z') & (offset > 0):
        offset -= 1
        time.sleep(0.05)
    if key.is_pressed('x') & (offset < 20):
        offset += 1
        time.sleep(0.05)

    #指定色での切り抜き
    if key.is_pressed('c'):
        minBGR = np.array([colorselect[0]-offset, colorselect[1]-offset, colorselect[2]-offset])
        maxBGR = np.array([colorselect[0]+offset, colorselect[1]+offset, colorselect[2]+offset])

        maskBGR = cv2.inRange(img_cut, minBGR, maxBGR)
        img_cut = cv2.bitwise_and(img_cut, img_cut, mask = maskBGR)#result

    #枠の表示
    img_cut = cv2.rectangle(img_cut, (x_y_00),(x_y_11),color[select], thickness=3)
    #速度表示
    img_cut = cv2.putText(img_cut,
                          'speed='+str(speed[i]),
                          (img.shape[1]-200, img.shape[0]-30),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          1.0,
                          color[select],
                          thickness=2)
    img_cut = cv2.putText(img_cut,
                          'offset='+str(offset),
                          (img.shape[1]-200, img.shape[0]-90),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          1.0,
                          color[select],
                          thickness=2)
    img_cut = cv2.putText(img_cut,
                          'BGR='+str(colorselect),
                          (img.shape[1]-400, img.shape[0]-60),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          1.0,
                          colorselect,
                          thickness=2)
    img_cut = cv2.putText(img_cut,
                          'help : press "p"',
                          (img.shape[1]-400, img.shape[0]-130),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          1.0,
                          color[select],
                          thickness=2)
    
    
    if key.is_pressed('p'):
        img_cut = cv2.rectangle(img_cut, (5,5),(1000,365),(0x10,0x10,0x10), thickness=-1)
        img_cut = cv2.putText(img_cut,
                              'wasd: move the frame',
                              (10,30),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              'hjkl: move the line of the frame',
                              (10,60),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '7/4: B++/B--',
                              (10,90),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '8/5: G++/G--',
                              (60,120),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '9/6: R++/R--',
                              (110,150),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '0: change the BGR as frame color',
                              (160,180),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              'f-g: Zoom-Shrink',
                              (10,210),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              'x/z: offset++/offset-- (0 to 20)',
                              (10,240),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '1: change speed/ 2: change the frame color(4colors)',
                              (10,270),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              'e: export the image in the frame and export BGR. Both are export in JPG format',
                              (10,300),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              'If you want to close window, press "q".',
                              (10,330),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
        img_cut = cv2.putText(img_cut,
                              '"c" : remove colors',
                              (10,360),
                              cv2.FONT_HERSHEY_SIMPLEX,
                              1.0,
                              color[select],
                              thickness=2)
    
    #速度切り替えと色切り替えは500msのdelayをつけている．（切り替えの感度良すぎるから）
    #決してラグいわけじゃないゾ
    cv2.imshow("import image", img_cut)
    #qを押して終了
    if cv2.waitKey(50) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()