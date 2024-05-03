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
        print("\nIsto será fácil para você.");
        return;
            
    elif(difficulty_value == 2):
        difficulty_name = str("Médio");
        min_range = int(0);
        max_range = int(100);
        chances_count = int(7);
        tips_count = int(3);
        print("\nVamos ter alguma diversão.");
        return;
            
    elif(difficulty_value == 3):
        difficulty_name = str("Díficil");
        min_range = int(0);
        max_range = int(1000);
        chances_count = int(10);
        tips_count = int(5);
        print("\nVocê realmente acredita que consegue?");
        return;
            
    elif(difficulty_value == 4):
        difficulty_name = str("Extremo");
        min_range = int(-1000);
        max_range = int(1000);
        chances_count = int(10);
        tips_count = int(7);
        print("\nÉ melhor você desistir, ou acha que vou facilitar para você?");
        return;
            
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
        print("\nBem... Veremos se você irá criar algo inovador.");
        return;
    else:
        os.system("cls");
        print("Valor inválido para a dificuldade.\n");
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
    
    print("Estou pensando em um número... Vamos começar!");
    time.sleep(0.2);
    print(f"Lembrando que o intervalo escolhido é de {min_range} até {max_range}");
    
    while chances_count >= 0:
        user_attempt = int(input("\nQual número você acha que estou pensando? "));
        chances_count -= 1;
    
        if (user_attempt != sorted_number):
            print(f"Resposta errada, você ainda tem {chances_count} chances.");
            
            if (tips_count > 0):
                wants_tip = bool(input(f"você possui {tips_count} dicas restando, deseja usar uma? [ENTER para passar] "));
                
                if (wants_tip):
                    if (user_attempt > sorted_number):
                        number_state = "maior";
                    else:
                        number_state = "menor";
                    
                    print(f"Aqui esta sua dica. O número é {number_state} que {user_attempt}.");
                    tips_count -= 1;
                else:
                    print("Como você não quer usar sua dica, vamos prosseguir");
            else:
                print("Você está cada vez mais próximo do fim, e está sem dicas.");
                
        else:
            print(f"Você acertou, eu realmente estava pensando no número {sorted_number}.");
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
                                    "-1 - Desistir.\n" +
                                    "Escolha: "));
        
        if (game_menu_value == 1):
            runGame();
        elif (game_menu_value == 2):
            configureGame();
        elif (game_menu_value == -1):
            print("Você desistiu? Nunca crio expectativas, mas espero que você tente novamente.");
            exit();
        else:
            os.system("cls");
            print("Valor inválido para a o menu do jogo.\n");
