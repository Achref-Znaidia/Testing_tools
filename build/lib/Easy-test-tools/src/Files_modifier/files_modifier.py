import flet as ft
import time
import os

global text
def main(page: ft.Page):
    # t = ft.Text(value="Hello, world!", color="green")
    # page.controls.append(t)
    # page.update()
    # t = ft.Text()
    # page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()
    #
    # for i in range(10):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1)
    # page.add(
    #     ft.Row(controls=[
    #         ft.TextField(label="Your name"),
    #         ft.ElevatedButton(text="Say my name!")
    #     ])
    # )
    # for i in range(10):
    #     page.controls.append(ft.Text(f"Line {i}"))
    #     if i > 4:
    #         page.controls.pop(0)
    #     page.update()
    #     time.sleep(0.3)
    # def button_clicked(e):
    #     page.add(ft.Text("Clicked!"))
    #
    # page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))
    # def add_clicked(e):
    #     page.add(ft.Checkbox(label=new_task.value))
    #     new_task.value = ""
    #     new_task.focus()
    #     new_task.update()
    #
    # new_task = ft.TextField(hint_text="Whats needs to be done?", width=300)
    # page.add(ft.Row([new_task, ft.ElevatedButton("Add", on_click=add_clicked)]))
    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # first_name.disabled = True
    # last_name.visible = True
    # page.add(first_name, last_name)
    # first_name = ft.TextField()
    # last_name = ft.TextField()
    # c = ft.Column(controls=[
    #     first_name,
    #     last_name
    # ])
    # c.disabled = True
    # page.add(c)
    # first_name = ft.TextField(label="First name", autofocus=True)
    # last_name = ft.TextField(label="Last name")
    # greetings = ft.Column()
    #
    # def btn_click(e):
    #     greetings.controls.append(ft.Text(f"Hello, {first_name.value} {last_name.value}!"))
    #     first_name.value = ""
    #     last_name.value = ""
    #     page.update()
    #     first_name.focus()
    #
    # page.add(
    #     first_name,
    #     last_name,
    #     ft.ElevatedButton("Say hello!", on_click=btn_click),
    #     greetings,
    # )
    # first_name = ft.Ref[ft.TextField]()
    # last_name = ft.Ref[ft.TextField]()
    # greetings = ft.Ref[ft.Column]()
    #
    # def btn_click(e):
    #     greetings.current.controls.append(
    #         ft.Text(f"Hello, {first_name.current.value} {last_name.current.value}!")
    #     )
    #     first_name.current.value = ""
    #     last_name.current.value = ""
    #     page.update()
    #     first_name.current.focus()
    #
    # page.add(
    #     ft.TextField(ref=first_name, label="First name", autofocus=True),
    #     ft.TextField(ref=last_name, label="Last name"),
    #     ft.ElevatedButton("Say hello!", on_click=btn_click),
    #     ft.Column(ref=greetings),
    # )
    """########################## app ####################################"""
    def upload_files(e):
        lv.controls.clear()
        folder_path = path_field.value
        for dirpath, _, filenames in os.walk(folder_path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                lv.controls.append(ft.Text(filepath))
                dd.options.append(ft.dropdown.Option(str(filename)))
        page.update()

    def filter_files_names(e):
        lv.scroll_to(key="20")

    def search_sentence_existence(e):
        Lines = ""
        searched_regex = searched_sentence_field.value

        col = ft.TextField(
            label="File content",
            multiline=True,
            min_lines=1,
            max_lines=6,
        )
        for line in globals()["text"].split("\n"):
            if searched_regex in line:
                Lines=Lines+"\n"+line
        col.value = f'{Lines}'
        c1.content = col
        page.update()

    def select_file(e):
        path_to_file = os.path.join(path_field.value, dd.value)
        with open(path_to_file, "r") as f:
            globals()["text"] = f.read()


    path_field = ft.TextField(label="Folder path", autofocus=True, width=page.width-130)
    searched_sentence_field = ft.TextField(label="Searched regex", width=page.width-130)
    replace_with_field = ft.TextField(label="Replace with", width=page.width - 430)
    lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True, height=200)
    c1 = ft.Container(width=page.width-60, height=200, bgcolor='#aaaaaa')
    c2 = ft.Container(width=300, height=200, bgcolor='#00ff00')
    c2.content = ft.Column(controls=[
            ft.IconButton(ft.icons.FILTER_LIST, on_click=filter_files_names),
            lv
        ])
    dd = ft.Dropdown(
        width=page.width-130,
    )
    c = ft.Column(controls=[
        ft.Row(controls=[
            path_field,
            ft.IconButton(ft.icons.FOLDER_OPEN, on_click=upload_files)
        ],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            dd,
            ft.IconButton(ft.icons.FILE_OPEN, on_click=select_file)
        ],
            alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            searched_sentence_field,
            ft.IconButton(ft.icons.SEARCH, on_click=search_sentence_existence)
        ],
        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            #c2,
            c1
        ],
        alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            replace_with_field,
            ft.ElevatedButton("Replace"),
            ft.ElevatedButton("Pass"),
            ft.ElevatedButton("Replace all")
        ],
            alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[
            ft.Text("""
                How to use:
                1- put the folder where the files will be saved.
                2- put the file name pattern
                3- put the file content pattern
                4- put the path to the excel file where data will be replaced in the patterns is saved
                5- click "Import data from excel"
                6- click "Generate"

                PS: the empty parts in the pattern will be filled with data from excel should be in this format:
                       ~[name of the collumn in the excel file]

                """)
        ],
            alignment=ft.MainAxisAlignment.CENTER),
    ])
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.add(c)
    page.update()
    """########################## app ####################################"""


ft.app(target=main)