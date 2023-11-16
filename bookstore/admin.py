from bookstore import app, db, security
from bookstore.views import MyModelView, MyAdminIndexView, StatsView
from bookstore.models import User, Role
from flask_admin import helpers as admin_helpers, Admin
from flask import url_for

# Create admin
admin = Admin(
    app,
    'BookStore: Auth',
    base_template='my_master.html',
    template_mode='bootstrap4',
    index_view=MyAdminIndexView()
)

# Add model views
admin.add_view(MyModelView(Role, db.session))
admin.add_view(MyModelView(User, db.session))
admin.add_view(StatsView(name='Thống Kê - Báo Cáo'))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )