import cv2
import numpy as np
import matplotlib.pyplot as plt

def yugami():
    # 画像を読み込む
    img = cv2.imread('./sources/hata.png')

    # 画像の横と縦の長さを切り出す
    rows,cols,ch = img.shape

    # 画像の座標上から4角を切り出す
    pts1 = np.float32([[320,236],[1104,402],[12,332],[1053,640]])
    pts2 = np.float32([[0,0],[1250,0],[0,500],[1250,500]])

    # 透視変換の行列を求める
    M = cv2.getPerspectiveTransform(pts1,pts2)

    # 変換行列を用いて画像の透視変換
    rst = cv2.warpPerspective(img,M,(1250,500))
    # 透視変換後の画像を保存
    cv2.imwrite('./sources/yugami.png',rst)


def extract_color (src,h_th_low,h_th_up,s_th,v_th):
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)   # HSV変換
    # 青色のHSV範囲
    #hsv_min = np.array([80, 150, 0])
    #hsv_max = np.array([150, 255, 255])

    h,s,v = cv2.split(hsv)


    # 色相の赤における0°と360°を調整
    if h_th_low > h_th_up:
        ret,h_dst_1 = cv2.threshold(h,h_th_low,255,cv2.THRESH_BINARY)
        ret,h_dst_2 = cv2.threshold(h,h_th_up,255,cv2.THRESH_BINARY_INV)

        # BINARYとBINARY_INVのどちらかをとる
        dst = cv2.bitwise_or(h_dst_1,h_dst_2)

    else:
        # 赤以外はそのまま適用する
        ret,dst = cv2.threshold(h,h_th_low,255,cv2.THRESH_TOZERO)
        ret,dst = cv2.threshold(dst,h_th_up,255,cv2.THRESH_TOZERO_INV)

        ret,dst = cv2.threshold(dst,0,255,cv2.THRESH_BINARY)

        # S(明度)とV(彩度)についても同様の場合分けを行う
        ret, s_dst = cv2.threshold(s, s_th, 255, cv2.THRESH_BINARY)
        ret, v_dst = cv2.threshold(v, v_th, 255, cv2.THRESH_BINARY)

        dst = cv2.bitwise_and(dst, s_dst)
        dst = cv2.bitwise_and(dst, v_dst)

        return dst


if __name__ == '__main__':
    yugami()

    right_image = cv2.imread('./sources/yugami.png')

    green_image = extract_color(right_image,0,178,50,0)
    m = cv2.countNonZero(green_image)
    h, w = green_image.shape
    per = round(100*float(m)/(w * h),1)
    print("Moment[px]:",m)
    print("Percent[%]:", per)

    cv2.imshow("Mask",green_image)
    cv2.imwrite('./sources/agri.png',green_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
