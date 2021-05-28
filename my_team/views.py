from django.shortcuts import render

def welcome(request):
    return render(request,"welcome.html")

def result(request):
    member = request.GET['member']
    memberList = member.split()
    return render(request,'result.html', {'member':member,'count':len(memberList),'memberList':memberList})