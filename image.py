import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
from sympy import preview

def latex_generator(latex, filename, colors=((0,0,0), (255, 255, 255)), folder = "images", fontsize=300):
    """
    Генерирует изображение из LaTeX формулы
    
    Параметры:
        latex (str): LaTeX формула
        filename (str): Название генерируемого файла
        colors (tuple): Кортеж с цветовой схемой
        fontsize (int): Размер шрифта
    """
    if folder is not None:
        filename=os.path.join(folder, filename)
    preview(latex, viewer='file', 
            filename=filename, euler=False, 
            dvioptions=['-D', f'{str(fontsize)}'])
    enchance_image(filename, 1.3, colors[0], colors[1]).save(filename)

def enchance_image(img_path, scale, fg, bg):
    """
    Преобразует изображение в финальный вид
    
    Параметры:
        img_path (str): Путь для экспорта изображения
        scale (float): Размер полей
        fg (tuple): Цвет текста
        bg (tuple): Цвет фона
    """
    img = Image.open(img_path)
    x,y = img.size
    nw = int(x*scale)
    nh = int(y*scale)
    eimg = Image.new('RGB',(nw, nh), 'white')
    nx = int((nw-x)/2)
    ny = int((nh-y)/2)
    eimg.paste(img,(nx,ny,nx+x,ny+y))
    eimg = eimg.convert('L')    
    cimg = ImageOps.colorize(eimg, fg, bg)
    return cimg

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