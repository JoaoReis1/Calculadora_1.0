import customtkinter
import time
janela = customtkinter.CTk()

digitados = list()
db = list()



def main():

    init_config()
    frame_result()
    config_button()

def init_config():  
    janela.title("Calculadora 1.0")
    janela.geometry("300x400")
    janela.maxsize(width=300,height=400 )
    janela.minsize(width=300,height=400 )



def frame_result():
    
    frama1 = customtkinter.CTkFrame( master=janela,width=285, height=90, corner_radius=30).place(x=5,y=10)
    
def config_button():
    
    btn1 = customtkinter.CTkButton(master=janela, text="1", width=90, height=50,corner_radius=30,command=valor1).place(x=10,y=275)
    btn2 = customtkinter.CTkButton(master=janela, text="2", width=90, height=50,corner_radius=30,command=valor2).place(x=105,y=275)
    btn3 = customtkinter.CTkButton(master=janela, text="6", width=90, height=50,corner_radius=30,command=valor3).place(x=200,y=275)
    
    btn4 = customtkinter.CTkButton(master=janela, text="4", width=90, height=50,corner_radius=30,command=valor4).place(x=10,y=220)
    btn5 = customtkinter.CTkButton(master=janela, text="5", width=90, height=50,corner_radius=30,command=valor5).place(x=105,y=220)
    btn6 = customtkinter.CTkButton(master=janela, text="6", width=90, height=50,corner_radius=30,command=valor6).place(x=200,y=220)
    
    btn7 = customtkinter.CTkButton(master=janela, text="7", width=90, height=50,corner_radius=30,command=valor7).place(x=10, y= 165)
    btn8 = customtkinter.CTkButton(master=janela, text="8", width=90, height=50,corner_radius=30,command=valor8).place(x=105, y=165)
    btn9 = customtkinter.CTkButton(master=janela, text="9", width=90, height=50,corner_radius=30,command=valor9).place(x=200, y=165)
    
    
    btn_result = customtkinter.CTkButton(master=janela, text="Resulto", width=120, height=50,corner_radius=30,command=resultado).place(x=90, y= 340)
    
    btn_soma = customtkinter.CTkButton(master=janela, text="+",width=90,height=50,corner_radius=30,command=fatiador).place(x=200,y=110)
    
def valor1():
    digitados.append(1)
    controle_erro()
def valor2():
    digitados.append(2)
    controle_erro()
def valor3():
    digitados.append(3)
    controle_erro()
def valor4():
    digitados.append(4)
    controle_erro()
def valor5():
    digitados.append(5)
    controle_erro()
def valor6():
    digitados.append(6)
    controle_erro()
def valor7():
    digitados.append(7)
    controle_erro()
def valor8():
    digitados.append(8)
    controle_erro()
def valor9():
    controle_erro()
    
def fatiador ():
    db.append(digitados[:])
    digitados.clear()
    

    
def resultado():
    if not db:
        #Caso nenhum operador seja escolhido mostrará os numeros digitados, IMPORTANT:Informação só tornará no prompt, na tela inda mostrará os numeros digitados conforme interação.
        print(digitados)
    else:
    
        # Precisamos chamar o fatiador para armazenar o ultimos valores digitados
        fatiador()
        
        #O primeiro laço descobre quantas lista tem dentro das lista
        soma = 0
        for i in range(0,len(db)):
            #Segundo laço retorna todos os valores dentro da lista atual para realizar operação
            for v in db[i]:
                soma = soma + v
        print()
        print(soma)

def controle_erro():
    
    valores = ""
    if not db:
        print("Aguardando operador") 
        
        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        
        #cod que retorna os valores em []
        #txtbox_result.insert("1.0",f"{digitados}")    
        
        #percorre a lista pelo enumerate e retorna sem o []
        digitados.reverse()
        for indi, value in enumerate(digitados):
            #print(value,end=' ')
            txtbox_result.insert("1.0",f"{value}") 
    else:
        print(db,end=' ')
        print(f"Aguardando dados:{len(db)+1}")
        
        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        digitados.reverse()
        for indi, value in enumerate(digitados):
            #print(value,end=' ')
            txtbox_result.insert("1.0",f"{value}") 
    
main()

janela.mainloop()