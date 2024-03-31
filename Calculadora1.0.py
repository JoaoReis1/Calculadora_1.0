import customtkinter
import tkinter
import re
import PIL



'1 Resolver o problema quando é digitado dois operadores logico, sempre trocar pelo ultimo digitado'



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

    txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=20, text_color = "white" ,width=275,height=85)
    txtbox_result.place(x=10,y=10)

def config_button():

    btn1 = customtkinter.CTkButton(master=janela, text="1", width=90, height=50,corner_radius=30,command=valor1).place(x=10,y=275)
    btn2 = customtkinter.CTkButton(master=janela, text="2", width=90, height=50,corner_radius=30,command=valor2).place(x=105,y=275)
    btn3 = customtkinter.CTkButton(master=janela, text="3", width=90, height=50,corner_radius=30,command=valor3).place(x=200,y=275)

    btn4 = customtkinter.CTkButton(master=janela, text="4", width=90, height=50,corner_radius=30,command=valor4).place(x=10,y=220)
    btn5 = customtkinter.CTkButton(master=janela, text="5", width=90, height=50,corner_radius=30,command=valor5).place(x=105,y=220)
    btn6 = customtkinter.CTkButton(master=janela, text="6", width=90, height=50,corner_radius=30,command=valor6).place(x=200,y=220)

    btn7 = customtkinter.CTkButton(master=janela, text="7", width=90, height=50,corner_radius=30,command=valor7).place(x=10, y= 165)
    btn8 = customtkinter.CTkButton(master=janela, text="8", width=90, height=50,corner_radius=30,command=valor8).place(x=105, y=165)
    btn9 = customtkinter.CTkButton(master=janela, text="9", width=90, height=50,corner_radius=30,command=valor9).place(x=200, y=165)
    btn0 = customtkinter.CTkButton(master=janela, text="0", width=90, height=50,corner_radius=30,command=valor9).place(x=105, y=335)

    btn_del =customtkinter.CTkButton(master=janela,text="Del", width=90,height=50,corner_radius=30,fg_color="teal",command=delete).place(x=10,y=335)

    btn_result = customtkinter.CTkButton(master=janela, text="=", width=90, height=50,corner_radius=30,fg_color="teal",command=resultado).place(x=200, y= 335)

    btn_soma = customtkinter.CTkButton(master=janela, text="+",width=90,height=50,corner_radius=30,fg_color="teal",command=soma).place(x=200,y=110)
    btn_mult = customtkinter.CTkButton(master=janela, text='x',width=90,height=50,corner_radius=30,fg_color="teal",command=mult).place(x=105,y=110)


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


def soma():
    digitados.append('+')
    controle_erro()
def mult():
    digitados.append('*')
    controle_erro()
def delete():
    digitados.pop()
    controle_erro()
    print("Numero deletado")

def resultado():
    db.append(digitados)

    transforma =''

    for i in str(db):
        transforma = transforma + i


    termos = re.findall(r"\d+|\*|\+", transforma)

    while '*' in termos:
        i = termos.index('*')
        resu = int(termos[i-1]) * int(termos[i+1])
        termos = termos[:i-1] + [str(resu)] + termos[i+2:]


    while '+' in termos:
        i = termos.index('+')
        resu = int(termos[i-1]) + int(termos[i+1])
        termos = termos[:i-1] + [str(resu)] + termos[i+2:]

    resultado_final = "".join(termos)  # Convertendo termos em uma string

    txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=20, text_color="white", width=275, height=85)
    txtbox_result.place(x=10, y=10)
    txtbox_result.configure(font=("Helvetica", 20))

    txtbox_result.insert("1.0",f"{resultado_final}")
    print(f"Resultado: {resultado_final}")


    db.clear()
    digitados.clear()
    db.append(resultado_final)

def controle_erro():

    if not db:
        #print("Aguardando operador")

        ''' Resolve o problema no ultimo sinal digitado'''
        for i,v in enumerate(digitados):
            if str(v) in '+*' and str(digitados[i-1]) in '+*':
                digitados.pop(i-1)

        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=20, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        txtbox_result.configure(font=("Helvetica", 20))


        tranforma_string1 = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string1)
        txtbox_result.insert("10.0",f"{n1}")
        print(n1)

    else:
        print(f"Aguardando dados:{len(db)+1}")

        txtbox_result = customtkinter.CTkTextbox(janela,corner_radius=20, text_color = "white" ,width=275,height=85)
        txtbox_result.place(x=10,y=10)
        txtbox_result.configure(font=("Helvetica", 20))

        tranforma_string1 = [str(i)for i in digitados]
        n1 = ''.join(tranforma_string1)
        txtbox_result.insert("10.0",f"{n1}")
        print(n1)

main()

janela.mainloop()