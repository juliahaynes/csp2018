import sys
import webbrowser
def lyric_game():
    print('Welcome to the Lyric Game! All you have to do is guess the lyrics and complete the levels. Good luck!')
    print('I only love my ___ and my momma.')
    guess = raw_input('Guess the lyric:')
    lyric = 'bed'
    if guess == lyric:
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
        sys.exit()
    print('One, don not pick up the phone, you know he is only calling cause he is drunk and ___')
    guess = raw_input('Guess the lyric:')
    lyric = 'alone'
    if guess == lyric:
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
        sys.exit()
    print("You just want attention, you don't want my _____. ")
    guess = raw_input('Guess the lyric:')
    lyric = 'heart'
    if guess == lyric:
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
        sys.exit()
    print("Half of my heart is in ______.")
    guess = raw_input('Guess the lyric:')
    lyric = 'havana'
    if guess == lyric:
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
        sys.exit()
    print("While we're young dumb. Young, young dumb and _____. ")
    guess = raw_input('Guess the lyric:')
    lyric = 'broke'
    if guess == lyric:
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
        sys.exit()
    print("Never gonna let you down, Never gonna run around and _____ you")
    guess = raw_input('Guess the lyric:')
    lyric = 'desert'
    if guess == lyric:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
        print('Good job! now let us make it a little harder')
    else:
        print('oh no!, wrong guess!')
    print("Well, the years start coming and they don't stop coming, ___ to the rules and I hit the ground running")
    guess = raw_input('Guess the lyric:')
    lyric = 'fed'
    if guess == lyric:
        webbrowser.open('https://youtu.be/L_jWHffIx5E')
        print('Good job')
    else:
        print('oh no!, wrong guess!')
        sys.exit()