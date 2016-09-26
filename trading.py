# tambah error handling ETC-BTC kebalik (belum)
# FIRST CODER : RAHMAT WAHYU HADI a.k.a bl4ckM4mba
# ---=== editted on september '16 by DANDY KALMA RAHMATULLAH a.k.a. bobi ===---


from bittrex import apiBittrex 
import json 
import telepot 
from time import sleep 
import sys 


bot = apiBittrex('df18e1d1ac4945d7b4e753d4a0e1a760', 'd2e45d6cbf414df2b899afa21b3d7e5c')
# bot code for API
telegram = telepot.Bot('237352669:AAHxTCWsz7XJjfp3MuVOl1gJtRbhKnX_LGw')

try:
	coin = str(sys.argv[1])

	altcoin = bot.getmarketsummary(coin)

		
	listhargatinggi = []
	listhargaterendah = []
	alamat = 189293115
	
	try:
		hargaterendah 	= altcoin[0]["Low"]
		listhargaterendah.append(hargaterendah)
		hargatertinggi 	= altcoin[0]["High"]
		listhargatinggi.append(hargatertinggi)
		pembelianterahir = altcoin[0]["Last"]
	except Exception:
		print "Tulisannya kebalik om"

	telegram.sendMessage(alamat , "COIN "+coin+" SUDAH DIDAFTARKAN")
	perulangan = True
	while perulangan is True:
		try:
			sleep(10)
			listaltcoin = bot.getmarketsummary(coin)
			bid 		= listaltcoin[0]["Bid"]
			ask 		= listaltcoin[0]["Ask"]
			last  	 	= listaltcoin[0]["Last"]
			volume 		= listaltcoin[0]["Volume"]
			low 		= listaltcoin[0]["Low"]
			high 	 	= listaltcoin[0]["High"]


			BTC = bot.getbalance("BTC")
			jumlahBTC = BTC["Balance"]


			if (jumlahBTC < 0.05):
				telegram.sendMessage(alamat , "Jumlah bitcoin anda kurang dari 0.05")
		
			else :
				order = bot.getopenorders(coin)
				if not order :

					modalbeli = jumlahBTC / 1.1
					hargabeliaman = float(listhargaterendah[-1] / 2)
					hargabeli = float(listhargaterendah[-1] / 1.1)
				
				

					if (last < hargabeliaman ) or (last ==  hargabeliaman):
						totalbeli = float(modalbeli / last)

						beli = bot.buylimit(coin, totalbeli, last)

						listhargaterendah.append(low)
						listhargatinggi.append(high)
						sleep(2)	
						order = bot.getopenorders(coin)
						if not order :
							telegram.sendMessage(alamat, "Bos anda telah melakukan order pada coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")

						else:
							jumlahcoin = bot.getbalance(coin)
							telegram.sendMessage(alamat, "Bos anda telah membeli coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")


					elif (last < hargabeli) or (last == hargabeli):
						totalbeli = float(modalbeli / last)

						beli = bot.buylimit(coin, totalbeli, last)

						listhargaterendah.append(low)
						listhargatinggi.append(high)	
						sleep(2)
						order = bot.getopenorders(coin)
						if not order :
							telegram.sendMessage(alamat, "Bos anda telah melakukan order pada coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")
						else:
							jumlahcoin = bot.getbalance(coin)
							telegram.sendMessage(alamat, "Bos anda telah membeli coin :"+coin+ "\nDengan harga :"+last+ "\nDengan jumlah coin :"+jumlahcoin+".")

				else:
					telegram.sendMessage(alamat, "Anda sedang melakukan order pada Coin "+coin+ ".")


		except Exception:
			telegram.sendMessage(alamat , "Bot mati")

			perulangan = True
except Exception:
	print "Nama koin belum ada atau terbalik"
