# ==============================================
# NUTRI SAÚDE - SISTEMA COMPLETO + IA
# Desenvolvedor: Matheus Dev
# Versão: 1.0 - COMPLETA E FUNCIONAL
# ==============================================

# ==============================================
# CLASSE PRINCIPAL: USUÁRIO E DADOS
# ==============================================
class Usuario:
    def __init__(self, nome, idade, peso, altura, objetivo):
        # Dados do cadastro
        self.nome = nome.upper()
        self.idade = idade
        self.peso = peso
        self.altura = altura
        # Padroniza logo no começo para não ter erro
        self.objetivo = objetivo.upper()
        
        # Dados que SÃO CALCULADOS AUTOMATICAMENTE
        self.imc = 0.0
        self.tmb = 0.0
        self.calorias_diarias = 0.0
        self.proteina_diaria = 0.0
        self.carboidrato_diario = 0.0
        self.gordura_diaria = 0.0
        
        # LISTA: GUARDA TUDO O QUE É CADASTRADO
        self.refeicoes = []

    # AUTOMAÇÃO: CALCULA TUDO SOZINHO
    def Calcular_Tudo(self):
        # Cálculo IMC
        self.imc = self.peso / (self.altura ** 2)
        
        # Cálculo Taxa Metabólica Basal
        self.tmb = 10 * self.peso + 6.25 * (self.altura * 100) - 5 * self.idade + 5

        # Define Meta de Calorias por OBJETIVO
        if self.objetivo == "EMAGRECER":
            self.calorias_diarias = self.tmb - 300
        elif self.objetivo == "GANHAR MASSA":
            self.calorias_diarias = self.tmb + 400
        else:  # MANTER PESO
            self.calorias_diarias = self.tmb

        # Distribuição de Macronutrientes (Automático)
        self.proteina_diaria = self.peso * 2.0  # 2g por kg de peso
        self.carboidrato_diario = (self.calorias_diarias * 0.5) / 4  # 50% do total
        self.gordura_diaria = (self.calorias_diarias * 0.25) / 9     # 25% do total

    # FUNÇÃO: ADICIONAR REFEIÇÃO NO SISTEMA
    def Adicionar_Refeicao(self, nome_refeicao, alimento, quantidade, calorias, proteina, carboidrato, gordura):
        refeicao = {
            "refeicao": nome_refeicao.upper(),
            "alimento": alimento,
            "qtd": quantidade,
            "calorias": calorias,
            "proteina": proteina,
            "carboidrato": carboidrato,
            "gordura": gordura
        }
        self.refeicoes.append(refeicao)
        return f"  '{alimento}' adicionado com sucesso!"

    #  FUNÇÃO: RELATÓRIO COMPLETO
    def Gerar_Relatorio(self):
        # Somar tudo que foi consumido
        total_cal = sum(r['calorias'] for r in self.refeicoes)
        total_prot = sum(r['proteina'] for r in self.refeicoes)
        total_carb = sum(r['carboidrato'] for r in self.refeicoes)
        total_gord = sum(r['gordura'] for r in self.refeicoes)

        relatorio = f"""
\n{'='*50}
  RELATÓRIO COMPLETO - NUTRI SAÚDE
  Usuário: {self.nome}
  Altura: {self.altura:.2f}m |  Peso: {self.peso:.1f}kg |   Objetivo: {self.objetivo}

  DADOS CALCULADOS AUTOMATICAMENTE:
  IMC: {self.imc:.2f}
  Gasto Diário: {self.tmb:.0f} kcal
  Meta Diária: {self.calorias_diarias:.0f} kcal

  CONSUMIDO HOJE:
  Calorias: {total_cal:.0f} / {self.calorias_diarias:.0f} kcal
  Proteínas: {total_prot:.1f}g / {self.proteina_diaria:.1f}g
  Carboidratos: {total_carb:.1f}g / {self.carboidrato_diario:.1f}g
  Gorduras: {total_gord:.1f}g / {self.gordura_diaria:.1f}g

  REFEIÇÕES REGISTRADAS:
"""
        # Lista todas as refeições
        for r in self.refeicoes:
            relatorio += f"   • {r['refeicao']}: {r['alimento']} ({r['qtd']}) - {r['calorias']:.0f} kcal\n"

        relatorio += f"{'='*50}\n"
        return relatorio


