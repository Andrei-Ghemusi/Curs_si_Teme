import random

# 11. Joc ghicit zarul
# Caută pe net și vezi cum se generează un număr random
# Ne imaginăm ca dai cu zarul și salvăm acest număr în dice_roll
#
# Luați un numărul ghicit de la utilizator
# Verificați și afișați dacă utilizatorul a ghicit
# Veți avea 3 opțiuni
# ● Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# ● Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# ● Ai ghicit. Felicitari! Ai ales x si zarul a fost y

player_choice = int(input("Predict the dice: "))
dice_roll = [1,2,3,4,5,6]
result_choice = random.choice(dice_roll)

def roll_dice():
  choices = {"player": player_choice, "result": result_choice}
  return choices

def check_win(player, result):
    if player == result:
        return f"Felicitari! Ai ales {player_choice} si zarul a fost {result_choice}"
    elif player > result:
        return f"Ai ales un numar mai mare. Ai ales {player_choice}  dar a fost {result_choice}"
    else:
        return f'Ai ales un numar mai mic. Ai ales {player_choice}  dar a fost {result_choice}'

roll = roll_dice()
final = check_win(roll["player"], roll["result"])
print(final)