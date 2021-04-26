import PySimpleGUI as sg 
import os.path
import PIL.Image 
import io
import base64
from foodClass import *
# Burger, BeefBurger, Fries, chickenNuggets, Water, Coke, Sprite, User, Details


def convert_to_bytes(file_or_bytes, resize=None):
    '''
    Will convert into bytes and optionally resize an image that is a file or a base64 bytes object.
    Turns into  PNG format in the process so that can be displayed by tkinter
    :param file_or_bytes: either a string filename or a bytes base64 image object
    :type file_or_bytes:  (Union[str, bytes])
    :param resize:  optional new size
    :type resize: (Tuple[int, int] or None)
    :return: (bytes) a byte-string object
    :rtype: (bytes)
    '''
    if isinstance(file_or_bytes, str):
        img = PIL.Image.open(file_or_bytes)
    else:
        try:
            img = PIL.Image.open(io.BytesIO(base64.b64decode(file_or_bytes)))
        except Exception as e:
            dataBytesIO = io.BytesIO(file_or_bytes)
            img = PIL.Image.open(dataBytesIO)
 
    cur_width, cur_height = img.size
    if resize:
        new_width, new_height = resize
        scale = min(new_height/cur_height, new_width/cur_width)
        img = img.resize((int(cur_width*scale), int(cur_height*scale)), PIL.Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
sg.theme('DarkAmber')
 


#Order List
orderList = []



#Info Page (MAINCPAGE)

image2 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/sides.png')
image9 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/entree.png')
image5 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/drinks.png')
layout = [ 
    [sg.Text('Hello Welcome to the online resturant.', text_color= 'green')], 
    [sg.Text('Please enter your Name, Age, and Phone.', text_color = 'red')], 
    [sg.Text('Name', size =(15, 1)), sg.InputText(size = (30,1))], 
    [sg.Text('Age', size =(15, 1)), sg.InputText(size = (30,1))], 
    [sg.Text('Phone', size =(15, 1)), sg.InputText(size = (30,1))],     


    [sg.Submit(), sg.Cancel()] 
] 
#CREATES WINDOW
window = sg.Window('Customer Information', layout)



#Entree Page (ENTREE)

chickenAmount = 0
beefAmount = 0

def EntreeWindow():
    image1 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/chicken1.png')
    image3 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/burger2.png')

    chicken = 6
    beef = 8
    layout = [ 
        [sg.Text('This is the Entree Ordering Page.', text_color= 'green')], 
        [sg.Text('Please click on the entree you want to order.', text_color = 'red')],    
        [sg.Text('Chicken Burger:'),sg.Button('',image_data=image1,image_size=(140,140),border_width=0,pad=(100,10)),sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'ChickenOrder')], 
        [sg.Text('Price: $' + str(chicken), text_color = 'white')], 
        [sg.Text('Ingredients: Chicken, White Bread Buns, Pickles, and American Cheese.', text_color = 'red')],
        [sg.Text('Beef Burger:'),sg.Button('',image_data=image3,image_size=(240,155),border_width=0,pad=(100,10)), sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'BeefOrder')],
        [sg.Text('Price: $' + str(beef), text_color = 'white')], 
        [sg.Text('Ingredients: Beef Patty, Sesame Bun, Iceberg Lettuce, and American Cheese.', text_color = 'red')], 


        [sg.Submit(), sg.Cancel()] 
    ] 
 
    window = sg.Window('Entree Page', layout)


    #TRUE LOOP
    while True:
        event, values = window.read() 
        # print(event, values[0], values[1], values[2])
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'ChickenOrder':
            cburger = Burger('Chicken Burger', values[0], chicken)
            chickenAmount = cburger.orderBurger()
            print(chickenAmount)
            details = Details(cburger.name, chickenAmount)
            orderList.append(details)
        elif event == 'BeefOrder':
            bburger = BeefBurger('Beef Burger', values[1], beef)
            beefAmount = bburger.orderBurger()
            print(beefAmount)
            details = Details(bburger.name, beefAmount)
            orderList.append(details)
            window.close() 


#Sides Page (SIDES)

friesAmount = 0
nuggetsAmount = 0

def SidesWindow():
    image2 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/fries.png')
    image4 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/nuggets.png')
    image5 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/drinks.png')

    fries = 3
    nuggets = 5

    layout = [ 
        [sg.Text('This is the Sides Ordering Page.', text_color= 'green')], 
        [sg.Text('Please click on the side you want to order.', text_color = 'red')],    
        [sg.Text('French Fries:'),sg.Button('',image_data=image2,image_size=(200,300),border_width=0,pad=(100,10)), sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'FriesOrder')], 
        [sg.Text('Price: $' + str(fries), text_color = 'white')], 
        [sg.Text('Ingredients: potatoes, vegetable oil, hydrogenated soybean oil', text_color = 'red')],
        [sg.Text('Chicken Nuggets:'),sg.Button('',image_data=image4,image_size=(240,159),border_width=0,pad=(100,10)), sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'NuggetsOrder')],
        [sg.Text('Price: $' + str(nuggets), text_color = 'white')],
        [sg.Text('Ingredients: White boneless chicken, vegetable oil, water, enriched flour, vegetable starch', text_color = 'red')],
        [sg.Submit(), sg.Cancel()] 
    ] 
    
    window = sg.Window('Sides Page', layout)

    #TRUE LOOP
    while True:
        event, values = window.read() 
        # print(event, values[0], values[1], values[2])
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'FriesOrder':
            fries = Fries('Fries', values[0], fries)
            friesAmount = fries.orderFries()
            print(friesAmount)
            details = Details(fries.name, friesAmount)
            orderList.append(details)
        elif event == 'NuggetsOrder':
            nuggets = chickenNuggets('Chicken Nuggets', values[1], nuggets)
            nuggetsAmount = nuggets.orderchickenNuggets()
            print(nuggetsAmount)
            details = Details(nuggets.name, nuggetsAmount)
            orderList.append(details)
            window.close() 


