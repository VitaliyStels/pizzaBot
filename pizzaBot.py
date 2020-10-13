import telebot
from secureKeyChain import botApiToken
from orders import pizza1, pizza2, pizza3, pizza4, pizza5, pizza6, pizza7, pizza8, pizza9, pizza10, pizza1Price, pizza2Price, pizza3Price, pizza4Price, pizza5Price, pizza6Price
#from prders import pizza1Image, pizza2Image, pizza3Image, pizza4Image, pizza5Image, pizza6Image
bot = telebot.TeleBot(botApiToken)



LookForPizzaProducts = "Look for Products"
ContinueButton = "Continue"
ConfirmButton = "Confirm"
CancelButton = "Cancel"
BuyButton = "Buy"
Pizza1Taked = False
Pizza2Taked = False
Pizza3Taked = False
Pizza4Taked = False
Pizza5Taked = False
Pizza6Taked = False
Pizza7Taked = False
Pizza8Taked = False
Pizza9Taked = False
Pizza10Taked = False
TotalPrice = 0

ClientTotalTook = ""

ClientTookPizza1 = False
ClientTookPizza2 = False
ClientTookPizza3 = False
ClientTookPizza4 = False
ClientTookPizza5 = False
ClientTookPizza6 = False
ClientTookPizza7 = False
ClientTookPizza8 = False
ClientTookPizza9 = False
ClientTookPizza10 = False

ClientTookPosition1 = ""
ClientTookPosition2 = ""
ClientTookPosition3 = ""
ClientTookPosition4 = ""
ClientTookPosition5 = ""
ClientTookPosition6 = ""

PizzaOrderNumber = ""

UserHaveImages = False
OrderStage = "None"



keyboardHidded = telebot.types.ReplyKeyboardRemove()

keyboardDev = telebot.types.ReplyKeyboardMarkup()
keyboardDev.row('/cl','/err')


keyboardOrder = telebot.types.ReplyKeyboardMarkup()
keyboardOrder.row(LookForPizzaProducts)

keyboardPizza = telebot.types.ReplyKeyboardMarkup()
keyboardPizza.row(pizza1, pizza2, pizza3, pizza4, pizza5, pizza6, ContinueButton)

keyboardConfirmStep1 = telebot.types.ReplyKeyboardMarkup()
keyboardConfirmStep1.row(pizza1, pizza2, pizza3, pizza4, pizza5, pizza6, ContinueButton, ConfirmButton)

keyboardConfirmStep2 = telebot.types.ReplyKeyboardMarkup()
keyboardConfirmStep2.row(CancelButton, BuyButton)


""" ON /START COMMAND  """

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Welcome to Our Pizzeria Bot!', reply_markup=keyboardOrder)
    

@bot.message_handler(commands=['cl'])
def check_list(message):
    bot.send_message(message.chat.id, "{}".format(ClientTookPizza1))

