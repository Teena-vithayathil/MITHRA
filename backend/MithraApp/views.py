from django.conf import settings
from django.shortcuts import redirect,render
from django.http import FileResponse, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from MithraApp.models import User,JoinCarpool,Delivery,CreateCarpool
    
@csrf_exempt 
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        user = User.objects.filter(email=email,password=password).count()
        if user>0:
                user = User.objects.get(email=email,password=password)
                f=open("active_user.txt","w")
                f.write(str(user.id))
                if user.name=="admin":
                    return JsonResponse({"message":"admin login successful"})
                if user.verified=="True":
                    return JsonResponse({"message":"login successful"})
                else:
                    return JsonResponse({"message":"not verified"})
        else:
             return JsonResponse({"message":"Invalid username or password"})

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        # Extract data from request
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        age = data.get('age')
        city = data.get('city')
        phone_number = data.get('phoneNumber')
        occupation = data.get('occupation')
        user = User.objects.create(
            name=name,  
            email=email,
            password=password,
            age=age,
            city=city,
            phno=phone_number,
            occupation=occupation,
            rating=0,
            review=""
        )
        f=open("active_user.txt","w")
        f.write(str(user.id))
        return JsonResponse({"message":"signup successful"})

    return JsonResponse({"message": "Sign up process not successfull"})

@csrf_exempt
def upload_files(request):
    if request.method == "POST":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        user = User.objects.get(id=uid)
        user.profile_pic="frontend/images/propics/default.jpg"
        if "id_proof" in request.FILES:
            id_proof = request.FILES.get("id_proof")
            user.id_proof=id_proof
            user.verified=False
        else:
             return JsonResponse({"message: Error in uploading"})
        if "driving_license" in request.FILES:
            driving_license = request.FILES.get("driving_license")
            user.driving_license=driving_license
        user.save()
        return JsonResponse({"message": "proof upload complete"})
    else:
        return JsonResponse({"message":"proof upload incomplete"})

