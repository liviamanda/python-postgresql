'''
=======================================================================================================================

Graded Challenge 1 (Unit Test)

Name   : Livia Amanda Annafiah
Batch  : BSD-005

Program ini dibuat untuk menyediakan platform belanja produk kosmetik kepada pengguna dengan userinterface yang mudah

=======================================================================================================================

'''

import unittest
from livia_amanda_app import shoppingCart, cartItem

class testShoppingCart(unittest.TestCase):
    '''
    Class ini berfungsi untuk melakukan unit test terhadap main program yang telah dibuat. Hal ini dapat membantu programmer untuk mengecek apakah program yang
    dibuat sesuai dengan apa yang diinginkan.
    '''

    def setUp(self):
        self.items = {'Powder': 75000, 'Foundation': 120000, 'Lipstick': 60000, 'Mascara': 90000, 'Blush': 60000}
        self.cart = shoppingCart()

    def testAddItem(self):
        '''
        Method ini berfungsi untuk mengecek apakah function addItem di main program sudah berjalan dengan benar. Apabila user menambahkan salah satu item di self.items,
        program seharusnya menambahkan item sejumlah yang diinginkan ke dalam cart.
        '''
        self.cart.addItem("Lipstick")
        self.assertEqual(len(self.cart.items), 1)   # Pada contoh ini, dianggap bahwa user memasukkan 2 item ke dalam cart

    def testRemoveItem(self):
        '''
        Method ini berfungsi untuk mengecek apakah function removeItem di main program sudah berjalan dengan benar. Apabila user mengurangi salah satu item di cart,
        program seharusnya mengurangkan item sejumlah yang diinginkan dari cart.
        '''
        removedItem = cartItem('Lipstick', 2, 60000) # Pada contoh ini, dianggap bahwa pada cart sudah terdapat 2 item 'Lipstick
        self.cart.addItem(removedItem)
        self.cart.emptyCart()
        self.assertEqual(len(self.cart.items), 0)  # Pada contoh ini, dianggap bahwa user mengurangi 2 item 'Lipstick' sehingga output yang dihasilkan berjumlah 0

    def testTotalPrice(self):
        '''
        Method ini berfungsi untuk menghitung total harga belanjaan yang seharusnya dibayar oleh user. Jika pengguna telah menambahkan beberapa item ke dalam keranjang
        belanja, metode ini akan menghitung total harga dengan cara menambahkan harga dari setiap item, kemudian mengalikannya dengan jumlah pesanan (quantity) dari masing-masing item.
        '''
        item1 = cartItem('Powder', 2, 75000)        # Pada contoh ini, dianggap bahwa user telah memesan 2 item 'Powder' dan 1 item 'Foundation'
        item2 = cartItem('Foundation', 1, 120000)
        self.cart.items.extend([item1, item2])
        total = self.cart.totalPrice()
        expected_total = item1.quantity * item1.price + item2.quantity * item2.price
        self.assertEqual(total, expected_total)

if __name__ == '__main__':
    unittest.main()