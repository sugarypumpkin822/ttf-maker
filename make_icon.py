from PIL import Image, ImageDraw, ImageFont

# Create a 256x256 image with a blue background
img = Image.new('RGBA', (256, 256), (30, 60, 200, 255))
draw = ImageDraw.Draw(img)

# Draw a white circle in the center
draw.ellipse((48, 48, 208, 208), fill=(255, 255, 255, 255))

# Draw a black 'F' in the center (for 'Font')
try:
    font = ImageFont.truetype('arial.ttf', 120)
except:
    font = ImageFont.load_default()
text = 'F'
# Use textbbox for Pillow 10+ compatibility
bbox = draw.textbbox((0, 0), text, font=font)
w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
draw.text(((256-w)//2, (256-h)//2), text, font=font, fill=(0, 0, 0, 255))

# Save as .ico
img.save('icon.ico', format='ICO', sizes=[(256,256), (128,128), (64,64), (32,32), (16,16)])
print('icon.ico generated.') 