from tabnanny import check
from flask import Flask, render_template, request, redirect
import sqlite3 as sql
app = Flask(__name__)
host = 'http://127.0.0.1:5000/'





@app.route('/')
def index():
    return render_template('home.html')





@app.route('/home.html')
def home():
    return render_template('home.html')





@app.route('/reg.html', methods=['POST', 'GET'])
def newUser():
    if  request.method == 'POST':
        dun = request.form['user_name']
        dpw = request.form['user_password']
        link=sql.connect('account.db')
        link.execute('insert into Users(email,password) Values(?,?)',(dun,dpw))
        link.commit()
    return render_template('reg.html')





@app.route('/loginC.html', methods=['GET', 'POST'])
def loginScreen():
    if request.method == 'POST':
        result = loginCheckVender(request.form['user_name'], request.form['user_password'])
        result1 = loginCheckBoth(request.form['user_name'], request.form['user_password'])
        result2 = loginCheck(request.form['user_name'], request.form['user_password'])
        global current
        current = request.form['user_name']
        if len(result)==0 and len(result1)==0 and len(result2) ==0:
            return render_template('/wrongPass.html')
        elif len(result)!=0:
            aun1 = checkInfor_Ven_Bname(request.form['user_name'])[0][0]
            aun2 = checkInfor_Ven_Business_Address(request.form['user_name'])[0][0]
            aun3 = checkInfor_Ven_Customer_Service_Number(request.form['user_name'])[0][0]
            aun4 = checkInforStr(aun2)[0][0]
            aun5 = checkInforStr_num(aun2)[0][0]
            aun6= checkInforZip(aun2)[0][0]
            aun7 = checkInforCity(aun6)[0][0]
            aun8 = checkInforState(aun6)[0][0]
            aun9 = checkSellerBalance(request.form['user_name'])[0][0]
            aun10 = checkSellerInforAccountnum(request.form['user_name'])[0][0]
            aun11 = checkSellerInforRounting(request.form['user_name'])[0][0]
            aun12 = ProductList(request.form['user_name'])
            aun13 = ProductList1(request.form['user_name'])
            return render_template('vendors.html',email=request.form['user_name'], company=aun1, City=aun7, street_name=aun4, Str_num=aun5, State=aun8, Zipcode=aun6, Customer_Service_Number=aun3,balance = aun9, account_num=aun10, rounting_num=aun11, answer2=aun12, answer3=aun13)
        
        elif len(result1)!=0:
            current = request.form['user_name']
            dun1 = checkInforF(request.form['user_name'])[0][0]
            dun2 = checkInforL(request.form['user_name'])[0][0]
            dun3 = checkInforG(request.form['user_name'])[0][0]
            dun4 = checkInforE(request.form['user_name'])[0][0]
            dun5 = checkInforA(request.form['user_name'])[0][0]



            ''''Home Address Function Call'''
            dun6 = checkInforHome(request.form['user_name'])[0][0]
            dun7 = checkInforAdd(dun6)[0][0]
            dun8 = checkInforStr(dun6)[0][0]
            dun9 = checkInforStr_num(dun6)[0][0]
            zip= checkInforZip(dun6)[0][0]
            dun10 = checkInforCity(zip)[0][0]
            dun11 = checkInforState(zip)[0][0]



            ''''Billing Address Function Call'''
            dun12 = checkInforBill(request.form['user_name'])[0][0]
            dun13 = checkInforAdd(dun12)[0][0]
            print(dun13)
            dun14 = checkInforStr(dun12)[0][0]
            dun15 = checkInforStr_num(dun12)[0][0]
            zip1= checkInforZip(dun12)[0][0]
            dun16 = checkInforCity(zip1)[0][0]
            dun17 = checkInforState(zip1)[0][0]



            ''''Credit Card Number Function Call'''
            dun18 = checkInforCredit(request.form['user_name'])[0][0]
            a=dun18[15]
            b=dun18[16]
            c=dun18[17]
            d=dun18[18]
            aun9 = checkSellerBalance(request.form['user_name'])[0][0]
            aun10 = checkSellerInforAccountnum(request.form['user_name'])[0][0]
            aun11 = checkSellerInforRounting(request.form['user_name'])[0][0]
            aun12 = ProductList(request.form['user_name'])
            aun13 = ProductList1(request.form['user_name'])
            if len(aun12)==0:
                aun12='No item listed!'
            return render_template('seller.html',answer2 = aun12,balance = aun9, account_num=aun10, rounting_num=aun11,name1=dun1,name2=dun2,gender=dun3,email=dun4,age=dun5,Zipcode=dun7,street_name=dun8,Str_num=dun9,City=dun10,State=dun11,City1=dun16,street_name1=dun14,Str_num1=dun15,State1=dun17,Zipcode1=zip1,credit1=a,credit2=b,credit3=c,credit4=d,answer3=aun13)    
        
        elif len(result2)!=0:
            dun1 = checkInforF(request.form['user_name'])[0][0]
            dun2 = checkInforL(request.form['user_name'])[0][0]
            dun3 = checkInforG(request.form['user_name'])[0][0]
            dun4 = checkInforE(request.form['user_name'])[0][0]
            dun5 = checkInforA(request.form['user_name'])[0][0]



            ''''Home Address Function Call'''
            dun6 = checkInforHome(request.form['user_name'])[0][0]
            dun7 = checkInforAdd(dun6)[0][0]
            dun8 = checkInforStr(dun6)[0][0]
            dun9 = checkInforStr_num(dun6)[0][0]
            zip= checkInforZip(dun6)[0][0]
            dun10 = checkInforCity(zip)[0][0]
            dun11 = checkInforState(zip)[0][0]



            ''''Billing Address Function Call'''
            dun12 = checkInforBill(request.form['user_name'])[0][0]
            dun13 = checkInforAdd(dun12)[0][0]
            print(dun13)
            dun14 = checkInforStr(dun12)[0][0]
            dun15 = checkInforStr_num(dun12)[0][0]
            zip1= checkInforZip(dun12)[0][0]
            dun16 = checkInforCity(zip1)[0][0]
            dun17 = checkInforState(zip1)[0][0]



            ''''Credit Card Number Function Call'''
            dun18 = checkInforCredit(request.form['user_name'])[0][0]
            len1=len(dun18)
            a=dun18[len1-4]
            b=dun18[len1-3]
            c=dun18[len1-2]
            d=dun18[len1-1]
            link = sql.connect ('account.db')
            return render_template('userPage.html',name1=dun1,name2=dun2,gender=dun3,email=dun4,age=dun5,Zipcode=dun7,street_name=dun8,Str_num=dun9,City=dun10,State=dun11,City1=dun16,street_name1=dun14,Str_num1=dun15,State1=dun17,Zipcode1=zip1,credit1=a,credit2=b,credit3=c,credit4=d)
    return render_template('loginC.html')





