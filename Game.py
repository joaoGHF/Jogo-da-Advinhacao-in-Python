# Projeto do aluno João Gabriel Horsth Fonseca
import random;
import time;
import os;

sorted_number= int(0);
difficulty_value = int(0);
wants_tip = bool(False);
is_win = bool(False);
wants_try_again = str("");

game_menu_value = int(0);

difficulty_name = str("");
min_range = int(0);
max_range = int(0);
tips_count = int(0);
chances_count = int(0);

initial_tips_count = int(0);
initial_chances_count = int(0);

user_attempt = int(0);
number_state = str("");

emoticon_1 = str("¯\_(ツ)_/¯");
emoticon_2 = str("( ‾ʖ̫‾)");
emoticon_3 = str("(￣＿￣)");
emoticon_4 = str("(°_°) ");
emoticon_5 = str("ツ");
emoticon_6 = str("(✪‿✪)");
emoticon_7 = str("⊙ ０⊙");

# Função que define os valores dos emoticons 
def setEmoticons():
    global emoticon_1;
    global emoticon_2;
    global emoticon_3;
    global emoticon_4;
    global emoticon_5;
    global emoticon_6;
    global emoticon_7;
    
    emoticon_1 = str("¯\_(ツ)_/¯");
    emoticon_2 = str("( ‾ʖ̫‾)");
    emoticon_3 = str("(￣＿￣)");
    emoticon_4 = str("(°_°) ");
    emoticon_5 = str("ツ");
    emoticon_6 = str("(✪‿✪)");
    emoticon_7 = str("⊙ ０⊙");

# Função que limpa os valores dos emoticons
def clearEmoticons():
    global emoticon_1;
    global emoticon_2;
    global emoticon_3;
    global emoticon_4;
    global emoticon_5;
    global emoticon_6;
    global emoticon_7;
    
    emoticon_1 = str("");
    emoticon_2 = str("");
    emoticon_3 = str("");
    emoticon_4 = str("");
    emoticon_5 = str("");
    emoticon_6 = str("");
    emoticon_7 = str("");
    

# Função que configura o jogo
def configureGame():
    
    global difficulty_name;
    global min_range;
    global max_range;
    global tips_count;
    global chances_count;
    global initial_tips_count;
    global initial_chances_count;

    print(f"\n{4*'='}MENU=DE=DIFICULDADE{4*'='}\n");

    difficulty_value = int(input("1 - Fácil, de 0 a 10, 4 chances, 3 dicas;\n" + 
                        "2 - Médio, de 0 a 100, 7 chances, 3 dicas;\n" + 
                        "3 - Díficil, de 0 a 1000, 10 chances, + 5 dicas;\n" + 
                        "4 - Extremo, de -1000 a 1000, 10 chances, 7 dicas;\n" + 
                        "5- Customizado.\n" + 
                        "Escolha: "));

    if(difficulty_value == 1):
        difficulty_name = str("Fácil");
        min_range = int(0);
        max_range = int(10);
        chances_count = int(4);
        tips_count = int(3);
        print(f"\nIsto será fácil para você {emoticon_3}");
            
    elif(difficulty_value == 2):
        difficulty_name = str("Médio");
        min_range = int(0);
        max_range = int(100);
        chances_count = int(7);
        tips_count = int(3);
        print(f"\nVamos ter alguma diversão {emoticon_5}");
            
    elif(difficulty_value == 3):
        difficulty_name = str("Díficil");
        min_range = int(0);
        max_range = int(1000);
        chances_count = int(10);
        tips_count = int(5);
        print(f"\nVocê realmente acredita que consegue? {emoticon_1}");
            
    elif(difficulty_value == 4):
        difficulty_name = str("Extremo");
        min_range = int(-1000);
        max_range = int(1000);
        chances_count = int(10);
        tips_count = int(7);
        print(f"\nÉ melhor você desistir, ou acha que vou facilitar para você? {emoticon_2}");
            
    elif(difficulty_value == 5):
        # Customizado
        difficulty_name = str("Customizado");
        min_range = int(input("Digite o valor mínimo: "));
        max_range = int(input("Digite o valor máximo: "));
        
        if(max_range <= min_range):
            os.system("cls");
            print(f"Valor inválido para o alcance {min_range} -> {max_range}.");
            return configureGame();
            
        chances_count = int(input("Digite a quantidade de chances: "));
        tips_count = int(input("Digite a quantidade de dicas: "));
        print(f"\nBem... Veremos se você criou algo inovador {emoticon_7}");
    else:
        os.system("cls");
        print(f"Valor inválido para a dificuldade.\n");
        configureGame();
        
    initial_tips_count = tips_count;
    initial_chances_count = chances_count;
        
