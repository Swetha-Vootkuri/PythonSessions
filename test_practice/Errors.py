'''fruit_basket = {"apple": 3, "orange": 5, "banana": 3, "kiwi": 5}
print(fruit_basket)
fruit_basket = dict(apple=3, orange=5, banana=3, kiwi=5)
print(fruit_basket)

for key in fruit_basket:
    print(key)

for key in fruit_basket.keys():
    print(key)

for value in fruit_basket.values():
    print(value)

for key, value in fruit_basket.items():
    print(key, value)

for key in fruit_basket:
    print(key, fruit_basket[key])

print(fruit_basket["kiwi"])'''


a_dict = { 'entitlements':{'ids': ['ANALYTICS', 'BIGBASIC', 'CRICKET', 'CUSTOMER_LOGGING_ENABLED', 'D12', 'ETHAN_APP_1', 'FOOTBALL', 'HD', 'HDBASIC', 'HDPREMIUM', 'MOVIES', 'NETFLIX', 'PDL', 'SKY_DRM_CE', 'SKY_DRM_MR', 'SKY_IPPV', 'SPORTS', 'ULTRA+', 'VIP', 'SKY+', 'GATEWAYENABLER', 'SIDELOAD'], 'state': 'AVAILABLE'},
            'version': 2
          }

entitlements_list = a_dict["entitlements"]["ids"]
print(entitlements_list)''''''