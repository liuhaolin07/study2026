# -*- coding: utf-8 -*-
"""生成算法训练站的桌面图标（.ico + .png）。运行：python scripts/make_icon.py"""
import os
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_ICO = os.path.join(ROOT, "site", "assets", "icon.ico")
OUT_PNG = os.path.join(ROOT, "site", "assets", "icon-256.png")

S = 256
BG = (15, 22, 33, 255)
BLUE = (77, 163, 255)
CYAN = (79, 214, 224)
GRAY = (139, 152, 169)


def gradient(size, c1, c2):
    w, h = size
    img = Image.new("RGB", (w, h))
    px = img.load()
    for y in range(h):
        for x in range(w):
            t = (x + y) / max(1, (w + h - 2))
            px[x, y] = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return img


def rounded_mask(size, radius):
    m = Image.new("L", size, 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=255)
    return m


def main():
    base = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    mask = rounded_mask((S, S), 54)
    base.paste(Image.new("RGBA", (S, S), BG), (0, 0), mask)

    # 渐变描边
    border = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    ImageDraw.Draw(border).rounded_rectangle([7, 7, S - 8, S - 8], radius=48,
                                             outline=(77, 163, 255, 110), width=3)
    base.alpha_composite(border)

    grad = gradient((S, S), BLUE, CYAN).convert("RGBA")

    # <AC/> 渐变字
    font = ImageFont.truetype(r"C:\Windows\Fonts\consola.ttf", 62)
    txt = "<AC/>"
    tw = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), txt, font=font)
    x = (S - (tw[2] - tw[0])) // 2 - tw[0]
    y = 78
    text_mask = Image.new("L", (S, S), 0)
    ImageDraw.Draw(text_mask).text((x, y), txt, font=font, fill=255)
    base.paste(grad, (0, 0), text_mask)

    # 算法训练
    font2 = ImageFont.truetype(r"C:\Windows\Fonts\msyh.ttc", 26)
    txt2 = "算法训练"
    tw2 = ImageDraw.Draw(Image.new("L", (1, 1))).textbbox((0, 0), txt2, font=font2)
    x2 = (S - (tw2[2] - tw2[0])) // 2 - tw2[0]
    ImageDraw.Draw(base).text((x2, 172), txt2, font=font2, fill=GRAY)

    os.makedirs(os.path.dirname(OUT_ICO), exist_ok=True)
    base.save(OUT_PNG)
    base.save(OUT_ICO, format="ICO",
              sizes=[(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)])
    print("OK:", OUT_ICO, OUT_PNG)


if __name__ == "__main__":
    main()
