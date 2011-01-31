from django.conf.urls.defaults import *


urlpatterns = patterns("whowillbemayor_project.apps.battle.views",
    url(r"^$", "home", name="battle_home"),
)