@app.route('/wrongPass')
def wrongPass():
    return render_template('wrongPass.html')





@app.route('/userPage.html', methods=['GET', 'POST'])
def userPage():
    if request.method == 'POST':
        newpass=request.form['user_newPassword']
        link=sql.connect('account.db')
        link.execute('update Users set password = (?) where email = (?)',(newpass,current))
        link.commit()
    return render_template('loginC.html')





@app.route('/shopping.html', methods=['GET'])
def shopping1():
    return render_template('shopping.html')





@app.route('/shopping.html', methods=['POST'])
def shopping2():
    if request.method=='POST':
        cate=CateCheck(request.form['root'])
        productName=ProductFind(request.form['root'])
        return render_template('shopping.html',answer1=cate, answer2=productName)
        
        


@app.route('/publish.html', methods=['GET'])
def publish():
    if request.method == 'GET':
        name = CateAll()
        return render_template('publish.html',answer3=name)








@app.route('/publish.html', methods=['POST'])
def publish1():
    if request.method == 'POST':
        Email = request.form['email']
        name = request.form['Product_Name']
        cate = request.form['choice']
        des = request.form['Product_Description']
        price = request.form['Price']
        qun = request.form['Quantity']
        title = request.form['title']
        link=sql.connect('account.db')
        point = link.execute('select max(Listing_ID) from Product_Listing')
        
        point1=point.fetchall()[0][0]
        point1=point1+4
        link.execute('insert into Product_Listing(Seller_Email,Listing_ID,Category,Title,Product_Name,Product_Description,Price,Quantity) Values(?,?,?,?,?,?,?,?)',(Email,point1,cate,title,name,des,price,qun))
        link.commit()
        return render_template('publish.html')





@app.route('/infor.html', methods=['GET'])
def hide():
    return render_template('infor.html')












@app.route('/vendors.html', methods=['GET', 'POST'])
def vendors():
    if request.method=='POST':
        answer = request.form['item_id']
        checkP = ProductCheckP(answer)
        if checkP==0:
            link=sql.connect('account.db')
            point=link.execute('update Product_Listing set chekP = 1 where Listing_ID = (?) COLLATE NOCASE',(answer,))
            link.commit()
        elif checkP==1:
            link=sql.connect('account.db')
            point=link.execute('update Product_Listing set chekP = 0 where Listing_ID = (?) COLLATE NOCASE',(answer,))
            link.commit()
        return render_template('infor.html')


@app.route('/seller.html', methods=['GET', 'POST'])
def seller():
    if request.method=='POST':
        answer = request.form['item_id']
        checkP = ProductCheckP(answer)
        if checkP==0:
            link=sql.connect('account.db')
            point=link.execute('update Product_Listing set chekP = 1 where Listing_ID = (?) COLLATE NOCASE',(answer,))
            link.commit()
        elif checkP==1:
            link=sql.connect('account.db')
            point=link.execute('update Product_Listing set chekP = (0) where Listing_ID = (?) COLLATE NOCASE',(answer,))
            link.commit()
        return render_template('infor.html')


