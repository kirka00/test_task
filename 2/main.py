from PIL import Image
import requests


def loading(url, n):  # загрузка картинок по url в рабочую директорию
    p = requests.get(url)
    out = open(f"{n}.jpg", "wb")
    out.write(p.content)
    out.close()


def overlay():
    loading('http://alitair.1gb.ru/test_prog_plashki/106044_benefit.jpg', 1)
    loading('http://alitair.1gb.ru/test_prog_plashki/benefit.png', 2)
    fon = Image.open('2.jpg').convert('RGB')  # открытие картинок
    im2 = Image.open('1.jpg').convert('RGB')

    fon.paste(im2, (30, 135))  # наложение картинок
    fon.save('output.jpg', quality=95)  # сохранение результата


overlay()
