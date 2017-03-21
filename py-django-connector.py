import sys
from django.utils import simplejson
import re
import odoorpc
from django.http import HttpResponseRedirect, HttpResponse, Http404
import json
import logging
from datetime import date as now, datetime, timedelta
now_me = datetime.now()
def process_data(request):
    if request.method == 'POST':
        datab = request.POST.get('data_b', None)
        usern = request.POST.get('username', None)
        passw = request.POST.get('password', None)
        addr = request.POST.get('url', None)
        port = request.POST.get('port', None)
        #ferst = request.get("contacts", None)
        if port:
                port = port
        else:
                port = 80
        mer = addr
        usernam = usern
        datad = datab
        password = passw  
		try:
            odoo = odoorpc.ODOO(mer, port=80)
            odoo.login(datad, usernam, password)
            Contact_list = odoo.env['res.partner']
            c_ids = Contact_list.search([])
            all_contacts = []
            for my_list in Contact_list.browse(c_ids):
                all_contacts.append(my_list)
            all_jsn = []
            to_json = []
            for obs in all_contacts:
				obs_dict = {}
                obs_dict['id'] = obs.id
                obs_dict['name'] = obs.name
                obs_dict['email'] = obs.email
                obs_dict['company'] = obs.parent_id.name
                obs_dict['job'] = obs.function
                obs_dict['phone'] = obs.phone
                obs_dict['mobile'] = obs.mobile
                obs_dict['fax'] = obs.fax
                obs_dict['website'] = obs.website
                obs_dict['street'] = obs.street
                to_json.append(obs_dict)
			user_dict = {}
            user_dict['url'] = mer
            user_dict['database'] = datad
            user_dict['username'] = usernam
            user_dict['password'] = password
            user_dict['port'] = port
            return HttpResponse(json.dumps({
                                                "error": "false",
                                                "user": user_dict,
                                                "email": usernam,
                                                "created_at": "%s" % now_me,
                                                "updated_at": "null",
                                                "uid": "1",
                                                "contacts": to_json }),
                                    content_type="application/json"
                                    )
		except:
            e = sys.exc_info()[0]
            return HttpResponse(
                                json.dumps({
                                            "tag": "login",
                                            "success": 0,
                                            "error": "true",
                                            "error_msg": "Error: %s %s %s %s %s " % (e, mer, usernam, password,$
                                            }),
                                    content_type="application/json"
                                    )
    else:
        return HttpResponse(
                                json.dumps({
                                            "tag": "login",
                                            "success": 0,
                                            "error": "true",
                                            "error_msg": "Not connected to server"
                                            }),
                                    content_type="application/json"
                                    )
									
									
def process_data_2(request):
        xdata = request.raw_post_data
		defr = xdata.replace('"[', '[').replace(']"', ']').replace('\\', '')
		df = unicode(defr, errors='ignore')
		dfd = str(df)
		json_data = json.loads(dfd)
        data = json_data['contacts']
        usern = json_data['username']
        passw = json_data['password']
        addr = json_data['url']
        port = json_data['port']
		
		if port:
                port = port
        else:
                port = 80
        mer = addr
        usernam = usern
        datad = datab
        password = passw
        try:
            odoo = odoorpc.ODOO(mer, port=port)
            odoo.login(datad, usernam, password)
			
			for idos in data:
				try:
                        ides = idos["sid"]
                except:
                        ides = None
                try:
                        names = idos["names"]
                except:
                        names = None
                try:
                        phone = idos["phones"]
                except:
                        phone = None
                try:
                        emailes = idos["emails"]
                except:
                        emailes = None
                try:
                        company = idos["company"]
                except:
                        company = None
                try:
                        addresses = idos["addrs"]
                except:
                        addresses = None
                try:
                        website = idos["website"]
                except:
                        website = None
                try:
                        jobs = idos["job"]
                except:
                        jobs = None
                try:
                        ide = int(ides)
                except:
                        ide = None
                try:
                        User = odoo.env['res.partner']
                        users = User.browse(ide)
                except:
                        try:
                                User.env['res.partner']
                                User.createUser.create({'name': names, 'phone': phone, 'email': emailes, 'email': emailes, 'street': addresses })
                                users = None
				
				except:
                                users = None
                try:
                        users.name = names
                        der = "OKay %s" % users.name
				except:
					der = "Not Okay"
				try:
                        users.phone =  phone
                        der = "OKay %s" % users.name
                except:
                        der = "Not Okay"
                try:
                        users.email = emailes
                        der = "OKay %s" % users.name
                except:
                        der = "Not Okay"
                try:
                        users.company = company
                        der = "OKay %s" % users.name
                except:
                        der = "Not Okay"
                try:
                        users.street = addresses
                        der = "OKay %s" % users.name
                except:
                        der = "Not Okay"
                try:
                        users.job = job
                        der = "OKay %s" % users.name
                except:
                        der = "Not Okay"
									
            return HttpResponse(json.dumps({
                                                "error": "None",
                                                "user": "Done", }),
                                    content_type="application/json"
                                    )
		


