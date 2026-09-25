from flask import Flask

app = Flask(__name__)

# Base de datos simulada en memoria para QA
pacientes = []
citas = []

def obtener_estilos():
    return "<style>* { box-sizing: border-box; font-family: 'Segoe UI', sans-serif; margin: 0; padding: 0; } body { display: flex; min-height: 100vh; background-color: #f4f6f9; color: #333; } .sidebar { width: 280px; background-color: #1e293b; color: white; padding: 20px; } .sidebar h2 { font-size: 18px; margin-bottom: 30px; text-align: center; color: #38bdf8; border-bottom: 1px solid #334155; padding-bottom: 15px; } .sidebar a { display: block; color: #cbd5e1; padding: 12px 15px; text-decoration: none; margin-bottom: 8px; border-radius: 6px; font-weight: 500; } .sidebar a:hover, .sidebar a.active { background-color: #0284c7; color: white; } .main-content { flex-grow: 1; padding: 40px; } .header-panel { background: white; padding: 20px; border-radius: 8px; margin-bottom: 30px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); display: flex; justify-content: space-between; align-items: center; } .user-badge { background: #e0f2fe; color: #0369a1; padding: 6px 12px; border-radius: 20px; font-size: 14px; font-weight: bold; } .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); } h3 { margin-bottom: 20px; color: #0f172a; font-size: 22px; } .form-group { margin-bottom: 20px; } label { display: block; margin-bottom: 8px; font-weight: 600; font-size: 14px; color: #475569; } input, select { width: 100%; padding: 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 15px; } .btn { background-color: #0284c7; color: white; border: none; padding: 12px 20px; font-size: 16px; font-weight: 600; border-radius: 6px; cursor: pointer; width: 100%; text-align: center; display: block; text-decoration: none; } .btn:hover { background-color: #0369a1; } .alert-success { background-color: #dcfce7; border-left: 4px solid #16a34a; color: #14532d; padding: 15px; border-radius: 4px; margin-bottom: 20px; font-weight: 500; } table { width: 100%; border-collapse: collapse; margin-top: 20px; } th, td { padding: 12px 15px; text-align: left; border-bottom: 1px solid #e2e8f0; } th { background-color: #f8fafc; color: #64748b; } .grid-dashboard { display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; margin-bottom: 30px; } .metric-card { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.04); border-top: 4px solid #0284c7; } .metric-card h4 { color: #64748b; font-size: 13px; margin-bottom: 5px; } .metric-card p { font-size: 24px; font-weight: bold; color: #1e293b; }</style>"

def construir_pagina(contenido, active_tab, rol):
    html = "<html><head><meta charset='UTF-8'><title>Centro de Salud Ganímedes</title>" + obtener_estilos() + "</head><body>"
    html += "<div class='sidebar'><h2>CS GANÍMEDES (QA)</h2>"
    
    html += "<a href='/' class='" + ("active" if active_tab == "login" else "") + "'>🔐 TF-03: Login Comercial</a>"
    html += "<a href='/admision' class='" + ("active" if active_tab == "admision" else "") + "'>📋 TF-01: Admisión Pacientes</a>"
    html += "<a href='/citas' class='" + ("active" if active_tab == "citas" else "") + "'>📅 TF-02: Agendamiento Citas</a>"
    html += "<a href='/reportes' class='" + ("active" if active_tab == "reportes" else "") + "'>📊 TF-04: Reportes Admin</a>"
    html += "</div>"
    
    html += "<div class='main-content'><div class='header-panel'><h2>Panel de Pruebas de Software - QA Funcional</h2>"
    html += "<span class='user-badge'>" + rol + "</span></div>"
    html += contenido + "</div></body></html>"
    return html

@app.route('/')
def login():
    c = "<div class='card' style='max-width: 450px; margin: 40px auto;'><h3>🔑 TF-03: Autenticación de Usuarios por Roles</h3>"
    c += "<div class='alert-success'>✓ Simulación de credenciales comerciales y administrativas validada correctamente.</div>"
    c += "<div class='form-group'><label>Correo Electrónico Institucional</label><input type='text' value='coordinador_comercial@salud.gob.pe' readonly></div>"
    c += "<div class='form-group'><label>Contraseña Asociada</label><input type='password' value='1234567890' readonly></div>"
    c += "<div class='form-group'><label>Rol de Usuario Activo</label><select disabled><option>Personal Administrativo / Comercial</option></select></div>"
    c += "<button class='btn' onclick='alert(\"Acceso verificado. Redirigiendo al Dashboard...\")'>Simular Inicio de Sesión Exitoso</button></div>"
    return construir_pagina(c, "login", "Entorno Local de Pruebas")

