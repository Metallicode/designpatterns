from pynput.mouse import Controller, Listener

with Listener(on_click=print) as listener:
    listener.join()
