import time
import webbrowser

name = input('Введите имя: ')

while True:
    music = input('Какую музыку слушаешь, ' + name + '? ')
    if music != 'фонк':
        print(music.title() + ' неплох, но не то. Попробуй ещё раз\n')
    if music == 'фонк':
        for i in range(5, 0, -1):
            print(str(i) + '...')
            time.sleep(0.5)   
        print('ФОНКЕРАМ САЛАМ, ОСТАЛЬНЫМ СОБОЛЕЗНУЮ')
        time.sleep(0.5)
        webbrowser.open('https://youtu.be/jaDtiUo_6nk?t=10')
        break
        
#edited






