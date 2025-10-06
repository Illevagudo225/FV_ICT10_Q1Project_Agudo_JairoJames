from pyscript import display, document

# 2 chatgpt uses, indicateed below in file. 1 google use. 


menu = {
     "item1": 11000,
     "item2": 12000,
     "item3": 2000,
     "item4": 1500,
     "item5": 2400
} 

def calculate_total():
     total = 0
     if document.getElementById("item1").checked: total += menu["item1"]
     if document.getElementById("item2").checked: total += menu["item2"]
     if document.getElementById("item3").checked: total += menu["item3"]
     if document.getElementById("item4").checked: total += menu["item4"]
     if document.getElementById("item5").checked: total += menu["item5"]
     return total

# i asked chatgpt how to use the return total thingy above

def show_order(e):
     name = document.getElementById("name").value
     address = document.getElementById("address").value
     contact = document.getElementById("contact").value
     total = calculate_total() 
 
     summary = f"""
     Name: {name} <br>
     
     Address: {address} <br>

     Contact: {contact} <br>

     Total: ₱{total} <br>

     """

# the code below i had no idea how to make it work so i asked chatpgpt what to put after display
     display(summary, target="output")
     #code below i was wondering why my br wasnt working for like 30 mins then i gave up and googled it now i remember...
     document.getElementById("output").innerHTML = summary