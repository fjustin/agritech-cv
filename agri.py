# OpenCVのモジュール読み込み
import cv2

# 定数定義
ORG_WINDOW_NAME = "org"
HSV_WINDOW_NAME = "hsv"
GRAY_WINDOW_NAME = "gray"
CANNY_WINDOW_NAME = "canny"

ORG_FILE_NAME  = "org.png"
HSV_FILE_NAME = "hsv.png"
GRAY_FILE_NAME = "gray.png"
CANNY_FILE_NAME = "canny.png"

# 元の画像を読み込み
org_img = cv2.imread(ORG_FILE_NAME,cv2.IMREAD_UNCHANGED)

# 彩度をあげる(HSVに変換)
img_hsv = cv2.cvtColor(org_img,cv2.COLOR_BGR2HSV)

# グレースケールに変換
gray_img = cv2.imread(ORG_FILE_NAME, cv2.IMREAD_GRAYSCALE)

# エッジ抽出
canny_img = cv2.Canny(img_hsv,100,200)

# ウィンドウに表示
cv2.namedWindow(HSV_FILE_NAME)
cv2.namedWindow(ORG_WINDOW_NAME)
cv2.namedWindow(GRAY_WINDOW_NAME)
cv2.namedWindow(CANNY_WINDOW_NAME)

cv2.imshow(HSV_FILE_NAME, img_hsv)
cv2.imshow(ORG_WINDOW_NAME, org_img)
cv2.imshow(GRAY_WINDOW_NAME, gray_img)
cv2.imshow(CANNY_WINDOW_NAME, canny_img)

# ファイルに保存
cv2.imwrite(GRAY_FILE_NAME, gray_img)
cv2.imwrite(CANNY_FILE_NAME, canny_img)

# 終了処理
cv2.waitKey(0)
cv2.destroyAllWindows()
