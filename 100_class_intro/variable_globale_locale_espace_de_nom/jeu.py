from pi import pi as pipi

# Toutes les variables globales en majuscule
PI = 3.14

# Ce pi est une variable globale
pi = pipi()

def print_pi(pi):
    """pi est une variable locale"""
    print(pi)
    
def print_a(a):
    print(a)  
    
print_pi(3)
print_a(3)
print_pi(PI)
print_pi(pi)
print_pi()