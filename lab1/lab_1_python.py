import sys
import math

def GetCoef(index, prompt):
    while True:
        try:
            coefStr = sys.argv[index]
            coef = float(coefStr)
            if index == 1 and coef == 0:
                raise ValueError("Коэффициент A не может равняться нулю.")
            
            return coef
        
        except IndexError:
            print("Аргумент не был передан через командную строку.")
            coefStr = input(prompt)
            try:
                coef = float(coefStr)
                if index == 1 and coef == 0:
                    raise ValueError("Коэффициент A не может равняться нулю.")
                return coef
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректное число.")

        except ValueError:
            print("Ошибка: Коэффицент некорректен.")
            coefStr = input(prompt)
            try:
                coef = float(coefStr)
                if index == 1 and coef == 0:
                    raise ValueError("Коэффициент A не может равняться нулю.")
                return coef
            except ValueError:
                print("Ошибка: Пожалуйста, введите корректное число.")



def Solution(a, b, c):

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        print("Дискриминант отрицательный.")
        return []
    
    y1 = (-b + math.sqrt(discriminant)) / (2 * a)
    y2 = (-b - math.sqrt(discriminant)) / (2 * a)
    
    roots = []
    
    if y1 >= 0:
        roots.append(math.sqrt(y1))
        roots.append(-math.sqrt(y1))
    
    if y2 >= 0:
        roots.append(math.sqrt(y2))
        roots.append(-math.sqrt(y2))
    
    return roots

def main():

    a = GetCoef(1, "Введите коэффициент A: ")
    b = GetCoef(2, "Введите коэффициент B: ")
    c = GetCoef(3, "Введите коэффициент C: ")

    roots = Solution(a, b, c)

    if not roots:
        print("Нет действительных корней.")
    else:
        print("Действительные корни уравнения:", sorted(set(roots)))

if __name__ == "__main__":
    main()
