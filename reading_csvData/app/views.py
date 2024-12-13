from django.shortcuts import render
import csv
from app.models import *
from django.http  import HttpResponse
# Create your views here.
def csv_data(request):
    with open('C:\\pranaya\\pranaya\\Scripts\\reading_csvData\\app\\bank.csv','r') as fo:
        ifo=csv.reader(fo)
        for bankName in ifo:
            bn=bankName[0].strip()
            bo=bank(bank_name=bn)
            bo.save()
    return HttpResponse('the data is inserted')

def insert_branch(request):
    with open('C:\\pranaya\\pranaya\\Scripts\\reading_csvData\\app\\branch1.csv','r') as fo:
        io=csv.reader(fo)
        next(io)
        for branch_ in io:
            bn=branch_[0]
            bo=bank.objects.filter(bank_name=bn)
            if bo:
                ifsc=branch_[1]
                branchName=branch_[2]
                add=branch_[3]
                ph=branch_[4]
                city=branch_[5]
                dis=branch_[6]
                state=branch_[7]
                brO=branch(bank_name=bo[0],ifsc=ifsc,branch_name=branchName ,address=add,phno=ph,city=city,district=dis,state=state)
                brO.save()
    return HttpResponse('branch details are inserted')


        
            