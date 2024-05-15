import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()

        # Verifico che quello inserito dall'utente sia un intero
        annoAdded = self._view._txtAnno.value
        try:
            intAnno = int(annoAdded)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un intero!"))
            self._view.update_page()

        # Verifico che l'anno inserito sia compreso tra 1826 e 2016
        if self._model.checkExistence(intAnno):
            self._view._txt_result.controls.append(ft.Text("Anno inserito valido"))

            self._model.creaGrafo(intAnno)

            self._view._txt_result.controls.append(ft.Text("Elenco degli stati:"))
            for v in self._model._grafo.nodes:
                self._view._txt_result.controls.append(ft.Text(f"{v.StateNme} -- {len(list(self._model._grafo.neighbors(v)))}"))
            self._view.update_page()
        else:
            self._view._txt_result.controls.append(ft.Text("Anno inserito non valido! Deve essere compreso tra il 1826 e il 2016"))
            self._view.update_page()


