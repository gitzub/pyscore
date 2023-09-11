from django.shortcuts import render
from .models import Gamelist
from datetime import datetime, timedelta, date


def home(request):
    start = request.GET.get("start")
    end = request.GET.get("end")

    try:
        start_date = datetime.strptime(start, "%Y-%m").replace(day=1)
    except Exception as e:
        start_date = date.today().replace(day=1)
        start = start_date.strftime("%Y-%m")

    try:
        end_date = datetime.strptime(end, "%Y-%m").replace(day=date.today().day)
    except Exception:
        end_date = date.today()
        end = end_date.strftime("%Y-%m")
    res = Gamelist.objects.filter(gamedate__range=[start_date, end_date]).all()

    # mylist = []
    # cnt = 1
    # for game in res:
    #     gamedate = game.gamedate
    #     gamememo = game.gamememo
    #     for data in mylist:
    #         if gamedate == data.get("gamedate"):
    #             if gamememo == gamememo:
    #                 data["gamememo"]
    #             elif id == id:
    #                 data["id"]
    #             break
    #     else:
    #         data = {
    #             "count": cnt,
    #             "gamedate": gamedate,
    #             "gamememo": gamememo,
    #         }

    #         mylist.append(data)

    # mylist.sort(key=lambda x: x["gamedate"], reverse=True)
    # for i in range(len(mylist)):
    #     mylist[i]["count"] = i + 1
    # context = {"mylist": mylist, "start": start, "end": end}
    # return render(request, "aaatest.html", context)

    context = {
        "mylist": res,
        "start": start,
        "end": end,
    }

    return render(request, "aaatest.html", context)
