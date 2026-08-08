def obter_aliquota_ir(dias):
    if dias <= 180:
        return 0.225
    elif dias <= 360:
        return 0.20
    elif dias <= 720:
        return 0.175
    else:
        return 0.15

def calcular_renda_fixa(capital, porcentagem_cdi, taxa_cdi_anual, prazo_meses, tipo_ativo):
    dias = prazo_meses * 30
    anos = prazo_meses / 12
    taxa_efetiva_anual = (porcentagem_cdi / 100) * (taxa_cdi_anual / 100)
    
    montante_bruto = capital * ((1 + taxa_efetiva_anual) ** anos)
    rendimento_bruto = montante_bruto - capital
    
    isento_ir = tipo_ativo.upper() in ['LCI', 'LCA']
    
    if isento_ir:
        aliquota_ir = 0.0
        imposto_devido = 0.0
    else:
        aliquota_ir = obter_aliquota_ir(dias)
        imposto_devido = rendimento_bruto * aliquota_ir
        
    montante_liquido = montante_bruto - imposto_devido
    rendimento_liquido = montante_liquido - capital
    rentabilidade_pct = (rendimento_liquido / capital) * 100
    
    return {
        'tipo': tipo_ativo.upper(),
        'capital_inicial': capital,
        'montante_bruto': montante_bruto,
        'rendimento_bruto': rendimento_bruto,
        'aliquota_ir': aliquota_ir * 100,
        'imposto_devido': imposto_devido,
        'montante_liquido': montante_liquido,
        'rendimento_liquido': rendimento_liquido,
        'rentabilidade_pct': rentabilidade_pct
    }

def obter_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor < 0:
                print("⚠️ Insira um valor positivo.")
                continue
            return valor
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números.")

def menu():
    while True:
        print("\n" + "="*45)
        print("💰 CALCULADORA FINANCEIRA EM PYTHON 💰")
        print("="*45)
        print("1. Simular Renda Fixa (CDB, LCI, LCA)")
        print("0. Sair")
        print("="*45)
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            print("\n--- 🏦 SIMULADOR DE RENDA FIXA ---")
            tipo = input("Digite o tipo de ativo (CDB, LCI, LCA): ").strip().upper()
            capital = obter_float("Valor a investir (R$): ")
            porcentagem_cdi = obter_float("% do CDI contratado (ex: 100 para 100%): ")
            taxa_cdi = obter_float("Taxa CDI Atual ao ano (%): ")
            prazo_meses = int(obter_float("Prazo (em meses): "))
            
            res = calcular_renda_fixa(capital, porcentagem_cdi, taxa_cdi, prazo_meses, tipo)
            
            print("\n📊 RESULTADO:")
            print(f"• Produto: {res['tipo']}")
            print(f"• Montante Bruto: R$ {res['montante_bruto']:,.2f}")
            print(f"• Imposto de Renda ({res['aliquota_ir']:.1f}%): R$ {res['imposto_devido']:,.2f}")
            print(f"💰 Montante Líquido: R$ {res['montante_liquido']:,.2f}")
            print(f"📈 Rendimento Líquido: R$ {res['rendimento_liquido']:,.2f} ({res['rentabilidade_pct']:.2f}%)")

        elif opcao == '0':
            print("\nAté logo! 👋")
            break
        else:
            print("\n❌ Opção inválida.")

if __name__ == "__main__":
    menu()