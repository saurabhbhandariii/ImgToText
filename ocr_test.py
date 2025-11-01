import easyocr
import cv2
import numpy as np


img_path = r"C:\Users\haris\Downloads\pipe\hn.png"

reader = easyocr.Reader(['en'], verbose=False)


results = reader.readtext(img_path)


extracted_text = " ".join([res[1] for res in results])

print("\nOCR Text Results:\n", extracted_text)

width, height = 800, 200


white_bg = np.ones((height, width, 3), dtype=np.uint8) * 255


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.8
color = (0, 0, 0) 
thickness = 2


wrapped = []
words = extracted_text.split()
line = ""
for w in words:
    if len(line + w) < 60:
        line += w + " "
    else:
        wrapped.append(line)
        line = w + " "
wrapped.append(line)


y0, dy = 50, 30
for i, line in enumerate(wrapped):
    y = y0 + i * dy
    cv2.putText(white_bg, line.strip(), (30, y), font, font_scale, color, thickness, cv2.LINE_AA)


cv2.imwrite("output_text_image.png", white_bg)
print("Saved image as output_text_image.png")


cv2.imwrite("output_text_image.png", white_bg)
print("\n Text image saved as 'output_text_image.png'")
