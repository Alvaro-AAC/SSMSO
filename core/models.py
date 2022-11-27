# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from django.db import models

class Atencion(models.Model):
    id_atencion = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    motivo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=1000, blank=True, null=True)
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico')
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    id_interconsulta = models.OneToOneField('self', models.DO_NOTHING, db_column='id_interconsulta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'atencion'


class BitacoraCirugia(models.Model):
    id_bitacora_cirugia = models.BigIntegerField(primary_key=True)
    detalle = models.CharField(max_length=3000)
    fecha = models.DateField()
    hora = models.DateTimeField()
    id_cirugia = models.ForeignKey('Cirugia', models.DO_NOTHING, db_column='id_cirugia')

    class Meta:
        managed = False
        db_table = 'bitacora_cirugia'


class Cargo(models.Model):
    id_cargo = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cargo'


class Cirugia(models.Model):
    id_cirugia = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    id_reserva_cirugia = models.OneToOneField('ProgramacionCirugia', models.DO_NOTHING, db_column='id_reserva_cirugia')

    class Meta:
        managed = False
        db_table = 'cirugia'


class Ciudad(models.Model):
    id_ciudad = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'ciudad'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad')

    class Meta:
        managed = False
        db_table = 'comuna'


class DetalleUnidad(models.Model):
    id_detalle_unidad = models.BigIntegerField(primary_key=True)
    id_unidad = models.ForeignKey('Unidad', models.DO_NOTHING, db_column='id_unidad')
    id_medico = models.ForeignKey('Medico', models.DO_NOTHING, db_column='id_medico')

    class Meta:
        managed = False
        db_table = 'detalle_unidad'


class DisponibilidadPabellon(models.Model):
    id_disponibilidad_pabellon = models.BigIntegerField(primary_key=True)
    disponible = models.CharField(max_length=1)
    id_pabellon = models.ForeignKey('Pabellon', models.DO_NOTHING, db_column='id_pabellon')
    id_modulo = models.ForeignKey('Modulo', models.DO_NOTHING, db_column='id_modulo')

    class Meta:
        managed = False
        db_table = 'disponibilidad_pabellon'


class Evaluacion(models.Model):
    id_evaluacion = models.BigIntegerField(primary_key=True)
    id_paciente = models.ForeignKey('Paciente', models.DO_NOTHING, db_column='id_paciente')
    fecha = models.DateField()
    atencion = models.CharField(max_length=50)
    riesgo = models.DecimalField(max_digits=5, decimal_places=2)
    id_atencion = models.ForeignKey(Atencion, models.DO_NOTHING, db_column='id_atencion')

    class Meta:
        managed = False
        db_table = 'evaluacion'
        unique_together = (('id_evaluacion', 'id_paciente'),)


class Medico(models.Model):
    id_medico = models.IntegerField(primary_key=True)
    rut = models.IntegerField(unique=True)
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    correo = models.CharField(max_length=200)
    password = models.CharField(max_length=2000)
    direccion = models.CharField(max_length=100)
    administrador = models.CharField(max_length=1)
    habilitado = models.CharField(max_length=1)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo')
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    id_jefe = models.ForeignKey('self', models.DO_NOTHING, db_column='id_jefe', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medico'


class Modulo(models.Model):
    id_modulo = models.IntegerField(primary_key=True)
    hora_ini = models.DateField()
    hora_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'modulo'


class Pabellon(models.Model):
    id_pabellon = models.IntegerField(primary_key=True)
    piso = models.IntegerField()
    numeracion = models.IntegerField()
    habilitado = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'pabellon'


class Paciente(models.Model):
    id_paciente = models.BigIntegerField(primary_key=True)
    rut = models.IntegerField()
    dv = models.CharField(max_length=1)
    nombre = models.CharField(max_length=50)
    apellido_p = models.CharField(max_length=50)
    apellido_m = models.CharField(max_length=50)
    genero = models.CharField(max_length=1)
    fecha_nac = models.DateField()
    telefono = models.IntegerField()
    correo = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'paciente'


class ProgramacionCirugia(models.Model):
    id_reserva_cirugia = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    notificado = models.CharField(max_length=1)
    id_medico = models.ForeignKey(Medico, models.DO_NOTHING, db_column='id_medico')
    id_evaluacion = models.ForeignKey(Evaluacion, models.DO_NOTHING, db_column='id_evaluacion', related_name='id_evaluacion_related')
    id_paciente = models.ForeignKey(Evaluacion, models.DO_NOTHING, db_column='id_paciente')
    id_detalle_unidad = models.ForeignKey(DetalleUnidad, models.DO_NOTHING, db_column='id_detalle_unidad')

    class Meta:
        managed = False
        db_table = 'programacion_cirugia'


class Recurso(models.Model):
    id_recurso = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    cantidad_actual = models.IntegerField()
    cantidad_maxima = models.IntegerField()
    cantidad_peligro = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'recurso'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'region'


class ReservaPabellon(models.Model):
    id_reserva = models.BigIntegerField(primary_key=True)
    fecha = models.DateField()
    id_reserva_cirugia = models.OneToOneField(ProgramacionCirugia, models.DO_NOTHING, db_column='id_reserva_cirugia')
    id_disponibilidad_pabellon = models.ForeignKey(DisponibilidadPabellon, models.DO_NOTHING, db_column='id_disponibilidad_pabellon')

    class Meta:
        managed = False
        db_table = 'reserva_pabellon'


class ReservaRecurso(models.Model):
    cantidad = models.IntegerField()
    id_recurso = models.OneToOneField(Recurso, models.DO_NOTHING, db_column='id_recurso', primary_key=True)
    id_reserva = models.ForeignKey(ReservaPabellon, models.DO_NOTHING, db_column='id_reserva')

    class Meta:
        managed = False
        db_table = 'reserva_recurso'
        unique_together = (('id_recurso', 'id_reserva'),)


class Unidad(models.Model):
    id_unidad = models.BigIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'unidad'
