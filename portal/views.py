from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def dashboard(request):
    stats = {
        "total_patients": 0,
        "sections": [
            {"label": "基本信息", "percent": 0},
            {"label": "诊疗数据", "percent": 0},
            {"label": "影像资料", "percent": 0},
        ],
    }
    return render(request, "pages/dashboard.html", {"stats": stats})


def patients_list(request):
    return render(request, "pages/patient_list.html")


def patients_create(request):
    return render(request, "pages/patient_create.html")


def settings_view(request):
    return render(request, "pages/settings.html")


def about(request):
    return render(request, "pages/about.html")
