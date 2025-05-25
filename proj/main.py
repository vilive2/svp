import sys
import types
from mytypes import *
from utils import *
from union import union
from product import product
from empty import empty

if __name__ == "__main__":

    while True:
        print("nbag-->", end='', flush=True)
        command = sys.stdin.readline().strip().split()
        
        match command[0]:
            case "help":
                print_help()
            case "exit":
                exit(0)
            case "empty":
                try:
                    A = read_nba_from_file(command[1])
                    print(empty(A))
                except Exception as e:
                    print("Error:", e)
                    print_help()
            case "union":
                try:
                    A = read_nba_from_file(command[1])
                    B = read_nba_from_file(command[2])
                    display(A, filename="nba_A")
                    display(B, filename="nba_B")
                    C = union(A, B)
                    display(C, filename="Union of Two NBA's")
                except Exception as e:
                    print("Error:", e)
                    print_help()
            case "product":
                try:
                    A = read_nba_from_file(command[1])
                    B = read_nba_from_file(command[2])
                    print(product(A, B))
                except Exception as e:
                    print("Error:", e)
                    print_help()
            
            case "display":
                try: 
                    A = read_nba_from_file(command[1])
                    display(A)
                except Exception as e:
                    print("Error:", e)
                    print_help()
                    
            case _:
                print_help()
            
            