''''get product id checkp'''
def ProductCheckP(itemid):
    link = sql.connect('account.db')
    point = link.execute('select chekP from Product_Listing where Listing_ID = (?) COLLATE NOCASE',(itemid,))
    link.commit()
    return point.fetchall()[0][0]




''''Product Find'''
def ProductFind(cat):
    link = sql.connect('account.db')
    point = link.execute('select Seller_Email,Listing_ID,Category,Title,Product_Name,Product_Description,Price,Quantity,chekP from Product_Listing  where chekP=1 and Category = (?)  COLLATE NOCASE',(cat,))
    link.commit()
    return point.fetchall()




def ProductList(email):
    link = sql.connect('account.db')
    point = link.execute('select Listing_ID,Category,Title,Product_Name,Product_Description,Price,Quantity,Category from Product_Listing where Seller_Email = (?) and chekP = 1 COLLATE NOCASE',(email,))
    link.commit()
    return point.fetchall()




def ProductList1(email):
    link = sql.connect('account.db')
    point = link.execute('select Listing_ID,Category,Title,Product_Name,Product_Description,Price,Quantity,Category from Product_Listing where Seller_Email = (?) and chekP = 0 COLLATE NOCASE',(email,))
    link.commit()
    return point.fetchall()





''''CateCheck'''
def CateCheck(root):
    link = sql.connect('account.db')
    point=link.execute('select category_name from Categories where parent_category = (?) COLLATE NOCASE',(root,))
    link.commit()
    return point.fetchall()

def CateAll():
    link = sql.connect('account.db')
    point=link.execute('select category_name from Categories ')
    link.commit()
    return point.fetchall()

'''PassWord Update'''
def PassWordUpdate(user_newPassword,email):
    link = sql.connect('account.db')
    point=link.execute('update Users set password = (?) where email = (?) COLLATE NOCASE',(user_newPassword,email))
    link.commit()
    return point.fetchall()





'''Check Login'''
def loginCheckVender(userEmail,userPassword):
    link=sql.connect('account.db')
    point=link.execute('select*from Users a,Local_Vendors b where a.email=(?) and a.password=(?) and b.Email=(?) ',(userEmail,userPassword,userEmail))
    link.commit()
    return point.fetchall()

def loginCheckBoth(userEmail,userPassword):
    link=sql.connect('account.db')
    point=link.execute('select*from Users a,Buyers b,Sellers c where a.email=(?) and a.password=(?) and b.emailBuyer=(?) and c.emailSeller=(?) COLLATE NOCASE',(userEmail,userPassword,userEmail,userEmail))
    link.commit()
    return point.fetchall()

def loginCheck(userEmail,userPassword):
    link=sql.connect('account.db')
    point=link.execute('select*from Users a, Buyers b where a.email=(?) and a.password=(?) and b.emailBuyer=(?) COLLATE NOCASE',(userEmail,userPassword,userEmail))
    link.commit()
    return point.fetchall()





'''check seller infor'''
def checkSellerInforRounting(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select routing_number from Sellers where emailSeller=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkSellerInforAccountnum(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select account_number from Sellers where emailSeller=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkSellerBalance(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select balance from Sellers where emailSeller=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()





''''check infor vendors'''
def checkInfor_Ven_Bname(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select Business_Name from Local_Vendors where Email=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInfor_Ven_Business_Address(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select Business_Address_ID from Local_Vendors where Email=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInfor_Ven_Customer_Service_Number(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select Customer_Service_Number from Local_Vendors where Email=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()




    
''''check infor buyer'''
def checkInforF(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select first_name from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforL(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select last_name from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforG(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select gender from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforA(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select age from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforE(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select emailBuyer from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforHome(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select home_address_id from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforBill(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select billing_address_id from Buyers where emailBuyer=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()

def checkInforAdd(dun6):
    link=sql.connect('account.db')
    point=link.execute('select zipcode from Address where address_id=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforAdd(dun6):
    link=sql.connect('account.db')
    point=link.execute('select zipcode from Address where address_id=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforStr(dun6):
    link=sql.connect('account.db')
    point=link.execute('select street_name from Address where address_id=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforStr_num(dun6):
    link=sql.connect('account.db')
    point=link.execute('select street_num from Address where address_id=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforZip(dun6):
    link=sql.connect('account.db')
    point=link.execute('select zipcode from Address where address_id=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforCity(dun6):
    link=sql.connect('account.db')
    point=link.execute('select city from Zipcode_Info where zipcode=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforState(dun6):
    link=sql.connect('account.db')
    point=link.execute('select state_id from Zipcode_Info where zipcode=(?) COLLATE NOCASE',(dun6,))
    link.commit()
    return point.fetchall()

def checkInforCredit(userEmail):
    link=sql.connect('account.db')
    point=link.execute('select credit_card_num from Credit_Cards where Owner_email=(?) COLLATE NOCASE',(userEmail,))
    link.commit()
    return point.fetchall()


if __name__ == "__main__":
    app.run(debug=True)