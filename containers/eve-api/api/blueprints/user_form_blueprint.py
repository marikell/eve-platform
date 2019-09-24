from api.config.configuration import ROUTE_CONFIG
from flask import Blueprint, jsonify, request
from werkzeug import Response
from flask_api import status
from api.services.service_handler import ServiceHandler
from api.utils.validate_fields import check_empty_string, check_if_key_exists
from api.utils.response_formatter import response, response_text
import json
from bson import json_util

route_name = ROUTE_CONFIG['USER_FORM_TYPE_NAME']
app_user_form = Blueprint(route_name,__name__, url_prefix='/api')

def validate_followup_request(json):
    keys = ['form_id','user_id', 'status']
    for k in keys:         
        check_if_key_exists(k, json)
        check_empty_string(k, json)            

@app_user_form.route(route_name, methods=['POST'])
def insert():
    try:
        json_obj = request.get_json()
        validate_followup_request(json_obj)

        form = ServiceHandler.get_service(ROUTE_CONFIG['FORM_TYPE_NAME']).get(json_obj['form_id'])

        if not form:
            raise Exception('Form not found!')

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(json_obj['user_id'])
        
        if not user:
            raise Exception('User not found!')
        
        obj = {
            "form": form,
            "user": user,
            "status" : json_obj['status']
        }
        
        inserted_id = ServiceHandler.get_service(route_name).insert(obj)

        obj = { 'inserted_id': str(inserted_id) }

        return response(json.dumps(obj), status=status.HTTP_201_CREATED)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/forms/<user_id>', methods=['GET'])
def get_forms_user(user_id):
    try:
        # forms = json.dumps()
        forms = []
        user_forms = []
        for f in ServiceHandler.get_service(ROUTE_CONFIG['FORM_TYPE_NAME']).get_all():
            forms.append(json.loads(f.to_json()))
        for uf in ServiceHandler.get_service(ROUTE_CONFIG['USER_FORM_TYPE_NAME']).get_all_forms_by_user(user_id):
            user_forms.append(json.loads(uf.to_json()))
        form = None
        #retorno um form quando o usuário poder fazer algum form
        #caso o usuario nao possa, retorno apenas o status
        #só retorno o nao posso, quando o usuario tiver algum user_form com status = 0 ou quando ele respondeu todos os forms

        done_forms = []
        currentForm = None

        for uf in user_forms:
            if uf['status'] == 1:
                #vou adicionando na lista os forms que ja foram respondidos
                done_forms.append(uf['form_id']['$oid'])
            else:
                #se encontro um form pendente, nao tem pq continuar
                form_id = uf['form_id']
                currentForm = uf['form_id']['$oid']
                break
        
        # #se a quantidade de forms for a mesma do user_forms para um usuário, significa que todos já foram feitos.
        if not currentForm and len(forms) != len(user_forms):
            #se nao tem um form current, entao eu continuo
            for f in forms:
                form_id = f['_id']['$oid']
                if form_id not in done_forms:
                    form = f
                    break
        if form:
            return response(form, status.HTTP_200_OK)
        else:
            return response(status.HTTP_200_OK)        
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)
    
@app_user_form.route('/{}/<id>'.format(route_name), methods=['GET'])
def get(id):
    try:
        obj = ServiceHandler.get_service(route_name).get(id)
        
        if not obj:
            raise Exception('User Form with id {} not found!'.format(id))

        obj = obj.to_json() if obj else None

        return response(obj, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/{}/<user_id>/<form_status>'.format(route_name), methods=['GET'])
def get_forms_by_user_status(user_id, form_status):
    try:
        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(user_id)

        if not user:
            raise Exception('User with id {} not found!'.format(user_id))

        obj = ServiceHandler.get_service(route_name).get_forms_by_user_status(user_id, form_status)
        obj = obj.to_json() if obj else None

        return response(obj, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/{}/get-form-user'.format(route_name), methods=['POST'])
def get_form_by_user():
    try:
        json_obj = request.get_json()

        user = ServiceHandler.get_service(ROUTE_CONFIG['USER_TYPE_NAME']).get(json_obj['user_id'])

        if not user:
            raise Exception('User with id {} not found!'.format(json_obj['user_id']))

        form = ServiceHandler.get_service(ROUTE_CONFIG['FORM_TYPE_NAME']).get(json_obj['form_id'])

        if not form:
            raise Exception('User with id {} not found!'.format(json_obj['form_id']))

        obj = ServiceHandler.get_service(route_name).get_form_by_user(json_obj['form_id'], json_obj['user_id'])
        obj = obj.to_json() if obj else None

        return response(obj, status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete_by_user(id):
    try:
        ServiceHandler.get_service(route_name).delete_by_id(id)

        return response(status=status.HTTP_200_OK)

    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/{}/<id>'.format(route_name), methods=['PUT'])
def update(id):
    try:        
        json_obj = request.get_json()
        obj = {
            'status': json_obj['status'],
            'id': id
        }
        ServiceHandler.get_service(route_name).update(obj)
        return response(status=status.HTTP_200_OK)
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/get-all-forms/<id>'.format(route_name), methods=['GET'])
def get_all_forms_by_user(id):
    try:

        forms = ServiceHandler.get_service(route_name).get_all_forms_by_user(id)

        return response(forms.to_json(), status.HTTP_200_OK)
    
    except Exception as e:
        return response_text(str(e), status.HTTP_400_BAD_REQUEST)

@app_user_form.route('/{}/<id>'.format(route_name), methods=['DELETE'])
def delete(id):
    try:        
        user = ServiceHandler.get_service(route_name).get(id)
        ServiceHandler.get_service(route_name).delete(id)
        return response(status=status.HTTP_200_OK)
        
    except Exception as e:
        return response(str(e), status.HTTP_400_BAD_REQUEST)
