import json
from flask import url_for,jsonify,request
from flask_httpauth import HTTPBasicAuth


#import the blueprint's instance
from . import apiobj
from hostelapp.mymodel import db, Property,Merchants

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    deets = db.session.query(Merchants.mer_pwd).filter(Merchants.mer_username==username).first()
    if deets:
        return deets.mer_pwd
    return None

@auth.error_handler
def unauthorized():
    return jsonify({"status":0,"message":"unauthorized access","data":[]}), 401

@apiobj.route('/listall/',methods=['GET'])
def listall():
    data = db.session.query(Property).all()
    if data:
        records = []
        for i in data:
            a={}
            a['propertyName']=i.prop_name
            a['propertyPrice']=i.prop_price
            a['propertyPix']=i.prop_filename
            a['propertyContact']=i.prop_contact
            records.append(a)
        resp ={"status":1,"message":"successful","data":records}
    else:
        resp ={"status":0,"message":"Not found","data":[]}
    return jsonify(resp)

@apiobj.route('/listone/<id>/',methods=['GET'])
def listone(id):
    records = db.session.query(Property).get(id)
    rsp={"propertyName":records.prop_name,"propertyPrice":records.prop_price,"propertyPix":records.prop_filename,"propertyContact":records.prop_contact}
    return jsonify(rsp)

@apiobj.route('/addnew/',methods=['POST'])
@auth.login_required
def addnew():
    if request.is_json:
        data = request.get_json() 
        propname = data.get('pname') 
        propfile = data.get('pfile') 
        price = data.get('pprice')   
        pcontact = data.get('pcontact')   
        phone = data.get('pphone')   
        property = Property(prop_contact=pcontact,prop_phone=phone,prop_filename=propfile,prop_price=price,prop_name=propname)
        db.session.add(property)
        db.session.commit()
        pid = property.prop_id
        resp = {"status":1,"message":f"Successful,added Hostel with id {pid}","data":[]}
        return jsonify(resp)
    else:
        resp = {"status":0,"message":"Bad Format, supply JSON","data":[]}
        return jsonify(resp)

@apiobj.errorhandler(400)
def badrequest(error):
    resp = {"status":0,"message":"Bad Format","data":[]}
    return jsonify(resp)


@apiobj.route('/update/<id>/',methods=['PUT'])
def update_hostel(id):
    data = request.get_json() 
    propname = data['pname']  
    propfile = data['pfile']  
    price = data['pprice']    
    pcontact = data['pcontact']   
    phone = data['pphone']   
    property = db.session.query(Property).get(id)
    property.prop_name=propname
    property.prop_contact=pcontact
    property.prop_phone=phone
    property.prop_filename=propfile
    property.prop_price=price
    db.session.commit()
    return 'Hostel updated'

@apiobj.route('/delete/<id>/',methods=['DELETE'])
def delete_hostel(id):
    property = db.session.query(Property).get(id)
    db.session.delete(property)
    db.session.commit()
    return 'successfully deleted'