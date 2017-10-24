'''
Color extraction by Python
'''
# OpenCVモジュールの追加
import cv2

# 色彩抽出の関数定義
def extract_color(src,h_th_low,h_th_up,s_th,v_th):

    # HSVへの変換
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
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


# 同ファイル内で関数実行する際の決まり文句
if __name__ == "__main__":

    # 読み取りファイルを定義
    ORG_WINDOW_NAME = "org"
    ORG_FILE_NAME  = "org.png"

    # Windowの名前を決める
    cv2.namedWindow("Capture",cv2.WINDOW_AUTOSIZE)
    cv2.namedWindow("Green",cv2.WINDOW_AUTOSIZE)

    while True:
        #元ファイルをそのままopenCVで読み込む
        image = cv2.imread(ORG_FILE_NAME,cv2.IMREAD_UNCHANGED)

        # 緑色を抽出
        green_image = extract_color(image,0,178,70,0)

        cv2.imshow("Capture",image)
        cv2.imshow("Green",green_image)

        # 時間内に緑を抽出した画像を保存
        if cv2.waitKey(33) >= 0:
            cv2.imwrite("green_image.png",green_image)
            break

    # 全てのウィンドウを閉じる
    cv2.destroyAllWindows()
