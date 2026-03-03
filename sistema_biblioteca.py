class SistemaBiblioteca:
    def prestar_libro(self, id_usuario, isbn_libro, dias):
        if not self._verificar_disponibilidad_libro(isbn_libro):
            raise Exception("Libro no disponible.")
        
        if self._tiene_multas_pendientes(id_usuario):
            raise Exception("Usuario tiene multas pendientes.")
        
        fecha_devolucion = self._calcular_fecha_devolucion(dias)
        
        costo = self._calcular_costo_prestamo(isbn_libro, dias)
        
        self._guardar_prestamo_en_bd(id_usuario, isbn_libro, fecha_devolucion, costo)
        
        self._actualizar_stock_libro(isbn_libro)
        
        self._enviar_email_recordatorio(id_usuario, isbn_libro, fecha_devolucion)
    
    def _verificar_disponibilidad_libro(self, isbn):
        print("Verificando disponibilidad del libro en base de datos...")
        return True
    
    def _tiene_multas_pendientes(self, id_usuario):
        print("Verificando multas del usuario...")
        return False
    
    def _calcular_fecha_devolucion(self, dias):
        from datetime import datetime, timedelta
        return datetime.now() + timedelta(days=dias)
    
    def _calcular_costo_prestamo(self, isbn, dias):
        if isbn.startswith("PREM"):
            return dias * 2
        return dias * 1
    
    def _guardar_prestamo_en_bd(self, id_usuario, isbn, fecha_devolucion, costo):
        print("Guardando préstamo en base de datos...")
    
    def _actualizar_stock_libro(self, isbn):
        print("Actualizando inventario del libro...")
    
    def _enviar_email_recordatorio(self, id_usuario, isbn, fecha_devolucion):
        print("Enviando email de recordatorio...")