# Função que executa o jogo
def runGame():
    global chances_count;
    global tips_count;
    global initial_chances_count;
    global initial_tips_count;
    global sorted_number;
    
    chances_count = initial_chances_count;
    tips_count = initial_tips_count;
    sorted_number = random.randint(min_range, max_range);
    
    is_win = False;
    
    print(f"Estou pensando em um número... Vamos começar! {emoticon_6}");
    time.sleep(0.2);
    print(f"Lembrando que o intervalo escolhido é de {min_range} até {max_range}");
    
    while chances_count > 0:
        user_attempt = int(input("\nQual número você acha que estou pensando? "));
        chances_count -= 1;
    
        if (user_attempt != sorted_number):
            print(f"Resposta errada {emoticon_4}, você ainda tem {chances_count} chances.");
            
            if (tips_count > 0):
                wants_tip = bool(input(f"você possui {tips_count} dicas restando {emoticon_5}, deseja usar uma? [ENTER para passar] "));
                
                if (wants_tip):
                    if (user_attempt < sorted_number):
                        number_state = "maior";
                    else:
                        number_state = "menor";
                    
                    print(f"Aqui esta sua dica. O número é {number_state} que {user_attempt}.");
                    tips_count -= 1;
                else:
                    print(f"Como você não quer usar sua dica, vamos prosseguir {emoticon_1}");
            else:
                print(f"Você está cada vez mais próximo do fim, e está sem dicas {emoticon_4}");
                
        else:
            print(f"Você acertou {emoticon_6}, eu realmente estava pensando no número {sorted_number}.");
            is_win = True;
            input("Aperte ENTER para continuar");
            break;
    
    if (is_win):
        print(f"\n{25*'*'}\n" + 
            f"{8 * '*'}IS_WINNER{8 * '*'}\n" + 
            f"{25*'*'}\n");
    else:
        print(f"\n{25*'*'}\n" + 
            f"{8 * '*'}GAME_OVER{8 * '*'}\n" + 
            f"{25*'*'}\n");

while True:
    # Explicação 
    print(f"{31*'='}");
    print(f"{7*'='}JOGO=DA=ADVIHAÇÃO{7*'='}");
    print(f"{31*'='}");
    print(f"Olá, seja bem vindo ao Jogo de Advinhação!");
    print(f"Você terá de advinhar o número que estou pensando.");
    print(f"E você terá opções para determinar a dificuldade do jogo");

    configureGame();
    #sorted_number = random.randint(min_range, max_range);
    
    while True:
        print(f"{9*'='}MENU=DO=JOGO{9*'='}");
        game_menu_value = int(input("1 - Iniciar Jogo.\n" +
                                    "2 - Reconfigurar Jogo.\n" +
                                    "3 - Habilitar/Desabilitar emoticons.\n" +
                                    "-1 - Desistir.\n" +
                                    "Escolha: "));
        
        if (game_menu_value == 1):
            runGame();
        elif (game_menu_value == 2):
            configureGame();
        elif (game_menu_value == 3):
            if (emoticon_1 == ""):
                setEmoticons();
                print(f"Emoticons ativados {emoticon_5}\n");
            else:
                clearEmoticons();
                print(f"Emoticons desativados\n");
        
        elif (game_menu_value == -1):
            print(f"Você desistiu? Nunca crio expectativas, mas espero que você tente novamente {emoticon_7}");
            exit();
        else:
            os.system("cls");
            print(f"Valor inválido para a o menu do jogo.\n");
