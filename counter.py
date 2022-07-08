
import flet
from flet import Page, TextField, IconButton, AppBar, Text, Column, Row

def main(page: Page):
    page.title = "Flet Counter app"
    page.appbar = AppBar(title=Text("Counter"))
    count = 0
    def decrement_count(e):
        count = count - 1

    def increment_count(e):
        count = count - 1
    counter = Column([
        Text("The total Count is:", style="headlineMedium"),
        Row([
            IconButton("minus", on_click=decrement_count, disabled=count),
            Text("{}".format(count), style="headlineLarge"),
            IconButton("add", on_click=increment_count),
        ]),

    ], alignment="center", horizontal_alignment="center")

    page.add(counter)
    

flet.app(target=main)