@bot.message_handler(content_types=['text'])
def pizza_menu(message):
    global UserHaveImages
    global OrderStage
    """ ON LookForPizzaProducts Click  """

    if message.text == LookForPizzaProducts and UserHaveImages == False and OrderStage == "None":
        #bot.send_photo(message.chat.id, pizza1Image)
        bot.send_message(message.chat.id, pizza1)

        #bot.send_photo(message.chat.id, pizza2Image)
        bot.send_message(message.chat.id, pizza2)

        #bot.send_photo(message.chat.id, pizza3Image)
        bot.send_message(message.chat.id, pizza3)

        #bot.send_photo(message.chat.id, pizza4Image)
        bot.send_message(message.chat.id, pizza4)

        #bot.send_photo(message.chat.id, pizza5Image)
        bot.send_message(message.chat.id, pizza5)

        #bot.send_photo(message.chat.id, pizza6Image)
        bot.send_message(message.chat.id, pizza6)

        
        bot.send_message(message.chat.id, 'This all Pizzas that we can bring to you', reply_markup=keyboardPizza)
        UserHaveImages = True
        OrderStage = "UserChoosingPizza"





    elif message.text == LookForPizzaProducts and UserHaveImages == True and OrderStage == "None":
        bot.send_message(message.chat.id, 'Earlier all Pizzas that we can bring to you', reply_markup=keyboardPizza)
        OrderStage = "UserChoosingPizza"




    elif message.text == pizza1 and OrderStage == "UserChoosingPizza":  
        global Pizza1Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza1Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza1))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza1))
        counter(message)


    elif message.text == "devmode":
        bot.send_message(message.chat.id, "DevMode enabled. /start to restart.", reply_markup=keyboardDev)



    elif message.text == pizza2 and OrderStage == "UserChoosingPizza":
        global Pizza2Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza2Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza2))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza2))
        counter(message)
    


    elif message.text == pizza3 and OrderStage == "UserChoosingPizza":
        global Pizza3Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza3Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza3))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza3))
        counter(message)
    





    elif message.text == pizza4 and OrderStage == "UserChoosingPizza":
        global Pizza4Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza4Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza4))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza4))
        counter(message)
    



    elif message.text == pizza5 and OrderStage == "UserChoosingPizza":
        global Pizza5Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza5Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza5))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza5))
        counter(message)
    



    elif message.text == pizza6 and OrderStage == "UserChoosingPizza":
        global Pizza6Taked
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        Pizza6Taked = True
        UserTook(message)
        bot.send_message(message.chat.id, "You take '{}'".format(pizza6))
        print("Username: {}, First Name: {}, User ID: {} take {}".format(username, userid, userFirstName, pizza6))
        counter(message)





    elif message.text == ContinueButton  and OrderStage == "UserChoosingPizza":
        global TotalPrice
        print(TotalPrice)
        bot.send_message(message.chat.id, "Total cost {}. Press Confirm to make order.".format(TotalPrice), reply_markup=keyboardConfirmStep1)

    elif message.text == ConfirmButton and OrderStage == "UserChoosingPizza":
        
        bot.send_message(message.chat.id, "What your adress?", reply_markup=keyboardHidded)
        OrderStage = "GetUserAdress"
    elif OrderStage == "GetUserAdress":
        username = message.from_user.username
        userid = message.from_user.id
        userFirstName = message.from_user.first_name
        UserAdress = message.text
        UserTook(message)
        print("ORDER User {}, Name: {}, ID: {}, Adress: {} Took(Ordered): {}, {}, {}, {}, {}, {} Total Price: {}".format(username, userFirstName, userid, UserAdress, ClientTookPosition1, ClientTookPosition2, ClientTookPosition3, ClientTookPosition4,ClientTookPosition5,ClientTookPosition6, TotalPrice))
        bot.send_message(message.chat.id,"Thank you", reply_markup=keyboardOrder)
        OrderStage = "None"
        TotalPrice = 0
    else:
        bot.send_message(message.chat.id, "Please Follow steps by pressing on keyboard")


