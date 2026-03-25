import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )
        self._lingua = ft.Dropdown(width=200, options=[ft.dropdown.Option("italian"),ft.dropdown.Option("english"),ft.dropdown.Option("spanish")], on_change= lambda e: self.__controller.printaLingua(self._lingua.value, e))
        self._tipo = ft.Dropdown(width=200, options=[ft.dropdown.Option("Default"), ft.dropdown.Option("Lineare"),
                                                       ft.dropdown.Option("Dicotomica")],  on_change= lambda e: self.__controller.printaModalita(self._tipo.value, e))
        self._inserisci = ft.TextField(label="Inserisci Parola da Correggere")
        self._correzione = ft.ElevatedButton(text="Starta", on_click = lambda e: self.__controller.handleSentence(self._inserisci.value, e))
        self._comunicazioni = ft.ListView(expand=True)
        row1 = ft.Row(controls=[self._lingua])
        row2 = ft.Row(controls=[self._tipo,self._inserisci, self._correzione])
        row3 = ft.Row(controls=[self._comunicazioni])
        self.page.add(row1,row2,row3)





        # Add your stuff here

        # self.page.add([])

        self.page.update()

    def update(self):
        self.page.update()
    def setController(self, controller):
        self.__controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
