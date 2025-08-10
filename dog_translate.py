import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
from matplotlib import rcParams

# フォントの指定
rcParams['font.family'] = 'MS Gothic'

# 翻訳API
translate_url = "http://127.0.0.1:5000/translate"

print("I will translate a dog breed into Japanese")
# 1. 犬の画像APIからデータ取得
dog_img_url = "https://dog.ceo/api/breeds/image/random"
dog_res = requests.get(dog_img_url).json()
img_url = dog_res["message"] # 画像のURL
dog_name_en = img_url.split("/breeds/")[1].split("/")[0].replace("-", " ")

# 翻訳実行
payload = {
    "q": dog_name_en,  # ハイフンをスペースに
    "source": "en",  
    "target": "ja",
    "format": "text"
}
translation_res = requests.post(translate_url, data=payload).json()
dog_name_ja = translation_res["translatedText"]

img_data = requests.get(img_url).content
img = Image.open(BytesIO(img_data))

# 4. 結果を表示
plt.imshow(img)
plt.axis("off")
plt.title(f"{dog_name_en} -> {dog_name_ja}", fontsize=14)
plt.show()
