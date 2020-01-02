# DOCS about type of methods for a class https://pythonista.io/cursos/py111/metodos-de-clase-y-metodos-estaticos

class Lamp:

    _LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, is_turned_on):
        self._is_turned_on = is_turned_on
        self._display_image()

    def turn_on(self):
        self._is_turned_on = True
        self._display_image()
        

    def turn_off(self):
        self._is_turned_on = False
        self._display_image()
    
    def _display_image(self):
        if self._is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


# THIS CODE IS OUT OF CLASS

if __name__ == '__main__':
    lamp = Lamp(is_turned_on = True)
    while True:
        action = input('''
        What do you do?
            * (TO) Turn On
            * (TOF) Turn Off
            * (E) Exit
        ''')
        if action == 'TO' or action == 'to':
            lamp.turn_on()
        elif action == 'TOF' or action == 'tof':
            lamp.turn_off()
        else:
            break
