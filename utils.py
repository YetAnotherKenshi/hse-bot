from datetime import datetime
import os

def generate_id(cid):
    return (str(cid)+str(int(datetime.now().timestamp())))

def save_feedback(cid, text, folder='reports'):
    fn = f'report_{str(cid)}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    path = os.path.join(folder, fn)
    try:
        with open(path, 'w') as f:
            f.write(text)
    except:
        return None
    return path

from PIL import Image, ImageDraw, ImageFont

color_schemes = {
    "1": ((0,0,0), (255,255,255)),
    "2": ((255,255,255), (0,0,0)),
    "3": ((255,255,255), (15, 40, 25)),
    "4": ((255,255,255), (15, 35, 65)),
}

def get_styles_preview(themes):
    W = 800
    H = 120 # Высота одного стиля
    img = Image.new(
        'RGB',
        (W, len(themes.values())*H),
        'white'
    )

    font = ImageFont.truetype('source_serif.ttf', int(H*0.5))

    d = ImageDraw.Draw(img)
    for i, t in enumerate(themes.values()):
        d.rectangle((0, H*i, W, H*(i+1)), t[1])
        d.text((W/2, H*(i+0.5)), f"Стиль {i+1}", t[0], font=font, align="center", anchor='mm')
    
    img.save("themes.png")