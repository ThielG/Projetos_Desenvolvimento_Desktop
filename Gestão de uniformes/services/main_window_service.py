import datetime
import pandas as pd
from PySide6.QtWidgets import QTableWidget, QMessageBox

from infra.repository.emprestimo_repository import EmprestimoRepository
from infra.repository.uniforme_repository import UniformeRepository
from infra.repository.funcionario_repository import FuncionarioRepository


class MainWindowService:
    def __init__(self):
        self.emprestimo_repository = EmprestimoRepository
        self.funcionario_repository = FuncionarioRepository
        self.uniforme_repository = UniformeRepository

    def populate_table_funcionario(self, main_window):
        main_window.tb_funcionario.setRowCount(0)
        lista_funcionario = self.funcionario_repository.select_all_funcionario()
        for funcionario in lista_funcionario[:]:
            if not funcionario.ativo:
                lista_funcionario.remove(funcionario)
        main_window.tb_funcionario.setRowCount(len(lista_funcionario))
        for linha, funcionario in enumerate(lista_funcionario):
            if funcionario.ativo:
                main_window.tb_funcionario.setItem(linha, 0, funcionario.nome)
                main_window.tb_funcionario.setItem(linha, 1, funcionario.cpf)

    def populate_table_uniforme(self, main_window):
        main_window.tb_uniforme.setRowCount(0)
        lista_uniforme = self.uniforme_repository.select_all_uniformes()
        for uniforme in lista_uniforme[:]:
            if not uniforme.ativo:
                lista_uniforme.remove(uniforme)
        main_window.tb_uniforme.setRowCount(len(lista_uniforme))
        for linha, uniforme in enumerate(lista_uniforme):
            if uniforme.ativo:
                main_window.tb_uniforme.setItem(linha, 0, uniforme.nome)

    def populate_table_emprestimos_ativos(self, main_window):
        main_window.tb_emprestimos_ativos.setRowCount(0)
        emprestimos_ativos = self.emprestimo_repository.select_emprestimo_ativos()
        main_window.tb_emprestimos_ativos.setRowCount(len(emprestimos_ativos))
        for linha, (emp, funcionario, uniforme) in enumerate(emprestimos_ativos):
            main_window.tb_emprestimos_ativos.setItem(linha, 0, funcionario.nome)
            main_window.tb_emprestimos_ativos.setItem(linha, 1, funcionario.cpf)
            main_window.tb_emprestimos_ativos.setItem(linha, 2, funcionario.data_emprestimo.strft('%d/#m/%Y'))
            main_window.tb_emprestimos_ativos.setItem(linha, 3, funcionario.uniforme.nome)
