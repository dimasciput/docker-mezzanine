__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '22/08/16'
__license__ = "GPL"
__copyright__ = 'kartoza.com'

from django.utils.translation import ugettext_lazy as _
from mezzanine.conf import register_setting

# Number of recent post in front page
register_setting(
    name="FRONT_PAGE_RECENT_POST",
    label="Recent posts in front page",
    description="The number of recent posts to show in front page.",
    editable=True,
    default=5,
)

register_setting(
    name="TEMPLATE_ACCESSIBLE_SETTINGS",
    default=("FRONT_PAGE_RECENT_POST",),
    append=True,
)

register_setting(
    name="FACEBOOK_APP_ID",
    description=_("Register an app at http://developers.facebook.com/"),
    editable=True,
    default="",
)

register_setting(
    name="FACEBOOK_APP_SECRET",
    editable=True,
    default="",
)
