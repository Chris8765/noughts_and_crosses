# Gra "Kółko i krzyżyk"

# stałe globalne
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
  print(
  """
  Instrukcja do gry \"Kółko i krzyżyk\".

  Swoje posunięcia wskażesz poprzez wprowadzenie liczby z zakresu 0 do 8.

  Liczba ta odpowiada pozycji na planszy zgodnie z poniższym schematem:

  0 | 1 | 2
  ---------
  3 | 4 | 5
  ---------
  6 | 7 | 8

  """  
  )

def ask_yes_no(question):
    """Pytanie, na które można odopowiedzieć tak lubi nie."""
    
    response = None
    
    while response not in range ("t", "n"):
        response = input(question).lower()
        return response

def ask_number(question, low, high):
    """Popros o podanie liczby z odpowiedniego zakresu."""
    response = None
    while response not in range (low, high):
        response = int(input(question))
    return response

def pieces():
    """Ustalamy czy pierwszy ruch należy do gracza, czy do komputera."""
    go_first = ask_yes_no("Czy chcesz mieć prawo do pierwszego ruchu? (t/n): ")
    if go_first == "t":
        print("A więc pierwszy ruch należy do Ciebie.")
        



def main():
  
  display_instruct()

main()
input("\n\nAby zakończyć grę, naciśnij klawisz Enter.")