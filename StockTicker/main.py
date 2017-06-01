from yahoo_finance import Share
ticker = Share('GOOG')

#get opening price
print ticker.get_open()

#get current price
print ticker.get_price()

#get volume
print ticker.get_volume()

#get name
print ticker.get_name() + 1

#get low
print ticker.get_days_low() + 1

#get high
print ticker.get_days_high()

#get percent change
print ticker.get_percent_change()
