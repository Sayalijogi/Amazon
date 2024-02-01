from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
# Step 1

# def samsung(request):
#     return HttpResponse("Samsung Brand")
#
#
# def iphone(request):
#     return HttpResponse("iphone Brand")
#
#
# def realme(request):
#     return HttpResponse("Realme Brand")

# Step 2
TodaysDeal = {
    "electronics": "light,Fan",
    "cosmetics": "Foundation,lipstick",
    "kitchenProducts": "VimBar,VimGel",
    "stationary": "Books,Pens"
}


# Step 2 Part 1

def cart(request, Offer):
    try:
        responseText = TodaysDeal[Offer]
        #return HttpResponse(f"<h1>{responseText}</h1>")
        return render(request,'website/website.html',{"text":responseText})

        #Step 5
    except:
        return HttpResponse("<h1>The Product doesn't exist</h1>")


# Step 3 (By entering number we should redirect on products)
def cart_int(request, Offer):
    list_of_product = list(TodaysDeal.keys())
    if Offer > len(list_of_product):
        # STR >4
        return HttpResponse("Offer sold")

    redirect_Offer = list_of_product[Offer - 1]
    redirect_path = reverse('amazon_cart', args=[redirect_Offer])
    return HttpResponseRedirect(redirect_path)


# step 4
# all list will show on index page after clicking on it it will show response
def index(request):
    list_of_product = ""
    Offer = list(TodaysDeal.keys())
    for item in Offer:
        c_item = item.capitalize()
        p_item = reverse('amazon_cart', args=[item])
        list_of_product = list_of_product + f"<li><a href =\"{p_item}\">{c_item}</a></li>"
    response_data = f"<ol>{list_of_product}</ol>"
    return HttpResponse(response_data)


