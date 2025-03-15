from flask import url_for
from flask_admin import Admin
from flask_admin import helpers as admin_helpers

from bookstore import app, db, security
from bookstore.models import Book, Configuration, Order, Role, User
from bookstore.views import (BookImportView, ConfigurationView,
                             MyAdminIndexView, OrderView, ProductView,
                             RoleAdmin, StatsView, UserAdmin)

# Create admin
admin = Admin(
    app,
    "Bookstore",
    base_template="my_master.html",
    template_mode="bootstrap4",
    index_view=MyAdminIndexView(),
)

# Add model views
admin.add_view(RoleAdmin(Role, db.session))
admin.add_view(UserAdmin(User, db.session))
admin.add_view(ProductView(Book, db.session))
admin.add_view(OrderView(Order, db.session))
admin.add_view(StatsView(name="Statistics"))
admin.add_view(BookImportView(name="Import Book"))
admin.add_view(ConfigurationView(Configuration, db.session))


# define a context processor for merging flask-admin's template context into the
# flask-security views.
# This processor is added to all templates
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for,
    )
