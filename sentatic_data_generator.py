import os
from PIL import Image, ImageDraw, ImageFont
import random
import numpy as np
import cv2
import arabic_reshaper
from bidi.algorithm import get_display

# مسیر ذخیره داده‌ها
output_dir = "synthetic_data_farsi"
os.makedirs(output_dir, exist_ok=True)

# Fonts list
fonts = [font for font in os.listdir("fonts") if font.endswith(".ttf")]

# Fonts paths
font_paths = [os.path.join("fonts", font) for font in fonts]

# Sample texts
sample_texts = [
    "سلام، این یک متن آزمایشی است.",
    "جهان پر از شگفتی‌های بزرگ است.",
    "کتاب‌ها دوستان بی‌صدا هستند."
]

# تولید تصویر
for i in range(10):  # تولید 10 تصویر نمونه
    # ایجاد بوم خالی (سفید)
    width, height = 800, 200
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # انتخاب تصادفی فونت و اندازه
    font_path = random.choice(font_paths)
    print(font_path)
    font_size = random.randint(20, 40)
    font = ImageFont.truetype(font_path, font_size)

    # انتخاب تصادفی متن
    text = random.choice(sample_texts)
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # شکل‌دهی متن فارسی (reshaping) و تنظیم جهت (bidi)
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    # محاسبه موقعیت متن
    text_bbox = draw.textbbox((0, 0), bidi_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    # نوشتن متن روی تصویر
    draw.text((x, y), bidi_text, font=font, fill=text_color)

    # ذخیره تصویر
    image_path = os.path.join(output_dir, f"image_{i}.png")
    image.save(image_path)

    # ذخیره متن
    text_path = os.path.join(output_dir, f"image_{i}.txt")
    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

print("Sentatic data generated successfully!")