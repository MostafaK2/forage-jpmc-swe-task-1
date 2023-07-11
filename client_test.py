import unittest
from client3 import getDataPoint
from client3 import getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       stock = quote['stock']
       bid_price = float(quote['top_bid']['price'])
       ask_price = float(quote['top_ask']['price'])
       self.assertEquals(getDataPoint(quote), (stock, bid_price, ask_price, (bid_price+ask_price)/2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
       stock = quote['stock']
       bid_price = float(quote['top_bid']['price'])
       ask_price = float(quote['top_ask']['price'])
       self.assertEquals(getDataPoint(quote), (stock, bid_price, ask_price, (bid_price+ask_price)/2))

  def test_ratio_whenBidPriceGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    price1 = (float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price']))/2
    price2 = (float(quotes[0]['top_bid']['price']) + float(quotes[0]['top_ask']['price']))/2

    self.assertAlmostEqual(getRatio(price1,price2), price1/price2, places=4)
  
  def test_ratio_whenDivisorIsZero(self):
     price1 = 4
     price2 = 0

     self.assertIsNone(getRatio(price1, price2))


if __name__ == '__main__':
    unittest.main()
