import thorpy


def init():
    global menu

    menu = thorpy.Menu()

def process_event(event):
    menu.react(event)