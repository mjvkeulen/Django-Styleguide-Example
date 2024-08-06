from django.urls import include, path

urlpatterns = [
    path("auth/", include(("bb.authentication.urls", "authentication"))),
    path("users/", include(("bb.users.urls", "users"))),
    path("errors/", include(("bb.errors.urls", "errors"))),
    path("files/", include(("bb.files.urls", "files"))),
]
