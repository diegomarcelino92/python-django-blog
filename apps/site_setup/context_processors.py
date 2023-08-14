from apps.site_setup.models import SiteSetup


def site_setup(request):
    setup = SiteSetup.objects.all().first()

    return {'setup': setup}
