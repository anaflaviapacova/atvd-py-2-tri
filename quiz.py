# Quiz Filosófico: Conhecimento a Priori vs a Posteriori

print("🧠 Quiz de Filosofia: Conhecimento a Priori vs a Posteriori")
print("=" * 60)
print("Instruções:")
print("- Digite 'P' para conhecimento A PRIORI")
print("- Digite 'E' para conhecimento A POSTERIORI (empírico)")
print("-" * 40)

# Lista de questões com explicações
questoes = [
    {
        "pergunta": "Todo triângulo tem três lados.",
        "resposta_correta": "P",
        "explicacao": "VERDADEIRO → Conhecimento a priori. Esta é uma verdade definicional da geometria que independe da experiência."
    },
    {
        "pergunta": "A água ferve a 100°C ao nível do mar.",
        "resposta_correta": "E",
        "explicacao": "VERDADEIRO → Conhecimento a posteriori. Esta verdade depende de observação empírica e condições específicas."
    },
    {
        "pergunta": "O sol nascerá amanhã.",
        "resposta_correta": "E",
        "explicacao": "VERDADEIRO → Conhecimento a posteriori. Baseia-se na experiência passada, não é uma necessidade lógica."
    },
    {
        "pergunta": "Esta mesa é de madeira.",
        "resposta_correta": "E",
        "explicacao": "VERDADEIRO → Conhecimento a posteriori. Requer verificação sensorial para confirmar."
    },
    {
        "pergunta": "A soma dos ângulos internos de um triângulo é 180 graus.",
        "resposta_correta": "P",
        "explicacao": "VERDADEIRO → Conhecimento a priori. Verdade matemática necessária que não depende da experiência."
    },
    {
        "pergunta": "O chocolate derrete quando exposto ao sol.",
        "resposta_correta": "E",
        "explicacao": "VERDADEIRO → Conhecimento a posteriori. Baseia-se na observação empírica de propriedades físicas."
    }
]

while True:
    pontuacao = 0
    print("\n" + "=" * 60)
    print("INICIANDO QUIZ - BOA SORTE!")
    print("=" * 60)
    
    # Loop através de todas as questões
    for i, questao in enumerate(questoes, 1):
        print(f"\nQuestão {i}: {questao['pergunta']}")
        
        # Validação da entrada
        while True:
            resposta = input("Sua resposta (P/E): ").strip().upper()
            
            if resposta == "":
                print("❌ Por favor, digite P para a priori ou E para a posteriori.")
                continue
            
            if resposta not in ['P', 'E']:
                print("❌ Opção inválida! Digite apenas P ou E.")
                continue
            else:
                break
        
        # Verifica se a resposta está correta
        if resposta == questao['resposta_correta']:
            print("✅ CORRETO!")
            pontuacao += 1
        else:
            print("❌ INCORRETO")
        
        # Mostra a explicação
        print(f"💡 {questao['explicacao']}")
        print("-" * 50)
    
    # Exibe a pontuação final
    print(f"\n🎯 QUIZ FINALIZADO! Sua pontuação: {pontuacao}/{len(questoes)}")
    
    # Feedback baseado na pontuação
    if pontuacao == len(questoes):
        print("🌟 EXCELENTE! Domínio total dos conceitos filosóficos!")
    elif pontuacao >= len(questoes) / 2:
        print("👍 BOM TRABALHO! Você compreende bem a diferença entre a priori e a posteriori.")
    else:
        print("💪 CONTINUE ESTUDANDO! Reveja os conceitos e tente novamente.")
    
    # Explicação geral
    print("\n" + "=" * 60)
    print("RESUMO DOS CONCEITOS:")
    print("A PRIORI → Conhecimento independente da experiência (ex: matemática, lógica)")
    print("A POSTERIORI → Conhecimento derivado da experiência (ex: ciências, observação)")
    print("=" * 60)
    
    # Pergunta se o usuário quer jogar novamente
    while True:
        jogar_novamente = input("\nDeseja refazer o quiz? (s/n): ").strip().lower()
        
        if jogar_novamente == "":
            print("Por favor, digite 's' para sim ou 'n' para não.")
            continue
        
        if jogar_novamente not in ['s', 'n']:
            print("Opção inválida! Digite apenas 's' para sim ou 'n' para não.")
            continue
        else:
            break
    
    if jogar_novamente == 'n':
        print("\nObrigado por testar seus conhecimentos filosóficos! 👋")
        break

    print("\n" + "=" * 60)
    print("REINICIANDO QUIZ...")
