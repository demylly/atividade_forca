import random

def jogo_forca():
    filmes = [
        "vingadores ultimato", "homem aranha sem volta para casa", "batman o cavaleiro das trevas", "coringa", "avatar",
        "titanic", "interestelar", "matrix", "velozes e furiosos 7", "pantera negra",
        "doutor estranho", "thor ragnarok", "capitao america guerra civil", "jurassic park", "rei leao",
        "toy story", "procurando nemo", "divertidamente", "frozen", "harry potter",
        "senhor dos aneis", "hobbit", "deadpool", "logan", "transformers",
        "homem de ferro", "mulher maravilha", "esquadrao suicida", "venom", "aquaman",
        "shrek", "madagascar", "kung fu panda", "meu malvado favorito", "minions",
        "it a coisa", "invocacao do mal", "anabelle", "atividade paranormal", "o exorcista",
        "rocky", "creed", "gladiador", "300", "troia",
        "clube da luta", "forrest gump", "a espera de um milagre", "o lobo de wall street", "django livre"
    ]

    musicas = [
        "shape of you", "blinding lights", "despacito", "see you again", "uptown funk",
        "happy", "shake it off", "bad guy", "old town road", "sunflower",
        "stay", "industry baby", "as it was", "heat waves", "levitating",
        "perfect", "someone like you", "rolling in the deep", "hello", "set fire to the rain",
        "bohemian rhapsody", "we will rock you", "another one bites the dust", "don't stop me now", "radio ga ga",
        "billie jean", "thriller", "smooth criminal", "beat it", "black or white",
        "ai se eu te pego", "evidencias", "tempo perdido", "anna julia", "garota nacional",
        "cheia de manias", "metamorfose ambulante", "pais e filhos", "dias de luta dias de gloria", "so os loucos sabem",
        "enzo ferrari", "malvada", "vai malandra", "bum bum tam tam", "sentadona",
        "trem bala", "deixa a vida me levar", "ta escrito", "ela vai voltar", "velha infancia"
    ]

    gastronomia = [
        "pizza", "hamburguer", "cachorro quente", "lasanha", "macarrao",
        "feijoada", "churrasco", "arroz e feijao", "strogonoff", "frango grelhado",
        "sushi", "temaki", "yakisoba", "ramen", "sashimi",
        "taco", "burrito", "nachos", "guacamole", "quesadilla",
        "pastel", "coxinha", "kibe", "esfiha", "empada",
        "bolo de chocolate", "brigadeiro", "beijinho", "pudim", "sorvete",
        "panqueca", "waffle", "crepe", "croissant", "donut",
        "salada", "omelete", "tapioca", "açai", "granola",
        "pao de queijo", "cuscuz", "farofa", "moqueca", "acaraje",
        "batata frita", "nuggets", "hot roll", "poke", "hamburguer artesanal"
    ]

    palavra: str = random.choice(gastronomia)

    print("Bem-vindo ao jogo da forca!")
    print("------------------------------------------------")
    print("Escolha uma categoria:")
    print("------------------------------------------------")
    print("1. Filmes")
    print("2. Músicas")
    print("3. Gastronomia")
    print("------------------------------------------------")

    opcao = input("Digite o número da categoria desejada: ")

    if opcao == "1":
        palavra = random.choice(filmes)
    elif opcao == "2":
        palavra = random.choice(musicas)
    elif opcao == "3":
        palavra = random.choice(gastronomia)
    else:
        print("Opção inválida. Escolhendo Gastronomia por padrão.")
        palavra = random.choice(gastronomia)

    letras_acertadas = []
    for letra in palavra:
        if letra == " ":
            letras_acertadas.append(" ")
        else:
            letras_acertadas.append("_")

    acertou = False
    enforcou = False
    limite_tentativas = len(palavra.replace(" ", "")) + 6
    tentativas_restantes = limite_tentativas
    letras_tentadas = []

    def mostrar_letras_acertadas():
        for letra in letras_acertadas:
            print(letra, end=" ")

    print("Tente adivinhar a palavra secreta: ")
    while not acertou and not enforcou:
        # mostrar as letras acertadas
        mostrar_letras_acertadas()
        print("")
        print(f"Tentativas restantes: {tentativas_restantes}")

        chute = input("Digite uma letra: ").strip()
        if not chute:
            print("Digite pelo menos uma letra.")
            continue

        letra_chute = chute[0].upper()
        if letra_chute in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra_chute)

        acertou_letra = False
        for i in range(len(palavra)):
            if letra_chute == palavra[i].upper():
                letras_acertadas[i] = palavra[i]
                acertou_letra = True

        if not acertou_letra:
            tentativas_restantes -= 1
            print(f"Que pena! A letra '{letra_chute}' não está na palavra.")

        if tentativas_restantes <= 0:
            print("Você perdeu :(\nA palavra era:", palavra)
            enforcou = True
            break

        if "_" not in letras_acertadas:
            print("Parabéns, você acertou a palavra secreta!")
            mostrar_letras_acertadas()
            acertou = True

