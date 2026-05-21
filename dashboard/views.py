from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from accounts.models import Users, Profile
from events.models import Event, TicketTier



@login_required
def dashboard_home(request):
    return render(request,"dashboard/home.html")

@login_required
def profile_page(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == "POST":
        profile.bio = request.POST.get("bio")
        profile.phone_number = request.POST.get("phone_number")
        profile.city = request.POST.get("city")
        profile.country = request.POST.get("country")
        profile.linkedin_url = request.POST.get("linkedin_url")
        profile.facebook_url = request.POST.get("facebook_url")
        profile.instagram_url = request.POST.get("instagram_url")
        profile.organisation_name = request.POST.get("organisation_name")
        profile.allow_networking = (request.POST.get("allow_networking") == "on")
        if request.FILES.get("profile_image"):
            profile.profile_image = request.FILES["profile_image"]
        profile.save()
        return redirect("profile_page")

    return render(request,"dashboard/profile.html",{"profile": profile}
    )

@login_required
def profile_view(request, username):
    user = get_object_or_404(Users,username=username)
    profile = user.profile
    return render(request,"dashboard/profile_view.html",{"profile": profile})

@login_required
def events_page(request):
    events = Event.objects.filter(is_active=True).order_by("-created_at")
    return render(request,"dashboard/events.html",{"events": events})

@login_required
def event_page(request, event_id):
    event = get_object_or_404(Event,id=event_id)
    return render(request,"dashboard/event_detail.html",{"event": event})

@login_required
def create_event(request):
    if request.user.role != "organizer":
        return redirect("dashboard")
    
    if request.method == "POST":
        title = request.POST.get("title")
        event = Event.objects.create(
            organizer=request.user,
            title=title,
            slug=slugify(title),
            description=request.POST.get("description"),
            ai_knowledge=request.POST.get("ai_knowledge"),
            category=request.POST.get("category"),
            mode=request.POST.get("mode"),
            venue=request.POST.get("venue"),
            city=request.POST.get("city"),
            start_date=request.POST.get("start_date"),
            end_date=request.POST.get("end_date"),
            start_time=request.POST.get("start_time"),
            end_time=request.POST.get("end_time"),
            chief_guest=request.POST.get("chief_guest"),
        )
        if request.FILES.get("event_logo"):
            event.event_logo = request.FILES["event_logo"]
        if request.FILES.get("banner_image"):
            event.banner_image = request.FILES["banner_image"]
        event.save()
        return redirect("my_events")
    return render(request,"dashboard/create_event.html")

@login_required
def my_events(request):
    
    if request.user.role != "organizer":
        return redirect("dashboard")

    events = Event.objects.filter(
        organizer=request.user
    ).order_by("-created_at")

    return render(
        request,
        "dashboard/my_events.html",
        {
            "events": events
        }
    )