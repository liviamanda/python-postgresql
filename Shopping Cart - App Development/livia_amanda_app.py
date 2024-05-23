from tabulate import tabulate

items = {'Powder': 75000,
        'Foundation': 120000,
        'Lipstick': 60000,
        'Mascara': 90000,
        'Blush': 60000}
    
class cartItem:
    '''
    Class ini berfungsi sebagai representasi item yang dapat dimasukkan ke dalam shopping cart.
    Terdapat 3 atribut, yaitu nama, jumlah, dan juga harga item.
    '''
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

class shoppingCart:
    '''
    Class ini berfungsi sebagai representasi keranjang belanja yang memiliki beberapa fungsi, seperti
    menambah item, mengurangi item, menghitung total belanja, dan lain-lain.
    '''
    def __init__(self):
        '''
        Method ini berfungsi sebagai inisiasi yang wajib diinput ketika membuat sebuah class.
        
        Contoh penggunaan:
            cart = shoppingCart()
        '''
        self.items = []

    def addItem(self, object):
        '''
        Method ini berfungsi untuk menambahkan item yang diinginkan ke dalam shopping cart.
        
        Contoh penggunaan:
            cart = shoppingCart()
            item = cartItem("Lipstick", 60000)
            
            cart.addItem(item)
            --------
            Output:
            Lipstik is successfully added to cart!
        '''
        self.items.append(object)

    def removeItem(self):
        '''
        Method ini berfungsi untuk menghapus item yang sebelumnya ditambahkan ke shopping cart.
        
        Terdapat atribut removedItem, yaitu nama item yang ingin dihapus
        
        Contoh penggunaan:
            cart = shoppingCart()
            cart.add_item(Item("Powder", 75000))

            cart.removeItem("Powder")
            --------
            Output:
            Powder has been removed from the cart.
        '''
        
        if not self.items:
            print("The cart is currently empty.")
        else:
            removedItemName = input("\nEnter item name to remove: ").capitalize()
            foundItem = None
            for item in self.items:
                if removedItemName == item.name:
                    foundItem = item
                    break
            
            if foundItem:
                itemQty = int(input("Enter the quantity of the item (number only): "))
                if itemQty <= foundItem.quantity:
                    foundItem.quantity -= itemQty
                    print(f"{itemQty}x {removedItemName} has been removed from the cart.")
                    if foundItem.quantity == 0:
                        self.items.remove(foundItem)
                else:
                    print(f"Insufficient quantity of {removedItemName} in the cart.")
            else:
                print(f"{removedItemName} is not in the cart.")

    def viewCart(self):
        '''
        Method ini berfungsi untuk menampilkan semua item dalam shopping cart jika ada dan pesan bahwa 
        shopping cart kosong jika tidak ada.

        Argumen yang digunakan adalah objek self yang berasal dari class shoppingCart.

        Contoh penggunaan:
            cart = shoppingCart()
            cart.add_item(Item("Lipstik", 60000))

            cart.viewCart()
            --------
            Output:
            Items in the cart:
            Lipstik = Rp.60000
        '''
        if not self.items:
            print("\nThe cart is currently empty.")
        else:
            print("\nCurrent items in cart: ")
            print(f'\n{"No.":<3} {"Item":<15} {"Qty":<5}')
            no = 1
            for item in self.items:
                print(f'{no:<3} {item.name:<15} {item.quantity:<5}')
                no += 1

    def emptyCart(self):
        '''
        Method ini berfungsi untuk menghapus semua item dalam shopping cart.

        Argumen yang digunakan adalah objek self yang berasal dari class shoppingCart.

        Contoh penggunaan:
            cart = shoppingCart()
            cart.add_item(Item("Lipstik", 60000))

            cart.emptyCart()
            --------
            Output:
            Cart is now empty
        '''
        self.items.clear()
        print("\nCart is now empty.")

    def totalPrice(self):
        '''
        Method ini berfungsi untuk menghitung total harga dari semua item yang telah ditambahkan 
        pada shopping cart dengan menggunakan rumus sum.

        Argumen yang digunakan adalah objek self yang berasal dari class shoppingCart.

        Contoh penggunaan:
            cart = shoppingCart()
            cart.addItem(Item("Lipstick", 60000))
            cart.addItem(Item("Bedak", 75000))

            cart.totalPrice()
            -----------------------------------------
            Output : Total purchases: 135000
        '''
        print(f'{"\nItem":<15} {"Qty":<5} {"Price":<8} {"Subtotal":<10}')
        print("-----------------------------------------")
        totalSubtotal = 0
        for item in self.items:
            if item.quantity > 0:
                subtotal = item.quantity * item.price
                totalSubtotal += subtotal
                print(f'{item.name:<15} {item.quantity:<5} {item.price:<8}{subtotal:<10}')
        return totalSubtotal

def main(items):
    '''
    Function ini berfungsi sebagai alur program utama untuk keranjang belanja. User dapat memilih aksi
    apa yang diinginkan dan program akan mengeluarkan output sesuai yang diminta.
    '''    
    print("\n============================")
    print(" Welcome to Blossom Beauty!")
    print("============================")
    print("\nHow may we help you?")

    cart = shoppingCart()

    while True:
        print("\nMain Menu:")
        print("1. View available items")
        print("2. Add item to cart")
        print("3. Remove item from cart")
        print("4. Display items in cart")
        print("5. Empty cart")
        print("6. View total purchases")
        print("7. Exit")

        choice = input("\nPlease enter the number you want: ")

        if choice == '1':
            print(f'\nHere are our available items:')
            print(tabulate(items.items(), headers=['Item', 'Price'], tablefmt="fancy_grid"))
            
            back = None
            while back != '0':
                back = input("\nPlease enter 0 and press Enter to go back to Main Menu: ")
                if back != '0':
                    print("Invalid input. Please enter '0' to go back.")
                
        elif choice == '2':
            while True:
                addedItem = input("\nEnter item name to buy: ").capitalize()
                if addedItem in items:
                    break
                else:
                    print(f"{addedItem} not found in the available items.")
            while True:
                try:
                    itemQty = int(input("Enter the quantity of the item (number only): "))
                    itemPrice = items[addedItem]
                    newCartItem = cartItem(addedItem, itemQty, itemPrice)
                    cart.addItem(newCartItem)
                    print(f"{newCartItem.quantity}x {newCartItem.name} is successfully added to cart!")
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number for quantity.")

        elif choice == '3':
            cart.removeItem()

        elif choice == '4':
            cart.viewCart()

        elif choice == '5':
            cart.emptyCart()

        elif choice == '6':
            total = cart.totalPrice()
            print(f"\nTotal purchases: {total}")

        elif choice == '7':
            print("\nThank you for choosing Blossom Beauty! Have a nice day :)")
            break

        else:
            print("\nInvalid input. Please only enter the number available (1-7)")

if __name__ == '__main__':
    '''
    Variabel items berfungsi untuk menyimpan daftar item dan juga harga yang terdapat di toko.
    '''
    main(items)
