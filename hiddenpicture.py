from PIL import Image
import itertools
import random
import string


img = Image.open("einstein.png")

pix = img.load()
w, h = img.size
color_list = []

# 各pixの色値を抽出
for y in range(h):
    color_list_sub = []
    for x in range(w):
        rgb = pix[x, y]
        hex_color = '{:02x}{:02x}{:02x}'.format(*rgb)
        color_list_sub.append(hex_color)
    color_list.append(color_list_sub)


# html用のランダムな文字列を作成
pixces = w * h
random_text = ''.join(random.choices(string.ascii_letters + string.digits, k=pixces))

# html作成
html_path = "index.html"

with open(html_path, encoding="UTF-8", mode="w") as html_f:
    content = ['<!DOCTYPE html>\n<html lang="ja">\n<head>\n    <meta charset="UTF-8">\n    <title>隠し画像</title>\n    <link rel="stylesheet" href="style.css">\n</head>\n<body>\n    <h1>隠し画像</h1>\n']
    html_f.writelines(content)
    for i, col_line in enumerate(color_list):
        html_f.write('    <div id="line-' + str(i) +'" class="inner">\n')
        for j, col in enumerate(col_line):
            num = i * w + j
            html_f.write('        <span class="color-' + col + '">' + random_text[num] + '</span>\n')
        html_f.write('    </div>\n')
    html_f.write('</body>')




# css用の重複なしの色リストを作成
unique_color_list = sorted(list(set(itertools.chain.from_iterable(color_list))))

# css作成
css_path = "style.css"

with open(css_path, encoding="UTF-8", mode="w") as css_f:
    css_f.write("body {font-family: monospace; padding: 15px;} \n")
    css_f.write("div.inner{display: table;} \n")
    for col in unique_color_list:
        text_col = ".color-"+ col + "::selection {background-color: #" + col + "; color: #fff;} \n"
        css_f.write(text_col)