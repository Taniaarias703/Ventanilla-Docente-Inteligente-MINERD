# Ventanilla Docente Inteligente - MINERD
# Prototipo 4 Sprint 3 - Equipo 15

import json
from datetime import datetime

def validar_cedula(cedula: str) -> bool:
    c = cedula.strip().replace('-', '')
    return len(c)==11 and c.isdigit()

def consultar_sigerd(cedula: str):
    mock = {
        '00112345678': {'nombre': 'Carlos Manuel Perez', 'existe': True},
        '00112246588': {'nombre': 'Tania Arias Garcia', 'existe': True, 'distrito': '01-03 Barahona'},
    }
    if cedula in mock:
        return {'fuente': 'SIGERD', 'existe': True, **mock[cedula]}
    return {'fuente': 'SIGERD', 'existe': False}

def consultar_map(cedula: str):
    return {'fuente': 'MAP', 'es_servidor_publico': True, 'tipo': 'Docente', 'distrito': '01-03 Barahona'}

def consultar_tss(cedula: str):
    return {'fuente': 'TSS', 'afiliado': True, 'regimen': 'Contributivo', 'empleador': 'MINERD'}

def cruzar_validacion(cedula: str):
    siger = consultar_sigerd(cedula)
    resultado = {
        'valido': True,
        'cedula': cedula,
        'fecha_consulta': datetime.now().isoformat(),
        'detalles': {'SIGERD': siger, 'MAP': consultar_map(cedula), 'TSS': consultar_tss(cedula)},
        'metricas': {'campos_validados_auto': 5, 'campos_manuales_pendientes': 3, 'reduccion': '-83%', 'SUS_antes': 48, 'SUS_ahora': 82},
        'faltantes': [],
        'proximo_paso': 'Subir foto 3 docs por WhatsApp - Certificado QR 48h'
    }
    return resultado

# Prueba
cedula = "00112246588"
print(json.dumps(cruzar_validacion(cedula), indent=2, ensure_ascii=False))