# Drinks Page (DRINKS)

waterAmount = 0
cokeAmount = 0
spriteAmount = 0

def DrinksWindow():
    image6 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/water.png')
    image7 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/coke.png')
    image8 = convert_to_bytes('C:/Users/lijac/OneDrive/Documents/code/python/createProject/image/sprite.png')

    water = 1
    coke = 2
    sprite = 2

    layout = [
        [sg.Text('This is the Drinks Ordering Page.', text_color= 'green')], 
        [sg.Text('Please click on the drink you want to order.', text_color = 'red')],    
        [sg.Text('Water:'),sg.Button('',image_data=image6,image_size=(240,152),border_width=0,pad=(100,10)),  sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'WaterOrder')], 
        [sg.Text('Price: $' + str(water), text_color = 'white')], 
        [sg.Text('Ingredients: fresh spring water', text_color = 'red')],
        [sg.Text('Coca-Cola:'),sg.Button('',image_data=image7,image_size=(240,167),border_width=0,pad=(100,10)),  sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'CokeOrder')],
        [sg.Text('Price: $' + str(coke), text_color = 'white')], 
        [sg.Text('Ingredients: carbonated water, high fructose corn syrup, caramel coloring, phosphoric acid natural flavoring, caffeine', text_color = 'red')],
        [sg.Text('Sprite:'),sg.Button('',image_data=image8,image_size=(240,135),border_width=0,pad=(100,10)), sg.InputText(default_text= 'Amount', size = (10,1)), sg.Button('Order', key = 'SpriteOrder')],
        [sg.Text('Price: $' + str(sprite), text_color = 'white')], 
        [sg.Text('Ingredients: water, citrus acid, natural citrus flavoring, high fructose corn syrup', text_color = 'red')],
        [sg.Submit(), sg.Cancel()] 
    ] 
    
    window = sg.Window('Drinks Page', layout)

    #TRUE LOOP
    while True:
        event, values = window.read() 
        # print(event, values[0], values[1], values[2])
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'WaterOrder':
            water = Water('Water', values[0], water)
            waterAmount = water.orderWater()
            print(waterAmount)
            details = Details(water.name, waterAmount)
            orderList.append(details)
        elif event == 'CokeOrder':
            coke = Coke('Coca-Cola', values[1], coke)
            cokeAmount = coke.orderCoke()
            print(cokeAmount)
            details = Details(coke.name, cokeAmount)
            orderList.append(details)
        elif event == 'SpriteOrder':
            sprite = Sprite('Sprite', values[2], sprite)
            spriteAmount = sprite.orderSprite()
            print(spriteAmount)
            details = Details(sprite.name, spriteAmount)
            orderList.append(details)
            window.close() 

# Menu Page (NAVIGATOR PAGE)

def MenuWindow():
    layoutSub = [ 
    [sg.Text('Entree Menu: '),sg.Button('',image_data=image9,image_size=(300,199),border_width=0,pad=(100,10), key = 'EntryMenu')], 
    [sg.Text('Sides Menu: '),sg.Button('',image_data=image2,image_size=(300,199),border_width=0,pad=(100,10), key = 'SidesMenu')], 
    [sg.Text('Drinks Menu: '),sg.Button('',image_data=image5 ,image_size=(300,199),border_width=0,pad=(100,10), key = 'DrinksMenu')],
         
    #[sg.Image(data=image1,key='__IMAGE__', size=(150, 160))],
    [sg.Ok(), sg.Cancel()] 
] 
    windowSub = sg.Window('Order', layoutSub)
    while True:
        event, values = windowSub.read()
        # print(event, values[0], values[1])
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == 'EntryMenu':
            EntreeWindow()
        elif event == 'SidesMenu':
            SidesWindow()
        elif event == 'DrinksMenu':
            DrinksWindow()
        elif event == 'Ok':
            OrderWindow()
    windowSub.close()


#Order Page (FINAL PAGE)


def OrderWindow():
    
    layout = [
    [sg.Text('All Ordered Items: ', text_color= 'green')], 
    
    ] 
    total = 0
    for i in orderList:
        layout.append([sg.Text(i.name), sg.Text(i.price)])
        total += i.price
    layout.append( [sg.Text('Total: '), sg.Text(total)])
    layout.append([sg.Submit(), sg.Cancel()])
    window = sg.Window('Order Page', layout)
    
    #TRUE LOOP
    while True:
        event, values = window.read() 
        # print(event, values[0], values[1], values[2])
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
    window.close() 

    
#TRUE LOOP
while True:
    event, values = window.read() 
    print(event, values[0], values[1], values[2])
    if event in (sg.WIN_CLOSED, 'Exit'):
            break
    elif event == 'Submit':
        User = User(values[0], values[2])
        User.printname()
        MenuWindow()
window.close() 
