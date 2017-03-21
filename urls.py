from .views import process_data, process_data_2

url(r'^odoo/rest/verify/$', process_data, name="Odoo-App-Connector"),
url(r'^odoo/rest/contactupdate/$', process_data_2, name="Odoo-App-Connector-2")
