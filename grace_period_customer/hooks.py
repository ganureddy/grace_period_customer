from . import __version__ as app_version

app_name = "grace_period_customer"
app_title = "Grace Period Customer"
app_publisher = "Ganu Reddy"
app_description = "Grace Period Customer"
app_email = "ganur379@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/grace_period_customer/css/grace_period_customer.css"
# app_include_js = "/assets/grace_period_customer/js/grace_period_customer.js"

# include js, css files in header of web template
# web_include_css = "/assets/grace_period_customer/css/grace_period_customer.css"
# web_include_js = "/assets/grace_period_customer/js/grace_period_customer.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "grace_period_customer/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

fixtures = [
    {
        "dt":
        "Custom Field",
        "filters": [[
            "name",
            "in",
            [
				"Customer-extra_payment_days",
				"Sales Invoice-grace_period",
            ]
        ]]
    },
]
# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "grace_period_customer.utils.jinja_methods",
#	"filters": "grace_period_customer.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "grace_period_customer.install.before_install"
# after_install = "grace_period_customer.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "grace_period_customer.uninstall.before_uninstall"
# after_uninstall = "grace_period_customer.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "grace_period_customer.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }
doc_events = {
	"Sales Invoice": {
		"on_submit":"grace_period_customer.events.Sales_extra_days_count",
		"before_submit":"grace_period_customer.events.sales_invoive_Changes_and_validation_count"
	},
}
# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"grace_period_customer.tasks.all"
#	],
#	"daily": [
#		"grace_period_customer.tasks.daily"
#	],
#	"hourly": [
#		"grace_period_customer.tasks.hourly"
#	],
#	"weekly": [
#		"grace_period_customer.tasks.weekly"
#	],
#	"monthly": [
#		"grace_period_customer.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "grace_period_customer.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "grace_period_customer.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "grace_period_customer.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"grace_period_customer.auth.validate"
# ]
