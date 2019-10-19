def get_garbage_solution(garbage_key):
    waste = {
        'battery': 'Contenedor pilas',
        'electronic_devices': 'Dispositivos electrónicos',
        'fabric': 'Contenedor textil',
        'glass': 'Contenedor verde',
        'leftover': 'Contenedor naranja',
        'medical_waste': 'Punto Sigre',
        'not_clear': 'Punto Limpio',
        'organic': 'Contenedor marrón',
        'plastic': 'Contenedor amarillo',
        'paper': 'Contenedor azul'
    }
    return waste[garbage_key]