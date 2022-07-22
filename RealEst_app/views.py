from django.shortcuts import render

def load_index(request):
    return render(request,'index.html')

def admin_propertylist(request):
    return render(request,'Admin_property_list.html')
    
def admin_propertyview(request):
    return render(request,'Admin_property_view.html')

def admin_agent(request):
    return render(request,'Admin_agent.html') 

def admin_agentadd(request):
    return render(request,'Admin_angentadd.html')
def admin_propertyadd(request):
    return render(request,'Admin_propertyadd.html')

def admin_staf(request):
    return render(request,'Admin_staf.html')

def admin_telecaller(request):
    return render(request,'Admin_telecaller.html')

def admin_telecalleradd(request):
    return render(request,'Admin_telecaller_add.html')

def admin_loc_visit_schedule(request):
    return render(request,'Admin_LocationVisitSchedule.html')


def staf_dashboard(request):
    return render(request,'Staf_dashboard.html')

def staf_propertyview(request):
    return render(request,'staf_propertyview.html')

def staf_cliant_propertyview(request):
    return render(request,'cliant_propertyview.html')

def staf_cliant_property(request):
    return render(request,'Cliant_property.html')