@csrf_exempt
def create_ride(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        start=data.get('startLocation')
        end=data.get('endLocation')
        via=data.get('viaRoute')
        search_route=start+"-"+via+"-"+end
        ride= CreateCarpool.objects.create(
            userid=uid,
            date=data.get('date'),
            time=data.get('startTime'),
            start=data.get('startLocation'),
            end=data.get('endLocation'),
            via=data.get('viaRoute'),
            vehicle_type=data.get('vehicleType'),
            vehicle_no=data.get('vehicleNo'),
            vehicle_model=data.get('vehicleModel'),
            max_seats=int(data.get('seatsAvailable')), 
            no_of_seats=int(data.get('seatsAvailable')),
            music=data.get('music',False),
            smoking=data.get('smoking', False),
            pet=data.get('pets', False),
            eatdrink=data.get('eatingDrinking', False),
            ac=data.get('ac', False),
            chitchat=data.get('chitChat', False),
            price=data.get('price'),
            product_delivery=data.get('productDelivery', False),
            search_route=search_route,
            delivery_price=data.get('deliveryPrice',False),
        )
        f=open("ride.txt","w")
        f.write(str(ride.id))
        return JsonResponse({'message': 'Ride created successfully'})
    else:
        return JsonResponse({'message': 'Ride creation unsuccessfull'})

@csrf_exempt
def payment_pic(request):
    if request.method =='POST':
        f=open("ride.txt","r")
        s=""
        for i in f.read():
            s+=i
        rid=int(s)
        if 'paymentPicture' not in request.FILES:
                return JsonResponse({'message': 'Please upload payment picture'})
        ride = CreateCarpool.objects.get(id=rid)
        ride.paymentpic = request.FILES.get('paymentPicture')
        ride.save()
        return JsonResponse({"message": "upload complete"})
    else:
         return JsonResponse({"messgae": "payment upload incomplete"})

@csrf_exempt
def verification(request):
    if request.method == 'POST':
        try:
            users = User.objects.filter(verified=False)
            user_data = []
            for user in users:
                user_info = {
                    'id': user.id,
                    'username': user.name,
                    'age': user.age,
                    'id_proof': user.id_proof.url if user.id_proof else None
                }
                id=user_info['id_proof']
                user_info['id_proof']=id[10:]
                user_data.append(user_info)
            return JsonResponse(user_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def verification_accept(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        print(user_id)
        try:
            user = User.objects.get(id=user_id)
            user.verified = True
            user.save()
            return JsonResponse({'message': 'User verification accepted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def verification_reject(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({'message': 'User removed successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
@csrf_exempt 
def search_ride(request):
    if request.method == 'POST':
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        data = json.loads(request.body)
        start_location = data.get('start_location')
        end_location = data.get('end_location')
        date = data.get('date')
        rides = CreateCarpool.objects.filter(date=date, no_of_seats__gt=0).exclude(userid=uid)
        ride_info=[]
        for ride in rides:
            name=User.objects.get(id=ride.userid).name
            request=JoinCarpool.objects.filter(passengerid=uid,carpool_id=ride.id).count()
            d=date[8:]+date[4:8]+date[:4]
            r={
                "id":ride.id,
                "user_id":ride.userid,
                "driverName":name,
                "vehicle_type":ride.vehicle_type,
                "vehicle_model":ride.vehicle_model,
                "availableSeats":ride.no_of_seats,
                "totalSeats":ride.max_seats,
                "date":d,
                "time":ride.time,
                "route":ride.search_route,
                "ac":ride.ac,
                "chit_chat":ride.chitchat,
                "music":ride.music,
                "pets":ride.pet,
                "smoking":ride.smoking,
                "eat_drink":ride.eatdrink,
                "price": 0
            } 
            if ride.ac=="False":
                r["ac"]=""
            if ride.chitchat=="False":
                r["chit_chat"]=""
            if ride.music=="False":
                r["music"]=""
            if ride.pet=="False":
                r["pets"]=""
            if ride.smoking=="False":
                r["smoking"]=""
            if ride.eatdrink=="False":
                r["eat_drink"]=""
            l = ride.search_route.split("-")
            if start_location in l and end_location in l and request==0:
                    start=l.index(start_location)
                    end = l.index(end_location)
                    r["price"] = (ride.price)*(end-start)
                    if start<end:
                        ride_info.append(r)
        if len(ride_info)>0:
            return JsonResponse(ride_info,safe=False)
        else:
            return JsonResponse("No rides available",safe=False)
    else:
        return JsonResponse({"message": "Search ride unsuccessfull"})

@csrf_exempt
def request_carpool(request):
    if request.method == 'POST':
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        data = json.loads(request.body)
        carpool_id = data.get('carpool_id')
        start_location = data.get('start_location')
        end_location = data.get('end_location')
        driver_id=data.get('driver_id')
        price = data.get('price')
        # Create a new entry in the JoinCarpool table
        join_carpool = JoinCarpool.objects.create(
            passengerid=uid,
            driverid=driver_id,
            carpool_id=carpool_id,
            start=start_location,
            end=end_location,
            request = "pending",
            price = price
        )
        
        # Redirect to some success page or URL
        return JsonResponse({"message":"requested"})
    else:
        # Render the form template
        return JsonResponse({"message":"request unsuccessfull"})
    
@csrf_exempt
def save_driver(request):
    if request.method=="POST":
        data=json.load(request)
        driver_id=data.get("driver_id")
        f=open("driver_details.txt","w")
        f.write(str(driver_id))
        return JsonResponse({"message":"Successfull"})
    else:
        # Render the form template
        return JsonResponse({"message":"request unsuccessfull"})

@csrf_exempt    
def view_profile(request):
    if request.method=="POST":
        f=open("driver_details.txt","r")
        s=""
        for i in f.read():
            s+=i
        id=int(s)
        user = User.objects.get(id=id)
        requests_list={"id":user.id,
        "name":user.name,
        "age":user.age,
        "profilePicture":user.profile_pic.url if user.profile_pic else None,
        "occupation":user.occupation,
        "phoneNumber":user.phno,
        "rating":user.rating,
        "reviews":user.review}
        requests_list["profilePicture"]=requests_list["profilePicture"][10:]
        if user.review!="":
            requests_list["reviews"]=user.review.split(",")
        return JsonResponse(requests_list, safe=False)

@csrf_exempt
def review_rating(request):
    if request.method == "POST":
        data=json.load(request)
        rating=data.get("rating")
        review=data.get("review")
        f=open("driver_details.txt","r")
        s=""
        for i in f.read():
            s+=i
        id=int(s)
        user = User.objects.get(id=id)
        #rating
        if rating!=0:
            if rating==1:
                user.r1=user.r1+1
            elif rating==2:
                user.r2=user.r2+1
            elif rating==3:
                user.r3=user.r3+1
            elif rating==4:
                user.r4=user.r4+1
            else:
                user.r5=user.r5+1
            average_rating = (5*user.r5 + 4*user.r4 + 3*user.r3 + 2*user.r2 + user.r1) / (user.r5 + user.r4 + user.r3 + user.r2 + user.r1)
            user.rating = average_rating
        #review
        if review!="":
            if user.review=="":
                user.review=review
            else:
                user.review=user.review+","+review

        user.save()
        return JsonResponse({"message":"successfull"})
    
@csrf_exempt
def get_carpool_requests(request):
    if request.method=="POST":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        requests = JoinCarpool.objects.filter(driverid=uid, request="pending").values()
        requests_list = list(requests)
        return JsonResponse(requests_list, safe=False)
    if request.method=="GET":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        requests = Delivery.objects.filter(driverid=uid, request="pending").values()
        requests_list = list(requests)
        return JsonResponse(requests_list, safe=False)
    
@csrf_exempt
def search_product_delivery(request):
    if request.method == 'POST':
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        data=json.load(request)
        start_location = data.get('start_location')
        end_location = data.get('end_location')
        date = data.get('date')
        rides = CreateCarpool.objects.filter(date=date,product_delivery=True).exclude(userid=uid)
        ride_info=[]
        for ride in rides:
            name=User.objects.get(id=ride.userid).name
            request=Delivery.objects.filter(passengerid=uid,carpool_id=ride.id).count()
            d=date[8:]+date[4:8]+date[:4]
            print(ride)
            r={
                "id":ride.id,
                "user_id":ride.userid,
                "driverName":name,
                "vehicle_type":ride.vehicle_type,
                "vehicle_model":ride.vehicle_model,
                "date":d,
                "time":ride.time,
                "route":ride.search_route,
                "price":0
            } 
            l = ride.search_route.split("-")
            if start_location in l and end_location in l and request==0:
                    start=l.index(start_location)
                    end = l.index(end_location)
                    r["price"] = (ride.delivery_price)*(end-start)
                    if start<end:
                        ride_info.append(r)
        if len(ride_info)>0:
            return JsonResponse(ride_info,safe=False)
        else:
            return JsonResponse({"message":"no data found"})
@csrf_exempt
def request_product_delivery(request):
    if request.method == 'POST':
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        data=json.load(request)
        carpool_id = data.get('carpool_id')
        start_location = data.get('start_location')
        end_location = data.get('end_location')
        driver_id = data.get('driver_id')
        pro_size = data.get('pro_size')
        pro_wgt = data.get('pro_wgt')
        pro_type = data.get('pro_type')
        pro_anyother = data.get('pro_anyother')
        price = data.get('price')
        join_delivery = Delivery.objects.create(
            driverid=driver_id,
            passengerid=uid,
            carpool_id=carpool_id,
            start=start_location,
            end=end_location,
            pro_size = pro_size,
            pro_wgt = pro_wgt,
            pro_type = pro_type,
            pro_anyother = pro_anyother,
            price=price
        )
        return JsonResponse({'message':'success page'})
    else:
        return JsonResponse({'message':'failed'})

@csrf_exempt
def request(request):
    if request.method == "POST":
            f=open("active_user.txt","r")
            s=""
            for i in f.read():
                s+=i
            uid=int(s)
            users = JoinCarpool.objects.filter(driverid=uid,request="pending")
            ride_info=[]
            for user in users:
                u = User.objects.get(id=user.passengerid)
                print(u)
                d=CreateCarpool.objects.get(id=user.carpool_id)
                if d.no_of_seats>0:
                    r={
                            "carpool_id":user.carpool_id,
                            "passenger_id":user.passengerid,
                            "driver_id":user.driverid,
                            "passengerName": u.name,
                            "route": d.search_route,
                            "start":user.start,
                            "end":user.end,
                            "date":d.date,
                            "time":d.time,
                            "message":"Carpool"
                    }
                    ride_info.append(r)
            return JsonResponse(ride_info,safe=False)    
    if request.method == "GET":
            f=open("active_user.txt","r")
            s=""
            for i in f.read():
                s+=i
            uid=int(s)
            users = Delivery.objects.filter(driverid=uid,request="pending")
            ride_info=[]
            for user in users:
                u = User.objects.get(id=user.passengerid)
                d=CreateCarpool.objects.get(id=user.carpool_id)
                r={
                        "carpool_id":user.carpool_id,
                        "passenger_id":user.passengerid,
                        "driver_id":user.driverid,
                        "passengerName": u.name,
                        "route": d.search_route,
                        "start":user.start,
                        "end":user.end,
                        "date":d.date,
                        "time":d.time,
                        "wgt":user.pro_wgt,
                        "size":user.pro_size,
                        "type":user.pro_type,
                        "anyother":user.pro_anyother,
                        "message":"Product"
                }
                if r["anyother"]==False:
                        r["anyother"]=""
                ride_info.append(r)
            return JsonResponse(ride_info,safe=False)      

@csrf_exempt
def accept_request(request):
    if request.method == "POST":
        data=json.load(request)
        carpool_id=data.get("carpool_id")
        passenger_id=data.get("passenger_id")
        message=data.get("message")
        if message=="Carpool":
            carpool = CreateCarpool.objects.get(id=carpool_id)
            carpool.no_of_seats -= 1
            carpool.save()
            join_request = JoinCarpool.objects.get(carpool_id=carpool_id,passengerid=passenger_id)
            join_request.request = 'accept'
            join_request.save()
        else:
            join_request = Delivery.objects.get(carpool_id=carpool_id,passengerid=passenger_id)
            join_request.request = 'accept'
            join_request.save()
        return JsonResponse({"message":"succesfull'"})  

@csrf_exempt
def reject_request(request):
    if request.method == "POST":
        data=json.load(request)
        carpool_id=data.get("carpool_id")
        passenger_id=data.get("passenger_id")
        message=data.get("message")
        if message=="Carpool":
            join_request = JoinCarpool.objects.get(carpool_id=carpool_id,passengerid=passenger_id)
            join_request.request = 'reject'
            join_request.save()
        else:
            join_request = Delivery.objects.get(carpool_id=carpool_id,passengerid=passenger_id)
            join_request.request = 'reject'
            join_request.save()
        return JsonResponse({"message":"succesfull'"})   
             
@csrf_exempt
def forget_password(request):
    if request.method == 'POST':
        data=json.load(request)
        email = data.get('email')
        try:
            user = User.objects.get(email=email)
            user.password=data.get("password")
            user.save()
            return JsonResponse({'success': True, 'message': 'Password changed'})
        except User.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Invalid credentials'})

@csrf_exempt        
def get_status(request):
    if request.method == "POST":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        users = JoinCarpool.objects.filter(passengerid=uid)
        ride_info=[]
        for user in users:
            u = User.objects.get(id=user.passengerid)
            d=CreateCarpool.objects.get(id=user.carpool_id)
            u1=User.objects.get(id=d.userid)
            r={
                    "carpool_id":user.carpool_id,
                    "driver_id":user.driverid,
                    "driverName": u1.name,
                    "route": d.search_route,
                    "start":user.start,
                    "end":user.end,
                    "date":d.date,
                    "time":d.time,
                    "status":user.request,
                    "price":d.price,
                    "paymentpic":""
            }
            if r["status"]=="accept":
                    r["paymentpic"]=d.paymentpic.url if d.paymentpic else None
                    r1=r["paymentpic"]
                    r['paymentpic']=r1[10:]
            ride_info.append(r)
        return JsonResponse(ride_info,safe=False)
    if request.method=="GET":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        users = Delivery.objects.filter(passengerid=uid)
        ride_info=[]
        for user in users:
            u = User.objects.get(id=user.passengerid)
            d=CreateCarpool.objects.get(id=user.carpool_id)
            u1=User.objects.get(id=d.userid)
            r={
                    "carpool_id":user.carpool_id,
                    "driver_id":user.driverid,
                    "driverName": u1.name,
                    "route": d.search_route,
                    "start":user.start,
                    "end":user.end,
                    "date":d.date,
                    "time":d.time,
                    "wgt":user.pro_wgt,
                    "size":user.pro_size,
                    "type":user.pro_type,
                    "anyother":user.pro_anyother,
                    "status":user.request,
                    "price":d.price,
                    "paymentpic":""
            }
            if r["status"]=="accept":
                    r["paymentpic"]=d.paymentpic.url if d.paymentpic else None
                    r1=r["paymentpic"]
                    r['paymentpic']=r1[10:]
            if r["anyother"]==False:
                    r["anyother"]=""
            ride_info.append(r)
        return JsonResponse(ride_info,safe=False)   
    
@csrf_exempt
def cancel_content(request):
    if request.method == "POST":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        users = JoinCarpool.objects.filter(passengerid=uid)
        ride_info=[]
        for user in users:
            u = User.objects.get(id=user.driverid)
            d = CreateCarpool.objects.get(id=user.carpool_id)
            if d.no_of_seats>0:
                r={
                        "id":d.userid,
                        "carpool_id":user.carpool_id,
                        "passenger_id":user.passengerid,
                        "driverName": u.name,
                        "route": d.search_route,
                        "start":user.start,
                        "end":user.end,
                        "date":d.date,
                        "time":d.time,
                        "status":user.request,
                        "message":"Carpool Join"
                }
                ride_info.append(r)
        return JsonResponse(ride_info,safe=False)    
    if request.method == "GET":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        users = Delivery.objects.filter(passengerid=uid)
        ride_info=[]
        for user in users:
            u = User.objects.get(id=user.driverid)
            d=CreateCarpool.objects.get(id=user.carpool_id)
            r={
                    "id":d.userid,
                    "carpool_id":user.carpool_id,
                    "passenger_id":user.passengerid,
                    "driverName": u.name,
                    "route": d.search_route,
                    "start":user.start,
                    "end":user.end,
                    "date":d.date,
                    "time":d.time,
                    "wgt":user.pro_wgt,
                    "size":user.pro_size,
                    "type":user.pro_type,
                    "status":user.request,
                    "anyother":user.pro_anyother,
                    "message":"Product Join"
            }
            if r["anyother"]==False:
                    r["anyother"]=""
            ride_info.append(r)
        return JsonResponse(ride_info,safe=False)  
    if request.method == "PUT":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        users = CreateCarpool.objects.filter(userid=uid)
        ride_info=[]
        for user in users:
            if user.no_of_seats==user.max_seats:
                r={
                        "id":user.userid,
                        "carpool_id":user.id,
                        "route": user.search_route,
                        "start":user.start,
                        "end":user.end,
                        "date":user.date,
                        "time":user.time,
                        "price":user.price,
                        "message":"Created carpool",
                }
                ride_info.append(r)
        return JsonResponse(ride_info,safe=False)  

@csrf_exempt
def cancel(request):
    if request.method=="POST":
        data=json.load(request)
        message=data.get("message")
        carpool_id=data.get("carpool_id")
        passenger_id=data.get("passenger_id")
        status=data.get("status")
        if message=="Carpool Join":
            if status=="accept":
                carpool=CreateCarpool.objects.get(id=carpool_id)
                carpool.no_of_seats=carpool.no_of_seats+1
                carpool.save()
            JoinCarpool.objects.get(carpool_id=carpool_id, passengerid=passenger_id).delete()
        elif message=="Product Join":
            Delivery.objects.get(carpool_id=carpool_id, passengerid=passenger_id).delete()
        else:  
            carpool = CreateCarpool.objects.get(id=carpool_id)  
            if carpool.no_of_seats == carpool.max_seats:
                JoinCarpool.objects.filter(carpool_id=carpool_id).delete()
                carpool.delete()
        return JsonResponse({"message":"successful"})

@csrf_exempt    
def admin_created_carpool(request):
    if request.method=="POST":
        rides = CreateCarpool.objects.all()
        ride_info=[]
        for ride in rides:
            name=User.objects.get(id=ride.userid).name
            date=ride.date
            d=date[8:]+date[4:8]+date[:4]
            r={
                "id":ride.id,
                "user_id":ride.userid,
                "driverName":name,
                "vehicle_type":ride.vehicle_type,
                "vehicle_model":ride.vehicle_model,
                "availableSeats":ride.no_of_seats,
                "totalSeats":ride.max_seats,
                "date":d,
                "time":ride.time,
                "route":ride.search_route,
                "ac":ride.ac,
                "chit_chat":ride.chitchat,
                "music":ride.music,
                "pets":ride.pet,
                "smoking":ride.smoking,
                "eat_drink":ride.eatdrink,
                "price": ride.price,
                "productDelivery":ride.product_delivery,
                "deliveryPrice":ride.delivery_price
            }
            if ride.product_delivery=="False":
                r["productDelivery"]="" 
            else:
                r["productDelivery"]="Available"
            if ride.ac=="False":
                r["ac"]=""
            if ride.chitchat=="False":
                r["chit_chat"]=""
            if ride.music=="False":
                r["music"]=""
            if ride.pet=="False":
                r["pets"]=""
            if ride.smoking=="False":
                r["smoking"]=""
            if ride.eatdrink=="False":
                r["eat_drink"]=""
            ride_info.append(r)
        if len(ride_info)>0:
            return JsonResponse(ride_info,safe=False)
        else:
            return JsonResponse("No rides available",safe=False)

@csrf_exempt
def edit_profile(request):
    if request.method == 'POST':
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        user = User.objects.get(id=uid)
        user_info={
            "name":user.name,
            "email":user.email,
            "age":user.age,
            "occupation":user.occupation,
            "phoneNumber":user.phno,
            'id_proof': user.id_proof.url if user.id_proof else None,
            'driving_license': user.driving_license.url if user.driving_license else None,
            'picture': user.profile_pic.url if user.profile_pic else None,
            "rating":user.rating
        }
        user_info["picture"]=user_info["picture"][10:]
        return JsonResponse(user_info, safe="False")

@csrf_exempt    
def edit_upload(request):
    if request.method == "POST":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        user = User.objects.get(id=uid)
        if "driving_license" in request.FILES:
            driving_license = request.FILES.get("driving_license")
            user.driving_license=driving_license
            user.driving_verified="pending"
        if "profile_pic" in request.FILES:
            profile_pic = request.FILES.get("profile_pic")
            user.profile_pic=profile_pic
        user.save()
        return JsonResponse({"message": "proof upload complete"})
    else:
        return JsonResponse({"message":"proof upload incomplete"})

@csrf_exempt    
def final_payment(request):
    if request.method=="GET":
        f=open("driver_details.txt","r")
        s=""
        for i in f.read():
            s+=i
        cid=int(s)
        c=CreateCarpool.objects.get(id=cid)
        payment_pic= c.paymentpic.url if c.paymentpic else None
        payment_pic = payment_pic[10:]
        info={"mainPicture":payment_pic}
        return JsonResponse(info,safe="False")
    else:
        return JsonResponse({"message":"unsuccessful"})

@csrf_exempt
def check_driver(request):
    if request.method=="GET":
        f=open("active_user.txt","r")
        s=""
        for i in f.read():
            s+=i
        uid=int(s)
        user=User.objects.get(id=uid)
        r={"driving_license": user.driving_verified}
        if user.driving_verified=="False":
            r["driving_license"]=""
        return JsonResponse(r,safe="False")
    
@csrf_exempt
def verification_dl(request):
    if request.method == 'POST':
        try:
            users = User.objects.filter(driving_verified=False).exclude(driving_license='')
            user_data = []
            for user in users:
                user_info = {
                    'id': user.id,
                    'username': user.name,
                    'age': user.age,
                    'driving_license': user.driving_license.url if user.driving_license else None
                }
                id=user_info['driving_license']
                user_info['driving_license']=id[10:]
                user_data.append(user_info)
            return JsonResponse(user_data, safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def verification_accept_dl(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.driving_verified = True
            user.save()
            return JsonResponse({'message': 'User verification accepted successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def verification_reject_dl(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_id = data.get('user_id')
        try:
            user = User.objects.get(id=user_id)
            user.driving_license=""
            user.save()
            return JsonResponse({'message': 'User removed successfully'})
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
