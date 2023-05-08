from .models import Builder, ResidentComplex, Apartment, Floor


def builder_verify(data):
    errors = []

    if len(data['bank_account']) == 0:
        errors.append({'bank_account': 'Вы не заполнили P/c'})

    if Builder.objects.filter(bank_account__iexact=data['bank_account']).exists():
        errors.append({'bank_account': f"{data['bank_account']} уже добавлен в базу"})

    if len(data['inn']) == 0:
        errors.append({'inn': 'more than 0 symbols'})

    if Builder.objects.filter(inn__iexact=data['inn']).exists():
        errors.append({'inn': f"{data['inn']} уже добавлен в базу"})

    if len(data['brand_name']) < 5:
        errors.append({'brand_name': 'more than 5 symbols'})

    if Builder.objects.filter(brand_name__iexact=data['brand_name']).exists():
        errors.append({'brand_name': f"{data['brand_name']} уже добавлен в базу"})

    if len(data['legal_name']) < 5:
        errors.append({'legal_name': 'more than 5 symbols'})

    if Builder.objects.filter(legal_name__iexact=data['legal_name']).exists():
        errors.append({'legal_name': f"{data['legal_name']} is already exists"})

    if len(data['address']) == 0:
        errors.append({'address': 'more than 0 symbols'})

    if data['license_period'] is None:
        errors.append({'license_period': 'license_period is empty'})

    return errors


def resident_verify(data):
    errors = []

    if len(data['name']) == 0:
        errors.append({'name': 'name is empty'})

    return errors


def complex_verify(data):
    errors = []
    if ResidentComplex.objects.filter(name__iexact=data['name']).exists():
        errors.append({'resident_complex': f"{data['name']} уже добавлен в базу"})

    if not data['total_apartment'] < 999:
        errors.append({'total_apartment': 'Rating cannot be more than 1000.'})

    if not data['total_apartment'] >= 1:
        errors.append({'total_apartment': 'Rating cannot be less than 1'})

    try:
        if data['image_banner'].size > 2 * 1024 * 1024:
            errors.append({'image_banner': 'image_banner should be less 2 mb'})
    except Exception:
        pass

    # if data['image_banner'].size > 2 * 1024 * 1024:
    #     errors.append({'image_banner': 'image_banner should be less 2 mb'})

    return errors


def apartment_validate(data):
    errors = []
    resident_complex_id = data['floor'].entrance.block.resident_complex.id
    apartment = Apartment.objects. \
        filter(name__iexact=data['name'], floor__entrance__block__resident_complex_id=resident_complex_id).first()
    if apartment:
        errors.append({'apartment_exists': f'{apartment.name} is already exists'})
    return errors


def floor_validate(data):
    errors = []
    MAX_SIZE = 1024 * 1024
    image_formats = ('jpg', 'jpeg', 'png')
    print(data['image_1'].size, 'sizeeeeeeeeeee')
    floor = Floor.objects.filter(name__iexact=data['name'], entrance_id=data['entrance'])
    if floor:
        errors.append({'floor': 'this floor is already exists'})

    # if data['floor_type'] is None:
    #     errors.append({'floor_type': 'you have to fill it'})
    #
    # if data['image_1'] is not None:
    #     image = str(data['image_1']).split('.').pop()
    #     if data['image_1'].size > 2 * MAX_SIZE:
    #         errors.append({'image_size': 'size should be less than 2 mb'})
    #     if image not in image_formats:
    #         errors.append({'image_format': 'only jpg, jpeg, png'})
    return errors


def apartment_put_validate(data):
    MAX_SIZE = 1024 * 1024
    image_formats = ('jpg', 'jpeg', 'png')
    errors = []
    resident_complex_id = data['floor'].entrance.block.resident_complex.id
    try:
        data['name']
    except KeyError:
        pass
    else:
        apartment = Apartment.objects.\
            filter(name__iexact=data['name'], floor__entrance__block__resident_complex_id=resident_complex_id).first()
        if apartment:
            errors.append({'apartment_exists': f'{apartment.name} is already exists'})
    try:
        if data['image_1'] is not None:
            if data['image_1'].size > 2 * MAX_SIZE:
                errors.append({'image_size_1': 'only less than 2mb'})
            if str(data['image_1']).split('.').pop().lower() not in image_formats:
                errors.append({'image_1_format': 'only jpg, png'})
    except KeyError:
        pass
    try:
        if data['image_2'] is not None:
            if data['image_2'].size > 2 * MAX_SIZE:
                errors.append({'image_size_2': 'only less than 2mb'})
            if str(data['image_2']).split('.').pop().lower() not in image_formats:
                errors.append({'image_2_format': 'only jpg, png'})
    except KeyError:
        pass
    return errors
