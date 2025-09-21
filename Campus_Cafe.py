"""
1.Define main
2.Print menu with prices
3.Collect user input:
a)how many coffees(int greater than 0)
b)how many muffins(int greater than 0)
c)tip percent(float greater than 0)
d)Message for a value error
4.Define line_total- calculate the price- number of items times price
5.Calculate subtotal(sum of line totals)
6.Calculate tax(subtotal*0.08875), tip(tip percent/100), and total(subtotal+tax+tip)
7.Define compute_total- get total price
8.Define format_currency before print(convert to string and round to hundreds place)
9.define print_receipt and format:
a)spacing
b)print coffee price, muffin price, subtotal,tax,tip each on separate lines, using format currency
10.Call main
 """
def main():
    print()
    print("======MENU======")
    print()
    print (" Coffee - $2.25 " )
    print()
    print (" Muffin - $2.75 " )
    print()
    try:
        coffees = int(input (" How many coffees? " ))
        if coffees<0:
            print("Please enter a positive number")
            coffees = int(input (" How many coffees? " ))
        print()
        muffins = int (input ( " How many muffins? " ))
        if muffins<0:
            print("Please enter a positive number")
            muffins = int (input ( " How many muffins? " ))
        print()
        tip_percent = float(input (" Enter tip percent " ))
        if tip_percent<0:
            print("Please enter a positive number")
            tip_percent = float(input (" Enter tip percent " ))
        print()
    except (ValueError):
        print("Invalid. Please enter an integer greater than 0")
    def line_total(unit_price:float,qty:int)->float:
        return(unit_price*qty)
    coffee_price = line_total(2.25,coffees)
    muffin_price = line_total(2.75,muffins)
    subtotal = (coffee_price + muffin_price ) 
    tax =  (subtotal * 0.08875)
    tip = ((subtotal * (tip_percent / 100)))
    def compute_totals(subtotal:float,tax_rate:float,tip_percent:float)->tuple[float,float,float]:
        return(subtotal+tax+tip)
    total = compute_totals(subtotal,tax,tip)
    def format_currency(x:float)->str:
        return(f"${x:.2f}")
    def print_receipt(coffees: int,muffins: int,subtotal:float, tax:float,tip:float)->None:
        print()
        print()
        print()
        print("-------Receipt-------")
        print()
        print(f" {coffees} x coffees @ $2.25 = {format_currency(coffee_price)}")
        print()
        print(f" {muffins} x muffins @ $2.75 = {format_currency(muffin_price)}")
        print()
        print(f"Subtotal = {format_currency(subtotal)}")
        print()
        print(f"Tax = {format_currency(tax)}")
        print()
        print(f"Tip = {format_currency(tip)}")
        print()
        print(f"Total = {format_currency(total)}")
        print()
        print("<<<<<<<<Thank you!>>>>>>>>>")
    print_receipt(coffees,muffins,subtotal,tax,tip)
main()

