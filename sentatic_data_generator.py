import os
import logging
import random
import numpy as np
import cv2
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

# logging config
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    filename="sentatic_data_generator.log",
    filemode="w",    
    )

logger = logging.getLogger(__name__)
logger.info("Sentatic data generator started.")

# مسیر ذخیره داده‌ها
output_dir = "synthetic_data_farsi"
os.makedirs(output_dir, exist_ok=True)

# Fonts list
fonts = [font for font in os.listdir("fonts") if font.endswith(".ttf")]
print(f"Number of fonts: {len(fonts)}")

# Fonts paths
font_paths = [os.path.join("fonts", font) for font in fonts]

# Sample texts
sample_texts = [
    "سلام، این یک متن آزمایشی است.",
    "جهان پر از شگفتی‌های بزرگ است.",
    "کتاب‌ها دوستان بی‌صدا هستند."
]

def check_font_validation(font_path, text):
    try:
        font = ImageFont.truetype(font_path, 32)
        return True
    except:
        return False
    
def check_fonts_paths(font_paths, text):
    for font_path in font_paths:
        print(f"{os.path.join(font_path)} is exsit.")
        


# تولید تصویر
for i in range(len(font_paths)):  # تولید 10 تصویر نمونه
    # logger.info(f"Generating image {i}...")
    
    # ایجاد بوم خالی (سفید)
    width, height = 800, 200
    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)

    # انتخاب تصادفی فونت و اندازه
    # font_path = random.choice(font_paths)
    font_path = font_paths[i]
    
    try:
        font_size = random.randint(20, 40)
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        logger.error(f"Font {font_path} is not valid. {e}")        
        print(f"Font {font_path} is not valid. {e}")
        continue
        
    
    # انتخاب تصادفی متن
    text = random.choice(sample_texts)
    text_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # شکل‌دهی متن فارسی (reshaping) و تنظیم جهت (bidi)
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    # محاسبه موقعیت متن
    try:
        text_bbox = draw.textbbox((0, 0), bidi_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        x = (width - text_width) // 2
        y = (height - text_height) // 2
    except Exception as e:
        logger.error(f"Error in calculation of {bidi_text} for textbox: {e}")
        logger.error(f"Font: {font_path}")
        logger.error(f"Font size: {font_size}") 
        print(f"Error in calculation of {bidi_text} for textbox: {e}")
        print(f"Font: {font_path}")
        print(f"Font size: {font_size}")
        continue
    # نوشتن متن روی تصویر
    draw.text((x, y), bidi_text, font=font, fill=text_color)

    # ذخیره تصویر
    # image_path = os.path.join(output_dir, f"image_{i}.png")
    name = font_path.split("\\")[-1]
    image_path = os.path.join(output_dir, f"{name}.png")
    image.save(image_path)
    logger.info(f"Image {i} saved successfully.")
    
    # ذخیره متن
    # text_path = os.path.join(output_dir, f"image_{i}.txt")
    # text_path = os.path.join(output_dir, f"{name}.txt")
    # with open(text_path, "w", encoding="utf-8") as f:
    #     f.write(text)

print("Sentatic data generated successfully!")