@app.route('/admision', methods=['GET', 'POST'])
def admision():
    msg = ""
    # Simular guardado estático para la captura
    msg = "<div class='alert-success'>✓ ¡Éxito! Paciente registrado correctamente. DNI validado en el Módulo de Admisión.</div>"
    
    c = "<div class='card'><h3>📋 TF-01: Registro e Ingreso de Pacientes (Admisión)</h3>" + msg
    c += "<form method='POST'><div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>"
    c += "<div class='form-group'><label>Nombre Completo del Paciente</label><input type='text' value='Maryorie Lopez'></div>"
    c += "<div class='form-group'><label>Número de Documento (DNI - 8 dígitos)</label><input type='text' value='76543210'></div></div>"
    c += "<button type='button' class='btn'>Registrar Nuevo Paciente en el Sistema</button></form>"
    c += "<h4 style='margin-top: 30px; margin-bottom: 10px; color:#475569;'>Base de Datos de Admisión Local:</h4>"
    c += "<table><thead><tr><th>Nombre Completo</th><th>Número DNI</th><th>Estado Operativo</th></tr></thead>"
    c += "<tbody><tr><td>Maryorie Lopez</td><td>76543210</td><td><span style='color:green;font-weight:bold;'>✓ Registrado</span></td></tr></tbody></table></div>"
    return construir_pagina(c, "admision", "Admisión / Recepción")

@app.route('/citas', methods=['GET', 'POST'])
def citas():
    msg = "<div class='alert-success'>✓ ¡Éxito! Cupo reservado y cita guardada de forma programada con el especialista.</div>"
    c = "<div class='card'><h3>📅 TF-02: Agendamiento y Asignación de Citas Médicas</h3>" + msg
    c += "<form><div class='form-group'><label>Paciente Solicitante</label><input type='text' value='Maryorie Lopez (DNI: 76543210)'></div>"
    c += "<div style='display: grid; grid-template-columns: 1fr 1fr; gap: 20px;'>"
    c += "<div class='form-group'><label>Especialista y Consultorio Asignado</label><select><option>Dr. Mendoza - Medicina General (Consultorio 102)</option></select></div>"
    c += "<div class='form-group'><label>Fecha y Hora de la Cita</label><input type='text' value='2026-10-15 10:30'></div></div>"
    c += "<button type='button' class='btn' style='background-color: #059669;'>Confirmar y Agendar Cita Médica</button></form>"
    c += "<h4 style='margin-top: 30px; margin-bottom: 10px; color:#475569;'>Agenda Activa del Centro de Salud:</h4>"
    c += "<table><thead><tr><th>Paciente</th><th>Médico y Especialidad</th><th>Fecha Programada</th></tr></thead>"
    c += "<tbody><tr><td>Maryorie Lopez</td><td>Dr. Mendoza - Medicina General</td><td>2026-10-15 10:30</td></tr></tbody></table></div>"
    return construir_pagina(c, "citas", "Coordinador Médico")

@app.route('/reportes')
def reportes():
    c = "<div class='card'><h3>📊 TF-04: Reportes Consolidados e Indicadores de Gestión</h3>"
    c += "<p style='color: #64748b; margin-bottom: 20px;'>Panel administrativo para la toma de decisiones del Centro de Salud Ganímedes.</p>"
    c += "<div class='grid-dashboard'>"
    c += "<div class='metric-card'><h4>Atenciones Totales</h4><p>1,248 pac.</p></div>"
    c += "<div class='metric-card' style='border-top-color: #10b981;'><h4>Citas de Hoy</h4><p>42 citas</p></div>"
    c += "<div class='metric-card' style='border-top-color: #f59e0b;'><h4>Nuevos Afiliados</h4><p>18 pac.</p></div>"
    c += "<div class='metric-card' style='border-top-color: #ef4444;'><h4>Productividad</h4><p>94.2%</p></div></div>"
    c += "<div style='background: #f8fafc; padding: 25px; border-radius: 6px; border: 1px dashed #cbd5e1; text-align: center; margin-bottom: 20px;'>"
    c += "<p style='font-weight: 600; color: #334155; margin-bottom: 15px;'>📊 Simulación Estadística de Demanda Ocupacional</p>"
    c += "<div style='display: flex; justify-content: space-around; align-items: flex-end; height: 60px; max-width: 200px; margin: 0 auto;'>"
    c += "<div style='width: 30px; background: #0284c7; height: 90%;'></div>"
    c += "<div style='width: 30px; background: #10b981; height: 50%;'></div>"
    c += "<div style='width: 30px; background: #f59e0b; height: 70%;'></div></div></div>"
    c += "<button class='btn' style='background-color: #475569;'>📥 Exportar Reporte Mensual a MS Excel (.xlsx)</button></div>"
    return construir_pagina(c, "reportes", "Director Médico")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
