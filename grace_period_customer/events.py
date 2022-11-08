import frappe
import datetime


def Sales_extra_days_count(doc,method=None):
    if frappe.db.exists("Customer", doc.customer):
        get_customer = frappe.get_doc("Customer", doc.customer)
        date_1 = datetime.datetime.strptime(doc.due_date, "%Y-%m-%d")
        end_date = date_1 + datetime.timedelta(days=get_customer.extra_payment_days)
        next_date = datetime.datetime.strptime(str(end_date), "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
        date_1 = datetime.datetime.strptime(doc.due_date, "%Y-%m-%d")
        print(next_date,doc.due_date,"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        frappe.db.set_value("Sales Invoice",doc.name,{"grace_period":next_date})
        frappe.db.commit()
        print("#################",frappe.db.get_list("Sales Invoice",filters={'customer' : doc.customer,'status':'overdue'},fields=['customer','status','name','grand_total','grace_period','posting_date'],order_by='posting_date asc'))
        
               
def sales_invoive_Changes_and_validation_count(doc,method=None):
    get_sales_invoice = frappe.db.get_list("Sales Invoice",filters={'customer' : doc.customer},fields=['customer','status','name','grand_total','grace_period','posting_date'],order_by='posting_date asc')
    for invoice in get_sales_invoice:
        if invoice.grace_period != None:
            if datetime.date.today() > invoice.grace_period:
                frappe.throw("This Customer have overdue invoice {} and amount {} and extra given days {}".format(invoice.name, invoice.grand_total, invoice.grace_period))
                
        else:
            Sales_extra_days_count(doc,method=None)
