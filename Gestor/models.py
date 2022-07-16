from django.db import models


# Create your models here.
class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    create_at = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)
    update_at = models.DateField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_at = models.DateField('Fecha de Eliminacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True


class Empresa(ModeloBase):
    nempresa = models.CharField('Nombre de la empresa', max_length=60, unique=True)
    imgref = models.ImageField('Imagen de Referencia', upload_to='empresa/', null=True, blank=True)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nempresa


class Oficina(ModeloBase):
    noficina = models.CharField('Nombre de la Oficina', max_length=60, unique=True)
    imgref = models.ImageField('Imagen de Referencia', upload_to='empresa/oficina', null=True, blank=True)

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return self.noficina


class Estante(ModeloBase):
    ubicacion = models.CharField('Ubicacion del Expedientes', max_length=60, unique=True)
    imgref = models.ImageField('Imagen de Referencia', upload_to='empresa/estante', null=True, blank=True)

    class Meta:
        verbose_name = 'Estante'
        verbose_name_plural = 'Estantes'

    def __str__(self):
        return self.ubicacion


class Empleado(ModeloBase):
    Lista_status = [('A', 'ACTIVO'),
                    ('E', 'EGRESO'),
                    ('J', 'JUBILADO'),
                    ]
    status = models.CharField('Estatus del Empleado', max_length=1, choices=Lista_status, null=False, default='A')
    lista_Genero = [('F', 'FEMENINO'),
                    ('M', 'MASCULINO'),
                    ('O', 'OTROS'),
                    ]
    genero = models.CharField('Genero', max_length=1, choices=lista_Genero, null=False, default='O')
    cedula = models.CharField('Cedula', max_length=10, null=False, unique=True)
    primerNombre = models.CharField('1er Nombre', max_length=60, null=False)
    primerApellido = models.CharField('1er Apellido', max_length=60, null=False)
    segundoNombre = models.CharField('2do Nombre', max_length=60)
    segundoApellido = models.CharField('2do Apellido', max_length=60)
    fecha_ingreso = models.DateField('F. de Ingreso', null=False)
    fecha_egreso = models.DateField('F. de Egreso', null=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    oficina = models.ForeignKey(Oficina, on_delete=models.CASCADE)
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)
    observacion = models.TextField('Observaciones', max_length=255)
    doc = models.FileField(null=True, blank=True, upload_to='empresa/doc')

    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'

    def __str__(self):
        return self.cedula
