# import telegram

# print(telegram.__bot_api_version__) # 6.7
# print(telegram.__bot_api_version_info__) # 6.7

# print(telegram.__version__) # 20.3
# print(telegram.__version_info__) # 20.3


try:
    son = 10
    print(son / 0)
except ZeroDivisionError:
    print("0 ga bo'lib bo'lmaydi")

except TypeError:
    print("Qiymatda xatolik bor")

except NameError:
    print("Nomida xatp bor")

except SyntaxError as err:
    print(err)

finally:
    print('Finishing up.')