# ==============================================
#   CLASSE: INTELIGÊNCIA ARTIFICIAL NUTRI
# ==============================================
class NutriIA:
    def __init__(self, usuario):
        self.usuario = usuario  # IA herda TODOS os dados do usuário

    #   FUNÇÃO 1: SUGERIR META PERSONALIZADA
    def Sugerir_Meta(self):
        if self.usuario.objetivo == "EMAGRECER":
            return f"""
  IA DIZ:
  Para emagrecer com saúde e manter massa muscular:
→ Coma entre {self.usuario.tmb - 400:.0f} e {self.usuario.tmb - 200:.0f} kcal/dia
→ Priorize proteínas e legumes, reduza açúcares e farinhas.
"""
        elif self.usuario.objetivo == "GANHAR MASSA":
            return f"""
  IA DIZ:
  Para ganhar massa magra com qualidade:
→ Coma cerca de {self.usuario.calorias_diarias:.0f} kcal/dia
→ Mantenha {self.usuario.proteina_diaria:.1f}g de proteína por dia.
→ Faça exercícios de força regularmente.
"""
        else:
            return f"""
  IA DIZ:
  Para manter seu peso e saúde:
→ Mantenha {self.usuario.calorias_diarias:.0f} kcal diárias.
→ Alimentação variada e equilibrada é o segredo.
"""

    #   FUNÇÃO 2: ANALISAR ALIMENTAÇÃO DO DIA
    def Analisar_Alimentacao(self):
        total_cal = sum(r['calorias'] for r in self.usuario.refeicoes)
        saldo = self.usuario.calorias_diarias - total_cal

        if saldo > 300:
            return f" IA: Você ainda tem {saldo:.0f} kcal livres hoje. Pode fazer um lanche leve (fruta/ovo) sem problemas!"
        elif saldo < -300:
            return f" IA: Cuidado! Você já passou {abs(saldo):.0f} kcal da meta. Tente comer coisas mais leves na próxima refeição."
        else:
            return " IA: Perfeito! Sua alimentação hoje está dentro do ideal, parabéns!"

    #  FUNÇÃO 3: CRIAR CARDÁPIO SEMANAL AUTOMÁTICO
    def Criar_Cardapio(self):
        if self.usuario.objetivo == "EMAGRECER":
            return """
  CARDÁPIO SUGERIDO PELA IA (EMAGRECER):
  CAFÉ: Ovo mexido + Pão Integral + Café preto
  ALMOÇO: Frango Grelhado + Salada Verde + Arroz Integral + Feijão
  LANCHE: Maçã + 1 colher de sopa de castanhas
  JANTA: Peixe Branco + Legumes cozidos + Batata-doce
  CEIA: Iogurte natural + Morangos
"""
        elif self.usuario.objetivo == "GANHAR MASSA":
            return """
  CARDÁPIO SUGERIDO PELA IA (GANHO DE MASSA):
  CAFÉ: 2 Ovos + Pão Integral + Queijo + Suco de Fruta
  ALMOÇO: Carne Vermelha/Frango + Arroz + Feijão + Legumes
  LANCHE: Vitamina de Fruta + Aveia + Ovo Cozido
  JANTA: Frango / Peixe + Macarrão / Batata-doce + Azeite
  CEIA: Leite / Iogurte + Aveia
"""
        else:
            return " CARDÁPIO EQUILIBRADO: Coma de tudo um pouco, variando os alimentos diariamente."


# ==============================================
#   SISTEMA PRINCIPAL / MENU INTERATIVO
# ==============================================
def Menu_Principal():
    print("\n" + "="*40)
    print(" NUTRI SAÚDE - SISTEMA COMPLETO + IA")
    print("="*40)

    #   CADASTRO DO USUÁRIO
    print(" CADASTRO DE USUÁRIO")
    nome = input("Nome completo: ")
    idade = int(input("Idade: "))
    peso = float(input("Peso atual (kg): "))
    altura = float(input("Altura (ex: 1.75): "))
    objetivo = input("Objetivo (Emagrecer / Ganhar Massa / Manter): ")

    #  CRIA O OBJETO E CALCULA TUDO
    usuario = Usuario(nome, idade, peso, altura, objetivo)
    usuario.Calcular_Tudo()

    #  LIGA A INTELIGÊNCIA ARTIFICIAL
    ia = NutriIA(usuario)

    #  LOOP DO SISTEMA
    while True:
        print("\n" + "-"*40)
        print(" MENU PRINCIPAL")
        print("1  Adicionar Refeição")
        print("2  Ver Relatório Completo")
        print("3  O que a IA diz? (Sugestões)")
        print("4  Ver Cardápio Semanal")
        print("5  Sair do Sistema")
        print("-"*40)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\n NOVA REFEIÇÃO")
            ref = input("Refeição (Café / Almoço / Lanche / Janta): ")
            alim = input("Nome do alimento: ")
            qtd = input("Quantidade (ex: 100g / 2 fatias): ")
            cal = float(input("Calorias totais: "))
            prot = float(input("Proteína (g): "))
            carb = float(input("Carboidrato (g): "))
            gord = float(input("Gordura (g): "))
            print(usuario.Adicionar_Refeicao(ref, alim, qtd, cal, prot, carb, gord))

        elif opcao == "2":
            print(usuario.Gerar_Relatorio())
            print(ia.Analisar_Alimentacao())  # IA analisa junto

        elif opcao == "3":
            print(ia.Sugerir_Meta())

        elif opcao == "4":
            print(ia.Criar_Cardapio())

        elif opcao == "5":
            print(" Saindo do Nutri Saúde... Sempre com você!")
            break

        else:
            print(" Opção inválida! Tente novamente.")


# ==============================================
#   INICIAR SISTEMA
# ==============================================
if __name__ == "__main__":
    Menu_Principal()
    