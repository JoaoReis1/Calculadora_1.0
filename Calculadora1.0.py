import customtkinter
import time
janela = customtkinter.CTk()

digitados = list()
db = list()
valores =list()
n1=''



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
    
    
    btn_result = customtkinter.CTkButton(master=janela, text="Resultado :)", width=120, height=50,corner_radius=30,command=resultado).place(x=90, y= 340)
    
    btn_soma = customtkinter.CTkButton(master=janela, text="+",width=90,height=50,corner_radius=30,command=soma).place(x=200,y=110)
    
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
    
def soma ():
    
    txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
    txtbox_result.place(x=10,y=10)
    
    
    tranforma_string = [str(i)for i in digitados]
    n1 = ''.join(tranforma_string)
    db.append(int(n1))
    digitados.clear()

    n1 = ''
    
def resultado():
    if not db:
        #Caso nenhum operador seja escolhido mostrará os numeros digitados, IMPORTANT:Informação só tornará no prompt, na tela inda mostrará os numeros digitados conforme interação.
        
        tranforma_string = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string)
        print(n1)
        
    else:
    
        ' primeiro laço descobre quantas lista tem dentro das lista'
        
        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        
        'Preciso tranformar em string o ultimo valor antes de mostrar o resultado'
        tranforma_string3 = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string3)
        db.append(int(n1))
        
        
        ' Aqui temos que fazer um loop com o len'
        resultado = 0
        descricao =''
        
        for ind, val in enumerate(db):
            resultado = resultado + val
    
        for i in db:
            descricao= descricao + f"{i}+"
        
        txtbox_result.insert("1.0",f"{descricao}={resultado}")  
        
        'Não mexe tá funcionando'
        n1=''
        digitados.clear()
        db.clear()
        db.append(resultado)
        resultado=0

def controle_erro():
    
    if not db:
        #print("Aguardando operador") 
        
        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        
        tranforma_string1 = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string1)
        txtbox_result.insert("1.0",f"{n1}") 
        print(n1)
        
    else:
        print(f"Aguardando dados:{len(db)+1}")
        
        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=0, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        
        tranforma_string1 = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string1)
        txtbox_result.insert("1.0",f"{n1}") 
        print(n1)
        
main()

janela.mainloop()