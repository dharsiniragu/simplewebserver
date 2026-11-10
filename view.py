from django.shortcuts import render

def calculate_churn(request):
    if request.method=="POST":
        initialCust=int(request.POST.get("initialCust"))
        PresentCust=int(request.POST.get("PresentCust"))
        churn=initialCust*PresentCust
        print(f"Length of Rectangle: {initialCust}cm \n : {PresentCust}cm \n churn of Rectangle: {churn}")
    return render(request, "mathapp/area.html",{"initialCust": initialCust, "PresentCust": PresentCust, "churn": churn})

