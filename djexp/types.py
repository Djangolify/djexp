from django.db import models


TYPES = {
	models.BigAutoField.__name__: '[]byte',
	models.BinaryField.__name__: '[]byte',
	models.FileField.__name__: '[]byte',
	models.ImageField.__name__: '[]byte',
	models.UUIDField.__name__: '[]byte',

	models.BooleanField.__name__: 'bool',
	models.NullBooleanField.__name__: 'bool',

	models.CharField.__name__: 'string',
	models.EmailField.__name__: 'string',
	models.FilePathField.__name__: 'string',
	models.GenericIPAddressField.__name__: 'string',
	models.SlugField.__name__: 'string',
	models.TextField.__name__: 'string',
	models.URLField.__name__: 'string',

	models.DateField.__name__: 'time.Time',
	models.DateTimeField.__name__: 'time.Time',
	models.DurationField.__name__: 'time.Time',
	models.TimeField.__name__: 'time.Time',

	models.SmallIntegerField.__name__: 'int32',

	models.AutoField.__name__: 'int64',
	models.BigIntegerField.__name__: 'int64',
	models.IntegerField.__name__: 'int64',

	models.PositiveSmallIntegerField.__name__: 'uint32',

	models.PositiveIntegerField.__name__: 'uint64',

	models.DecimalField.__name__: 'float64',
	models.FloatField.__name__: 'float64'
}

RELATION_TYPES = {
	models.ForeignKey: 'ForeignKey({})',
	models.ManyToManyField: 'ManyToManyField({})',
	models.OneToOneField: 'OneToOneField({})'
}
