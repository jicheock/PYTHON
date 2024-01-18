def hello(some):
    print('안녕')
    some()
def bye():
    print("잘가")
print(bye)

egg=['🐣']
def cookegg(egg,index,recipe):
    recipe(egg,index)
def makefry(egg,index):
    egg[index]='🐔'
def makefood(egg, index):
          egg[index]='🥠'


