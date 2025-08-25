import customtkinter

def calcular_imc():
    try:
        if not caixa_peso.get().strip():
            caixa_resultado.configure(state='normal')
            caixa_resultado.delete('1.0', 'end')
            caixa_resultado.insert('end', 'Por favor preencha o campo peso.', 'vermelho')
            caixa_resultado.configure(state='disable')
            return
        
        if not caixa_altura.get().strip():
            caixa_resultado.configure(state='normal')
            caixa_resultado.delete('1.0', 'end')
            caixa_resultado.insert('end', 'Por favor preencha o campo altura.', 'vermelho')
            caixa_resultado.configure(state='disable')
            return        

        peso = float(caixa_peso.get().replace(',','.'))
        altura = float(caixa_altura.get().replace(',','.'))

        resultado = peso / (altura * altura)
        
        caixa_resultado.configure(state='normal')
        caixa_resultado.delete('1.0', 'end')
        caixa_resultado.insert('end', f'Índice de massa corporal: {resultado:.2f}\n')
        
        if resultado < 17:
            caixa_resultado.insert('end', 'Muito abaixo do peso!\n', 'vermelho')
        elif resultado >= 17 and resultado < 18.5:
            caixa_resultado.insert('end', 'Abaixo do peso.\n', 'laranja')
        elif resultado >= 18.5 and resultado < 24.9:
            caixa_resultado.insert('end', 'Peso normal.\n', 'verde')
        elif resultado >= 24.9 and resultado < 29.9:
            caixa_resultado.insert('end', 'Acima do peso\n', 'laranja')
        elif resultado >= 29.9 and resultado < 34.9:
            caixa_resultado.insert('end', 'Obesidade I\n', 'vermelho')
        elif resultado >= 34.9 and resultado < 39.9:
            caixa_resultado.insert('end', 'Obesidade II (severa)\n', 'vermelho')
        elif resultado > 39.9:
            caixa_resultado.insert('end', 'Obesidade III (morbida)\n', 'vermelho')
        caixa_resultado.configure(state='disable')

    except ValueError:
        caixa_resultado.configure(state='normal')
        caixa_resultado.insert('end', 'Digite um valor válido.')
        caixa_resultado.configure(state='disable')



janela = customtkinter.CTk()
janela.geometry('280x300')
janela.title('Cálculo de IMC.')
janela.grid_anchor('center')

titulo_peso = customtkinter.CTkLabel(janela, text='Peso: ')
titulo_peso.grid(row=0, column=0, padx=0, pady=10, sticky='e')
caixa_peso = customtkinter.CTkEntry(janela, width=100, height=10, placeholder_text='Kg')
caixa_peso.grid(row=0, column=1, padx=0, pady=10, sticky='w')

titulo_altura = customtkinter.CTkLabel(janela, text='Altura: ')
titulo_altura.grid(row=1, column=0, padx=0, pady=0, sticky='e')
caixa_altura = customtkinter.CTkEntry(janela, width=100, height=10, placeholder_text='Metros')
caixa_altura.grid(row=1, column=1, padx=0, pady=0, sticky='w')

botao_calcular = customtkinter.CTkButton(janela, text='CALCULAR', command=calcular_imc)
botao_calcular.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

texto_resultado = customtkinter.CTkLabel(janela, text='Resultado:')
texto_resultado.grid(row=3, column=0, pady=0, padx=0, columnspan=2)
caixa_resultado = customtkinter.CTkTextbox(janela, width=220, height=100, state='disable')
caixa_resultado.grid(row=4, column=0, pady=0, padx=0, columnspan=2)

caixa_resultado.tag_config('vermelho', foreground='red')
caixa_resultado.tag_config('laranja', foreground='orange')
caixa_resultado.tag_config('verde', foreground='green')

janela.mainloop()