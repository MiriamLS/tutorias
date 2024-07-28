# context_processors.py dentro de tu app, por ejemplo: myapp/context_processors.py

def user_info(request):
    user_info_dict = {}
    if request.user.is_authenticated:
        user_info_dict['user_name'] = request.user.username
        user_info_dict['user_gender'] = request.user.gender if hasattr(request.user, 'gender') else None
    return {'user_info': user_info_dict}



