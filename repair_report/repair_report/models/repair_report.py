from odoo import models, fields, api
import logging
from datetime import datetime, timedelta
_logger = logging.getLogger(__name__)

class RepairReport(models.Model):
    _inherit = 'repair.order'

    test_before_disassembly = fields.Selection([
    ('yes', 'Sí'),
    ('no', 'No')
    ], string="¿Se pudo probar la bomba antes de desarmar?")

    test_details = fields.Text(string="Detalles de la prueba", required=False)
    vacuum_level = fields.Text(string="Nivel de vacío(Mbar)")
    electricity_consumption = fields.Text(string="Consumo de electrico (Amp)")
    noise_normal = fields.Boolean(string="Normal")
    noise_anormal = fields.Boolean(string="Anormal")
    stuck_engine = fields.Boolean(string="Motor trabado")
    stuck_bomb = fields.Boolean(string="Bomba trabada")
    without_engine = fields.Boolean(string="Sin motor")
    disarmed_bomb = fields.Boolean(string="Bomba desarmada")
    without_components = fields.Boolean(string="Sin componentes")
    another = fields.Boolean(string="Otro")
    another_text = fields.Text(string="Agregue motivo")
    diagnostic_result = fields.Selection([
    ('motor', 'Falla en motor'),
    ('cableado', 'Problema de cableado'),
    ('otro', 'Otro')
    ], string="Resultado del diagnóstico")
    yes_reparation = fields.Boolean(string="Si")
    reparation_maintenance = fields.Boolean(string="Mantenimiento")
    no_reparation = fields.Boolean(string="No")
    post_yes_description = fields.Html(string="Agregar Descripción ")
    #acciones de pestañas  de acciones correctivas
    complete_disassembly_and_cleaning = fields.Boolean(string="Desarme completo y limpieza")
    assembly_and_commissioning = fields.Boolean(string="Montaje y puesta a punto")
    testing_protocol = fields.Boolean(string="Protocolo de pruebas")
    painting = fields.Boolean(string="Pintura")
    #repuestos materiales e insumos
    maintenaice_kit = fields.Boolean(string="Kit de mantenimiento")
    motor_bearing = fields.Boolean(string="Rodamiento de motor")
    oil = fields.Boolean(string="Aceite")
    gasket_kit = fields.Boolean(string="Kit de juntas")
    grinding_of_covers = fields.Boolean(string="Rectificado de tapas")
    actions_other = fields.Boolean(string="Otros")
    text_actiones_other = fields.Text(string="Especificar")
    #########
    #acciones de pestañas  de acciones de mantenimiento
    internal_crankcase_cleaning = fields.Boolean(string="Limpieza interna de cárter")
    external_cleaning = fields.Boolean(string="Limpieza externa")
    testing_protocol_maintenaice = fields.Boolean(string="Protocolo de pruebas")
    painting_mantenaice = fields.Boolean(string="Pintura")
    #repuestos materiales e insumos
    mist_filters = fields.Boolean(string="Filtros de neblina")
    oil_filters = fields.Boolean(string="Filtros de aceite")
    oil_maintenaice = fields.Boolean(string="Aceite")
    drag = fields.Boolean(string="Arrastre")
    aspiration_filter = fields.Boolean(string="Filtro de aspiración")
    valve_gasket = fields.Boolean(string="Junta de válvula")
    filter_gasket = fields.Boolean(string="Especificar")
    filter_material = fields.Boolean(string="Materia filtrante") 
    #################
    #acciones de 'no tiene reparación'
    acquisition_of_new_equipment = fields.Boolean(string="Adquisición de nuevo equipo")
    actions_other_no_repair = fields.Boolean(string="Otros")
    text_actiones_other_no_repair = fields.Text(string="Especificar")
    ##############
    #datos del motor
    serial_number = fields.Char(string="Número de serie del motor")
    power = fields.Char(string="Potencia del motor(KW)")
    revolution = fields.Char(string="Revoluciones del motor(RPM)")
    voltage = fields.Char(string="Voltaje del motor(V)")
    amperage = fields.Char(string="Amperaje del motor(A)")
    frequency = fields.Char(string="Frecuencia del motor(Hz)")
    time = fields.Datetime(string="Tiempo de reparación (minutos)")
    vacuum_level = fields.Char(string="Nivel de vacío (mbar)")
    temperature = fields.Char(string="Temperatura (°C)")
    diagnostic_notes = fields.Text(string="Notas del diagnóstico")
    normal_noise = fields.Boolean(string="Ruido normal")
    pump_operational_and_within_parameters = fields.Boolean(string="Bomba operativa y dentro de parámetros")
    operational_pum_with_observations = fields.Boolean(string="Bomba operativa con observaciones")
    does_not_meet_parameters = fields.Boolean(string="No cumple con los parámetros")
    corrective_actions = fields.Text(string="Acciones correctivas")

    @api.onchange('diagnostic_result')
    def _onchange_diagnostic_result(self):
        if self.diagnostic_result == 'motor':
            self.corrective_actions = "Reemplazo de motor"
        elif self.diagnostic_result == 'cableado':
            self.corrective_actions = "Revisión de conexiones"
    
    final_test_passed = fields.Boolean(string="¿La bomba pasó la prueba final?")
    final_test_notes = fields.Text(string="Observaciones de la prueba final")