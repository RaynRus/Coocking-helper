import telebot

def syrniki_IzTvoroga_text() -> str:
    """Выдает рецепт сырников из творога"""
    with open("syirnikiIzTvoroga.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text

def soup_s_frikadelykami() -> str:
    """Выдает рецепт супа с фрикадельками"""
    with open("syirnikiIzTvoroga.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text

def seledyPodShuboy() -> str:
    """Выпадает рецет селеди под шубой"""
    with open("seledyPodShuboy.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text

def blinyNaMoloke() -> str:
    """Выпадает рецепт блинов на молоке"""
    with open("blinyNaMoloke.txt", "r", encoding="utf-8") as file:
        text = file.read()
    return text