def UserTook(message):
    global ClientTotalTook
    global ClientTookPosition1
    global ClientTookPosition2
    global ClientTookPosition3
    global ClientTookPosition4
    global ClientTookPosition5
    global ClientTookPosition6
    global ClientTookPizza1
    global ClientTookPizza2
    global ClientTookPizza3
    global ClientTookPizza4
    global ClientTookPizza5
    global ClientTookPizza6
    if ClientTookPizza1 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition1 = pizza1
        ClientTookPizza1 = False
    elif ClientTookPizza1 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition2 = pizza1
        ClientTookPizza1 = False
    elif ClientTookPizza1 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition3 = pizza1
        ClientTookPizza1 = False
    elif ClientTookPizza1 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition4 = pizza1
        ClientTookPizza1 = False
    elif ClientTookPizza1 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition5 = pizza1
        ClientTookPizza1 = False
    elif ClientTookPizza1 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza1
        ClientTookPosition6 = pizza1
        ClientTookPizza1 = False
    
    
    elif ClientTookPizza2 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition1 = pizza2
        ClientTookPizza2 = False
    elif ClientTookPizza2 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition2 = pizza2
        ClientTookPizza2 = False
    elif ClientTookPizza2 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition3 = pizza2
        ClientTookPizza2 = False
    elif ClientTookPizza2 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition4 = pizza2
        ClientTookPizza2 = False
    elif ClientTookPizza2 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition5 = pizza2
        ClientTookPizza2 = False
    elif ClientTookPizza2 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza2
        ClientTookPosition6 = pizza2
        ClientTookPizza2 = False
    

    elif ClientTookPizza3 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition1 = pizza3
        ClientTookPizza3 = False
    elif ClientTookPizza3 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition2 = pizza3
        ClientTookPizza3 = False
    elif ClientTookPizza3 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition3 = pizza3
        ClientTookPizza3 = False
    elif ClientTookPizza3 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition4 = pizza3
        ClientTookPizza3 = False
    elif ClientTookPizza3 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition5 = pizza3
        ClientTookPizza3 = False
    elif ClientTookPizza3 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza3
        ClientTookPosition6 = pizza3
        ClientTookPizza3 = False
    

    elif ClientTookPizza4 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition1 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza4 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition2 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza4 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition3 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza4 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition4 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza4 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition5 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza4 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza4
        ClientTookPosition6 = pizza4
        ClientTookPizza4 = False


    elif ClientTookPizza5 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition1 = pizza5
        ClientTookPizza5 = False
    elif ClientTookPizza5 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition2 = pizza5
        ClientTookPizza5 = False
    elif ClientTookPizza5 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition3 = pizza5
        ClientTookPizza5 = False
    elif ClientTookPizza5 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition4 = pizza5
        ClientTookPizza5 = False
    elif ClientTookPizza5 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition5 = pizza5
        ClientTookPizza5 = False
    elif ClientTookPizza5 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza5
        ClientTookPosition6 = pizza5
        ClientTookPizza5 = False


    elif ClientTookPizza6 == True and ClientTookPosition1 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition1 = pizza6
        ClientTookPizza6 = False
    elif ClientTookPizza6 == True and ClientTookPosition2 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition2 = pizza6
        ClientTookPizza6 = False
    elif ClientTookPizza6 == True and ClientTookPosition3 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition3 = pizza6
        ClientTookPizza6 = False
    elif ClientTookPizza6 == True and ClientTookPosition4 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition4 = pizza6
        ClientTookPizza6 = False
    elif ClientTookPizza6 == True and ClientTookPosition5 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition5 = pizza4
        ClientTookPizza4 = False
    elif ClientTookPizza6 == True and ClientTookPosition6 == "":
        ClientTotalTook = ClientTotalTook + pizza6
        ClientTookPosition6 = pizza6
        ClientTookPizza4 = False



    """ COUNT PRICE FUNCTION """

def counter(message):
    while message.text != ContinueButton:
        global TotalPrice, Pizza1Taked, Pizza2Taked, Pizza3Taked, Pizza4Taked,Pizza5Taked,Pizza6Taked,Pizza7Taked,Pizza8Taked,Pizza9Taked,Pizza10Taked,ClientTookPizza1,ClientTookPizza2,ClientTookPizza3,ClientTookPizza4,ClientTookPizza5,ClientTookPizza6,ClientTookPizza7,ClientTookPizza8,ClientTookPizza9,ClientTookPizza10
        if Pizza1Taked == True:
            TotalPrice = TotalPrice + pizza1Price
            ClientTookPizza1 = True
            Pizza1Taked = False
            break
        elif Pizza2Taked == True:
            TotalPrice = TotalPrice + pizza2Price
            ClientTookPizza2 = True
            Pizza2Taked = False
            break
        elif Pizza3Taked == True:
            TotalPrice = TotalPrice + pizza3Price
            ClientTookPizza3 = True
            Pizza3Taked = False
            break
        elif Pizza4Taked == True:
            TotalPrice = TotalPrice + pizza4Price
            ClientTookPizza4 = True
            Pizza4Taked = False
            break
        elif Pizza5Taked == True:
            TotalPrice = TotalPrice + pizza5Price
            ClientTookPizza5 = True
            Pizza5Taked = False
            break
        elif Pizza6Taked == True:
            TotalPrice = TotalPrice + pizza6Price
            ClientTookPizza6 = True
            Pizza6Taked = False
            break


bot.polling()
