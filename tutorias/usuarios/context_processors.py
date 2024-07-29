# context_processors.py dentro de tu app, por ejemplo: myapp/context_processors.py
from django.contrib.auth.models import Group
from generales.models import Posgrado

def user_info(request):
    user_info_dict = {}
    if request.user.is_authenticated:
        full_name = ' '.join(filter(None, [request.user.first_name, request.user.last_name]))

        user_info_dict['user_name'] = request.user.username
        user_info_dict['full_name'] = full_name if full_name else 'Sin nombre especificado'

        user_info_dict['user_gender'] = request.user.gender if hasattr(request.user, 'gender') else None
    return {'user_info': user_info_dict}





def ensure_groups_exist(request):
    # Lista de nombres de grupos a crear
    group_names = ["Coordinador", "Docente", "Alumno"]

    # Verificar cada grupo y crearlo si no existe
    for name in group_names:
        Group.objects.get_or_create(name=name)

    # Esta función no necesita retornar nada en el contexto
    return {}



def ensure_posgrados_exist(request):
    # Lista de nombres de posgrados a crear
    posgrados_names = [
        "Maestría en Sistemas Computacionales",
        "Maestría en Ingeniería Mecatrónica",
        "Maestría en Ingeniería Administrativa",
        "Doctorado en Ciencias de la Ingeniería"
    ]

    # Verificar cada posgrado y crearlo si no existe
    for name in posgrados_names:
        Posgrado.objects.get_or_create(nombre=name)

    # Esta función no necesita retornar nada en el contexto
    return {}


def group_context(request):

    context = {
        'es_coordinador': request.user.groups.filter(name='Coordinador').exists(),
        'es_docente': request.user.groups.filter(name='Docente').exists(),
        'es_alumno': request.user.groups.filter(name='Alumno').exists(),
        'es_superusuario': request.user.is_superuser,  # Verificación para superusuario

    }
    return context