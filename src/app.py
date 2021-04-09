from lib.gestorDeDados import *

#Janela principal
janela = tk.Tk()
largura = 625
altura = 300
janela.title("Controle de Estoque")
janela.resizable(0, 0)
janela.geometry("%dx%d" % (largura, altura))
janela.config(bg="#ADD8E6")

lista = csvParaLista()

#tabela.
my_tree = ttk.Treeview(janela)
my_tree['columns'] = (lista[0])

#Passando os dados da lista para a Tree.
for i in range(0, len(lista[0])):
    if (i > 0 and i < 7):
        my_tree.column(cont[i], width=40, minwidth=25)
        my_tree.heading(cont[i], text=lista[0][i], anchor=tk.W)

    else:
        if(i>11):
            break
        my_tree.column(cont[i], width=77, minwidth=25)
        my_tree.heading(cont[i], text=lista[0][i], anchor=tk.N)
#Adicionando intens na Tree.
for i in range(1, len(lista)):
    listaAux = []
    for j in range(1, len(lista[i])):
        listaAux.append(lista[i][j])
    my_tree.insert(parent="", index='end', iid=i, text=lista[i][0], values=listaAux)
my_tree.pack(pady=20)

#my_tree.item(1, values="0")

#Container para armazenar os botões.
container = tk.Frame(master=janela, bg="white", pady=2).pack()

#Botões.
botao1 = tk.Button(master=container, text="Grafico 2", width=10, height=15, command=lambda: grafico2()).pack(side=tk.RIGHT)
botao2 = tk.Button(master=container, text="Grafico 1", width=10, height=15, command=lambda: grafico1_2()).pack(side=tk.RIGHT, padx=2)
botao3 = tk.Button(master=container, text="Gerar", width=10, height=15, command=lambda: geraNovosDados(numeroDeProdutos, my_tree)).pack(side=tk.RIGHT)

tk.mainloop()
