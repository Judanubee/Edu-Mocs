def tipo_usuario(request):
    es_alumno = False
    es_profesor = False

    if request.user.is_authenticated:
        es_alumno = hasattr(request.user, "perfil_alumno")
        es_profesor = hasattr(request.user, "perfil_profesor")

    return {
        "es_alumno": es_alumno,
        "es_profesor": es_profesor,
    }