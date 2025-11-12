
def tipCalc(total, tipPercent):
    tip = total + (total*tipPercent)
    return tip

def main():
    totalPreTip = float(input("Enter the total: "))
    tip = float(input("Enter the tip percentage: "))/100

    print(f"The total after the tip is {tipCalc(totalPreTip, tip)}.")

main()