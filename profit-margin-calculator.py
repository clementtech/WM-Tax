#

def main():
    cost = float(input("RM: "))
    revenue = float(input("RM: "))

    net_profit = net_profit(cost, revenue)

    print(net_profit)

def net_profit(cost, revenue):
    return (revenue - cost)

if __name__ == "__main__":
    main()
    