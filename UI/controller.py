import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._currentCountry = None

    def handleCalcola(self, e):
        self._view._txt_result.controls.clear()

        # Verifico che quello inserito dall'utente sia un intero
        annoAdded = self._view._txtAnno.value
        try:
            intAnno = int(annoAdded)
        except ValueError:
            self._view._txt_result.controls.append(ft.Text("Il valore inserito non è un numero intero!"))
            self._view.update_page()

        # Verifico che l'anno inserito sia compreso tra 1826 e 2016
        if self._model.checkExistence(intAnno):
            self._view._txt_result.controls.append(ft.Text("Grafo correttamente creato."))

            self._model.creaGrafo(intAnno)

            self._view._txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumComponentiConnesse()} componenti connesse."))
            self._view._txt_result.controls.append(ft.Text("Di seguito il dettaglio sui nodi:"))
            for n in self._model.getNodes():
                self._view._txt_result.controls.append(ft.Text(f"{n.StateNme} -- {self._model.getNumConfinanti(n)} vicini."))

            self._view._ddStato.disabled = False
            self._view._btnRaggiungibili.disabled = False

            self._fillDD()

            self._view.update_page()
        else:
            self._view._txt_result.controls.append(ft.Text("Anno inserito non valido! Deve essere compreso tra il 1826 e il 2016"))
            self._view.update_page()

    def handleRaggiungibili(self, e):
        raggiungibili = self._model.getRaggiungibili(self._currentCountry)
        self._view._txt_result.controls.clear()
        self._view._txt_result.controls.append(ft.Text(f"Da {self._currentCountry} è possibile raggiungere a piedi "
                                                       f"{len(raggiungibili)} stati:"))
        for r in raggiungibili:
            self._view._txt_result.controls.append(ft.Text(f"{r}"))
        self._view.update_page()

    def _fillDD(self):
        allStati = self._model.getNodes()
        for s in allStati:
            self._view._ddStato.options.append(ft.dropdown.Option(text=s.StateNme,
                                                                  data=s,
                                                                  on_click=self.read_DD_Stato))
        self._view.update_page()

    def read_DD_Stato(self, e):
        if e.control.data is None:
            self._currentCountry = None
        else:
            self._currentCountry = e.control.data
