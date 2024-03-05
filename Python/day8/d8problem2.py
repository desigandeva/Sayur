# problem 2
# 
# VIP -> profit 30% of ticket price + Rs120 for every ticket sold.
# General -> profit 20% of ticket price + Rs80 for every ticket sold.
# Matinee -> profit 15% of the ticket price.
# 
# build the profit calculation function()
def profitCal(mclass,ticket_price):
    if(mclass=="vip"):
        ticket_price = (ticket_price*30/100) + ticket_price
    elif(mclass=="general"):
        ticket_price = (ticket_price*20/100) + ticket_price
    elif(mclass=="matinee"):
        ticket_price = (ticket_price*15/100) + ticket_price
    return ticket_price

# build total collection function()
def totalCollection():
    # print greeting
    print("Wellcome!, to Theatre revenue ")

    # get vip ticket price
    vip_ticket_price = float(input("Enter Vip ticket price : "))
    # get no of vip ticket sold
    no_of_vticket =  int(input("Enter no of Vip ticket sold : "))
    # get general ticket price
    general_ticket_price = float(input("Enter General ticket price : "))
    # get no of general ticket sold
    no_of_gticket =  int(input("Enter no of General ticket sold : "))
    # get matinee ticket price
    matinee_ticket_price = float(input("Enter Matinee show ticket price : "))
    # get no of matinee ticket sold
    no_of_mticket =  int(input("Enter no of Matinee show ticket sold : "))

    # assign total collection initialy 0
    total_collection = 0

    # find total vip ticket price with profit
    total_collection = total_collection + (profitCal("vip",vip_ticket_price)*no_of_vticket)
    # find total general ticket price add to vip ticket price with profit
    total_collection = total_collection + (profitCal("general",general_ticket_price)*no_of_gticket)
    # find total matinee ticket price add with vip and general price with profit
    total_collection = total_collection + (profitCal("matinee",matinee_ticket_price)*no_of_mticket)

    # return the total collection
    return total_collection

# call total colletion function()
total_revenue = totalCollection()
# print total revenue
print("Total revenue of this day is :",total_revenue)

