import sys
import pycep_correios
from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import (QApplication, QMainWindow, QCheckBox, QLineEdit,
                               QWidget, QLabel, QVBoxLayout, QComboBox,QFrame)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("Cadastro de Clientes") #Definindo o título da minha janela

        #Atribuindo os elementos a uma instância
        self.lbl0 = QLabel("Nome completo")
        self.input0 = QLineEdit()
      
        self.lbl1 = QLabel("Gênero")
        self.selection0 = QComboBox()
        self.selection0.addItems(["Masculino", "Feminino"])
        
        self.lbl2 = QLabel("CEP")
        self.input1 = QLineEdit()
      
        self.lbl3 = QLabel("Logradouro")
        self.input2 = QLineEdit()
      
        self.lbl4 = QLabel("Número")
        self.input3 = QLineEdit()
      
        self.lbl5 = QLabel("Bairro")
        self.input4 = QLineEdit()
      
        self.lbl6 = QLabel("Cidade")
        self.input5 = QLineEdit()
      
        self.lbl7 = QLabel("UF")
        self.input6 = QLineEdit()


        #Atribuindo uma caixa de layout à variável 'layout'
        layout = QVBoxLayout()

        #Adicinando os elementos ao layout
        layout.addWidget(self.lbl0)
        layout.addWidget(self.input0)
        layout.addWidget(self.lbl1)
        layout.addWidget(self.selection0)
        layout.addWidget(self.lbl2)
        layout.addWidget(self.input1)
        layout.addWidget(self.lbl3)
        layout.addWidget(self.input2)
        layout.addWidget(self.lbl4)
        layout.addWidget(self.input3)
        layout.addWidget(self.lbl5)
        layout.addWidget(self.input4)
        layout.addWidget(self.lbl6)
        layout.addWidget(self.input5)
        layout.addWidget(self.lbl7)
        layout.addWidget(self.input6)

        #Atribuindo o elemento QFrame() à variável container
        container = QFrame()
        container.setLayout(layout) #Adicionando o layout ao 'container'
        self.setCentralWidget(container) #Adicionando o 'container' à instância
    
        self.input1.editingFinished.connect(self.consulta_cep)
        
    def consulta_cep(self):
        adress = pycep_correios.get_address_from_cep(self.input1.text())
        self.input2.setText(adress['logradouro'])
        self.input4.setText(adress['bairro'])
        self.input5.setText(adress['cidade'])
        self.input6.setText(adress['uf'])

app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
